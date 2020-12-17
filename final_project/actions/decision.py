import random
from random import randint

from final_project.actions.comment import *
from final_project.actions.like import *


def decision(probability: float):
    """Function that gives you a decision based on a given probability
    :param probability: float between 0 and 1
    :type: float
    :return: True or False
    :rtype: bool
    """
    if random.random() < probability:
        print("You know what let's do it...")
        return True

    else:
        print("We will pass for this time...")
        return False


def select_from_list(items: list, how_many: int):  # pragma: no cover
    """Function that randomly select multiple items from a list
    :param items: list of items
    :param how_many: int representing number of items to select
    :return: randomly selected sample of items
    :rtype: list
    """
    return random.sample(items, how_many)


def how_many_acct(accounts: list):  # pragma: no cover
    """Function that decides how many acct should be selected.
    This will help ensure that not too many accounts are selected.
    Also, this will enable to ensure that the bot doesn't run for hours (not human-like.
    :param
    :return: number of accounts to select
    :rtype: int
    """
    list_length = len(accounts)

    if list_length > 1000:
        # This number can be change depending on your needs
        # Recommend settings =< 20
        how_many = randint(5, 20)

    else:
        # Returns a number between 1% to 5% of the list length
        how_many = int(list_length * random.uniform(0.01, 0.03))

    return how_many


def random_likes_comments(
    tgt_obj: str, detected_obj: list, comment_list: list
):  # pragma: no cover

    count_likes = 0
    count_comments = 0

    if detected_obj is None:
        # Object detection will already tell the user if it didn't detect anything
        return [count_likes, count_comments]

    elif tgt_obj in detected_obj:

        # Randomly sleeps 2 to 5 seconds
        # Slows down a bit the process to be more human-like
        sleep(randint(2, 5))

        # To randomly decide to like or not
        print("Should we like?...")
        if decision(0.80):
            lk = like()
            # Adding to likes counter if like() returns 1
            count_likes += lk

            # To randomly decide to comment or not
            # With the condition that the picture was not already liked
            print("Should we comment?...")
            if lk == 1 and decision(0.50):
                # Randomly choose one comment from the provided list
                text_comment = random.choice(comment_list)

                # Posting comment
                post_comment(text_comment)

                # Adding to comments counter
                count_likes += 1

                # FOR FUTURE VERSION: CHECK IF THE COMMENT HAS BEEN USED JUST BEFORE
                # AVOID POSTING TWICE IN A ROW THE SAME COMMENT

                # ALSO, COULD POTENTIALLY HAVE USER DEFINE HOW OFTEN THEY WANT
                # THE COMMENT TO BE POSTED AND THIS WOULD BE ON A SCALE FROM 1 to 5

        return [count_likes, count_comments]

    else:
        # Let know the user that the target object wasn't present in the media
        print("No", tgt_obj, "detected in the picture.")
        return [count_likes, count_comments]
