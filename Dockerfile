FROM python:3

RUN git clone laurldeturepositorio

COPY src carpeta

RUN  pip install tulibreria

WORKDIR /carpeta

CMD ["python3","-m","unittest"]