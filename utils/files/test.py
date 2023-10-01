import base64, json
import requests
def GetToken():
    client_id = '93dfe93f21fb46aaad10947eadfde562'
    client_secret = '36bb6e205ff143c6aeab7c3eb9bafd3a'

    token_url = 'https://accounts.spotify.com/api/token'

    client_credentials = f'{client_id}:{client_secret}'
    base64_credentials = base64.b64encode(client_credentials.encode()).decode()

    headers = {
        'Authorization': f'Basic {base64_credentials}'
    }

    payload = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(token_url, headers=headers, data=payload)
    token = response.json().get('access_token')
    return token


def get_outh_header(token):
    return {"Authorization":"Bearer "+token}


def SearchMusic(token, query):
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=3&country=UZ"
    headers = get_outh_header(token)
    response = requests.get(url, headers=headers)

    json_result = json.loads(response.content)['tracks']['items']

    if len(json_result)==0:
        print("NOTHING TO FIND")
    
    return json_result[0]



token = GetToken()
musics = SearchMusic(token, "janze")
print(json.dumps(musics, indent=4, ensure_ascii=False))
print(musics[''])