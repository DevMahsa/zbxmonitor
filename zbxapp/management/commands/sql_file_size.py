from django.core.management.base import BaseCommand
from zbxapp.models import Server, LastMemory, LastCpu
import pymssql


def sql_file_size():
    try:
        obj = Server.objects.get(name='testi219')
        connection = pymssql.connect(host='192.168.112.219', server='SQL2017', port='49950', user='sa', password='P@$$w0rd')
        cursor = connection.cursor()
        cursor.execute('''with fs
as
(
 select database_id, type, size * 8.0 / 1048576 size
 from sys.master_files
)
select 
 name,
 (select sum(size) from fs where type = 0 and fs.database_id = db.database_id) DataFileSizeGB,
 (select sum(size) from fs where type = 1 and fs.database_id = db.database_id) LogFileSizeGB
from sys.databases db''')
        #cursor.execute("EXEC sp_helpdb @dbname='msdb';")
        result = cursor.fetchall()
        for i in range(len(result)):
            obj.sql_file_size +=str(result[i][0])+' : '+str(float(result[i][1])+float(result[i][2]))+'\n'
        obj.save()
        # obj.sql_file_size= ""
        # for i in range(len(result)):
        #     obj.sql_file_size += (str(result[i][4]).split(' K')[0])
        # obj.sql_file_size = float(obj.sql_file_size)/(1024*1024)
        # obj.save()
    except Exception as e:
        print e


class Command(BaseCommand):
    def handle(self, **options):
        sql_file_size()