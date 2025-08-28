import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load the dataset
data = pd.read_csv('data/phishing_dataset.csv')

# Drop 'Index' column
data = data.drop(columns=['Index'])

# Separate features and target
X = data.drop(columns=['class'])
y = data['class']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save the model
os.makedirs('model', exist_ok=True)
joblib.dump(clf, 'model.pkl')

print("[+] Model trained and saved to 'model.pkl'")
