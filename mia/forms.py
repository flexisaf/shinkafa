from django import forms

__author__ = 'peter'


class BackupDBForm(forms.Form):
    db_host = forms.CharField()
    db_name = forms.CharField()
    db_pass = forms.CharField(widget=forms.PasswordInput())
    db_user = forms.CharField()
