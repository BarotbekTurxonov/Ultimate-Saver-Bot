from bs4 import BeautifulSoup
import requests

song = input("Enter song name: ")
base_url = f"https://api-v2.soundcloud.com/search/tracks?q={song}&variant_ids=&facet=genre&user_id=453404-199663-253172-634394&client_id=LF6OAAOD1pPvKtdzJmuQf6Be2yrcvwCp&limit=20&offset=0&linked_partitioning=1&app_version=1695900919&app_locale=en"
response = requests.get(base_url)
