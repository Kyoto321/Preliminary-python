from django import forms
from django.forms import TextInput, EmailInput

class PollingResultForm(forms.Form):
    polling_unit_uniqueid = forms.CharField()
    

class UserInfoForm(forms.Form):
    #result_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    polling_unit_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Polling Unit', 'style': 'width: 300px;', 'class': 'form-control'}))
    part_abbreviation = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Party', 'style': 'width: 300px;', 'class': 'form-control'}))
    party_score = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Party Score', 'style': 'width: 300px;', 'class': 'form-control'}))
    entered_by_user = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Polling Agent', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_entered = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'Date', 'style': 'width: 300px;', 'class': 'form-control'}))
    user_ip_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    