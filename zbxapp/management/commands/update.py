from django.core.management.base import BaseCommand
from datetime import datetime
from pyzabbix import ZabbixAPI
from zbxapp.models import Name

def update():
    try:
        zapi = ZabbixAPI("http://192.168.112.157:4720")
        zapi.login("Mahsa", "Mahsa871^")
        for h in zapi.host.get(output="extend"):
            if not Name.objects.filter(server = h['name']).exists():
                get = Name(server=h['name'])
                get.save()
        print 'complete'
    except Exception as e:
        print e


class Command(BaseCommand):
    def handle(self, **options):
        update()