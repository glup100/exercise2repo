from fastapi import FastAPI, HTTPException
from math_functions import add, subtract, multiply, divide
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World", "value": str(add(random.randint(0, 10), random.randint(11, 30)))}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}