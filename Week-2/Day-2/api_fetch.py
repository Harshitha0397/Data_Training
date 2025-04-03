import requests

def fetch_data(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes (e.g., 404, 500)
        data = response.json()  # Parse JSON response
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    return None

if __name__ == "__main__":
    # Example API endpoint; you may choose an alternate free API like JSONPlaceholder
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    result = fetch_data(api_url)
    
    if result:
        print("Fetched API Data:")
        print(result)
    else:
        print("Failed to fetch data from the API.")