from django.core.management.base import BaseCommand
from pyzabbix import ZabbixAPI
from zbxapp.models import Server


def update():
    try:
        zapi = ZabbixAPI("http://192.168.112.157:4720")
        zapi.login("riri", "rayta")
        count = 0
        query= zapi.host.get(output="extend", selectInterfaces="extend", selectParentTemplates="Array")
        length = query.__len__()
        for count in range(length):
            if Server.objects.filter(name=query[count]['name']).exists():
                count +=1
                continue
            get = Server(name=query[count]['name'])
            get.ip=query[count]['interfaces'][0]['ip'].encode('utf-8')
            get.name= query[count]['name'].encode('utf-8')
            get.hostid = query[count]['hostid'].encode('utf-8')
            get.save()

    except Exception as e:
        print e


class Command(BaseCommand):
    def handle(self, **options):
        update()
