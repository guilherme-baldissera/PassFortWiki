from django.test import TestCase
from .models import Text, Document


class TestViewApis(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_elements = 5

        for document_id in range(number_of_elements):
            document = Document.objects.create(
                title=f'Tittle{document_id}',
            )
            if document_id == 1:
                for text_id in range(number_of_elements):
                    Text.objects.create(
                        content= f"TEXT ID : {text_id}",
                        document= document,
                    )

    def setUp(self):
        self.number_of_elements = 5

    def test_get_all_documents_with_success(self):
        response = self.client.get('/documents')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), self.number_of_elements)

    def test_get_all_reviews_succeed_when_there_are_5_texts(self):
        response = self.client.get('/documents/Tittle1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), self.number_of_elements)

    def test_get_all_reviews_succeed_when_there_are_0_texts(self):
        response = self.client.get('/documents/Tittle2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_get_all_reviews_failed_when_passed_invalid_document_title(self):
        response = self.client.get('/documents/something')
        self.assertEqual(response.status_code, 400)

    def test_get_the_latest_document_succeed_when_there_are_5_doc(self):
        response = self.client.get('/documents/Tittle1/latest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], "TEXT ID : 4")

    def test_get_the_latest_document_failed_when_there_is_no_doc(self):
        response = self.client.get('/documents/Tittle2/latest')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["message"], "Document with no Content-Text")

    def test_get_the_latest_document_failed_when_passed_invalid_document_title(self):
        response = self.client.get('/documents/TittleAA/latest')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["message"], "Document Not Found")
