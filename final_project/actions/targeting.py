from final_project.actions.search import *
from final_project.actions.post import *
from final_project.actions.decision import *
from final_project.actions.like import *
from final_project.actions.comment import *
from final_project.yolo.img_objects import *
from final_project.actions.user_data import *
from final_project.actions.follow import *
from random import randint, choice


def target_hashtags(tgt_hashtag: list, tgt_obj: str, comment_list: list):  # pragma: no cover
    """ Auto liking and commenting on user defined hashtags and object."""

    likes = 0
    comments = 0

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
                pass
                # The video detection for the moment isn't fully working
                # I am trying to find a way to make the process faster
                # vid = get_vid()
                # vid_analyzed = vid_objects...

            else:
                img = get_img()
                img_analyzed = img_object_detection(img)

                # if tgt_obj in img_analyzed is None:
                #    pass

                if img_analyzed is None:
                    pass

                elif tgt_obj in img_analyzed:

                    # Randomly sleeps 2 to 5 seconds
                    # Slows down a bit the process to be more human-like
                    sleep(randint(1, 5))

                    # To randomly decide to like or not
                    print("Should we like?...")
                    if decision(0.80):
                        lk = like()
                        # Adding to likes counter if like() returns 1
                        likes += lk

                        # To randomly decide to comment or not
                        # With the condition that the picture was not already liked
                        print("Should we comment?...")
                        if lk == 1 and decision(0.50):

                            # randomly choose a comment from the provided list
                            comment = choice(comment_list)

                            # Posting comment
                            post_comment(comment)

                            # Adding to comments counter
                            comments += 1

                            # FOR FUTURE VERSION: CHECK IF THE COMMENT HAS BEEN USED JUST BEFORE
                            # AVOID POSTING TWICE IN A ROW THE SAME COMMENT
                            # POTENTIALLY USER COULD DEFINE HOW OFTEN THEY WANT THE COMMENT
                            # TO BE POSTED AND THIS WOULD BE ON A SCALE FROM 1 to 5

                else:
                    print("No", tgt_obj, "detected in the picture.")
                    pass

            # Counting down
            post_countdown -= 1

            # Going to next post
            next_post()

        # Closing the last opened post
        close_post()

    return [likes, comments]


def target_accounts(tgt_acct: list, tgt_obj: str, comments: list):  # pragma: no cover
    """ Auto liking, commenting, and following on user defined accounts and object."""

    likes = 0
    comments = 0
    following = []

    for acct in tgt_acct:

        # Going to target account profile
        search_account(acct)

        # Get followers list of targeted account
        acct_followers = get_followers()

        # Randomly accessing account in the list based on a random maximum number
        ...

        # Checking a random number of posts for each accounts
        post_countdown = 3

        search_account(acct)
        ...
        #########################################
        # ADD RANDOM FOLLOWERS OF TARGET ACCOUNTS
        # PLUS CHECK RANDOM NUMBER OF THEIR POST
        # IF TARGET OBJECT PRESENT THEN LIKE AND
        # SOMETIMES COMMENT
        #########################################
        ...

        # Counting down
        post_countdown -= 1

        # Going to next post
        next_post()

    # Save list of people the bot just followed
    save_following(following)

    return [likes, comments]
