from django import forms
from django.contrib.auth.forms import UserChangeForm

from .models import City, Language, Vakation, Resume, Document


class findForm(forms.Form):
    class Meta:
        model=Vakation


    city=forms.ModelChoiceField(queryset=City.objects.all(),to_field_name='slug',required=False,
                                    widget=forms.Select(attrs={'class':'form-select'}))
    language = forms.ModelChoiceField(queryset=Language.objects.all(),to_field_name='slug',required=False,
                                      widget=forms.Select(attrs={'class':'form-select'}))





class resume_form(UserChangeForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(), to_field_name='slug', required=False,
                                  widget=forms.Select(attrs={'class': 'form-select'}))
    language = forms.ModelChoiceField(queryset=Language.objects.all(), to_field_name='slug', required=False,
                                      widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model=Resume
        fields=('name','phone_number','email','experience','education','city',
                'language','skills','profession','telegram_link','linked','about_meu')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )