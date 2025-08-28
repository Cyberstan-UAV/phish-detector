import re
import tldextract

def is_phishing(url):
    if "@" in url:
        return True
    if url.startswith("http://") or url.startswith("https://"):
        return True
    if url.count('-') > 3:
        return True
    if re.search(r'\d{1,3},?:\.\d{1,3}{3}', url):
        return True
    if len(url) > 75:
        return True
    
    ext = tldextract.extract(url)
    domain = ex.domain + '.' + ext.suffix
    if domain in ["exaple.com", "testsite.xyz",]:  #replace later with api call
        return True
    
    return False