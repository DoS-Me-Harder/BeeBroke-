import pyautogui
import pyfiglet
import time
result = pyfiglet.figlet_format("BeeBroke")
 print(result)

 print("Thanks for downloading BeeBroke!")
 print("It's really simple, just press enter and click where you want to spam")
 print("Happy trolling!")

 input("Press Enter To Continue. . .")

 time.sleep(5)

 f = open("beemovie", 'r')

 for word in f:
  pyautogui.typewrite(word)
  pyautogui.press("enter")
