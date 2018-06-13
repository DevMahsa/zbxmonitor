from django.core.management.base import BaseCommand
from zbxapp.models import Server, LastMemory, LastCpu
import pymssql


def sql_login_user():
    try:
        obj = Server.objects.get(name='testi219')
        connection = pymssql.connect(host='192.168.112.219', server='SQL2017', port='49950', user='Zabbix1', password='Zabbix@')
        cursor = connection.cursor()
        cursor.execute("select * from sys.sql_logins where is_disabled =0")
                # cursor.execute(
                #    "SELECT CONVERT(INT, ISNULL(value, value_in_use)) AS config_value FROM sys.configurations WHERE name = N'xp_cmdshell' ;")
        result = cursor.fetchall()
        obj.sql_login_user = ""
        for i in range(len(result)):
            obj.sql_login_user += str(result[i][0]) + ', '+'\n'
        obj.save()
    except Exception as e:
        print e


class Command(BaseCommand):
    def handle(self, **options):
        sql_login_user()