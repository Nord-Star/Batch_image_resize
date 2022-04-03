import os  # library for 'open files' dialog
import PIL  # library to wok with images
from PIL import Image  # library to wok with images
import PySimpleGUI as sg  # Interface library


def resize_img(basewidth = 640, baseheight = 480):
    for jpg_image in jpg_images:
        if jpg_image.endswith('.jpg'):  # check if it is a jpg-file
            img = Image.open(jpg_image)  # open the file
            img_size = img.size  # read the size of the file

            # check if the image is horizontal or vertical
            if img_size[0] > img_size[1]:
                new_width = basewidth  # new width will be = 640
                # calculate the height
                new_height = img_size[1] / (img_size[0] / basewidth)
            elif img_size[1] >= img_size[0]:
                new_height = baseheight  # new heght will be = 480
                # calculate the width
                new_width = img_size[0] / (img_size[1] / baseheight)
            # resize the image
            resized_image = img.resize((int(new_width), int(new_height)),
                                       PIL.Image.ANTIALIAS)
            # give a name to a resized file and save it
            new_name = jpg_image.split('.')[0] + '_resized.jpg'
            resized_image.save(new_name)


# Interface
window = sg.Window('Batch image resize').Layout([
    [sg.Input(key='_FILES_'), sg.FilesBrowse()],
    [sg.Ok(), sg.Exit()]
    ])

while True:
    event, values = window.Read()
    jpg_images = values['_FILES_'].split(';')  # get the names of files
    if event == sg.WIN_CLOSED or event == 'Exit':  # exit the application
        break
    else:
        resize_img()

window.close()
