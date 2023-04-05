import os
from mutagen.mp3 import MP3

def rename_files(folder_path):
    i = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            audio = MP3(file_path)
            artist = audio["TPE1"].text[0]
            album = audio["TALB"].text[0]
            title = audio["TIT2"].text[0]
            # remove special characters
            artist = artist.replace("/", "-").replace(":", "-").replace("*", "").replace("?", "")
            artist = ''.join(e for e in artist if e.isalnum() or e == "-")
            album = album.replace("/", "-").replace(":", "-").replace("*", "").replace("?", "")
            album = ''.join(e for e in album if e.isalnum() or e == "-")
            title = title.replace("/", "-").replace(":", "-").replace("*", "").replace("?", "")
            title = ''.join(e for e in title if e.isalnum() or e == "-")
            artist_folder = os.path.join(folder_path, artist, album)
            if not os.path.exists(artist_folder):
                os.makedirs(artist_folder)
            new_name = f"{title}.mp3"
            new_path = os.path.join(artist_folder, new_name)
            os.rename(file_path, new_path)
            print(str(i) +". "+ new_name + " Complete ✅")
            i=i+1

folder_path = "Download"
rename_files(folder_path)
