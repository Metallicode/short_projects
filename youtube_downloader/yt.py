from pytube import YouTube
from tqdm import tqdm
import threading

with open("videos2download.txt", "r") as f:
	lines = f.readlines()
	
def download_video(vid):
	vid.download()
	
for i in tqdm(range(len(lines))):
	yt_video = YouTube(lines[i], )
	yt_video = yt_video.streams.get_highest_resolution()
	t = threading.Thread(target=download_video, args=(yt_video,))
	t.start()

print('your video is downloaded successfully')
input()
