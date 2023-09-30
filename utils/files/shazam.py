from shazamio import Shazam
import asyncio

shazam = Shazam()
async def shazamtop(name):
  out = await shazam.recognize_song(name)
  title = out['track']['title']
  artist = out['track']['subtitle']
  try:
      lyric = out['track']['sections'][1]['text']
      lyrics = '<b>'
      for i in lyric:
          lyrics += i + '\n'
      lyrics += '</b>'
  except:
      lyrics = None
  return {'title':title,'artist':artist,'lyrics':lyrics}

