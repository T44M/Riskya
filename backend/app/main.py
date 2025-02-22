from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/weather/{lat}/{lon}")
async def get_weather(lat: float, lon: float):
    return {
        "location": {"lat": lat, "lon": lon},
        "weather": {
            "temp": 25.0,
            "humidity": 60,
            "risk": 30
        }
    }