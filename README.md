# Project definition
This is a well-balanced easy-to-use docker-compose app to serve rembg server on docker for small to large companies without paying any money! Totally Free.<br />
You can just configure your Linux server and install it using docker-compose or swarm, then you are free to remove the background of any picture you wish.<br />
It is also highly maintainable and we have increased Its observability using Grafana, Prometheus, and ...<br />
Integrated with Nvidia Container Toolkit for GPU usage to increase speed and performance.<br />

## Stack
1. Docker
2. Nginx
3. Rembg
4. Grafana
5. Cadvisor
6. Prometheus
7. Nginx Prometheus exporter

## Installation
1. `sh nvidia_container.sh`
2. `docker compose build`
3. `docker compose up -d`
   
Rembg: http://localhost<br />
Grafana: http://localhost/grafana<br />
Grafana-username: admin<br />
Grafana-password: admin<br />
