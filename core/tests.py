from unittest import TestCase
from core import database_backup
import os

__author__ = 'peter'


class DatabaseBackupTestCase(TestCase):
    def setUp(self):
        self.db_name = "hrms"
        self.db_password = "p@55w0rd"
        self.db_host = "localhost"
        self.db_user = "root"

    def test_that_with_right_db_credential_file_is_backup(self):
        created_zip = database_backup.backup_database_server(db_user=self.db_user,
                                                             db_password=self.db_password,
                                                             db_host=self.db_host,
                                                             db_name=self.db_name)
        self.assertIsNotNone(created_zip)
        self.assertTrue(os.path.exists(created_zip.filename))
