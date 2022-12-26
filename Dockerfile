
FROM python:3.8
WORKDIR /usr/src/app
COPY . .
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR ./project
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000