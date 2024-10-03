from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Employee
from .rectangle import Rectangle
import threading

def signal_test_view(request):
    employee = Employee.objects.create(name="John Doe", contract_end_date="2025-01-01")
    thread_name = threading.current_thread().name
    
    return JsonResponse({
        "message": f"Employee created and signal triggered.",
        "main_thread": thread_name
    })

def test_transaction_view(request):
    try:
        Employee.objects.create(name="Error", contract_end_date="2025-01-01")
    except Exception as e:
        return JsonResponse({"message": str(e)})

def test_rectangle_view(request):
    rect = Rectangle(10, 5)
    dimensions = [dim for dim in rect]

    return JsonResponse({"dimensions": dimensions})
