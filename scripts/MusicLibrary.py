#!user/bin/env python3
# -*- coding:utf-8 -*-


import pandas as pd

def listening_history(input_file):
    """
    Drops Redundant columns from the csv converted version of 'Apple Music Library Tracks.json'
    """

    pd.set_option("display.max_rows", None, "display.max_columns", None, 'display.expand_frame_repr', False)
    df = pd.read_csv('../input_data/MusicLib.csv')
    keep_cols=['Title', 'Artist', 'Album Artist', 'Album']
    df = df[keep_cols]

    print(df.describe())
    print(df.head())

    return df.to_csv('../preprocess_data/MusicLibrary.csv')


if __name__ == "__main__":
    listening_history('../input_data/MusicLib.csv')

