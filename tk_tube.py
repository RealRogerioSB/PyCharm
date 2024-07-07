import customtkinter as ctk
import tkinter as tk
from pytube import YouTube


def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        title.configure(text=yt_object.title, text_color="white")
        finish_label.configure(text="")
        video.download()
        finish_label.configure(text="Baixado!", text_color="green")
    except Exception:
        finish_label.configure(text="Deu erro...", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completed = bytes_downloaded / total_size * 100
    per = str(int(percent_completed))
    percent.configure(text=per + "%")
    percent.update()
    barra.set(float(percent_completed) / 100)


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("700x220")
app.title("YouTube Downloader")

title = ctk.CTkLabel(app, text="Insira um link de YouTube...")
title.pack(padx=10, pady=10)

url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finish_label = ctk.CTkLabel(app, text="")
finish_label.pack()

percent = ctk.CTkLabel(app, text="0%")
percent.pack()

barra = ctk.CTkProgressBar(app, width=400)
barra.set(0)
barra.pack(padx=10, pady=10)

download = ctk.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

if __name__ == '__main__':
    app.mainloop()
