web: PYTHONPATH=/home/matin/Desktop/current_project/chess/web_ui gunicorn web_ui.wsgi:application --bind 0.0.0.0:8000
api: uvicorn chess_engine.api.main:app --host 0.0.0.0 --port 8001