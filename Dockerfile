 FROM python:3.6.7
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install --upgrade pip
 RUN pip install -r requirements.txt
 ADD . /code/
 RUN python -m nltk.downloader punkt