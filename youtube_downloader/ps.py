from pytube import YouTube

yt_video = YouTube("https://www.youtube.com/watch?v=961uG4Ixg_Y")
yt_video = yt_video.streams.get_highest_resolution()
yt_video.download()
