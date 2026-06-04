import os
import pandas as pd

from load_data import load_data
from clean_data import clean_chess, clean_registry

def main():

    chess_df = pd.read_csv('data/raw/chess_games.csv'
    )

    registry_df = pd.read_csv(
        "data/raw/player_registry.csv"
    )

    chess_df = clean_chess(chess_df)
    registry_df = clean_registry(registry_df)

    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    chess_df.to_csv(
        "data/processed/chess_games_clean.csv",
        index=False
    )

    registry_df.to_csv(
        "data/processed/player_registry_clean.csv",
        index=False
    )

    print("Processed files saved.")


if __name__ == "__main__":
    main()
