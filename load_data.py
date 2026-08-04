import pandas as pd

taylor_album_songs = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2023/2023-10-17/taylor_album_songs.csv')
taylor_all_songs = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2023/2023-10-17/taylor_all_songs.csv')
taylor_albums = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2023/2023-10-17/taylor_albums.csv')

print(taylor_album_songs.head())
print(taylor_album_songs.shape)