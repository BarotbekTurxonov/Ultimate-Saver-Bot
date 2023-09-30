import requests
import json

def TikTokDownlaoder(url):
    # URL and payload
    endpoint_url = "https://lovetik.com/api/ajax/search"
    payload = {
        "query": url
    }

    # Request headers
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "identity",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uz;q=0.6",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "_ga=GA1.1.1833214182.1695580123; _ga_30X9VRGZQ4=GS1.1.1695580122.1.1.1695580300.0.0.0",
        "Origin": "https://lovetik.com",
        "Referer": "https://lovetik.com/ru/video/@couple.pg/7249460976632761602",
        "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    # Send the POST request
    response = requests.post(endpoint_url, data=payload, headers=headers)

    # Check the response
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        data = dict(data)

        
        # Format and print the JSON response with indentation
        pretty_json = json.dumps(data, indent=4)
        # print(pretty_json)
        
        return data['links'][0]['a']
    else:
        return None

# Example usage:
# url_to_send = input("link > > ")
# result = send_post_request(url_to_send)
# print(result)