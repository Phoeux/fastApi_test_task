FROM python:latest

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


#RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
#ADD ./requirements.txt .
#RUN pip install -r requirements.txt
#RUN sudo mkdir src
#ADD ./src src
#WORKDIR src
#User user