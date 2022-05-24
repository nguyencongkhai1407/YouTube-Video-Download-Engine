from tkinter import *
from tkinter import filedialog

# Set up the GUI
screen = Tk()
title = screen.title(
    'YouTube Downloader'
)
canvas = Canvas(screen, width=500, height= 500)
canvas.pack()

# Youtube Logo
logo = PhotoImage(file= 'youtube_logo.png')
# Resize the image
logo = logo.subsample(2,2)

canvas.create_image(250, 80, image = logo)

# Link field and label
link_field = Entry(screen, width = 50)
link_label = Label(screen, text = "Enter Download Link:", font = ('Arial', 15))

# download button
download_btn = Button(screen, text = "Download File")

# Select path to save the file to
path_label = Label(screen, text = "Select Path For Download", font = ('Arial', 15))
select_btn = Button(screen, text = "Select")

# Add link field and label to window
canvas.create_window(250, 170, window = link_label)
canvas.create_window(250, 220, window = link_field)
canvas.create_window(250, 280, window = path_label)
canvas.create_window(250, 300, window = select_btn)
canvas.create_window(250, 330, window = download_btn)

screen.mainloop()