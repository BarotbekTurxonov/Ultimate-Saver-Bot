import requests

def download_video(url, save_as):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        

        with open(f"{save_as}.mp4", 'wb') as video_file:
            video_file.write(response.content)
        
            return f"Video downloaded and saved as {save_as}"
    except Exception as e:
        return f"Error occurred: {str(e)}"

