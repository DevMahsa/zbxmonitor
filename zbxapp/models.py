from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateField(blank=True, null=True)
    firewall = models.CharField(max_length=500, null=True)
    mcafee = models.CharField(max_length=500, null=True)
    maxusedmemory = models.CharField(max_length=500, null=True)
    maxusedcpu = models.CharField(max_length=500, null=True)
    freediskc = models.CharField(max_length=500, null=True)
    freediskd = models.CharField(max_length=500, null=True)
    freediske = models.CharField(max_length=500, null=True)
    freediskf = models.CharField(max_length=500, null=True)
    freediskg = models.CharField(max_length=500, null=True)
    freediskh = models.CharField(max_length=500, null=True)
    freediski = models.CharField(max_length=500, null=True)
    telnet = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name






class LastMemory(models.Model):
    memory = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    server = models.ForeignKey(Server, related_name='memory')

    def __str__(self):
        return self.server.name


class LastCpu(models.Model):
    cpu = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    server = models.ForeignKey(Server, related_name='cpu')

    def __str__(self):
        return self.server.name
