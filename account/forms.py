import datetime
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import PasswordInput, CharField, EmailField, DateTimeField, DateField, ModelForm
from django.forms.fields import ImageField
from django.forms.widgets import DateInput
from .models import User, Customer

def set_min_age_for_datefield():
    today = datetime.date.today()
    mat_year = today.year - 17
    date_pass = datetime.date(mat_year, today.month, today.day)
    return date_pass

class CustomerCreateForm(UserCreationForm):
    birth_date = DateField(initial=set_min_age_for_datefield, widget=DateInput(attrs={'type': 'date'}))
    photo = ImageField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'birth_date', 'photo']


class CustomeProfileForm(ModelForm):
    email = EmailField()
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'photo']
