import sys
from final_project.actions.login import *
from final_project.actions.data_folder import *
from final_project.actions.pages import Pages as p
from final_project.actions.targeting import *
from final_project.actions.user_data import *
import time


def main():

    # Start timer
    time_start = time.perf_counter()

    # Path of the user dashboard
    dashboard_path = "final_project/user/dashboard.xlsx"

    # Filename of dashboard parquet file
    os.makedirs("data/dashboard", exist_ok=True)
    dash_pqt = "data/dashboard/dashboard.parquet"

    # Saving dashboard to parquet and formatting before use
    dash_data(file=dashboard_path, save_to=dash_pqt)

    # Read the dashboard parquet file
    df = pd.read_parquet(dash_pqt)

    # Store each target type into a list (removing NaN if any)
    tgt_obj = df["object"].dropna().tolist()
    tgt_obj = str(tgt_obj[1])
    tgt_hashtag = df["hashtags"][1:].dropna().tolist()
    tgt_acct = df["accounts"][1:].dropna().tolist()
    comments = df["comments"].dropna().tolist()
    comments = comments[1:]

    # Showing the dashboard settings that the user provided
    print(
        "##########################################"
        "\nThese are the settings you provided:\n"
        "\nTarget Object:",
        tgt_obj,
        "\nTarget Hashtags:",
        len(tgt_hashtag),
        "\nTarget Accounts:",
        len(tgt_acct),
        "\nComments:",
        len(comments),
        "\n\n##########################################",
    )

    # Requires a minimum of comments in order to run
    # 50 is the recommended minimum
    min_comments = 50
    if len(comments) < min_comments:
        # Close browser and stops the run
        # Also provide to the user an explanatory warning
        close_browser()
        raise sys.exit(
            f"WARNING: A minimum of {min_comments} comments are required in order for the bot to run."
        )

    # Requires a minimum of target hashtag or account in order to run
    # 1 is the recommended minimum
    min_lk_cmt = 1
    if len(tgt_hashtag) < 1 and len(tgt_acct) < 1:
        close_browser()
        raise sys.exit(
            f"WARNING: A minimum of {min_lk_cmt} target hashtag or account is required in order for the bot to run."
        )

    username = os.environ.get("username")
    password = os.environ.get("password")

    # Launching Instagram and login-in
    login(username, password)

    # p.account_page("thatdood_theodore")
    # open_first_post()
    # like()

    # Going to your profile
    p.your_account_page(username)

    # Get list of your followers
    your_followers = get_followers()
    total_followers = len(your_followers)

    # Filename of followers txt file
    os.makedirs("data/followers", exist_ok=True)
    fol_txt = "data/followers/followers.txt"

    # Saving followers list locally (if already exists just updating list)
    new_followers = save_followers(file=fol_txt, followers=your_followers)

    # Targeting hashtags - auto & randomly like and comment
    tag_likes, tag_comments = target_hashtags(
        tgt_hashtag=tgt_hashtag, tgt_obj=tgt_obj, comment_list=comments
    )

    # Targeting accounts - auto like, comment, follow
    acct_likes, acct_comments = target_accounts(
        tgt_acct=tgt_acct, tgt_obj=tgt_obj, comment_list=comments
    )

    # FOR FUTURE VERSION
    # Unfollowing randomly accounts
    # This will in the future ensure that we don't follow too many accounts
    # We could unfollow first the accounts not following us and that we started following a while back
    # This is possible only if we save the list of accounts we follow and save the date when we started following them
    # unfollowed = unfollowing(...)

    # Closing the browser session
    close_browser()
    # delete_folder("images")
    # delete_folder("videos")

    # Total of posts liked and commented
    likes = acct_likes + tag_likes
    comments = acct_comments + tag_comments
    # followed =  # FOR FUTURE VERSION
    # unfollowed =  # FOR FUTURE VERSION

    # Printing the summary of the run
    print("\n################ SUMMARY ################\n")
    print("Total of pictures liked = ", likes)
    print("Total of comments posted = ", comments)
    # print("Total of people followed = ", followed)  # FOR FUTURE VERSION
    # print("Total of people unfollowed = ", unfollowed)  # FOR FUTURE VERSION
    print("Total of followers = ", total_followers)
    print("Total of new followers since last run = ", new_followers)
    print("\n##########################################")

    # Stop timer
    time_stop = time.perf_counter() - time_start

    # Convert run time to minutes if needed
    if time_stop > 120:
        time_stop = time_stop / 60
        print(f"The bot ran for: {time_stop:.2f} minutes")
    else:
        print(f"The bot ran for: {time_stop:.2f}s")
