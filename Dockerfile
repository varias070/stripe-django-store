FROM python:3.8

RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN pip install .
RUN --mount=type=ssh git clone git@github.com:varias070/stripe-django-store.git
