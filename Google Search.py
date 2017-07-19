"""This is meant to be a simple and a small browser that will be open all the
 time as a small window and will allow me to search for a words meaning irrespective
  of the thing that is on my screen at the moment. Thank you
"""

# I'll need a GUI library for the purpose.
import bs4 as bs
import mechanize
from Tkinter import *
import re

root = Tk()
label = Label(root, text="This is awesome!")
label.pack(side=BOTTOM)

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('user-agent', 'chrome')]

area = Entry(root, bg="White", width=23)
area.pack(side=LEFT)

global var1
var2 = []

def searchFunction():
    query = area.get().lstrip() + "+meaning"

    url = "http://www.google.com/search?q="+query
    text = br.open(url).read()
    soup = bs.BeautifulSoup(text, 'lxml')
    i = 1
    for row in soup.find_all('div'):
        if i is 23:
            var1 = row.find_all("li")
        i += 1

    j = 1
    for ls in var1:
        if 'cached' not in ls.text and 'similar' not in ls.text:
            var2.append(str(j) + ". " + ls.text.capitalize())
        j += 1
    mix = '\n\n'.join(var2)
    mix = str(mix)
    """
    mix = mix.replace('Cached\n\n', '')
    mix = mix.replace('Similar\n\n', '')
    """
    strp = re.sub("\d+" + ". Cached\n\n", "", mix)
    strp = re.sub("\d+" + ". Similar\n\n", "", strp)

    strp = re.sub("\d+" + ". Cached", "", strp)
    strp = re.sub("\d+" + ". Similar", "", strp)
    label.config(text="")
    label.config(text=strp)

searchButton = Button(root, text="Search", fg="black", command=searchFunction)
searchButton.pack(side=RIGHT)

root.mainloop()
