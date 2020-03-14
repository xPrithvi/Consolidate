import random
import shutil
import os

class Wallpaper:
    def __init__(self):
        pass

    def select_wallpaper(self):
        wallpaper_number = random.randint(1, 5)
        source_directory = "assets/" + str(wallpaper_number) + ".png"
        filename = str(wallpaper_number) + ".png" 
        destination_directory = "selected_wallpaper/"
        filename_directory = destination_directory + filename
        renamed_filename_directory = destination_directory + "selected_wallpaper.png"


        try:
            os.remove(renamed_filename_directory)
        except:
            pass
        shutil.copy(source_directory, destination_directory)
        os.rename(filename_directory, renamed_filename_directory)

