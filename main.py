from detect import is_phishing 

print("|==phishing detector==|")
url = input("Enter the URL to check: ").strip()
result = is_phishing(url)
if result:
    print("The URL is likely a phishing site.")
else:
    print("The URL is likely safe.")
print("|==end==|")