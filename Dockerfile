FROM python:3.8
RUN pip install rembg[gpu,cli]
WORKDIR "/root"
EXPOSE 7000
VOLUME ["/root/.u2net"]
