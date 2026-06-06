FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
FROM mcr.microsoft.com/playwright/python:v1.60.0
COPY . .
RUN mkdir -p logs
CMD ["pytest", "-v"]

