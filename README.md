# Pipeline Dev Predictor

Magic 8-Ball predictor microservice for the msite application.

## Features

- Magic 8-Ball page at /
- Health check endpoint at /health/
- Hash-based consistent predictions
- Stateless service with no database requirements
- Whitenoise for static file serving

## Installation

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. Run development server:
   ```bash
   python manage.py runserver
   ```

5. Test endpoints:
   - Magic 8-Ball: http://localhost:8000/
   - Health: http://localhost:8000/health/

## Production Deployment

```bash
gunicorn predictor.wsgi:application --bind 0.0.0.0:8000
```

## How It Works

The Magic 8-Ball uses a hash-based algorithm to ensure consistency:
- Same question always returns the same answer
- Questions are normalized (case-insensitive, whitespace-trimmed)
- SHA256 hashing provides deterministic results
- 20 classic magic 8-ball responses

## Environment Variables

- `SECRET_KEY`: Django secret key (default: 'dev-secret-key')
- `DEBUG`: Enable debug mode (default: 'False')
- `ALLOWED_HOSTS`: Allowed hosts (default: '*')
