import requests
import json

BASE_URL = "https://h-dhub-bypass-api.vercel.app"
HEADERS = {"Content-Type": "application/json"}

def test_find():
    url = f"{BASE_URL}/find"
    target = "https://4khdhub.dad/love-through-a-prism-series-5331/"
    payload = {"url": target}

    print(f"[*] Testing {url}...")
    try:
        resp = requests.post(url, json=payload, headers=HEADERS, timeout=30)
        print(f"    Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            print(f"    Title: {data.get('title')}")
            print(f"    Type: {data.get('type')}")
            print(f"    Total Links: {data.get('total_links')}")
            print("\n--- Sample Links ---")
            for link in data.get("links", [])[:5]:
                print(f"    [{link.get('category')}] {link.get('quality')} | {link.get('size')} | {link.get('host')}")
        else:
            print(f"    Error: {resp.text[:300]}")
    except Exception as e:
        print(f"    Exception: {e}")

if __name__ == "__main__":
    test_find()
