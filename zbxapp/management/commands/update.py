from django.core.management.base import BaseCommand
from pyzabbix import ZabbixAPI
from zbxapp.models import Server


def update():
    try:
        zapi = ZabbixAPI("http://192.168.112.157:4720")
        zapi.login("riri", "rayta")
        for h in zapi.host.get(output="extend"):
            if not Server.objects.filter(name=h['name']).exists():
                get = Server(name=h['name'])
                get.save()
    except Exception as e:
        print e


class Command(BaseCommand):
    def handle(self, **options):
        update()
