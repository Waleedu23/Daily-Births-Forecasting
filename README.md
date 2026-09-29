# BirthCast FastAPI Backend

Complete backend for the supplied React frontend.

## Run on Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload --port 8000
```

Swagger: http://127.0.0.1:8000/docs

## Endpoints

- POST /api/auth/register
- POST /api/auth/login
- POST /api/forecast (Bearer JWT required)
- GET /health

## Database

SQLite is used by default. Users and forecast records are persisted in `birthcast.db`.

## ML model

The project includes a genuine scikit-learn RandomForestRegressor using lag, rolling-window, calendar, and trend features, with recursive multi-day forecasting.

Important: the bundled data generator is a reproducible demonstration because the original article's exact CSV is not included here. Replace `DailyBirthsModel.data()` with the article's historical daily-births dataset to reproduce the article's data/results. Do not present the demo results as the article's exact results.

## Production

Use PostgreSQL, HTTPS, a strong secret, restricted CORS, rate limiting, refresh-token rotation, migrations, and model/version monitoring before public deployment.
