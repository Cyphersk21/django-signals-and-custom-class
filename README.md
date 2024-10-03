# Django Signals Project

This project demonstrates the usage of Django signals and answers common questions about their behavior, such as:

1. **Are Django signals executed synchronously or asynchronously by default?**
2. **Do Django signals run in the same thread as the caller?**
3. **Do Django signals run in the same database transaction as the caller?**

Additionally, this project includes a custom Python class that demonstrates the use of a `Rectangle` class that behaves like an iterable.

## Project Setup

To run this project, follow these steps:

### Prerequisites

- Python 3.x
- Django 4.x
- Git

### Installation

1. Clone this repository:

   ```bash
   git clone [https://github.com/Cyphersk21/django-signals-project.git](https://github.com/Cyphersk21/django-signals-and-custom-class.git)
2. Navigate to the project directory:
   ```bash
   cd django-signals-project
3. Create a virtual environment:
   ```bash
   python -m venv venv
4. Activate the virtual environment:
   
   * For Windows:
     ```bash
     venv\Scripts\activate
   * For macOS/Linux:
     ```bash
     source venv/bin/activate
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
6. Apply migrations to create the database schema:
   ```bash
   python manage.py migrate

###  Running the Project

To run the development server:
   ```bash
   python manage.py runserver
```

### Endpoints
   * **Test Signal Execution (Synchronous/Threading):**
   
     Endpoint: /signals/signal-test/
     This endpoint will trigger a signal when creating an Employee object and demonstrate whether signals run synchronously in the same thread.
   
   * **Test Database Transaction Behavior in Signals:**
   
     Endpoint: /signals/transaction-test/
     This endpoint will show if signals run within the same database transaction.
   
   * **Test Custom Rectangle Class:**
   
     Endpoint: /signals/rectangle-test/
     This endpoint tests the custom Rectangle class to show how it behaves as an iterable.




