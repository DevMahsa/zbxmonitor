from  datetime import datetime
from django.core.management.base import BaseCommand
from pyzabbix import ZabbixAPI
from zbxapp.models import Server


def get_items():
    try:
        # FREE DISK SPACE LOGICAL F:
        zapi = ZabbixAPI("http://*")
        zapi.login("*", "*")
        for h in zapi.host.get(output="extend"):
            for host in Server.objects.filter(name=h['name']):
                # curr=Server.objects.filter(name=h['name'])
                # nameserver = curr.get(name__contains=h['name']).name.encode('utf-8') ==host.name
                for i in zapi.item.get(filter={'host': host.name}):
                    host.date = datetime.now()
                    if i['name'].encode('utf-8').lower().find('windows firewall status') == 0:
                        host.firewall = i['lastvalue'].encode('utf-8')
                    if i['name'].encode('utf-8').lower().find('mcafee task manager') == 0:
                        host.mcafee = i['lastvalue'].encode('utf-8')
                    if i['name'].encode('utf-8').lower().find('telnet service') == 0:
                        host.telnet = i['lastvalue'].encode('utf-8')
                    if i['name'].encode('utf-8').lower().find('free disk space logical c:') == 0:
                        host.freediskc = i['lastvalue'].encode('utf-8')
                    if i['name'].encode('utf-8').lower().find('free disk space logical d:') == 0:
                        host.freediskd = i['lastvalue'].encode('utf-8')
                    if i['name'].encode('utf-8').lower().find('free disk space logical e:') == 0:
                        host.freediske = i['lastvalue'].encode('utf-8')
                    if i['name'].encode('utf-8').lower().find('free disk space logical f:') == 0:
                        host.freediskf = i['lastvalue'].encode('utf-8')
                    if i['name'].encode('utf-8').lower().find('free disk space logical g:') == 0:
                        host.freediskg = i['lastvalue'].encode('utf-8')
                    if i['name'].encode('utf-8').lower().find('free disk space logical h:') == 0:
                        host.freediskh = i['lastvalue'].encode('utf-8')
                    if i['name'].encode('utf-8').lower().find('free disk space logical i:') == 0:
                        host.freediski = i['lastvalue'].encode('utf-8')

                host.save()

    except Exception as e:
        print e


class Command(BaseCommand):
    def handle(self, **options):
        get_items()
