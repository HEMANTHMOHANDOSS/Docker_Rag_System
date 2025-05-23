import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_docker_pages(base_url="https://docs.docker.com/engine/reference/commandline/"):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    anchors = soup.select('a[href^="/engine/reference/commandline/"]')

    links = set()
    for a in anchors:
        href = a.get('href')
        if href and href.endswith('/'):
            full_url = urljoin("https://docs.docker.com", href)
            links.add(full_url)

    # Always include the base page itself
    links.add(base_url)

    print(f"🔗 Found {len(links)} pages to load")
    return list(links)
