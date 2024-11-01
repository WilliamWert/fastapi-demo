#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Tom Brady": "is the GOAT"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
	return {"product": c * d}

@app.get("/square/{e}")
def square(e: int):
	return {"squared value": e * e}

@app.get("/pi")
def pi():
	return {"First 10 digits of pi": 3.1415926535}
