from  datetime import datetime
from django.core.management.base import BaseCommand
from pyzabbix import ZabbixAPI
from zbxapp.models import Server

def get_items():
    try:

        zapi = ZabbixAPI("http://192.168.112.157:4720")
        zapi.login("riri", "rayta")
        for h in zapi.host.get(output="extend"):

            for host in Server.objects.filter(name=h['name']):
                # curr=Server.objects.filter(name=h['name'])
                # nameserver = curr.get(name__contains=h['name']).name.encode('utf-8') ==host.name
                for i in zapi.item.get(filter={'host': host.name}):
                    host.date = datetime.now()

                    if i['name'].lower().find('mcafee task manager') == 0:
                        host.mcafee = i['lastvalue']
                    if i['name'].lower().find('telnet service') == 0:
                        host.telnet = i['lastvalue']
                    if i['name'].lower().find('free disk space logical c:') == 0:
                        host.freediskc = i['lastvalue']
                    if i['name'].lower().find('free disk space logical d:') == 0:
                        host.freediskd = i['lastvalue']
                    if i['name'].lower().find('free disk space logical e:') == 0:
                        host.freediske = i['lastvalue']
                    if i['name'].lower().find('free disk space logical f:') == 0:
                        host.freediskf = i['lastvalue']
                    if i['name'].lower().find('free disk space logical g:') == 0:
                        host.freediskg = i['lastvalue']
                    if i['name'].lower().find('free disk space logical h:') == 0:
                        host.freediskh = i['lastvalue']
                    if i['name'].lower().find('free disk space logical i:') == 0:
                        host.freediski = i['lastvalue']
                    if i['name'].lower().find('ports open firewall rules') == 0:
                        host.open_port = i['lastvalue']
                    if i['name'].lower().find('microsoft update') == 0:
                        host.microsoft_update = i['lastvalue']
                    if i['name'].lower().find('local users') == 0:
                        host.local_user = i['lastvalue']
                    if i['name'].lower().find('eventlog max size') == 0:
                        host.eventlog_max_size = i['lastvalue']
                    if i['name'].lower().find('sys event') == 0:
                        host.new_system_event = i['lastvalue']
                    if i['name'].lower().find('app event') == 0:
                        host.new_app_event = i['lastvalue']
                    if i['name'].lower().find('file sharing port') == 0:
                        host.file_sharing_port = i['lastvalue']


                    try:
                        if i['name'].lower().find('win xpr date') == 0:
                            host.win_active = i['lastvalue'].split(':')[1]
                        if i['name'].lower().find('software version') == 0:
                            host.windows_version = i['lastvalue'].split('BuildLab')[2].split('REG_SZ')[1].split('.amd')[0]
                        if i['name'].lower().find('all program files x86') == 0:
                            any_desk = i['lastvalue'].split('AnyDesk')
                            if len(any_desk)>=2:
                                host.anydesk = "1"
                            else:
                                host.anydesk = "0"
                        if i['name'].lower().find('all process') == 0:
                            any_desk = i['lastvalue'].split('AnyDesk')
                            if len(any_desk)>=2:
                                host.anydesk = "1"
                            else:
                                host.anydesk = "0"
                        if i['name'].lower().find('time win sync') == 0:
                            time = i['lastvalue'].split('time.ut.ac.ir')
                            if len(time)>=2:
                                host.time_win_sync = "YES"
                            else:
                                host.time_win_sync = "NO"
                        if i['name'].lower().find('firewall status') == 0:
                            firewall = i['lastvalue'].split('EnableFirewall')[1].split('REG_DWORD')[1].split('0x1')
                            if len(firewall)>=2:
                                host.firewall = "ON"
                            else:
                                host.firewall = "OFF"
                        if i['name'].lower().find('smb config') == 0:
                            smb = i['lastvalue'].split('EnableSMB1Protocol')[1].split('EnableSMB2Protocol')[0].split('True')
                            if len(smb)>=2:
                                host.smb1_config = "Enable"
                            else:
                                host.smb1_config = "Disable"

                    except IndexError:
                        continue
                    #if i['name'].encode('utf-8').lower().find('all open port')==0:
                     #   host.open_ports = i['lastvalue'].encode('utf-8')

                host.save()


    except Exception as e:
        print (e)


class Command(BaseCommand):
    def handle(self, **options):
        get_items()
