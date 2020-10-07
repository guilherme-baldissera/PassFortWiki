from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Document, Text
from .serializers import DocumentSerializer, TextSerializer, Error
import datetime


@api_view(['GET'])
def get_all_documents(request):
    try:
        documents = Document.objects.all()
        documents_serializer = DocumentSerializer(documents, many=True)
        return Response(status=status.HTTP_200_OK, data=documents_serializer.data)
    except Exception as e:
        Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                 data=Error("Unknown Error occurred").serialize())


@api_view(['GET', 'POST'])
def get_all_reviews_or_add_review(request, title):
    if request.method == "GET":
        return get_all_reviews(title)
    else:
        return add_review(request, title)


@api_view(['GET'])
def get_document_by_timestamp(request, title, timestamp):
    try:
        document = Document.objects.get(title=title)
        all_texts = Text.objects.filter(document=document).order_by("-created")
        text_serializer = None
        for text in all_texts:
            if timestamp >= int(datetime.datetime.timestamp(text.created)):
                text_serializer = TextSerializer(text)
                break

        if text_serializer is None:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=Error("Document with no Content-Text").serialize())

        return Response(status=status.HTTP_200_OK, data=text_serializer.data)
    except ObjectDoesNotExist as odne:
        print(f"ObjectDoesNotExist {odne}")
        return Response(status=status.HTTP_400_BAD_REQUEST, data=Error("Document Not Found").serialize())
    except Exception as e:
        print(f"Exception {e}")
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data=Error("Unknown Error occurred").serialize())


@api_view(['GET'])
def get_the_latest_document(request, title):
    try:
        document = Document.objects.get(title=title)
        all_texts = Text.objects.filter(document=document).order_by("-created")
        text_serializer = TextSerializer(all_texts[0])
        return Response(status=status.HTTP_200_OK, data=text_serializer.data)
    except ObjectDoesNotExist as odne:
        print(f"ObjectDoesNotExist {odne}")
        return Response(status=status.HTTP_400_BAD_REQUEST, data=Error("Document Not Found").serialize())
    except IndexError as ie:
        print(f"IndexError {ie}")
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=Error("Document with no Content-Text").serialize())
    except Exception as e:
        print(f"Exception {e}")
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data=Error("Unknown Error occurred").serialize())


def get_all_reviews(title):
    try:
        document = Document.objects.get(title=title)
        all_texts = Text.objects.filter(document=document)
        all_texts_serializer = TextSerializer(all_texts, many=True)

        return Response(status=status.HTTP_200_OK, data=all_texts_serializer.data)
    except ObjectDoesNotExist as odne:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=Error("Document Not Found").serialize())
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data=Error("Unknown Error occurred").serialize())


def add_review(request, title):
    try:
        document = Document.objects.get(title=title)
        content = request.data['content']

        text = Text(
            content=content,
            document=document
        )
        text.save()
        text_serializer = TextSerializer(text)
        return Response(status=status.HTTP_200_OK, data=text_serializer.data)
    except ObjectDoesNotExist as odne:
        print(f"ObjectDoesNotExist {odne}")
        return Response(status=status.HTTP_400_BAD_REQUEST, data=Error("Document Not Found").serialize())
    except KeyError as ke:
        print(f"KeyError {ke}")
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=Error("Content was not sent").serialize())
    except Exception as e:
        print(f"Exception {e}")
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        data=Error("Unknown Error occurred").serialize())
