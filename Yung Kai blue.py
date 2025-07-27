import time 
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)
    
def sing_song():
    lyrics = [
        ("\n" "You'd be mineeeeee", 0.08),
        ("would you mind if i took your hand tonight?", 0.08),
        ("know you're all that i want this life", 0.08),
        ("\n""I'll imagine we fall in love", 0.08),
        ("I'll nap under moonlight skies with you", 0.08),
        ("I think I'll picture us, you with the waves",0.08),
        ("The oceon's colors on your face", 0.08),
        ("I'll leave my heart with your air", 0.08),
        ("So let me fly with you", 0.08),
        ("Will you be forever with me?", 0.15),
    ]    

    delays = [0.3, 2.4, 7.5, 14.7, 17.6, 20.4, 24.5, 26.5, 30.0, 34.3]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()