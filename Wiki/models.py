from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=50, null=False, unique=True)


class Text(models.Model):
    created = models.DateTimeField(null=False, auto_now_add=True)
    content = models.TextField(max_length=999999, null=False)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

