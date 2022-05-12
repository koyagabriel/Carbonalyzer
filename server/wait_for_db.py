import os
from django.db import connections


def test_database_connection():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
    db_connection = connections['default']
    db_connection.cursor()
    db_connection.close()


if __name__ == '__main__':
    test_database_connection()
