from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
from time import sleep

class Employee(models.Model):
    name = models.CharField(max_length=100)
    contract_end_date = models.DateField()

# Signal to demonstrate synchronous/asynchronous execution
@receiver(post_save, sender=Employee)
def employee_saved(sender, instance, **kwargs):
    print(f"Signal: Employee {instance.name} has been saved.")
    print(f"Current Thread: {threading.current_thread().name}")
    sleep(2)  # Sleep to simulate long-running task

    # Demonstrate database transaction
    if instance.name == "Error":
        raise Exception("Signal failed.")
