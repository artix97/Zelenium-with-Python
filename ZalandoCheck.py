from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pygame import mixer
import os
import time
from pathlib import Path
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from tkinter import *
print(Path(__file__).resolve().parent)



testing=False
entered_text =""

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-features=VizDisplayCompositor")
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options) 



def PlaySong():
    mixer.init()
    mixer.music.load(str(Path(__file__).resolve().parent)+"\\money.mp3")
    mixer.music.play()



    

def close_window():
    window.destroy()
    exit()

    
def click():
    entered_text=textentry.get()  
    while True:
        try:
                                
            driver.get(entered_text) # Go to the given url
            data = driver.find_element_by_xpath("//h2[contains(., 'Artykuł wyprzedany')]")  #Put name of "not avilable product" in ur lang
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            definition = (data.text+" "+current_time)



        except NoSuchElementException:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            definition = ("Produkt dostępny"+" "+current_time)
            output.insert(0.0, definition )
            browser = webdriver.Chrome(executable_path='chromedriver.exe')   #chromredriver added to PATH
            browser.get(entered_text)
            PlaySong()
            window.update()
            window.destroy()

    
        except TypeError:
            pass
        else:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            definition = (data.text+" "+current_time)


        output.delete(0.0 , END) 
        output.insert(0.0, definition )
        window.update()
        time.sleep(2)
        
        
    


#Main
window = Tk()
window.title("ZalandoAlert")
window.configure(background="orange")
window.resizable(0,0)
##Background
photo = PhotoImage(file=str(Path(__file__).resolve().parent)+"\\background.png")
Label (window,image=photo, bg = "orange").grid(row=0,column=0,sticky=W)
#create label
Label (window, text="Put a url adress of thing, which You are interested in:", bg="orange", fg="black", font="none 12 bold").grid(row=1,column=0,sticky=S)
#create a text entry box
textentry = Entry(window, width=80, bg="white")
textentry.grid(row=2, column=0, sticky=N)
#add a submit button
Button(window, text="Submit", width=5, height=1, command= click ).grid(row=2,column=0,sticky=E)


#create another label
Label (window, text="\nAuction Status:",bg="orange", fg="black", font="none 12 bold").grid(row=3,column=0,sticky=W)
#create a text box
output = Text(window, width=50, height=1, wrap=WORD, background="white",fg="black")
output.grid(row=4,column=0, columnspan=2, sticky=N)

#add a exit button
Button(window,text="Exit", width=5, height=1, command=close_window).grid(row=7,column=0,sticky=E)
#add a mainloop
window.mainloop()




