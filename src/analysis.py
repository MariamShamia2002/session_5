from src.clean_data import clean_chess
import pandas as pd

df = pd.read_csv('data/raw/chess_games.csv')

df = clean_chess(df)

print(df.head())