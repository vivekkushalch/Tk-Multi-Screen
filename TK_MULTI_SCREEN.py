from tkinter import *

w = Tk() #MAIN WINDOW
w.geometry('600x500')
w.title('TK MULTI-SCREEN')
w.config(bg='#ffffff')

#DEFAULTS
PRIMARY_COLOUR = 'white'
ACCENT_COLOUR = 'black'
TAB_FONT = 'Roboto 12'

#DEFAULT ARGS FOR TABS
tab_kwrgs = {
    'relief': 'flat',
    'width': 10,
    'font': TAB_FONT,
    'bg': ACCENT_COLOUR,
    'fg': PRIMARY_COLOUR,
    'cursor':'hand2'
}


def change_screen(screens_list,tabs_list,show_screen,enable_tab):
    """Enables the show_screen and removes all other widgets and screens

    - screens_list(list): list of screens to remove
    - tabs_list(list): list of tabs to remove
    - show_screen(widget): Screen to show
    - enable_tab(widget): Tab to activate

    """
    for screen in screens_list:
        screen.pack_forget()
    for tab in tabs_list:
        tab.config(bg=ACCENT_COLOUR,fg=PRIMARY_COLOUR)
    show_screen.pack(fill=BOTH,expand=YES)
    enable_tab.config(bg=PRIMARY_COLOUR,fg=ACCENT_COLOUR)        


#SCREEN CHANGER
def show_screen1():
    change_screen([screen2,screen3],[tab2,tab3],screen1,tab1)
def show_screen2():
    change_screen([screen1,screen3],[tab1,tab3],screen2,tab2)    
def show_screen3():
    change_screen([screen1,screen2],[tab1,tab2],screen3,tab3)   


#FRAME FOR TABS
toolbar = Frame(w,height=1,bg=ACCENT_COLOUR)
toolbar.pack(fill=X)

#TABS
tab1 = Button(toolbar,text='Tab1',relief='flat',width=10,font=TAB_FONT,bg=PRIMARY_COLOUR,fg=ACCENT_COLOUR,cursor='hand2',command=show_screen1)
tab2 = Button(toolbar,text='Tab2',command=show_screen2,**tab_kwrgs)
tab3 = Button(toolbar,text='Tab3',command=show_screen3,**tab_kwrgs)

#SCREENS
screen1 = Frame(w,bg=PRIMARY_COLOUR)
screen2 = Frame(w,bg=PRIMARY_COLOUR)
screen3 = Frame(w,bg=PRIMARY_COLOUR)


#GRID TABS
tabs_list = [tab1,tab2,tab3]
for i,tab in enumerate(tabs_list):
    tab.grid(row=0,column=i)


#PACK FIRST SCREEN    
screen1.pack(fill=BOTH,expand=YES)


#WIDGETS FOR RESPECTED SCREENS
for i in range(3):
    screens = [screen1,screen2,screen3]
    l = Label(master=screens[i],text=f'Screen {i+1}',font='Roboto 20',bg=PRIMARY_COLOUR,fg=ACCENT_COLOUR)
    l.pack(padx=10,pady=50)




w.mainloop()

"""
#SCHEMATIC FOR THE IMPLEMENTATION

MAIN WINDOW(w)
    -Frame(toolbar)
        -Tabs(tab1,tab2,tab3)
    -Frame(screen1,screen2,screen3)
        -Widgets(label)

"""