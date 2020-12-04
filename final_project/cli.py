import os
import shutil
import pandas as pd
from final_project.csci_utils.io.io import atomic_write
from final_project.actions.login import login, close_browser
from final_project.actions.data_folder import delete_folder, delete_file
from final_project.actions.search import search_general
from final_project.actions.pages import Pages as p
from final_project.actions.picture import open_first_post, next_post, close_post, get_img, get_vid
from final_project.actions.follow import follow, unfollow
from final_project.actions.like import like
from final_project.actions.comment import post_comment
from final_project.actions.login import driver
from final_project.yolo.img_objects import object_detection


def main():

    # Path of the user dashboard
    dashboard_path = "final_project/user/dashboard.xlsx"

    # Filename of dashboard parquet file
    dash_pqt = "final_project/data/dashboard/dashboard.parquet"

    # Deleting old parquet file
    # This will be improved in future versions
    if os.path.exists(dash_pqt):
        delete_file(dash_pqt)

    # Copying locally the excel file to a parquet file
    # This file will be used to retrieve some of its data
    with atomic_write(dash_pqt, mode="w", as_file=False) as f:

        # Read the dashboard excel file into a pandas DataFrame
        df = pd.read_excel(dashboard_path)
        # Get only the columns object, tags, and accounts
        df = df[["object", "tags", "accounts"]]
        # Drop rows that have all NaNs in it
        df = df.dropna(axis=0, how="all")
        # Drop row 0 that contains the name of the columns (see on excel file row 14)
        df = df.iloc[1:]
        # Convert to a parquet file format
        df.to_parquet(f)

    # Read the dashboard parquet file
    df = pd.read_parquet(dash_pqt)

    # Store each target type into a list (removing NaN if any)
    tgt_obj = df["object"].dropna().tolist()
    tgt_tag = df["tags"].dropna().tolist()
    tgt_acct = df["accounts"].dropna().tolist()

    # Showing the targets that the user provided
    print("##########################################"
          "\nThese are the targets you provided:"
          "\n\nTarget Object:", tgt_obj,
          "\n\nTarget Tags:", tgt_tag,
          "\n\nTarget Accounts:", tgt_acct,
          "\n\n##########################################"
          )

    # username = os.environ.get("username")
    # password = os.environ.get("password")
    #
    # # if .env are presents then ask user their secure salt
    # # if incorrect return error
    # # if correct decrypt variables for use in login
    #
    # login(username, password)
    #
    # # driver.get("https://www.instagram.com/p/CIEiasqBp9B/")
    # # p.account_page("cavalier.juzz")  # not really human like as it goes to a url and not using clicks
    #
    # # Object you want to target for liking, commenting, etc.
    # # Need to use at least one of the 80 COCO object labels
    # target_object = "dog"
    #
    # # Setting up counter
    # likes = 0
    # comments = 0
    # # img_countdown = 9
    #
    # # START FIRST FOR LOOP or WHILE? CHECKING LIST OF TAGS LEN OR SOMETHING
    # p.tag_page("cavalier")
    #
    # open_first_post()
    #
    # # START SECOND FOR LOOP
    # # check the type of media...
    # # if img then get_img() if vid then get_vid()
    # f = get_img()
    # g = object_detection(f)
    # if target_object in g:
    #     h = like()
    #     likes += h
    # else:
    #     print("No dog detected...")
    # next_post()
    # f = get_img()
    # g = object_detection(f)
    # if target_object in g:
    #     h = like()
    #     likes += h
    # else:
    #     print("No dog detected...")
    # # END SECOND FOR LOOP
    # # END FIRST FOR LOOP
    #
    # close_browser()
    #
    # delete_folder("images")
    #
    # # Printing summary of the run
    # print("\n################ SUMMARY ################\n")
    # print("Total of pictures liked = ", likes)
    # print("Total of comment posted = ", comments)
    # print("\n##########################################")
    #
    # # Check Chrome installed
    # # Get Chrome Version
    # # Install chromedriver based on Chrome version
    #
    # # add count to show how many pictures liked, commented, follow, etc.
    # # count = 0
    # # count = count + 1
    # # print(count)
    # # if count < > = X stop action go to next
    #
    # # Chrome option: add_argument("--headless")
