from django.core.management.base import BaseCommand
from zbxapp.models import Server, LastMemory, LastCpu
import pymssql


def sql_version():
    try:
        obj = Server.objects.get(name='testi219')
        connection = pymssql.connect(host='192.168.112.219', server='SQL2017', port='49950', user='Zabbix1', password='Zabbix@')
        cursor = connection.cursor()
        cursor.execute("SELECT @@version;")
        result = cursor.fetchall()
        obj.sql_version = str(result[0][0]).split('\n')[0]
        obj.save()
    except Exception as e:
        print e

class Command(BaseCommand):
    def handle(self, **options):
        sql_version()