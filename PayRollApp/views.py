from django.shortcuts import redirect, render # type: ignore

from PayRollApp.forms import EmployeeForm
from PayRollApp.models import Employee # type: ignore

# Create your views here.
def EmployeesList(request):
    # Employees= Employee.objects.all()
    Employees = Employee.objects.select_related("EmpDepartment", "EmpCountry").all()
    print(Employees.query)
    TemplateFile="PayRollApp/EmployeesList.html"
    Dict= {"Employees": Employees}
    return render(request, TemplateFile, Dict)


def EmployeeDetails(request, id):
    # employee= Employee.objects.get(id=id)
    Employees = Employee.objects.select_related("EmpDepartment", "EmpCountry").all().filter(id=id)

    TemplateFile="PayRollApp/EmployeeDetails.html"
    Dict= {"Employee": Employees[0]}
    return render(request, TemplateFile, Dict)

def EmployeeDelete(request, id):
    Employees = Employee.objects.select_related("EmpDepartment", "EmpCountry").all().filter(id=id)

    # employee= Employee.objects.get(id=id)
    TemplateFile="PayRollApp/DeleteEmployeePage.html"
    Dict= {"Employee": Employees[0]}

    if request.method == "POST":
        Employees.delete()
        return redirect("EmployeesList")
    return render(request, TemplateFile, Dict) 


def EmployeeUpdate(request, id):
    # employee= Employee.objects.get(id=id)
    employee = Employee.objects.select_related("EmpDepartment", "EmpCountry").all().filter(id=id)

    TemplateFile="PayRollApp/EmployeeUpdate.html"

    for emp in employee:
        # form = EmployeeForm(instance=employee)
        form = EmployeeForm(instance=emp)
        Dict= {"form": form}


    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
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



























