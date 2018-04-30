
from django.conf.urls import url, include
from django.contrib import admin
from crudbuilder import urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
