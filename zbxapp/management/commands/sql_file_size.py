from django.core.management.base import BaseCommand
from zbxapp.models import Server, LastMemory, LastCpu
import pymssql


def sql_file_size():
    try:
        obj = Server.objects.get(name='testi219')
        connection = pymssql.connect(host='192.168.112.219', server='SQL2017', port='49950', user='Zabbix1', password='Zabbix@')
        cursor = connection.cursor()
        cursor.execute("EXEC sp_helpfile ;")
        result = cursor.fetchall()
        obj.sql_file_size= ""
        for i in range(len(result)):
            obj.sql_file_size += (float(str(result[i][4]).split(' K')[0]))
        obj.sql_file_size = float(obj.sql_file_size)/(1024*1024)
        obj.save()
    except Exception as e:
        print e


class Command(BaseCommand):
    def handle(self, **options):
        sql_file_size()