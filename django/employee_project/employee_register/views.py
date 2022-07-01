from django.shortcuts import render

from employee_project.employee_register.forms import EmployeeForm
from .forms import EmployeeForm
# Create your views here.

def employee_list(reqest):
    return render(request, "employee_register/employee_list.html")

def employee_form(reqest):
    form = EmployeeForm()
    return render(request, "employee_register/employee_form.html",{'form':form})

def employee_delete(reqest):
    return