import pygame

def play_audio(filename):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1)  # -1表示循环播放

    while True:
        pass  # 让程序持续运行，直到手动停止

if __name__ == "__main__":
    audio_file = "t3.wav"
    play_audio(audio_file)
