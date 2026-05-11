# Job Portal Project

A professional Django-based Job Portal application integrated with MongoDB Atlas.

## 🌐 Live Demo
https://jobportal-website-32oo.onrender.com

## Features
- User Registration & Login (Candidate/Recruiter)
- Job Posting and Management
- Job Application Tracking
- Admin Dashboard for User and Recruiter management
- Production-ready with WhiteNoise and Gunicorn

## Tech Stack
- **Framework**: Django 6.0.1
- **Database**: MongoDB Atlas (via `django-mongodb-backend`)
- **Static Files**: WhiteNoise
- **Deployment Server**: Gunicorn

## Local Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Jobportal
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add:
   ```env
   MONGODB_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/?appName=Cluster0
   MONGODB_NAME=jobportal_db
   DJANGO_SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=*
   ```

5. **Run Migrations**:
   ```bash
   python jobportal/manage.py migrate
   ```

6. **Start the Development Server**:
   ```bash
   python jobportal/manage.py runserver
   ```

## Deployment Instructions

This project is configured for deployment on platforms like Render, Railway, or Heroku.

### Environment Variables for Production
Ensure the following variables are set in your hosting provider's dashboard:
- `MONGODB_URI`: Your production MongoDB connection string.
- `MONGODB_NAME`: Your database name.
- `DJANGO_SECRET_KEY`: A secure, random string.
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: Your deployment domain (e.g., `jobportal.onrender.com`).

### Build Command
```bash
pip install -r requirements.txt && python jobportal/manage.py collectstatic --noinput
```

### Start Command
```bash
gunicorn --chdir jobportal jobportal.wsgi --log-file -
```
