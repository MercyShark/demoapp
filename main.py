from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World from rishabh's backend app version star kid!"}

@app.get("/config")
def read_config():
    my_name = os.getenv("TEST_ENV_NAME", "Default Name")
    return {"message": f"Hello {my_name} from the backend app!"}

