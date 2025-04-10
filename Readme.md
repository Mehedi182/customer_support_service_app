# Help Request Form (Customer Support Portal)

A lightweight Django-based web application designed for submitting customer support or help requests via a user-friendly web form. It incorporates both server-side and client-side validation, along with a responsive design.

### Key Features
- Collects essential support details: name, email, issue category, and description.
- Implements server-side validation using Django Forms.
- Enhances security with client-side JavaScript validation.
- Provides a responsive layout with basic CSS styling.
- Displays clear and user-friendly error messages.
- Uses the built-in SQLite database for simplicity and ease of setup.

### Local Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Mehedi182/customer_support_service_app.git
    cd customer_support_service_app
    ```

2. **Create a Virtual Environment and Install Dependencies**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Apply Database Migrations**:
    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser for the Admin Panel**:
    ```bash
    python manage.py createsuperuser
    ```

5. **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the Application**:
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

7. **Access the Admin Panel**:
    Open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) in your browser.

### To Run Using Docker

To run the application using Docker:

1. **Build and Start the Docker Container**:
    ```bash
    docker-compose up --build
    ```

2. **Stop and Clean Up**:
    ```bash
    docker-compose down
    ```
### Live Application

The application is live and accessible at: [http://172.187.178.63/](http://172.187.178.63/)