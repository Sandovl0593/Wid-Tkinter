import pytube as pt
import os, os.path as op
import requests
from bs4 import BeautifulSoup

def none(*args): pass

async def download_video(url: str, process: function = none, error: function = none):
    destinatation = "videos"

    if op.exists(f"./{destinatation}"):
        os.mkdir(destinatation)

    process("Descargando el video")

    try: 

        r = requests.get(url)
        soup = BeautifulSoup(r.text)

        link = soup.find_all(name="title")[0]
        title = str(link).replace("<title>","").replace("</title>","")
        title = "_".join(title.split(" ")[:20])

        yt_ins = pt.YouTube(url)
        
        await yt_ins.streams.get_highest_resolution() \
              .download(output_path=destinatation, filename=f"{title}.mp4")

    except:
        error("No se pudo descargar el video")