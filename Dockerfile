FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1 
WORKDIR /app
COPY requirements.txt .
COPY . . 
RUN pip3 install requirements.txt
EXPOSE 8000
CMD ["python", "runserver", "0.0.0.0:8000"]
