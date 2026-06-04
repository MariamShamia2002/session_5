def clean_chess(df):
    df = df.copy()

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
    df = df.drop_duplicates()
    # Validation
    assert df['rating_diff'].notna().all()
    assert df.duplicated().sum() == 0

    return df

def clean_registry(df):
    df = df.copy()

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    # Clean usernames
    df['username'] = (
        df['username']
        .str.strip()
    )

    # Clean country names
    df['country'] = (
        df['country']
        .str.strip()
    )

    # Remove duplicate usernames
    df = df.drop_duplicates(subset=['username'])

    return df