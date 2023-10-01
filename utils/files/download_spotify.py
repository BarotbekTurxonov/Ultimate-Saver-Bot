import requests
from typing import List, Union

def DownloadMusic(UrlList: Union[List[str], str]):
    audio_urls = []

    if type(UrlList)!=list:
        return "required list"
    for i in UrlList:
        url = "https://api.spotify-downloader.com/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Accept": "*/*",
            "Accept-Encoding": "identity",
            "Accept-Language": "en-US,en;q=0.9,uz;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://spotify-downloader.com",
            "Referer": "https://spotify-downloader.com/",
            "Sec-Ch-Ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }

        data = {
            "link": i
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            try:
                json_data = response.json()
                audio_url = json_data['audio']['url']
                audio_name = json_data['name']
                audio_info = {
                    "name": audio_name,
                    "url": audio_url
                }
                audio_urls.append(audio_info)
            except KeyError:
                print(f"Error: Failed to extract audio URL from the response JSON for URL: {url}")
        else:
            print(f"Error: Request failed with status code {response.status_code} for URL: {url}")

    return audio_urls
