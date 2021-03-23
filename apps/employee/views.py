from django.http import JsonResponse

from .models import Employee


def employee_list(request):
    employees = Employee.objects.all()
    data = {"results": list(employees.values("pk", "name", "salary"))}
    return JsonResponse(data)
