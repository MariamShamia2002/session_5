def clean_chess(df):

    df[['time_base', 'time_inc']] = (
        df['time_increment']
        .str.split('+', expand=True)
        .astype(int)
    )

    df['rating_diff'] = (
        df['white_rating']
        - df['black_rating']
    )

    df['opening_family'] = (
        df['opening_fullname']
        .str.split(':')
        .str[0]
        .str.strip()
    )

    df = df.drop(columns=['opening_response'])

    df['is_suspicious'] = (
        df['turns'] < 5
    )

    return df