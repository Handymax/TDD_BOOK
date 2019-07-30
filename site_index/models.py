from mongoengine import Document, StringField

# Create your models here.


class Person(Document):
    name = StringField(max_length=200)
