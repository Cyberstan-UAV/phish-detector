import sys
import joblib
import pandas as pd 
from url_features import extract_features

if len(sys.argv) != 2:
    print("usage: python check_url.py <url>")
    sys.exit(1)

url = sys.argv[1]

model = joblib.load('model.pkl')
features = extract_features(url)

X = pd.DataFrame([features])

prediction = model.predict(X)[0]

if prediction == 1:
    print("The URL is likely a phishing site.")
else:
    print("The URL is likely safe.")
print("|==end==|")

