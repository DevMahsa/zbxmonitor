from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=500)
    hostid = models.CharField(max_length=500, null=True)
    ip=models.CharField(max_length=50,null=True)
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
    ssl_cert_exp = models.CharField(max_length=500, null=True)
    win_active = models.CharField(max_length=500, null=True)
    sql_login_user = models.CharField(max_length=500 , null= True)
    sql_xp_cmdshell= models.CharField(max_length=500 , null= True)
    sql_version = models.CharField(max_length=500 , null= True)
    sql_file_size = models.CharField(max_length=500 , null= True)
    open_port = models.TextField( null= True)
    windows_version = models.CharField(max_length=500 , null= True)
    anydesk = models.CharField(max_length=500 ,null= True)
    time_win_sync = models.CharField(max_length=500 ,null= True)
    microsoft_update = models.CharField(max_length=500 ,null= True)
    local_user = models.TextField( null= True)
    backup_name = models.TextField( null= True)
    smb1_config = models.CharField(max_length=500 ,null= True)
    eventlog_max_size = models.TextField(null=True)
    new_system_event = models.TextField(null=True)
    new_app_event = models.TextField(null=True)
    file_sharing_port = models.TextField(null=True)



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
