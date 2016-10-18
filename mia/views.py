from django.shortcuts import render
from django.views.generic import TemplateView
from django.http.response import HttpResponse
from .forms import BackupDBForm
from core import database_backup


# Create your views here.


class HomePage(TemplateView):
    template_name = 'mia/index.html'



class DBBackupView(TemplateView):
    template_name = 'mia/backup.html'

    def post(self, request, *args, **kwargs):
        backup_form = BackupDBForm(request.POST)
        if backup_form.is_valid():
            db_host = backup_form.cleaned_data.get("db_host")
            db_name = backup_form.cleaned_data.get("db_name")
            db_user = backup_form.cleaned_data.get("db_user")
            db_pass = backup_form.cleaned_data.get("db_pass")

            zipfilename, in_memory_zip_file = database_backup.backup_database_server(db_user=db_user,
                                                                                     db_name=db_name,
                                                                                     db_password=db_pass,
                                                                                     db_host=db_host)
            if in_memory_zip_file:
                response = HttpResponse(in_memory_zip_file.getvalue(), content_type='application/x-zip-compressed')
                response['Content-Disposition'] = 'attachment; filename=%s' % zipfilename + ".zip"
                response['Content-Length'] = in_memory_zip_file.tell()
                return response
        else:
            return render(request, template_name=self.template_name, context={})


