FROM python:3.9

WORKDIR /code

# We copy this first and install it to cache this operation ahead of other code changes
# which makes a huge difference on raspberry pi when it comes to compling modules.
COPY requirements.txt .
RUN pip install -r requirements.txt

env FLASK_APP app.py
env FLASK_ENV development

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
