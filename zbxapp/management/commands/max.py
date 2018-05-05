from django.core.management.base import BaseCommand
from django.db.models import Max
from pyzabbix import ZabbixAPI

from zbxapp.models import Server,LastMemory,LastCpu

def max():
    try :
        zapi = ZabbixAPI("http://192.168.112.157:4720")
        zapi.login("Mahsa", "Mahsa871^")
        for h in zapi.host.get(output="extend"):
            for host in Server.objects.filter(name=h['name']):
                host.maxusedcpu = LastCpu.objects.filter(server_id=host.id).aggregate(Max('cpu'))['cpu__max']
                host.maxusedmemory=LastMemory.objects.filter(server_id=host.id).aggregate(Max('memory'))['memory__max']
                host.save()
    except Exception as e:
        print e
class Command(BaseCommand):
    def handle(self, **options):
        max()
