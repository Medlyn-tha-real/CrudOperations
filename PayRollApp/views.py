from django.shortcuts import redirect, render # type: ignore

from PayRollApp.forms import EmployeeForm
from PayRollApp.models import Employee # type: ignore

# Create your views here.
def EmployeesList(request):
    Employees= Employee.objects.all()
    TemplateFile="PayRollApp/EmployeesList.html"
    Dict= {"Employees": Employees}
    return render(request, TemplateFile, Dict)


def EmployeeDetails(request, id):
    employee= Employee.objects.get(id=id)
    TemplateFile="PayRollApp/EmployeeDetails.html"
    Dict= {"Employee": employee}
    return render(request, TemplateFile, Dict)

def EmployeeDelete(request, id):
    employee= Employee.objects.get(id=id)
    TemplateFile="PayRollApp/DeleteEmployeePage.html"
    Dict= {"Employee": employee}

    if request.method == "POST":
        employee.delete()
        return redirect("EmployeesList")
    return render(request, TemplateFile, Dict) 


def EmployeeUpdate(request, id):
    employee= Employee.objects.get(id=id)
    TemplateFile="PayRollApp/EmployeeUpdate.html"
    form = EmployeeForm(instance=employee)
    Dict= {"form": form}


    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect("EmployeesList")
    return render(request, TemplateFile, Dict)

def EmployeeInsert(request):
    TemplateFile="PayRollApp/EmployeeInsert.html"
    form = EmployeeForm()

    if request.method == "POST":
        form= EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("EmployeesList")
    return render(request, TemplateFile, {"form":form})



























