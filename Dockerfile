FROM python:3.12
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH "${PYTHONPATH}:/code/app"
CMD ["fastapi", "run", "app/main.py", "--port", "8080"]