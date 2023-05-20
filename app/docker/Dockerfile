FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PUTHONDONTWRITEBYTECODE 1

WORKDIR /django
COPY ./ /django
RUN pip install -q --upgrade pip
ENTRYPOINT ["/django/docker/entrypoint.sh"]
EXPOSE 8000