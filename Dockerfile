FROM python:2.7
ENV PYTHONUNBUFFERED 1

EXPOSE 7777
RUN mkdir /config
  
ADD /config/requirements.pip /config/

WORKDIR /usr/src/python
RUN pip install -r /config/requirements.pip  
RUN mkdir /src;  
WORKDIR /src

ENV DATABASE_TYPE postgres
CMD [ "python", "manage.py", "runserver", "0.0.0.0:7777" ]
