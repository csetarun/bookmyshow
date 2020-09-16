FROM python:3.7.4
RUN mkdir /code
ADD requirements.txt /code
RUN pip install -r /code/requirements.txt
ADD . /code
WORKDIR /code/bms
VOLUME /code

ENTRYPOINT bash -c "python manage.py migrate --noinput && python manage.py loaddata dashboard.json && python manage.py runserver 0.0.0.0:8000"