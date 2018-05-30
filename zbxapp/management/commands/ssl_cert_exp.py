from django.core.management.base import BaseCommand
from zbxapp.models import Server
import OpenSSL
import ssl
from datetime import timedelta, tzinfo

from datetime import datetime


def ssl_cert_exp():
    try:
        obj = Server.objects.get(name='pms-app')
        cert = ssl.get_server_certificate(('pms1.ut.ac.ir', 443))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        rawdate = x509.get_notAfter().decode('utf-8')
        year = rawdate[0:4]
        month = rawdate[4:6]
        day = rawdate[6:8]
        #dt = datetime(int(year), int(month), int(day))
        obj.ssl_cert_exp =str(year +'-'+month+'-'+day)
        obj.save()
    except Exception as e:
        print e


class Command(BaseCommand):
    def handle(self, **options):
        ssl_cert_exp()