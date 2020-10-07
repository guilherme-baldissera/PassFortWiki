from rest_framework.serializers import ModelSerializer
from .models import Document, Text


class DocumentSerializer(ModelSerializer):
    """
    Serializes/deserialize Document object.
    """

    class Meta:
        model = Document
        fields = '__all__'


class TextSerializer(ModelSerializer):
    """
    Serializes/deserialize Text object.
    """

    class Meta:
        model = Text
        exclude = ['document']


class Error:
    """
    Defines a data response in case of exception.
    """
    message = None

    def __init__(self, message):
        """
        Requires an error message.
        """
        self.message = message

    def serialize(self):
        """
        Serialize Error instance to a JSON formatted str.
        """
        return self.__dict__
