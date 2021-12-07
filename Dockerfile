FROM python:3.7
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install flask

RUN mkdir -p /var/log/hmc

RUN ln -s /dev/stdout /var/log/hmc/hmc.log && \
    ln -s /dev/stderr /var/log/hmc/hmc.log

EXPOSE 8080

CMD ["python","main.py"]