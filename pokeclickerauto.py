import pyautogui
import time
import keyboard
import sys

"""This auto clicker is designed to train and breed pokemon while leaving pokeclicker on unattended. It will occupy your system while in use because it gives mouse input. It will click where you tell it to a certain number of times, open the breeding menu, then go back to clicking. Lining up the clicks with the breeding menu will cause the script to refill the egg queue. 
Hold 'q' to quit the script. 
Hold 'w' to open the breeding menu manually
Note- The script is a bit slow and running a faster autoclicker at 20 clicks per second really speeds things up. 
Note2- The script and any other autoclicker have to be run as an admin to work on pokeclicker
"""
class Clicker():
    def __init__(self):
        """The x,y positions in these tuples are set for my system. To modify them take a screenshot of pokeclicker, paste it into something like paint, and find your desired x and y coordinates. self.breed_menu should be the breed menu button. self.clicking should be set to a location that overlaps both where you want to click and one of the pokemon on the breeding menu when it is open."""
        self.breed_menu = (1870,130)
        #Enable to click on the first pokemon in the breed menu
        #self.clicking = (600,400)
        #Enable to click on Kanto champ Blue
        self.clicking = (630,608 )
        #Enable and change to your own (x,y)
        #self.clicking = (x,y)
        
    def click(self, x_coord, y_coord):
        time.sleep(.05)
        pyautogui.click(x=x_coord, y=y_coord, button="left")
    
    def main_action(self):
        """Change the range in the first for loop to change how often the breeding menu is open. 500 works well once you reach alola (96 egg queue)."""
        while True:
            for i in range (500):
                if keyboard.is_pressed('q'):
                    break
                elif keyboard.is_pressed('w'):
                    self.click(self.breed_menu[0], self.breed_menu[1])
                else:
                    self.click(self.clicking[0], self.clicking[1])
            if keyboard.is_pressed('q'):
                break  
            self.click(self.breed_menu[0], self.breed_menu[1])
    
"""Change the sleep timer here in seconds to give yourself enough time to switch to pokeclicker before the script runs"""
time.sleep(3)   
clicker= Clicker()
Clicker.main_action(clicker)