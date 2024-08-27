from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Employee


class Employeeform(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        lables = {
            'fullname': 'Full Name',
            'emp_code': 'Employee Code',
            'position': 'Position',
            'mobile': 'Mobile'
        }

