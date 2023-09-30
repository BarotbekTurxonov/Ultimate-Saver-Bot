import requests

def download_youtube_audio(youtube_url):
    try:
        full_url = f"https://saver-uz.onrender.com/youtube/download/audio/?url={youtube_url}"
        results_dict = {}
        response = requests.get(full_url)
        js = response.json()

        url = js['result']['1']['url']
        title = js['result']['1']['title']
        
        return {'url':url,"title":title}
        
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Example usage:
# youtube_url = "https://www.youtube.com/watch?v=QKTYAGHbU_c"
# response = download_youtube_audio(youtube_url)
# print(response)
    