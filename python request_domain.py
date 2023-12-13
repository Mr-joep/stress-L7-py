import requests

def request_domain(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        print(f"Request to {url} was successful.")
        print("Response content:")
        print(response.text)
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {url}: {e}")

if __name__ == "__main__":
    # Replace "https://example.com" with the desired domain
    domain_url = "http://192.168.154.139"
    
    # Make the request to the domain
    request_domain(domain_url)
