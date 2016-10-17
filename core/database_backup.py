from django.http.response import HttpResponseBadRequest
import subprocess
import tempfile
import os
import zipfile
import io

__author__ = 'peter'


def backup_database_server(db_user='root', db_password=None, db_name=None, db_host="localhost"):
    # check if the database name is none
    tmp_file = get_tem_file(db_name=db_name)
    if db_name is None:
        return "Database name cannot be empty"
    db_host = "--host=%s" % db_host
    db_password = "--password=%s" % db_password
    db_user = "--user=%s" % db_user
    command = ["mysqldump", db_host, db_user, db_password, db_name, "-r", tmp_file]
    dump_cmd = subprocess.call(command)
    if dump_cmd == 0:
        print("Backup completed....\n Zipping backup file")
        return prepare_zip_file(sql_file=tmp_file)


def get_tem_file(db_name=None):
    if not os.path.exists('/tmp'):
        os.mkdir("/tmp")
    with tempfile.NamedTemporaryFile(suffix=".sql", prefix=db_name, delete=False) as tp:
        tmp_file_location = tp.name
    return tmp_file_location


def zip_backup_database_file(sql_backup_filename=''):
    # check if the file does not exits
    zip_filename = sql_backup_filename + ".zip"
    with zipfile.ZipFile(zip_filename, mode='w', compression=zipfile.ZIP_DEFLATED) as backup_zip:
        backup_zip.write(sql_backup_filename)
    return backup_zip


def prepare_zip_file(sql_file=''):
    # check that the temp created file exits
    if not os.path.exists(sql_file):
        return HttpResponseBadRequest()
    zip_io = io.BytesIO()
    with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as backup_zip:
        backup_zip.write(sql_file)

    # do a clean up of the file
    filepath, filename = os.path.split(sql_file)
    try:
        os.remove(sql_file)
    except FileNotFoundError:
        pass

    return filename, zip_io
