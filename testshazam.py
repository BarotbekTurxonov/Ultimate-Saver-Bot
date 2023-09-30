import asyncio
# from shazamio import Shazam


# async def main():
#   shazam = Shazam()
#   out = await shazam.recognize_song('video.mp4')
#   print(out)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

from shazamio import Shazam

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



loop = asyncio.get_event_loop()
loop.run_until_complete(shazamtop("1.mp4"))