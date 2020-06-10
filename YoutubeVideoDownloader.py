from pytube import YouTube

base_url = "https://www.youtube.com/watch?v=" # base url of any youtube video so user does not have to enter anything but the video ID
video_id = input("Enter YouTube video ID: ")
full_url = base_url + video_id

path = '.\Desktop' # the path to download the video to

yt = YouTube(full_url)

title = yt.title
print(title)

stream = yt.streams.get_highest_resolution()
stream.download()
