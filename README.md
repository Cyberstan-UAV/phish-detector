# phish-detector
an chrome extension for detecting PHISHING links 


Features
- Extracts and analyzes **50+ features** from URLs.  
- Uses **machine learning models** trained on phishing datasets.  
- Command-line interface (CLI) for quick detection.  
- Detects suspicious patterns such as:
  - URL length, presence of `@`, `//`, or `-` in domains.  
  - Use of HTTPS vs. HTTP.  
  - Domain age, subdomain count.  
  - External resource linking.
 
Clone the Repository
bash
-git clone https://github.com/Cyberstan-UAV/phish-detector.git cd phish-detector


cretae virtual environment 
bash:-
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)


install dependencies 
bash:-
pip install -r requirements.txt




Usage

Run the tool from terminal:

python main.py


Example:

python main.py --url https://example.com


Output:

[+] URL: https://example.com
[+] Result: Legitimate Website ✅

Dataset & Model

-Trained on phishing detection datasets from UCI ML Repository and Kaggle.
-Current model uses supervised learning (Random Forest / Logistic Regression).
-extracted 50 handcrafted features for detection.

Future Improvements

Web-based GUI for non-technical users.
Real-time browser extension integration.
Advanced ML models (XGBoost, Deep Learning).
Continuous dataset updates.

License
This project is licensed under the MIT License — free to use and modify.

 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

 Author

Cyberstan-UAV
GitHub Profile

 Cybersecurity & Defense Tech Enthusiast
