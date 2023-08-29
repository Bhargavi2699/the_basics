import lyricsgenius

# generate an api key and paste it
# https://genius.com/api-clients
genius = lyricsgenius.Genius("api-key-here")

# def save_lyrics(songs, artist_name, album_name):
#     for i in range(len(songs
#     )):
#         song_title = songs[i]
#         song = genius.search_song(song_title, artist_name)
#         lyrics = song.lyrics
#         with open('songs/{}/{}_{}_{}.txt'.format('_'.join(artist_name.split(' ')), i+1, album_name, '-'.join(''.join(song_title.split('\'')).split(' '))), 'w') as f:
#             f.writelines(lyrics.split('\\n'))

def save_lyrics(songs, artist_name, album_name):
    for i, song_title in enumerate(songs):
        song = genius.search_song(song_title, artist_name)
        
        if song:
            if song.lyrics:
                lyrics = song.lyrics
                with open(f'songs/{artist_name}_{album_name}_{song_title}.txt', 'w', encoding='utf-8') as f:
                    f.write(lyrics)
            else:
                print(f"Lyrics for '{song_title}' are empty.")
        else:
            print(f"Song '{song_title}' not found.")


if __name__ == '__main__':
    songs = [
        'the box',
        'down below',
        'project dreams',
        'die young',
        'boom boom room',
        'high fashion',
        'roll dice',
        'war baby',
        'every season'
    ]
    save_lyrics(songs, 'roddy ricch', '')
