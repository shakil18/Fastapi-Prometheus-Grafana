from fastapi import FastAPI
from prometheus_client import Counter
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

# instrumentator = Instrumentator(
#     should_group_status_codes=False,
#     should_ignore_untemplated=True,
#     should_respect_env_var=True,
#     should_instrument_requests_inprogress=True,
#     excluded_handlers=[".*admin.*", "/metrics"],
#     env_var_name="ENABLE_METRICS",
#     inprogress_name="inprogress",
#     inprogress_labels=True,
# )
#
# instrumentator.add(
#     metrics.request_size(
#         should_include_handler=True,
#         should_include_method=False,
#         should_include_status=True,
#         metric_namespace="a",
#         metric_subsystem="b",
#     )
# ).add(
#     metrics.response_size(
#         should_include_handler=True,
#         should_include_method=False,
#         should_include_status=True,
#         metric_namespace="namespace",
#         metric_subsystem="subsystem",
#     )
# )

# instrumentator.instrument(app)


# creating a counter which tracks counts of events or running totals.
counter_test_metric = Counter("prometheus_test_counter", "Testing Prometheus with Fast API.")

# register the instrumentation with FastAPI instance => instrument(app), exposing endpoint (default endpoint '/metrics')
Instrumentator().instrument(app).expose(app)

@app.get("/")
def test():
    counter_test_metric.inc()
    return {"Hello Shakil!"}

@app.get("/test/")
def test():
    counter_test_metric.inc()
    return {"Hi, I'm test"}


#
# @app.get("/metrics")
# def metrics():
#     return Response(generate_latest(REGISTRY), media_type=CONTENT_TYPE_LATEST)
