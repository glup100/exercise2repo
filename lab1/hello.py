from fastapi import FastAPI, HTTPException
from math_functions import add, subtract, multiply, divide
from pydantic import BaseModel
import random

app = FastAPI()

class Operation(BaseModel):
    x: float
    y: float

@app.get("/")
async def root():
    return {"message": "Hello World", "value": str(add(random.randint(0, 10), random.randint(11, 30)))}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

    @app.post("/add")
async def add_numbers(operation: Operation):
    try:
        result = add(operation.x, operation.y)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/subtract")
async def subtract_numbers(operation: Operation):
    try:
        result = subtract(operation.x, operation.y)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/multiply")
async def multiply_numbers(operation: Operation):
    try:
        result = multiply(operation.x, operation.y)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/divide")
async def divide_numbers(operation: Operation):
    try:
        result = divide(operation.x, operation.y)
        if isinstance(result, str):  # Check if the result is an error message
            raise HTTPException(status_code=400, detail=result)
        return {"result": result}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))