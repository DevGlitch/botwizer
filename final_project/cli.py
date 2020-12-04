import os
import sys
import pandas as pd
from final_project.csci_utils.io.io import atomic_write
from final_project.actions.login import login, close_browser
from final_project.actions.data_folder import delete_folder, delete_file
from final_project.actions.pages import Pages as p
from final_project.actions.picture import open_first_post, next_post, close_post, get_img, get_vid, is_post_a_video
from final_project.actions.follow import follow, unfollow
from final_project.actions.like import like
from final_project.actions.comment import post_comment
from final_project.actions.decision import decision
from final_project.yolo.img_objects import object_detection
from time import sleep
from random import randint


def main():

    # __init__.py in actions will launch chrome with chromedriver
    # Chrome option: add_argument("--headless")

    # Path of the user dashboard
    dashboard_path = "final_project/user/dashboard.xlsx"

    # Filename of dashboard parquet file
    dash_pqt = "data/dashboard/dashboard.parquet"

    # Deleting old parquet file
    # This will be improved in future versions
    if os.path.exists(dash_pqt):
        delete_file(dash_pqt)

    # Copying locally the excel file to a parquet file
    # This file will be used to retrieve the data the user provided
    with atomic_write(dash_pqt, mode="w", as_file=False) as f:
        print("Loading user data...")
        # Read the dashboard excel file into a pandas DataFrame
        # df = pd.read_excel(dashboard_path, sheet_name="main")
        df = pd.concat(pd.read_excel(dashboard_path, sheet_name=None), ignore_index=True)
        # Get only the columns object, tags, and accounts
        df = df[["object", "hashtags", "accounts", "comments"]]
        # Drop any row that has only NaNs in it
        df = df.dropna(axis=0, how="all")
        # Drop row 0 that contains the name of the columns (see on excel file row 14)
        df = df.iloc[1:]
        # Convert to a parquet file format
        df.to_parquet(f)

    # Read the dashboard parquet file
    df = pd.read_parquet(dash_pqt)

    # Store each target type into a list (removing NaN if any)
    tgt_obj = df["object"].dropna().tolist()
    tgt_obj = str(tgt_obj[0])
    tgt_hashtag = df["hashtags"].dropna().tolist()
    tgt_acct = df["accounts"].dropna().tolist()
    comments = df["comments"].dropna().tolist()
    comments = comments[1:]

    # Requires a minimum of comments in order to run
    # 50 is the recommended minimum
    min_comments = 10
    if len(comments) < min_comments:
        # Close browser and stops the run
        # Also provide to the user an explanatory warning
        close_browser()
        raise sys.exit(f"WARNING: A minimum of {min_comments} comments is required in order for the bot to run.")

    # Showing the targets that the user provided
    print("##########################################"
          "\nThese are the targets you provided:\n"
          "\nTarget Object:", tgt_obj,
          "\nTarget Hashtags:", len(tgt_hashtag),
          "\nTarget Accounts:", len(tgt_acct),
          "\nComments provided:", len(comments),
          "\n\n##########################################"
          )

    username = os.environ.get("username")
    password = os.environ.get("password")

    # Launching Instagram and login-in
    login(username, password)

    # Setting up counter
    likes = 0
    comments = 0

    for hashtag in tgt_hashtag:

        # Go the page of the specific tag
        p.hashtag_page(hashtag)

        # Open the first post in the page
        open_first_post()

        # From Instagram: "Recent posts from all hashtags are temporarily hidden to help prevent
        # the spread of possible false information and harmful content related to the election."

        # Due to this Instagram "block" for the moment we will be using all 9 posts that are
        # the only ones available to see. As soon as the block is removed then we can randomize
        # the total number of post to view as well as randomize how many time we click next_post()
        # and even randomize even more by not liking everytime there is the target object. Until then
        # it is best to keep it the way it is below.

        post_countdown = 2

        # Running until it reaches 0
        while post_countdown != 0:

            # Check the type of media
            post_video = is_post_a_video()

            if post_video is True:
                pass
                # The video detection for the moment isn't fully working
                # I am trying to find a way to make the process faster
                # vid = get_vid()
                # vid_analyzed = vid_objects...

            else:
                img = get_img()
                img_analyzed = object_detection(img)

                if tgt_obj in img_analyzed:

                    # Randomly sleeps 2 to 5 seconds
                    sleep(randint(1, 5))

                    # To randomly decide to like or not
                    # 0.66 is the recommended setting
                    print("Should we like?...")
                    if decision(0.66):
                        lk = like()
                        # Adding to likes counter if like() returns 1
                        likes += lk

                        # To randomly decide to comment or not
                        # 0.33 is the recommended setting
                        print("Should we comment?...")
                        if decision(0.33):
                            # post_comment(text_comment)  # variable will be a str from comment list
                            comments += 1

                            # Should store the text_comment
                            # This way next run we can check to ensure next comment is not the same

                else:
                    print("No ", tgt_obj, "detected in the picture.")
                    pass

            # Counting down
            post_countdown -= 1

            # Going to next post
            next_post()

    # Closing the last opened post
    close_post()

    #########################################
    # ADD RANDOM FOLLOWERS OF TARGET ACCOUNTS
    # PLUS CHECK RANDOM NUMBER OF THEIR POST
    # IF TARGET OBJECT PRESENT THEN LIKE AND
    # SOMETIMES COMMENT
    #########################################
    # for i in tgt_acct:
    #     p.account_page(i)
    #     ...

    # Closing the browser session
    close_browser()

    # delete_folder("images")

    # # Printing the summary of the run
    # print("\n################ SUMMARY ################\n")
    # print("Total of pictures liked = ", likes)
    # print("Total of comment posted = ", comments)
    # # print("Total of people followed = ", followed)
    # # print("Total of people unfollowed = ", unfollowed)
    # # print("Total of new followers since last run = ", new_followers)
    # print("\n##########################################")
