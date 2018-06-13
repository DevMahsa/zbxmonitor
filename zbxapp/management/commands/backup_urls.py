from django.core.management.base import BaseCommand
from zbxapp.models import Server, LastMemory, LastCpu
import pymssql


def backup_url():
    try:
        obj = Server.objects.get(name='testi219')
        connection = pymssql.connect(host='192.168.112.219', server='SQL2017', port='49950', user='Zabbix1',
                                     password='Zabbix@')
        cursor = connection.cursor()
        cursor.execute('''SELECT 
A.[Server], 
A.last_db_backup_date, 
B.backup_start_date, 
B.expiration_date, 
B.backup_size, 
B.logical_device_name, 
B.physical_device_name, 
B.backupset_name, 
B.description 
FROM 
( 
SELECT 
CONVERT(CHAR(100), SERVERPROPERTY('Servername')) AS Server, 
msdb.dbo.backupset.database_name, 
MAX(msdb.dbo.backupset.backup_finish_date) AS last_db_backup_date 
FROM msdb.dbo.backupmediafamily 
INNER JOIN msdb.dbo.backupset ON msdb.dbo.backupmediafamily.media_set_id = msdb.dbo.backupset.media_set_id 
WHERE msdb..backupset.type = 'D' 
GROUP BY 
msdb.dbo.backupset.database_name 
) AS A 

LEFT JOIN

( 
SELECT 
CONVERT(CHAR(100), SERVERPROPERTY('Servername')) AS Server, 
msdb.dbo.backupset.database_name, 
msdb.dbo.backupset.backup_start_date, 
msdb.dbo.backupset.backup_finish_date, 
msdb.dbo.backupset.expiration_date, 
msdb.dbo.backupset.backup_size, 
msdb.dbo.backupmediafamily.logical_device_name, 
msdb.dbo.backupmediafamily.physical_device_name, 
msdb.dbo.backupset.name AS backupset_name, 
msdb.dbo.backupset.description 
FROM msdb.dbo.backupmediafamily 
INNER JOIN msdb.dbo.backupset ON msdb.dbo.backupmediafamily.media_set_id = msdb.dbo.backupset.media_set_id 
WHERE msdb..backupset.type = 'D' 
) AS B 
ON A.[server] = B.[server] AND A.[database_name] = B.[database_name] AND A.[last_db_backup_date] = B.[backup_finish_date] 
ORDER BY 
A.database_name''')


        # cursor.execute(
        #    "SELECT CONVERT(INT, ISNULL(value, value_in_use)) AS config_value FROM sys.configurations WHERE name = N'xp_cmdshell' ;''')
        result = cursor.fetchall()
        obj.backup_name = ""
        for i in range(len(result)):
            obj.backup_name+= str(result[i][7])+', '+'\n'
        obj.save()
    except Exception as e:
        print e


class Command(BaseCommand):
    def handle(self, **options):
        backup_url()
