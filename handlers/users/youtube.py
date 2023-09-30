import requests

class YouTube:
    def __init__(self, url):
        self.url = url
        self.headers = {
                "authority": "x2download.app",
                "method": "POST",
                "path": "/api/ajaxSearch",
                "scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "identity",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Length": "64",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie": ".AspNetCore.Antiforgery.O86muWubw_8=CfDJ8JNBRFsZlIVMlnSvprcwQBuVOp0n36B_rEFR_ctHiB-oGv7I8EOT4VKlD8dBRztYd5EqhE63DuYJFJfq6z05FHFwz3Sk0V_MMh0PaE327DBQlhqDiXj3WGEqdmNVgGRCxQaGBUDLl5YReV0sRf1uT3s; __cflb=0H28vzSfxwfQLrkLZtEtzroDaDVis4YgNhsuf6SW2KX",
                "Origin": "https://x2download.app",
                "Referer": "https://x2download.app/en93",
                "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
}

    def ForConvert(self):
        try:
            response = requests.post("https://x2download.app/api/ajaxSearch", headers=self.headers, data={"q":self.url, 'vt':'home'})
            if response.status_code == 200:
                vid =  response.json()['vid']
                fn = response.json()['fn']
                token = response.json()['token']
                timeExpires = response.json()['timeExpires']
                return f"{vid,fn,token,timeExpires}"
            
            else:
                return None

        except Exception as e:
            return f"An error occurred: {str(e)}"
        
    def Convert(self):
        medias = self.ForConvert()
        print(medias)
        headers_2 = {
                "authority": "dt162.dlsnap10.xyz",
                "method": "POST",
                "path": "/api/json/convert",
                "scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "identity",
                "Accept-Language": "uz,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6,ko;q=0.5",
                "Content-Length": "168",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://x2download.app",
                "Referer": "https://x2download.app/",
                "Sec-Ch-Ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
            }
        payload = {'v_id' : media[0], 'ftype':'mp4', 'fquality' : '480p', 'fname':media[1], 'token':media[2], 'timeExpire' : media[3]}
        response = requests.post("https://dt162.dlsnap10.xyz/api/json/convert", headers=headers_2, data=payload)
        if response.status_code == 200 :
            if response.json()['status'] == "success":
                download_link = response.json()['result']
                return download_link
        else:
            return None






# Example usage:
if __name__ == "__main__":
    app = YouTube("http://www.youtube.com/watch?v=jNQXAC9IVRw")
    media = app.ForConvert()
    url = app.Convert()
    print(url)