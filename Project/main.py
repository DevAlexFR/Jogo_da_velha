import os
import toml
import local as lc
import arcade as ac

from tkinter import *

def menu_principal():
    
    colors = toml.load(r'Jogo_da_velha\Project\colors.toml')

    #CRIANDO MENU
    menu = Tk()
    menu.title('MENU')
    menu.geometry('260x260')
    menu.configure(bg=colors['fundo'])

    #CRIANDO FRAME DO MENU
    frame = Frame(menu, width=240, height=240, bg=colors['preto'])
    frame.grid(row=0,sticky=NW, padx=10, pady=10)

    def m_local():
        menu.destroy()
        lc.multiplayer_local()
        
    def m_arcade():
        menu.destroy()
        ac.arcade_modo()
        
    b_local = Button(frame, command=m_local, text='LOCAL', width=20, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
    b_local.place(x=40,y=40)

    b_arcade = Button(frame, command=m_arcade, text='ARCADE', width=20, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
    b_arcade.place(x=40,y=160) 
                
    menu.mainloop()
    
if __name__ == '__main__':
    menu_principal()
