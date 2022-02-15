FROM python:3.9

WORKDIR /proyectyara


COPY ./requirements.txt /proyectyara/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /proyectyara/requirements.txt


COPY ./ ./proyectyara


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]