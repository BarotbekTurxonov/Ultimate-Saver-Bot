import requests

def searchYoutube(query):
    base_url = f"https://foydaliapi.uz/YouTubeqidir.php?search={query}"

    res = requests.get(url=base_url)

    results_dict = {}

    # Convert the JSON response to a dictionary
    js = res.json()

    for item in js['results']:
        title = item['title']
        link = item['url']
        results_dict[title] = link
    
    return results_dict

# yt = searchYoutube("onam")
# for title, link in yt.items():
#     print(f"Title: {title}")
#     print(f"Link: {link}")
