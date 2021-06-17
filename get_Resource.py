import youtube_dl

with youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'outtmpl': 'current','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'wav','preferredquality': '192',}]}) as ydl:
	ydl.download(["https://www.youtube.com/watch?v=gfDE3eJP9vc"])
		
