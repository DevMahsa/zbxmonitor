from django.core.management.base import BaseCommand
from datetime import datetime
from pyzabbix import ZabbixAPI
from zbxapp.models import Name

def update():
    zapi = ZabbixAPI("http://192.168.112.157:4720")
    zapi.login("Mahsa", "Mahsa871^")
    return zapi

    for h in zapi.host.get(output="extend"):
        get = Name(server=h['name'], date = datetime.now())
        get.save()


class Command(BaseCommand):
    def handle(self, **options):
        update()