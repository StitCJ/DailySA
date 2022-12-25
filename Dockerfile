FROM lcj0417/DailySA:latest
RUN pip3 install django
WORKDIR /usr/src/app
WORKDIR ./DailySA
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000