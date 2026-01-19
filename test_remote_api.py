import requests
import json
import time

BASE_URL = "https://h-dhub-bypass-api.vercel.app"
HEADERS = {"Content-Type": "application/json"}

def log(msg):
    print(f"[*] {msg}")

def test_scrape():
    url = f"{BASE_URL}/scrape"
    # Use a known moviesmod/hdhub link
    target = "https://4khdhub.dad/are-you-here-movie-5381/"
    payload = {"url": target}

    log(f"Testing {url} with {target}...")
    try:
        start = time.time()
        resp = requests.post(url, json=payload, headers=HEADERS, timeout=30)
        dur = time.time() - start
        print(f"    Status: {resp.status_code} ({dur:.2f}s)")
        if resp.status_code == 200:
            data = resp.json()
            print(f"    Title: {data.get('title')}")
            print(f"    Batch Links: {len(data.get('batch', []))}")
            print(f"    Single Links: {len(data.get('singles', []))}")
        else:
            print(f"    Error: {resp.text[:200]}")
    except Exception as e:
        print(f"    Exception: {e}")
    print("-" * 30)

def test_bypass():
    url = f"{BASE_URL}/bypass"
    # GadgetsWeb link
    target = "https://gadgetsweb.xyz/?id=Q1dxTzFnbjhrQm5kMG5lL01tQzcvZzhmMjZOTkNrdktvSEp1VXBaU3FnZjZhRkRCdkxtZG5oY1NMak84L0xhWjNyVklCRlIwS1FQWENHbWprV1A5eGc9PQ=="
    payload = {"url": target}

    log(f"Testing {url}...")
    try:
        start = time.time()
        resp = requests.post(url, json=payload, headers=HEADERS, timeout=30)
        dur = time.time() - start
        print(f"    Status: {resp.status_code} ({dur:.2f}s)")
        if resp.status_code == 200:
            print(f"    Result: {json.dumps(resp.json(), indent=2)}")
        else:
            print(f"    Error: {resp.text[:500]}") # Show more for debug
    except Exception as e:
        print(f"    Exception: {e}")
    print("-" * 30)

def test_bypass_all():
    url = f"{BASE_URL}/bypass_all"
    target = "https://4khdhub.dad/love-through-a-prism-series-5331/"
    payload = {"url": target}

    log(f"Testing {url}...")
    try:
        start = time.time()
        resp = requests.post(url, json=payload, headers=HEADERS, timeout=60) # Long timeout
        dur = time.time() - start
        print(f"    Status: {resp.status_code} ({dur:.2f}s)")
        if resp.status_code == 200:
            data = resp.json()
            print(f"    Title: {data.get('title')}")
            # Count bypassed links
            total_bypassed = 0
            for item in data.get('batch', []):
                total_bypassed += len(item.get('direct_links', {}))
            print(f"    Total Bypassed Links: {total_bypassed}")
        else:
            print(f"    Error: {resp.text[:200]}")
    except Exception as e:
        print(f"    Exception: {e}")
    print("-" * 30)

if __name__ == "__main__":
    print("=== START API TEST ===\n")
    test_scrape()
    test_bypass()
    # test_bypass_all() # Optional, can be slow
    print("\n=== END API TEST ===")
