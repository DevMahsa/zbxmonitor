from  datetime import datetime
from django.core.management.base import BaseCommand
from pyzabbix import ZabbixAPI
from zbxapp.models import Server, LastCpu, LastMemory


def export():
    try:
        zapi = ZabbixAPI("http://192.168.112.157:4720")
        zapi.login("riri", "rayta")
        for h in zapi.host.get(output="extend"):
            for host in Server.objects.filter(name=h['name']):
                for i in zapi.item.get(filter={'host': host.name}):
                    if i['name'].encode('utf-8').lower().find('cpu usage') == 0:
                        LastCpu.objects.get_or_create(server=host, cpu=i['lastvalue'].encode('utf-8'),
                                                      date=datetime.now())
                    if i['name'].encode('utf-8').lower().find('used memory') == 0:
                        LastMemory.objects.get_or_create(server=host, memory=i['lastvalue'].encode('utf-8'),
                                                         date=datetime.now())

    except Exception as e:
        print (e)


class Command(BaseCommand):
    def handle(self, **options):
        export()
