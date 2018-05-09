# use a Tkinter label as a panel/frame with a background image
# (note that Tkinter reads only GIF and PGM/PPM images)
# put a button on the background image

from tkinter import *

root = Tk()
root.title('background image')
# pick a .gif image file you have in the working directory
# or give full path to the image file

image = PhotoImage(file='undercover.gif')
# get the width and height of the image
# w = image.width()
# h = image.height()
w = 800
h = 600
# position coordinates of root 'upper left corner'
x = 600
y = 200
# size the root to fit the image
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
# tk.Frame has no image argument
# so use a label as a panel/frame
panel = Label(root, image=image)
panel.pack(side=TOP, fill=BOTH, expand='yes')
# put a button widget on the panel
# button = Button(panel, text='button widget')
# button.pack(side='top', pady=5)
# save the panel's image from 'garbage collection'
panel.image = image
# start the event loop
root.mainloop()