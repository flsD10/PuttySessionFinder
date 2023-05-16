import os
import time

try:
    config = open('config.txt', 'r')
    

except FileNotFoundError:
    config = open('config.txt', 'w')
    config.write("PuttyFileLocation=")
sessions =os.popen("powershell Get-ChildItem HKCU:\Software\SimonTatham\PuTTY\Sessions -Name").read().split('\n')

from tkinter import *

root = Tk()
root.geometry("600x400")

def update(data):
    listbox.delete(0,END)

    for item in data:
        listbox.insert(END, item)


def check(e):
    typed = my_entry.get()
    if typed == '':
        data = sessions
    else: 
        terms = typed.split(' ')
        print(terms)
        data = []
        for session in sessions:
            data.append(session)
        print("data: ",data)
        print("session: ", sessions)
        for session in sessions:
            for term in terms:
                if term == '':
                    pass
                else: 
                    if term.lower() in session.lower():
                        pass
                    else:
                        try:
                            data.remove(session)
                            print(data)
                        except ValueError:
                            pass
    data = [*set(data)]
    while("" in data):
        data.remove("")
    update(data)

searchLabel=Label(root, text = "Search:") 
searchLabel.pack()

my_entry = Entry(root)
my_entry.pack()

changeLabel=Label(root, text = "File Location: ") 
changeLabel.pack()
path = Entry(root,width=75)

with open('config.txt') as f:
    lines = f.readline()
    file_location = lines.split("=")[1]
path.insert(0, file_location)
path.pack()



def changeDirectory():
    time.sleep(0.5)
    file_location = path.get()
    print(file_location)
    config = open('config.txt', 'w')
    config.write("PuttyFileLocation=" + str(file_location))
    path.delete(0, END)
    path.insert(0, file_location)



changeButton = Button(root, text ="Change", command=changeDirectory)
changeButton.pack()

listbox = Listbox(root, width=50)
listbox.pack(pady=40)

update(sessions)

my_entry.bind("<KeyRelease>", check)
def launch():
    for i in listbox.curselection():
        session = str(listbox.get(i)).replace('%20', ' ')
        os.system(('"'+ file_location + '"' + " -load " + str(session)))


launchButton = Button(root, text ="Launch", command=launch)
launchButton.pack()

mainloop()












"""
sessions =os.popen("powershell Get-ChildItem HKCU:\Software\SimonTatham\PuTTY\Sessions -Name").read()

print(sessions)
sessions = sessions.split('\n')


def input_char(message):
    try:
        win = curses.txttscr()
        win.addstr(0, 0, message)
        while True: 
            ch = win.getstr()
            
            for session in sessions:
                session = session.lower()
                try: 
                    session.index(str(ch))
                    print(session)
                except ValueError:
                    pass
            time.sleep(0.1)
    finally:
        curses.endwin()
    return chr(ch)
c = input_char('Search: ')
print(c)
"""


"""
Get list of saved servers
User input(search term)


sessions = ["session 1", "session 2"]
for session in sessions:
    session = session.lower()
    try: 
        session.index(searchTerm)
        print(session)
    except IndexError:
        pass
"""