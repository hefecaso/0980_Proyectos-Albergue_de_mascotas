FROM python:3.8

ENV PYTHONUNBUFFERED = 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install -r librearias.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "Albergue_mascotas", "Albergue_mascotas.wsgi:application"]
