FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED = 1

WORKDIR /albergue_mascotas

COPY librearias.txt librearias.txt
RUN pip install -r librearias.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
