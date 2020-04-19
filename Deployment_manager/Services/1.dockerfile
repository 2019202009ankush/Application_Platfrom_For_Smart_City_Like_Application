FROM python:3.7-alpine
COPY . /src
WORKDIR /src CMD [' pyhton3 ',"Algorithm_Repo/Algorithm.py","Temperatue"]