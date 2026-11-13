from pathlib import Path
import argparse, joblib, pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--model",default="ticket_model.joblib"); a=ap.parse_args()
    df=pd.read_csv(a.csv)
    model=Pipeline([("tfidf",TfidfVectorizer(ngram_range=(1,2))),("clf",LogisticRegression(max_iter=1000))])
    model.fit(df["text"].astype(str),df["category"].astype(str)); Path(a.model).parent.mkdir(parents=True, exist_ok=True); joblib.dump(model,a.model); print("saved",a.model)
if __name__=="__main__":main()
