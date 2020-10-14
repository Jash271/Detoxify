import re
import numpy as np
import os
from fastai.text import *
from fastai import *
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi import FastAPI, Form, status
import requests
from pydantic import BaseModel
from fastapi import Body, FastAPI
from fastai.text import load_learner
import fastai
import warnings

warnings.filterwarnings("ignore")

path = os.path.join(os.getcwd(), "export.pkl")

app = FastAPI()


origins = ["http://localhost", "http://localhost:8080", "*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    query: str


def clean_text(x):
    k = re.findall(r"[^!@#$%&*..()_+=?/;,\n]+", x)
    k = " ".join(k)
    return k


@app.post("/classify")
def classify(qstr: Query):
    k = qstr.query
    k = clean_text(k)

    learn = load_learner(".")
    res = learn.predict(k)
    r = str(res)
    print(r)
    p = r.split(", tensor")[2]
    i = r.split(", tensor")[1]
    i = re.findall(r"\w+", i)
    result = [int(x) for x in i]
    print(result)
    k = re.findall(r"[-+]?\d*\.\d+|\d+", p)

    score = [float(x) for x in k]
    label_cols = [
        "toxic",
        "severe_toxic",
        "obscene",
        "threat",
        "insult",
        "identity_hate",
    ]
    d = {}
    l = []

    for i in range(0, len(label_cols)):
        if result[i] == 1:
            l.append(label_cols[i])
            d[label_cols[i]] = score[i]

    final = {"result": r, "list": score, "dict": d}
    return final
