from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adres email'}))
    first_name = forms.CharField(label="", max_length=100, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię'}))
    last_name = forms.CharField(label="", max_length=100, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko'}))

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nazwa użytkownika'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Wymagana. 150 znaków lub mniej. Tylko litery, cyfry i @/./+/-/_ .</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Hasło'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Twoje hasło nie może być podobne do Twoich danych osobowych.</li><li>Twoje hasło musi zawierać co najmniej 8 znaków.</li><li>Twoje hasło nie może być często używanym hasłem.</li><li>Twoje hasło nie może zawierać wyłącznie cyfr</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Potwierdź hasło'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Wpisz to samo hasło w celu weryfikacji.</small></span>'


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię'}))
    last_name = forms.CharField(required=True, label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko'}))
    email = forms.CharField(required=True, label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adres email'}))
    phone = forms.CharField(required=True, label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numer telefonu'}))
    address = forms.CharField(required=True, label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adres'}))
    city = forms.CharField(required=True, label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Miasto'}))
    zipcode = forms.CharField(required=True, label="", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kod pocztowy'}))
    
    class Meta():
        model = Record
        exclude = ("user",)

 