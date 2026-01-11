class AudioPlayer:
    def play(self, audio_type: str, filename: str):
        if audio_type == "mp3":
            print(f"playing {filename} as MP3....")
        elif audio_type == "wav":
            print(f"playing {filename} as WAV....")
        else:
            raise ValueError(f"Unsupported format {audio_type}")


class AdvanceAudioPlayer:  # Adaptee
    def play(self, filename: str):
        print(f"playing {filename} as MP4....")


class MediaPlayer:  # target
    def play(self, audio_type: str, filename: str):
        raise NotImplementedError


class Mp4Adapter(MediaPlayer):
    def __init__(self, audio_player):
        self.__audio_player = audio_player

    def play(self, audio_type: str, filename: str):
        if audio_type == "mp4":
            self.__audio_player.play(filename)


if __name__ == "__main__":
    audio_player = AudioPlayer()
    audio_player.play("mp3", "hello.mp3")
    audio_player.play("wav", "call_recording.wav")
    # audio_player.play("mp4", "dhoom.mp4") # exception

    mp4_adapter = Mp4Adapter(AdvanceAudioPlayer())
    mp4_adapter.play("mp4", "dhoom.mp4")
