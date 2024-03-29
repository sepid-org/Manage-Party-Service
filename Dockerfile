# pull official base image
FROM python:3.9

# set work directory
WORKDIR /app

RUN pip install --upgrade pip

# copy requirements
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# copy project
COPY . /app/

RUN adduser sepid

RUN mkdir -p /app/logging && chown -R sepid /app/logging \
	&& mkdir -p /app/staticfiles && chown -R sepid /app/staticfiles \
	&& mkdir -p /app/media && chown -R sepid /app/media

RUN chown -R sepid /app/

USER sepid

RUN python manage.py collectstatic --noinput
