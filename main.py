from fastapi import FastAPI, Response
import os
from prometheus_client import Counter, Histogram, generate_latest

app = FastAPI()

REQUEST_COUNT = Counter("http_requests_total", "Total HTTP Requests")
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request latency")
@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    return {"message": "Hello World from rishabh's backend app version star kid!"}

@app.get("/config")
def read_config():
    my_name = os.getenv("TEST_ENV_NAME", "Default Name")
    return {"message": f"Hello {my_name} from the backend app!"}


@app.get("/slow")
def slow():
    with REQUEST_LATENCY.time():
        import time
        time.sleep(1)
    return {"msg": "slow"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")