from fastapi import FastAPI
from backend.analyzer import generate_insights
import pandas as pd

df=pd.read_csv("/Users/jiyaarora/Downloads/SampleSuperstore.csv")
app=FastAPI()

@app.get("/")
def home():
    return {
        "status":"running"
    }

@app.get("/insights")
def insights():
    return generate_insights(df)