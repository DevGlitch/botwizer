import os
import pandas as pd
from csci_utils.io.io import atomic_write
from final_project.actions.data_folder import *


def dash_data(file: str, save_to: str):
    """ Get dashboard data, format to pd, saving relevant columns to a parquet file"""

    # Deleting old parquet file - This will be improved in future versions
    if os.path.exists(save_to):
        delete_file(save_to)

    # Copying locally the excel file to a parquet file
    # This file will be used to retrieve the data the user provided
    with atomic_write(save_to, mode="w", as_file=False) as f:
        print("Loading user data...")
        # Read dashboard excel sheets and merge them into one single pandas DataFrame
        df = pd.concat(
            pd.read_excel(file, sheet_name=["main", "comments"]),
            ignore_index=True,
        )
        # Get only the columns object, tags, and accounts
        df = df[["object", "hashtags", "accounts", "comments"]]
        # Drop any row that has only NaNs in it
        df = df.dropna(axis=0, how="all")
        # Drop row 0 that contains the name of the columns (see on excel file row 14)
        # df = df.iloc[1:]
        # Convert to a parquet file format
        df.to_parquet(f)


def save_following(following: list):
    """ Saving list of people bot followed in order to unfollow when needed """
    # FOR FUTURE VERSION
    ...
