from unittest import TestCase
from site_index.models import Person


class HackPersonTest(TestCase):

    def test_can_save_person(self):
        self.assertEqual(Person.objects.count(), 0)
        person_1 = Person(name='Perter')
        person_1.save()
        self.assertEqual(Person.objects.first().name, 'Perter')

