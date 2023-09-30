import asyncio
from shazamio import Shazam


async def ShazamIO(video_path:str):
	shazam = Shazam()
	out = await shazam.recognize_song(video_path)
	return out


