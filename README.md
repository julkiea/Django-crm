# Django CRM Applicstion 👥
This project is a CRM platform built with Django & Python. 

## Features ✨


## Installation 🔧

1. Clone the repository:
   
    ```bash
    git clone
    cd Django-to-do-site
    ```

2. Install `virtualenv`:
    ```bash
    pip install virtualenv
    ```

3. Create a new virtual environment:
    ```bash
    virtualenv virt
    ```

4. Activate the virtual environment:
    ```bash
    source virt/Scripts/activate
    ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Create a `.env` file in the project root directory and set your environment variables:
     ```bash
    # Example .env file
    SECRET_KEY=my_secret_key_value
    DEBUG=True
    ```
     
8. Generate a new secret key. You can use the following Python script to generate one:

   ```python
   import secrets
   print(secrets.token_urlsafe(50))


9. Apply migrations:
    ```bash
    python manage.py migrate
    ```

10. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

11. Run the development server:
    ```bash
    python manage.py runserver
    ```
