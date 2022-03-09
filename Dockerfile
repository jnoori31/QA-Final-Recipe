FROM python:3
RUN mkdir /code/
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]