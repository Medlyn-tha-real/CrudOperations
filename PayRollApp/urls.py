from django.urls import path # type: ignore

from PayRollApp import views

urlpatterns =[
    path("EmployeesList", views.EmployeesList, name="EmployeesList"),
    path("EmployeeDetails/<int:id>", views.EmployeeDetails, name="EmployeeDetails"),
    path("EmployeeDelete/<int:id>", views.EmployeeDelete, name="EmployeeDelete"),
    path("EmployeeUpdate/<int:id>", views.EmployeeUpdate, name="EmployeeUpdate"),
    path("EmployeeInsert", views.EmployeeInsert, name="EmployeeInsert"),

]













