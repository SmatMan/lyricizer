# Lyricizer - A Python Library to Communicate with [https://genius.com](Genius) without an API key. It makes use of a website scraper to obtain lyrics and (soon) searches.

## *Disclaimer:* This library was created for fun and is not a good alternative to the API. Due to it using a scraper, it has cooldowns that can and will block your usage in some cases. If you want to use this in a project, you should much rather use [https://pypi.org/project/lyricsgenius/](LyricsGenius), which requires an API key.

### Features included so far:
- Obtaining Lyrics from a Genius link

##### This library Requires:
- BeautifulSoup (bs4)
- urllib (urllib3)
- requests (requests)


### Example:

An example of obtaining song lyrics from a Genius link:
```
>>> from get_lyrics_from_link import searchFromLink
>>> output = searchFromLink("https://genius.com/Away-and-midoca-too-close-lyrics")
>>> print(output)

[Verse 1]
Take the long way back to me
...
```
It's that easy!
