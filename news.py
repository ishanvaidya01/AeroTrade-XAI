import requests
import urllib.parse

def fetch_real_disruption(origin: str, destination: str) -> dict | None:
    # Build GDELT query with OR syntax for disruption keywords and required cities
    keywords = '("port strike" OR "shipping delay" OR "customs outage" OR "typhoon" OR "canal blockage" OR "trucking strike")'
    query_str = f'{keywords} "{origin}" "{destination}"'
    encoded_query = urllib.parse.quote(query_str)
    
    url = f"https://api.gdeltproject.org/api/v2/doc/doc?query={encoded_query}&mode=artlist&format=json&maxrecords=10"
    
    try:
        response = requests.get(url, timeout=3.0)
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])
            if articles:
                # Pick the first article (GDELT returns recent/relevant by default)
                article = articles[0]
                title = article.get("title", "Supply Chain Disruption Detected")
                url_link = article.get("url", "#")
                domain = article.get("domain", "News Source")
                
                # Derive a short name from the title
                short_name = " ".join(title.split()[:6]) + "..."
                
                description = f"{title} (Source: {domain})"
                
                return {
                    "name": short_name,
                    "description": description,
                    "url": url_link
                }
    except Exception:
        pass
        
    return None
