<!-- DEPLOYMENT  -->

## Table of Contents

- [FastAPI-Prometheus-Grafana <a name = "about_the_project"></a>](#fastapi-prometheus-grafana-)
  - [Deployment <a name = "deployment"></a>](#deployment-)
  - [Contact <a name = "contact"></a>](#contact-)
  - [References <a name = "references"></a>](#references-)

---

<!-- ABOUT THE PROJECT -->

# FastAPI-Prometheus-Grafana <a name = "about_the_project"></a>

To deploy the FastAPI project with Prometheus metrics and Grafana.

<br/>

<!-- DEPLOYMENT -->

## Deployment <a name = "deployment"></a>

1. **Run** the FastAPI Python app

```python
uvicorn app:app
```

2. **Adjust** the **prometheus-config/prometheus.yml** [add job in the job section]
3. **Run** grafana and prometheus container: **docker-compose up**

<br/>

<!-- CONTACT -->

## Contact <a name = "contact"></a>

**Azizul Hakim Shakil** - [@ShakilAzizul](https://twitter.com/ShakilAzizul) - azizulhakim.shakil18@gmail.com

Project Link: [https://github.com/shakil18/Fastapi-Prometheus-Grafana](https://github.com/shakil18/Fastapi-Prometheus-Grafana)

<br/>

<!-- REFERENCES -->

## References <a name = "references"></a>

- [FastAPI](https://fastapi.tiangolo.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
