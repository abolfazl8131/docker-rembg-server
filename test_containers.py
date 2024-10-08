import requests

def test_rembg_server():
    response = requests.get('http://localhost:7000')
    assert response.status_code == 200

def test_cadvisor_running():
    response = requests.get('http://localhost:8080')
    assert response.status_code == 200

def test_prometheus_running():
    response = requests.get('http://localhost:9090')
    assert response.status_code == 200

def test_nginx():
    response = requests.get('http://localhost:80/rembg')
    assert response.status_code == 200

    response = requests.get('http://localhost:80/grafana')
    assert response.status_code == 200