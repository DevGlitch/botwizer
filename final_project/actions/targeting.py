from final_project.actions.decision import *
from final_project.actions.follow import *
from final_project.actions.post import *
from final_project.actions.search import *
from final_project.actions.user_data import *
from final_project.yolo.img_objects import *


def target_hashtags(tgt_hashtag: list, tgt_obj: str, comment_list: list):
    """ Auto liking and commenting on user defined hashtags and object."""

    counting_likes = 0
    counting_comments = 0

    for hashtag in tgt_hashtag:

        # Go the page of the specific tag
        search_hashtag(hashtag)
        # p.hashtag_page(hashtag)  # Can also be used but less human-like

        # Open the first post in the page
        open_first_post()

        # From Instagram: "Recent posts from all hashtags are temporarily hidden to help prevent
        # the spread of possible false information and harmful content related to the election."

        # Due to this Instagram "block" for the moment we will be using all 9 posts that are
        # the only ones available to see. As soon as the block is removed then we can randomize
        # the total number of post to view as well as randomize how many time we click next_post()
        # and even randomize even more by not liking everytime there is the target object. Until then
        # it is best to keep it the way it is below.

        # Randomly choose the total number of post to view
        # post_countdown = randint(9, 20) - DO NOT USE FOR THE MOMENT (SEE UPPER)
        post_countdown = 8  # = total of 9 as this doesn't include the first opened post

        # Running until it reaches 0
        while post_countdown != 0:

            # Check the type of media
            post_video = is_post_a_video()

            if post_video is True:
                # Only getting the first frame of the video
                media = get_vid()

            else:
                # Getting image from the post
                media = get_img()

            detected_obj = img_object_detection(media)

            # Randomly liking and commenting on pictures
            actions = random_likes_comments(
                tgt_obj=tgt_obj,
                detected_obj=detected_obj,
                comment_list=comment_list,
            )

            # Updating counting
            l, c = actions
            counting_likes += l
            counting_comments += c

            # Counting down
            post_countdown -= 1

            # Going to next post
            next_post()

        # Closing the last opened post
        close_post()

    return [counting_likes, counting_comments]


def target_accounts(tgt_acct: list, tgt_obj: str, comment_list: list):
    """ Auto liking, commenting, and following on user defined accounts and object."""

    counting_likes = 0
    counting_comments = 0
    following = []

    for acct in tgt_acct:

        # Going to target account profile
        search_account(acct)

        # Get followers list of targeted account
        acct_followers = get_followers()

        # Randomly decides how many accounts we want to access
        how_many = how_many_acct(acct_followers)

        # Randomly selecting accounts in the list
        print("Randomly selecting a list of accounts...")
        selected_acct = select_from_list(items=acct_followers, how_many=how_many)

        # Randomly accessing account in the list based on a random maximum number
        for acct_name in selected_acct:

            # Access each single selected accounts
            search_account(acct_name)

            # Follow this specific account
            follow()

            # Open first post of this specific account
            try:
                open_first_post()

            # This is in case the account is private
            # Basically not possible to see posts and open
            except NoSuchElementException:
                continue

            # Checking a random number of posts for each accounts
            # This range can be changed. Recommended setting is < 5
            post_countdown = randint(2, 4)

            while post_countdown != 0:

                # Check the type of media
                post_video = is_post_a_video()

                if post_video is True:
                    # Only getting the first frame of the video
                    media = get_vid()

                else:
                    # Getting image from the post
                    media = get_img()

                detected_obj = img_object_detection(media)

                # Randomly liking and commenting on pictures
                actions = random_likes_comments(
                    tgt_obj=tgt_obj,
                    detected_obj=detected_obj,
                    comment_list=comment_list,
                )

                # Updating counting
                l, c = actions
                counting_likes += l
                counting_comments += c

                # Counting down
                post_countdown -= 1

                # Going to next post
                next_post()

    # Save list of people the bot just followed
    save_following(following)

    return [counting_likes, counting_comments]
