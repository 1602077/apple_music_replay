#!usr/bin/env python3
# -*- conding: utf-8 -*-

import pandas as pd


def preprocess(input_file):
    
    df = pd.read_csv(input_file, encoding='utf-8')

    df.columns = df.columns.str.replace("’","")
    print(f'input dataframe shape: {df.shape}.\n')

    cols_to_drop = ['Apple Music Subscription',
                    'Build Version',
                    'Content Provider',
                    'Event Reason Hint Type',
                    'Feature Name',
                    'Metrics Bucket Id',
                    'Provided Audio Bit Depth',
                    'Provided Audio Channel',
                    'Provided Audio Sample Rate',
                    'Provided Bit Rate',
                    'Provided Codec',
                    'Provided Playback Format',
                    'Store Country Name',
                    'Targeted Audio Bit Depth',
                    'Targeted Audio Sample Rate',
                    'Targeted Audio Channel',
                    'Targeted Codec',
                    'Targeted Playback Format',
                    'Users Audio Quality',
                    'Users Playback Format',
                    'UTC Offset In Seconds',
                    'Metrics Client Id',
                    'Offline',
                    'Source Type',
                    'Start Position In Milliseconds',
                    'Targeted Bit Rate'
    ]


    df.drop(columns=cols_to_drop, inplace=True)

    #filter for music listening only i.e. ignore radio streams
    df = df[df['Content Specific Type']=='Song']

    print(df.dtypes)
    print()
    print(df.head(10))
    print(f'\noutput dataframe shape: {df.shape}.')

    return df.to_csv('preprocess_data/listening_history_music_only.csv')


if __name__ == "__main__":
    preprocess("input_data/Apple_Music_Play_Activity.csv")
