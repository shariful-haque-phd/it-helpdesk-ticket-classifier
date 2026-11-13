import argparse, joblib, re
def priority(text):
    s=text.lower()
    critical=any(k in s for k in ["entire company","all users","production down","security breach","ransomware"])
    high=any(k in s for k in ["blocked","cannot work","multiple users","entire team","urgent","unavailable"])
    if critical:return "P1"
    if high:return "P2"
    if any(k in s for k in ["slow","intermittent","error"]):return "P3"
    return "P4"
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("model"); ap.add_argument("text"); a=ap.parse_args()
    m=joblib.load(a.model); probs=m.predict_proba([a.text])[0]; classes=m.classes_
    best=probs.argmax()
    print({"category":classes[best],"category_confidence":round(float(probs[best]),4),"priority":priority(a.text)})
if __name__=="__main__":main()
