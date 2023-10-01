import requests
import json

async def instadownloader(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "5af05fa5fdmsh92e2f2c2d0849bdp1f99ccjsn2f4010a76d64",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)
    print(rest)

    result_dict = {}
    if None in rest:
        return result_dict
    else:
        if rest['Type'] == 'Post-Image':
            result_dict['Type'] = 'image'
            result_dict['media'] = rest['media']
        elif rest['Type'] == 'Carousel':
            result_dict['Type'] = 'carousel'
            result_dict['media'] = rest['media']
        elif rest['Type'] == 'Post-Video':
            result_dict['Type'] = 'video'
            result_dict['media'] = rest['media']
        elif rest['Type'] == 'Story-Video':
            result_dict['Type'] = 'story'
            result_dict['media'] = rest['media']
        return result_dict



class InstaDownloader():
    def __init__(self,video_link):
        self.video_link = video_link

    def DownloadReelPost(self):
        import requests,json
        headers = {
            'authority': 'sssinstagram.com',
            'method': 'POST',
            'path': '/r',
            'scheme': 'https',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'identity',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uz;q=0.6',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'random_n=eyJpdiI6IkxxUlJub0RCNk9La0g4MWxKQmdrT1E9PSIsInZhbHVlIjoiemRWYUoxUGhPQzR1bjV4NHNoQnJGQ0t0b1NPRUMxT0xRT24rSThVc2pRMkV2bjJzb3JHVy9zdjJKYmhGVU1rRCIsIm1hYyI6ImVkM2I5ZjhjMGE1ZTMyN2U5YmFmNWQ3ZTQyMjMwMTVjYmFjZmZkMDkzYjM2ODhlNjNhYTVjNDFhZWU4ZGQxZjciLCJ0YWciOiIifQ%3D%3D; _gid=GA1.2.153804415.1695495118; _ga_90WCZ6NHEE=GS1.1.1695495118.1.0.1695495118.0.0.0; _ga=GA1.2.1799749594.1695495118; XSRF-TOKEN=eyJpdiI6ImdJYStrbXJxZnFsUU44bWE5ZGZNL3c9PSIsInZhbHVlIjoiUG1LWGFpRDJneDJVUm9wT09iMGhDUmNlbGZKTnlWMUd4akEza05lRXprUnNrdnhyVlRNV0d4UkhIOXI2MGtDc1NaaW0wWklRQkx2Qm5pUVd6czVtVUNNTHhvQkhhSDRhQmU3Z2d2Z3JpMVZMTk5WZE5oa2FwV1VYZUd1OC9sNFYiLCJtYWMiOiJkOGI1ZDgzMWJkOWQyYjNhOWMyZWZmZWJjNDg0MTE5YjdjNDAxNTdiYTc5OWYxNDBlOGM4NTU0MThlZDRiYjZlIiwidGFnIjoiIn0%3D; sssinstagram_session=eyJpdiI6IlVMS1NCMTdDc1E5ZVpFeDZQSXR0T3c9PSIsInZhbHVlIjoielg3NnB4c3VFV1I2WktQQU52aGVNczliOTJ5alFhcUFSS1IvQTVkSWFNdmx2WWdYd3RqdXFRL1JkazN1TjBFZWExNkhxaTFLY2NkeDFaMWUzaHVsdjNwcUoyMGY5dDhtUEhsSW5Sek0yWkZVNSs3QTVoWlZDcEtSM2lwUHJBTk0iLCJtYWMiOiIyZDgxYzEyMTI5ZGNkYTNiYWY4NzY3MjExZDJhYjg5N2Q4N2UzYTk5MGVjMTU5ZGRhZTI4YWJlNGE2MjE3MzYzIiwidGFnIjoiIn0%3D; _gat_UA-3524196-4=1; _ga_CN2Z3TL83Y=GS1.2.1695495120.1.1.1695495233.60.0.0',  # Replace with your actual cookies
            'Origin': 'https://sssinstagram.com',
            'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',  # Replace with your actual user-agent
            'X-Requested-With': 'XMLHttpRequest',
            'X-Xsrf-Token': 'eyJpdiI6ImdJYStrbXJxZnFsUU44bWE5ZGZNL3c9PSIsInZhbHVlIjoiUG1LWGFpRDJneDJVUm9wT09iMGhDUmNlbGZKTnlWMUd4akEza05lRXprUnNrdnhyVlRNV0d4UkhIOXI2MGtDc1NaaW0wWklRQkx2Qm5pUVd6czVtVUNNTHhvQkhhSDRhQmU3Z2d2Z3JpMVZMTk5WZE5oa2FwV1VYZUd1OC9sNFYiLCJtYWMiOiJkOGI1ZDgzMWJkOWQyYjNhOWMyZWZmZWJjNDg0MTE5YjdjNDAxNTdiYTc5OWYxNDBlOGM4NTU0MThlZDRiYjZlIiwidGFnIjoiIn0=',  # Replace with your actual XSRF token
        }

        payload = {
            'link': self.video_link,
            'token': ''
        }

        url = 'https://sssinstagram.com/r'
        response = requests.post(url, json=payload, headers=headers)
        # print(response.text)

        if response.status_code == 200:
            result_photo = []
            result_video = []
            result = {}
            
            data = json.loads(response.text)
            
            if data["data"]["items"][0]["urls"][0]["extension"] == "mp4":
                for i in data["data"]["items"][0]["urls"]:
                    result_video.append(i['urlDownloadable'])

                # Natijani lug'atga o'zgartiring
                result['type'] = 'video'

                result['video'] = result_video

                return result

            elif data["data"]["items"][0]["urls"][0]["extension"] == "webp":
                for i in data["data"]["items"][0]["urls"]:
                    result_photo.append(i['url'])
                    
                # Natijani lug'atga o'zgartiring
                result['type'] = 'photo'
                result['photo'] = result_photo
                return result

        else:
            return None

    def DownloadStoryHigh(self):
        import requests,json
        headers = {
            'authority': 'sssinstagram.com',
            'method': 'POST',
            'path': '/r',
            'scheme': 'https',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'identity',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uz;q=0.6',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'random_n=eyJpdiI6IkxxUlJub0RCNk9La0g4MWxKQmdrT1E9PSIsInZhbHVlIjoiemRWYUoxUGhPQzR1bjV4NHNoQnJGQ0t0b1NPRUMxT0xRT24rSThVc2pRMkV2bjJzb3JHVy9zdjJKYmhGVU1rRCIsIm1hYyI6ImVkM2I5ZjhjMGE1ZTMyN2U5YmFmNWQ3ZTQyMjMwMTVjYmFjZmZkMDkzYjM2ODhlNjNhYTVjNDFhZWU4ZGQxZjciLCJ0YWciOiIifQ%3D%3D; _gid=GA1.2.153804415.1695495118; _ga_90WCZ6NHEE=GS1.1.1695495118.1.0.1695495118.0.0.0; _ga=GA1.2.1799749594.1695495118; XSRF-TOKEN=eyJpdiI6ImdJYStrbXJxZnFsUU44bWE5ZGZNL3c9PSIsInZhbHVlIjoiUG1LWGFpRDJneDJVUm9wT09iMGhDUmNlbGZKTnlWMUd4akEza05lRXprUnNrdnhyVlRNV0d4UkhIOXI2MGtDc1NaaW0wWklRQkx2Qm5pUVd6czVtVUNNTHhvQkhhSDRhQmU3Z2d2Z3JpMVZMTk5WZE5oa2FwV1VYZUd1OC9sNFYiLCJtYWMiOiJkOGI1ZDgzMWJkOWQyYjNhOWMyZWZmZWJjNDg0MTE5YjdjNDAxNTdiYTc5OWYxNDBlOGM4NTU0MThlZDRiYjZlIiwidGFnIjoiIn0%3D; sssinstagram_session=eyJpdiI6IlVMS1NCMTdDc1E5ZVpFeDZQSXR0T3c9PSIsInZhbHVlIjoielg3NnB4c3VFV1I2WktQQU52aGVNczliOTJ5alFhcUFSS1IvQTVkSWFNdmx2WWdYd3RqdXFRL1JkazN1TjBFZWExNkhxaTFLY2NkeDFaMWUzaHVsdjNwcUoyMGY5dDhtUEhsSW5Sek0yWkZVNSs3QTVoWlZDcEtSM2lwUHJBTk0iLCJtYWMiOiIyZDgxYzEyMTI5ZGNkYTNiYWY4NzY3MjExZDJhYjg5N2Q4N2UzYTk5MGVjMTU5ZGRhZTI4YWJlNGE2MjE3MzYzIiwidGFnIjoiIn0%3D; _gat_UA-3524196-4=1; _ga_CN2Z3TL83Y=GS1.2.1695495120.1.1.1695495233.60.0.0',  # Replace with your actual cookies
            'Origin': 'https://sssinstagram.com',
            'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',  # Replace with your actual user-agent
            'X-Requested-With': 'XMLHttpRequest',
            'X-Xsrf-Token': 'eyJpdiI6ImdJYStrbXJxZnFsUU44bWE5ZGZNL3c9PSIsInZhbHVlIjoiUG1LWGFpRDJneDJVUm9wT09iMGhDUmNlbGZKTnlWMUd4akEza05lRXprUnNrdnhyVlRNV0d4UkhIOXI2MGtDc1NaaW0wWklRQkx2Qm5pUVd6czVtVUNNTHhvQkhhSDRhQmU3Z2d2Z3JpMVZMTk5WZE5oa2FwV1VYZUd1OC9sNFYiLCJtYWMiOiJkOGI1ZDgzMWJkOWQyYjNhOWMyZWZmZWJjNDg0MTE5YjdjNDAxNTdiYTc5OWYxNDBlOGM4NTU0MThlZDRiYjZlIiwidGFnIjoiIn0=',  # Replace with your actual XSRF token
        }

        payload = {
            'link': self.video_link,
            'token': ''
        }

        url = 'https://sssinstagram.com/r'
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            result_video = []
            result = {}
            
            data = json.loads(response.text)
            
            url_downloadable =  data["data"]["items"][0]["urls"][0]["url_downloadable"]
            for i in data["data"]["items"][0]["urls"]:
                result_video.append(i['url_downloadable'])
                result['story'] = result_video
                print(result)

                return result
        else:
            return None





# save = InstaDownloader("https://www.instagram.com/p/CxeFKjZIKw8/?utm_source=ig_web_copy_link")
# print(save.DownloadReelPost())


import requests,json
from bs4 import BeautifulSoup

class FastDLAppDownloader:
    def __init__(self):
        self.base_url = "https://fastdl.app/c/"
        self.headers = {
            "authority": "fastdl.app",
            "accept": "*/*",
            "accept-encoding": "identity",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://fastdl.app",
            "referer": "https://fastdl.app/",
            "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }

    def download_url(self, url):
        payload = {
            "url": url,
            "lang_code": "en",
            "token": ""
        }

        # try:
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 200 :
            soup = BeautifulSoup(response.text, 'html.parser')
            download_button = soup.find('a', attrs={'id':'download-btn'})['href']
            return download_button
        else:
            return f"{response.status_code}"