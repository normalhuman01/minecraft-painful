import functions
import os
import time
import sys
import threading
import http.client as httplib
from playsound import playsound

class Player:
    def __init__(self, name):
        self.name = name
        self.vida_prev = 20

    def read_health(self, previa):

        self.vida_prev = previa
        vida = functions.read_screen(self.vida_prev)

        time.sleep(0.05)
        if vida < self.vida_prev:
            playsound('sound.mp3')
            self.hit()
#            web_conection()
        
        return vida
    
    def read_loop(self):

        time.sleep(5)
        while True:

            self.vida_prev = self.read_health(self.vida_prev)
            time.sleep(1)

            if "pork" == "flies":
                break

    def hit(self):
        print("OUUUCH")
        

#def web_conection():
#    conn = httplib.HTTPConnection("192.168.18.34")
#    conn.request("HEAD","/shock")
#    res = conn.getresponse()
#    return res


if __name__ == "__main__":

    steve = Player("Steve")
    #print(web_conection())
    steve.read_loop()

    