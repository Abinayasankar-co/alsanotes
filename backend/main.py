from fastapi import FastAPI


app = FastAPI()


@app.get("/v1/health")
def app_health():
    return {"Alsa":'AlsaNotes is Healthy'}


