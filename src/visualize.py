import pandas as pd
from clean_data import clean_chess
import os
import matplotlib.pyplot as plt
from openpyxl import chart
os.makedirs("output/plots", exist_ok=True)

chess_df = pd.read_csv('data/raw/chess_games.csv')
# Clean data (creates rating_diff, opening_family, etc.)
chess_df = clean_chess(chess_df)

# 1. Bar chart — Winner counts
chess_df['winner'].value_counts().plot(kind='bar')

plt.title('Winner Counts')
plt.xlabel('Winner')
plt.ylabel('Count')

plt.savefig('output/plots/winner_counts.png')
plt.close()

# 2. Scatter plot — Rating Difference vs Turns
plt.scatter(
    chess_df['rating_diff'],
    chess_df['turns']
)

plt.title('Rating Difference vs Turns')
plt.xlabel('Rating Difference')
plt.ylabel('Turns')

plt.savefig('output/plots/rating_diff_vs_turns.png')
plt.close()

# 3. Box plot — Turns by Victory Status
chess_df.boxplot(
    column='turns',
    by='victory_status'
)

plt.title('Turns by Victory Status')
plt.suptitle('')  # removes extra pandas title
plt.xlabel('Victory Status')
plt.ylabel('Turns')

plt.savefig('output/plots/turns_by_victory_status.png')
plt.close()