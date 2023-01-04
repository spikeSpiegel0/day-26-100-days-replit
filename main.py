from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    play = input("\033[90mPress Y to play or P to pause \033[0m")
    if play == "y":
      source.paused = False  # unpause the playback
    elif play == "p":
      source.paused = True  # pause the playback
    else:
      continue

    

while True:
  print("\033[1m\033[36mmy playa 🎵\033[0m")
  # clear the screen 
  time.sleep(2)
  os.system("clear")
  # Show the menu
  print("\033[33mPress 1 to Play\033[0m")
  print("\033[33mPress 2 to Exit\033[0m")
  print("\033[33mPress anything else to see the menu again.\033[0m")
  print()
  time.sleep(4)
  os.system("clear")
  # take user's input
  userIn = input("")
  # check whether you should call the play() subroutine depending on user's input
  if userIn == "1":
    print("song playing..")
    time.sleep(1)
    os.system("clear")
    play()
  elif userIn == "2":
    print("exit..")
    time.sleep(1)
    os.system("clear")
    break
  else:
    os.system("clear")
    continue