import pickle

from flask import Flask, jsonify, request
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression


app = Flask(__name__)


def _load_model(file_path:str):
    with open(file_path, "rb") as fp:
        return pickle.load(fp)


app.dv = _load_model("dv.bin")
app.model = _load_model("model2.bin")


@app.post("/score")
def score():
    req_body = request.json
    X = app.dv.transform(req_body)
    score = app.model.predict_proba(X)[0, 1]
    return jsonify({"score": score})
