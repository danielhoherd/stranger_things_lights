FROM python:3.7

WORKDIR /code

# We copy this first and install it to cache this operation ahead of other code changes
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]
CMD ["app.py"]
