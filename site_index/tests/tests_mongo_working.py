# from datetime import date
from django.test import TestCase
# from mongoengine import Document, StringField, DateTimeField
import os


# class TestPerson(Document):
#     name = StringField(max_length=200)
#     birthday = DateTimeField()


class HackTest(TestCase):
    def test_can_get_var_from_envirament(self):
        self.assertEqual(1, 2-1)

    # def _can_save_to_db(self):
    #     peter = TestPerson(name='Peter', birthday=date(2010, 12, 12))
    #     peter.save()
    #     self.assertEqual(TestPerson.objects.first().name, 'Peter')
