import shutil
import os


def delete_folder(folder_name):
    """ Deletes a folder in folder "data" """

    folder_name = os.path.join("../final_project/data/", folder_name)

    try:
        shutil.rmtree(folder_name)
        print("Folder", folder_name, "successfully deleted.")

    except OSError as e:
        print("Error: %s : %s" % (folder_name, e.strerror))


def delete_file(filename):

    try:
        os.remove(filename)
        # print("File", filename, "successfully deleted.")

    except OSError as e:
        print("Error: %s : %s" % (filename, e.strerror))