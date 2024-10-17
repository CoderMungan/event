# Event Reminder Project

This project is an event reminder application that allows users to create, update, and delete events. It uses JWT-based authentication and takes Turkey's timezone (+3 hours difference) into account.

## Steps to Run the Project

### 1. Install Required Dependencies

Install the project dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### 2. Set Up the `.env` File

```bash
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgres://user:password@localhost:5432/your_database_name
```

### 3. Set Up the Database

Go to the [NEON](https://neon.tech) And create your free postgresql database.

Add the `DATABASE_URL` to `.env` file

Run the database migrations to create the necessary database tables:

```bash
python manage.py migrate
```

### 4. Create a Superuser

Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### 5. Start the Server

```bash
python manage.py runserver
```

Once the server starts successfully, the project will be available at http://127.0.0.1:8000/ on your local machine.

# API Endpoints

## User Authentication (JWT)

- Obtain Token (Login):

```bash
POST /api/user/token/
```

- Refresh Token:

```bash
POST /api/user/token/refresh/
```

## User Operations

- User List: Retrieves all users

```bash
GET /api/user/list/
```

## Event Operations

- Event List and Create: List all events and create a new event

```bash
GET /api/events/
POST /api/events/
```

- Event Detail, Update, and Delete: Retrieves, updates, or deletes a specific event.

```bash
GET /api/events/<int:pk>/
PUT /api/events/<int:pk>/
PATCH /api/events/<int:pk>/
DELETE /api/events/<int:pk>/
```

- Upcoming Events: Lists events happening within the next 24 hours.

```bash
GET /api/events/upcoming/
```

- Events by Category: Lists events based on a specific category.

```bash
GET /api/events/category/<str:category>/
```

### Extras

If u want the delete past events every 1 min with checker u can be active the cronjob.

`apps/events/cronjob.py`
`apps/events/jobs.py`
`apps/events/apps.py`

have the comment line. just add it.

Have fun with the project!
