from django import forms

from PayRollApp.models import Employee

# Creating a form based model
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

        widgets = {
            "BirthDate": forms.widgets.DateInput(attrs={'type': 'date'}),
            "HireDate": forms.widgets.DateInput(attrs={'type': 'date'}),
        }


























