"""
#Python
#title 		:Web_Scraping.py
#description:This is a web scraper app
#author 	:JohnBedeir
#website	:johnydesigns.com
#date		:22Oct20
"""
from tkinter import *
import requests 
from bs4 import BeautifulSoup

window=Tk()
window.title("HTML Scraper")


def url_to_content():
    r=requests.get(e1_text.get())
    c=r.content
    soup=BeautifulSoup(c, "html.parser")
    result=str(soup.prettify)
    t1.delete("1.0", END)
    t1.insert(END, result)



#LABELS
l1=Label(window,text="Enter URL here:")
l1.grid(row=0, column=0)

l2=Label(window,text="Website Content")
l2.grid(row=0, column=2)

#ENTRY
e1_text=StringVar()
e1=Entry(window, textvariable=e1_text)
e1.grid(row=1, column=0)

#BUTTON
bt1=Button(window, text="Scraping", command=url_to_content)
bt1.grid(row=1, column=1)


#TEXTAREA
t1=Text(window)
t1.grid(row=1,column=2,rowspan=6,columnspan=2)


#SCROLLBAR

sb1=Scrollbar(window)
sb1.grid(row=2,column=4)

t1.configure(yscrollcommand=sb1.set)
sb1.configure(command=t1.yview)


window.mainloop()