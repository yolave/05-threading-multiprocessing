import httpx


class ThirdPartyAPI:
    def fetch_data(self):
        response = httpx.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        return response.json()
