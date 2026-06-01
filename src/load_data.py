import pandas as pd
import os

def load_data(url, local_path):
    if os.path.exists(local_path):
        print(f"Loading from cache: {local_path}")
        return pd.read_csv(local_path)

    print(f"Downloading from {url}...")
    df = pd.read_csv(url)

    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    df.to_csv(local_path, index=False)

    return df

url1 = "https://drive.google.com/file/d/1eR3NZtwIC6ECN3vhtrynqmx8okG0twA7/view?usp=sharing"
url1 = "https://drive.google.com/uc?id=" + url1.split("/")[-2]

chess_df = load_data(
    url1,
    "data/raw/chess_games.csv"
)

url2 = "https://drive.google.com/file/d/1wCSAkGagMzWiToedLC3ZGo_lGf_laF-k/view?usp=sharing"
url2 = "https://drive.google.com/uc?id=" + url2.split("/")[-2]

player_registry_df = load_data(
    url2,
    "data/raw/player_registry.csv"
)