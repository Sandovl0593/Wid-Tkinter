from internal import *
from tkinter import ttk

url_text = tk.StringVar()

async def download_video_ui():
    from videoyt import download_video

    await download_video(url_text.get(), message_show, message_close)


button_load = tk.Button(frame, text="Descargar", command=download_video_ui)
button_load.pack(side=BOTTOM)


label = tk.Label(frame, text="Inserta un video de youtube:")
label.pack(fill=X, expand=1)

entry = ttk.Entry(frame, textvariable=url_text)
entry.place(x=50, y=50)


button_exit = tk.Button(frame, text="Salir", command=window.destroy)
button_exit.pack(side=BOTTOM)


window.mainloop()