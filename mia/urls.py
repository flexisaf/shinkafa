from django.conf.urls import url
from mia import views
__author__ = 'peter'


urlpatterns = [
    url(r'^backup/$', view=views.DBBackupView.as_view(), name="backup_db")
]
