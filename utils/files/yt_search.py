import requests

def searchYoutube(query, num_results=7):
    base_url = f"https://foydaliapi.uz/YouTubeqidir.php?search={query}"

    res = requests.get(url=base_url)

    results_list = []

    # Convert the JSON response to a list of dictionaries
    js = res.json()
    for item in js['results'][:num_results]:
        title = item['title']
        link = item['url']
        result_dict = {
            "title": title,
            "url": link
        }
        results_list.append(result_dict)
    
    return results_list

yt = searchYoutube("onam", num_results=5)
# for item in yt:
#     print(item)


# for title, link in yt.items():
#     print(f"Title: {title}")
#     print(f"Link: {link}")
