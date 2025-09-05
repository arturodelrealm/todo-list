FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Comamand to run on server
 CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
