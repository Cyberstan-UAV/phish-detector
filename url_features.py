from urllib.parse import urlparse
import tldextract
import re
import socket

def extract_features(url):
    features = []

    # 1. UsingIP
    features.append(1 if re.match(r"^(http|https)://\d+\.\d+\.\d+\.\d+", url) else 0)

    # 2. LongURL
    features.append(1 if len(url) >= 75 else 0)

    # 3. ShortURL
    shortening_services = r"(bit\.ly|goo\.gl|shorte\.st|tinyurl|ow\.ly|t\.co|bitly)"
    features.append(1 if re.search(shortening_services, url) else 0)

    # 4. Symbol@
    features.append(1 if "@" in url else 0)

    # 5. Redirecting//
    features.append(1 if url.count('//') > 1 else 0)

    # 6. PrefixSuffix-
    features.append(1 if '-' in urlparse(url).netloc else 0)

    # 7. SubDomains
    netloc = urlparse(url).netloc
    features.append(1 if netloc.count('.') > 2 else 0)

    # 8. HTTPS
    features.append(1 if urlparse(url).scheme == 'https' else 0)

    # 9. DomainRegLen — placeholder (since we can’t access WHOIS here)
    features.append(1)  # 1 = short registration, 0 = long

    # 10. Favicon — placeholder
    features.append(1)

    # 11. NonStdPort
    port = urlparse(url).port
    features.append(1 if port and port not in [80, 443] else 0)

    # 12. HTTPSDomainURL
    features.append(1 if 'https' in urlparse(url).netloc else 0)

    # 13. RequestURL
    features.append(1 if re.search(r'\.(jpg|png|gif|ico)', url) else 0)

    # 14. AnchorURL
    features.append(1 if "#" in url else 0)

    # 15. LinksInScriptTags — placeholder
    features.append(1)

    # 16. ServerFormHandler — placeholder
    features.append(1)

    # 17. InfoEmail
    features.append(1 if "mailto:" in url else 0)

    # 18. AbnormalURL — placeholder
    features.append(1)

    # 19. WebsiteForwarding — placeholder
    features.append(1)

    # 20. StatusBarCust — placeholder
    features.append(1)

    # 21. DisableRightClick — placeholder
    features.append(1)

    # 22. UsingPopupWindow — placeholder
    features.append(1)

    # 23. IframeRedirection — placeholder
    features.append(1)

    # 24. AgeofDomain — placeholder
    features.append(1)

    # 25. DNSRecording — placeholder
    features.append(1)

    # 26. WebsiteTraffic — placeholder
    features.append(1)

    # 27. PageRank — placeholder
    features.append(1)

    # 28. GoogleIndex — placeholder
    features.append(1)

    # 29. LinksPointingToPage — placeholder
    features.append(1)

    # 30. StatsReport — placeholder
    features.append(1)

    return features