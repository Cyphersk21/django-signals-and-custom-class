# Django Signals and Custom Classes

## Topic: Django Signals

### Question 1: Are Django signals executed synchronously or asynchronously by default?
**Answer:**
* By default, Django signals are executed **synchronously**. This means that the signal handler (receiver) is executed in the same flow as the calling function, and the program will wait for the signal to finish execution before proceeding.

**Proof with Code:**
```python
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)  # Simulate a delay
    print("Signal completed")
```
**Explanation:**

* When a new User object is saved, the post_save signal triggers the user_saved function. The time.sleep(5) introduces a delay of 5 seconds.
When you save the user in your view, the program will halt for 5 seconds before continuing, proving that the signal is executed synchronously.


### Question 2: Do Django signals run in the same thread as the caller?
**Answer:**
* Yes, by default, Django signals run in the same thread as the caller. Both the caller and the signal handler execute in the same thread unless explicitly handled otherwise (e.g., using asynchronous tasks).

**Proof with Code:**

```python
#signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# views.py
import threading
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_user_view(request):
    print(f"View running in thread: {threading.current_thread().name}")
    user = User.objects.create(username="test_user")
    return HttpResponse("User created!")
```
Explanation:

* Both the view function and the signal handler print the current thread's name. If both print the same thread name, it proves that they run in the same thread.


### Question 3: Do Django signals run in the same database transaction as the caller?
**Answer**
* Yes, Django signals run in the same transaction as the caller by default. If a signal is triggered during a transaction, it will be part of that transaction. If the transaction rolls back, the signal's changes will also be rolled back.

***Proof with Code:**

```python

# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    if kwargs.get('created', False):
        print(f"Signal executed inside the transaction: {transaction.get_autocommit()}")
```

**Explanation:**

* The signal handler checks if it is being executed inside a transaction by calling transaction.get_autocommit(). If it returns False, the signal is running inside the same transaction.

## Topic: Custom Classes in Python
### Task: Creating a Rectangle Class
* You need to create a Rectangle class that allows iteration over its length and width in a specific format.

```python

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Testing the Rectangle class
rect = Rectangle(10, 5)
for dimension in rect:
    print(dimension)
```

**Explanation:**

* The Rectangle class defines an __init__ method to initialize the length and width.
The __iter__ method allows iteration over the instance, first yielding the length and then the width.

