import unittest
import pyclbr

from django.test import TestCase
from django.test.runner import DiscoverRunner

from . import settings


from mongoengine import connection, connect


def suite():
    raise Exception('suite func just been actived')
    # Not sure when and where it should be used
    # return unittest.TestLoader().discover("./tests/", pattern="test*.py")


class NoSQLTestRunner(DiscoverRunner):
    def setup_databases(self):
        settings.test_conf['local'] = True
        settings.test_conf['fork'] = True
        settings.test_conf['clone'] = True
        settings.test_conf['push'] = True
        settings.test_conf['pull'] = True

        self.clearing_db_connection()
        new_db_name = "unit_tests_db"
        connect(new_db_name)

    def teardown_databases(self, *args):
        db_name = connection._connection_settings['default']['name']
        connection.get_connection().drop_database(db_name)
        connection.disconnect()

    def clearing_db_connection(self):
        # disconnect the connection with the db
        connection.disconnect()
        # remove the connection details
        connection._dbs = {}
        connection._connections = {}
        connection._connection_settings = {}
        # getting call classes defined in models.py
        models = []
        for app in settings.INSTALLED_APPS[5:]:
            models += list(pyclbr.readmodule(app + '.models').keys())

        for class_model in models:
            # delete the collection to prevent automatically connecting with the old db (the live one)
            try:
                del globals()[class_model]._collection
            except Exception:
                continue


class NoSQLTestCase(TestCase):

    def _fixture_setup(self):
        pass

    def _fixture_teardown(self):
        pass

