FROM python
MAINTAINER Nick Smith "nsmith@amplience.com"
RUN apt-get update -y
RUN apt-get install -y wbritish
COPY . /bcm
WORKDIR /bcm
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["bcm.py"]