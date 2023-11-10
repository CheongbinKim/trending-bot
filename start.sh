nohup gunicorn -k uvicorn.workers.UvicornWorker --access-logfile ./log/gunicorn-access.log app:app --bind 0.0.0.0:8000 --timeout 600 &
