from django.contrib import admin
from .models import Place
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PlaceAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Place
        fields = '__all__'


class PlaceAdmin(admin.ModelAdmin):
    form = PlaceAdminForm


admin.site.register(Place, PlaceAdmin)
