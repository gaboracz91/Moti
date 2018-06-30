release: ./release-tasks.sh
clock: python clock.py
web: gunicorn project.wsgi --name moti --workers 3 --access-logfile "-" --error-logfile "-"