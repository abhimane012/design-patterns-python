# Music Pattern

from abc import ABC, abstractmethod


class MusicPlayer:
    def __init__(self, implementation):
        self.implementation = implementation

    def play(self, song: str):
        self.implementation.play_song(song)


class MusicPlayerImplementation(ABC):
    def play_song(self, song: str):
        pass


class AppleMusic(MusicPlayerImplementation):
    def play_song(self, song: str):
        print(f"Playing song {song} on Apple Music")


class Spotify(MusicPlayerImplementation):
    def play_song(self, song: str):
        print(f"Playing song {song} on Spotify")


if __name__ == "__main__":
    apple_music = AppleMusic()
    spotify = Spotify()

    music_player = MusicPlayer(apple_music)
    music_player.play("Weekend")

    music_player = MusicPlayer(spotify)
    music_player.play("Waka Waka")
