import os
from tkinter import *
import toml
import Project.main as mn
from random import choice

def arcade_modo():
    os.system('cls')

    colors = toml.load(r'C:\Users\alexs\Desktop\JOGOS\PYTHON\JOGO DA VELHA\colors.toml')

    #CRIANDO JANELA PRINCIPAL
    janela = Tk()
    janela.title('')
    janela.geometry('260x400')
    janela.configure(bg=colors['fundo'])

    #DIVIDINDO JANELA EM 2 FRAMES
    frame_cima = Frame(janela, width=240, height=100, bg=colors['preto'])
    frame_cima.grid(row=0,sticky=NW, padx=10, pady=10)

    frame_baixo = Frame(janela, width=240, height=300, bg=colors['fundo'])
    frame_baixo.grid(row=1, sticky=NW)

    #CONFIGURANDO FRAME DE CIMA
    fase = Label(frame_cima, text='FASE', font=('Ivy 25 bold'), bg=colors['preto'], fg=colors['branco'])
    fase.place(x=10,y=30)

    meio = Label(frame_cima, text=':', font=('Ivy 30 bold'), bg=colors['preto'], fg=colors['branco'])
    meio.place(x=130,y=25)

    pontos = Label(frame_cima, text='1', font=('Ivy 30 bold'), bg=colors['preto'], fg=colors['branco'])
    pontos.place(x=180,y=28)

    #LOGICA
    global jogador_1
    global jogador_2
    global score
    global score
    global jogando
    global jogar
    global contador
    global contador_de_rodada
    global ja_tem_um_vencedor
    
    jogador_1 = 'X'
    jogador_2 = 'O'

    score = 1

    jogando = 'X'
    jogar = ''
    contador = 0
    contador_de_rodada = 0
    ja_tem_um_vencedor = False
    
    #FUNÇÃO
    def iniciar_jogo():
        global ja_tem_um_vencedor
        global lista_botoes
        
        b_jogar.destroy()

        # CONTROLADOR DO JOGO
        def controlar(i):
            global jogando
            global contador 
            global jogar
            
            jogando = 'X'
            
            if lista_botoes[int(i)]['text']=='':
 
                lista_botoes[int(i)]['fg'] = colors['vermelho']
                lista_botoes[int(i)]['text'] = jogando
                                    
                # PROXIMA RODADA
                contador += 1
                    
                # VERIFICADOR DE VENCEDOR
                print('verificar contador do jogador esta em: ' + str(contador))
                if contador >= 5:
                    
                    # LINHAS
                    if lista_botoes[0]['text'] == lista_botoes[1]['text'] == lista_botoes[2]['text'] != '':
                        vencedor(lista_botoes[0]['text'])
                    elif lista_botoes[3]['text'] == lista_botoes[4]['text'] == lista_botoes[5]['text'] != '':
                        vencedor(lista_botoes[3]['text'])
                    elif lista_botoes[6]['text'] == lista_botoes[7]['text'] == lista_botoes[8]['text'] != '':
                        vencedor(lista_botoes[6]['text'])

                    # COLUNAS
                    if lista_botoes[0]['text'] == lista_botoes[3]['text'] == lista_botoes[6]['text'] != '':
                        vencedor(lista_botoes[0]['text'])
                    elif lista_botoes[1]['text'] == lista_botoes[4]['text'] == lista_botoes[7]['text'] != '':
                        vencedor(lista_botoes[1]['text'])
                    elif lista_botoes[2]['text'] == lista_botoes[5]['text'] == lista_botoes[8]['text'] != '':
                        vencedor(lista_botoes[2]['text'])

                    # DIAGONAIS
                    if lista_botoes[0]['text'] == lista_botoes[4]['text'] == lista_botoes[8]['text'] != '':
                        vencedor(lista_botoes[0]['text'])
                    elif lista_botoes[2]['text'] == lista_botoes[4]['text'] == lista_botoes[6]['text'] != '':
                        vencedor(lista_botoes[2]['text'])
            
                    # EMPATE
                    if contador >= 9:
                        vencedor('EMPATE')
            global ja_tem_um_vencedor 
                            
            if ja_tem_um_vencedor == False:        
                maquina()
                        
        # Maquina
        def maquina(): 
            global contador
                      
            jogando = 'O'
            
            #################################################################################
            
            lista = range(9)
            l = choice(lista)
        
            while lista_botoes[l]['text'] != '':
                l = choice(lista)
                
            lista_botoes[l]['text'] = jogando
            lista_botoes[l]['fg'] = colors['azul']  
            
            #################################################################################
            # PROXIMA RODADA
            contador += 1
                
            # VERIFICADOR DE VENCEDOR
            print('verificar contador da maquina esta em: ' + str(contador))
            if contador >= 5:
                # LINHAS
                if lista_botoes[0]['text'] == lista_botoes[1]['text'] == lista_botoes[2]['text'] != '':
                    vencedor(lista_botoes[0]['text'])
                elif lista_botoes[3]['text'] == lista_botoes[4]['text'] == lista_botoes[5]['text'] != '':
                    vencedor(lista_botoes[3]['text'])
                elif lista_botoes[6]['text'] == lista_botoes[7]['text'] == lista_botoes[8]['text'] != '':
                    vencedor(lista_botoes[6]['text'])

                # COLUNAS
                if lista_botoes[0]['text'] == lista_botoes[3]['text'] == lista_botoes[6]['text'] != '':
                    vencedor(lista_botoes[0]['text'])
                elif lista_botoes[1]['text'] == lista_botoes[4]['text'] == lista_botoes[7]['text'] != '':
                    vencedor(lista_botoes[1]['text'])
                elif lista_botoes[2]['text'] == lista_botoes[5]['text'] == lista_botoes[8]['text'] != '':
                    vencedor(lista_botoes[2]['text'])

                # DIAGONAIS
                if lista_botoes[0]['text'] == lista_botoes[4]['text'] == lista_botoes[8]['text'] != '':
                    vencedor(lista_botoes[0]['text'])
                elif lista_botoes[2]['text'] == lista_botoes[4]['text'] == lista_botoes[6]['text'] != '':
                    vencedor(lista_botoes[2]['text'])
                            
                # EMPATE
                if contador >= 9:
                    vencedor('EMPATE')
     
        # VENCEDOR
        def vencedor(i):
            global score
            global contador
            
            print(str(i) + ' venceu! contador esta em: ' + str(contador))
            
            # LIMPA E BLOQUEIA OS BOTÕES               
            b_1['state'] = 'disable'
            b_2['state'] = 'disable'
            b_3['state'] = 'disable'
            b_4['state'] = 'disable'
            b_5['state'] = 'disable'
            b_6['state'] = 'disable'
            b_7['state'] = 'disable'
            b_8['state'] = 'disable'
            b_9['state'] = 'disable'

            if i == 'X':                
                app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['branco'])
                app_linhaV1.place(x=158,y=2)
                app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['branco'])
                app_linhaV2.place(x=90,y=2)
                app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['branco'])
                app_linhaH1.place(x=29,y=60)
                app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['branco'])
                app_linhaH2.place(x=29,y=125)
                
                def start0():               
                    global contador
                    global jogando
                    global score
                    
                    app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['vermelho'])
                    app_linhaV1.place(x=158,y=2)
                    app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['vermelho'])
                    app_linhaV2.place(x=90,y=2)
                    app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['vermelho'])
                    app_linhaH1.place(x=29,y=60)
                    app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['vermelho'])
                    app_linhaH2.place(x=29,y=125)
                    
                    # LIMPA OS BOTÕES
                    b_1['state'] = 'normal'
                    b_2['state'] = 'normal'
                    b_3['state'] = 'normal'
                    b_4['state'] = 'normal'
                    b_5['state'] = 'normal'
                    b_6['state'] = 'normal'
                    b_7['state'] = 'normal'
                    b_8['state'] = 'normal'
                    b_9['state'] = 'normal'
                    
                    b_1['text'] = ''
                    b_2['text'] = ''
                    b_3['text'] = ''
                    b_4['text'] = ''
                    b_5['text'] = ''
                    b_6['text'] = ''
                    b_7['text'] = ''
                    b_8['text'] = ''
                    b_9['text'] = ''

                    b_jogar.destroy()
                    b_np.destroy()
                    
                    contador = 0
                    jogando = 'X'
                    score += 1
                    pontos['text'] = score
                    global ja_tem_um_vencedor
                    ja_tem_um_vencedor = False
                    os.system('cls')
                    
                b_np = Button(frame_baixo, command=start0, text='PROXIMA FASE', width=10, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
                b_np.place(x=85,y=210) 
            
            else:
                app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['branco'])
                app_linhaV1.place(x=158,y=2)
                app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['branco'])
                app_linhaV2.place(x=90,y=2)
                app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['branco'])
                app_linhaH1.place(x=29,y=60)
                app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['branco'])
                app_linhaH2.place(x=29,y=125)        
    
                def start():               
                    global contador
                    global jogando
                    global score
                    
                    app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['vermelho'])
                    app_linhaV1.place(x=158,y=2)
                    app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['vermelho'])
                    app_linhaV2.place(x=90,y=2)
                    app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['vermelho'])
                    app_linhaH1.place(x=29,y=60)
                    app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['vermelho'])
                    app_linhaH2.place(x=29,y=125)
                    
                    # LIMPA OS BOTÕES
                    b_1['state'] = 'normal'
                    b_2['state'] = 'normal'
                    b_3['state'] = 'normal'
                    b_4['state'] = 'normal'
                    b_5['state'] = 'normal'
                    b_6['state'] = 'normal'
                    b_7['state'] = 'normal'
                    b_8['state'] = 'normal'
                    b_9['state'] = 'normal'
                    
                    b_1['text'] = ''
                    b_2['text'] = ''
                    b_3['text'] = ''
                    b_4['text'] = ''
                    b_5['text'] = ''
                    b_6['text'] = ''
                    b_7['text'] = ''
                    b_8['text'] = ''
                    b_9['text'] = ''

                    b_jogar.destroy()
                    b_np.destroy()
                    
                    contador = 0
                    jogando = 'X'
                    score = 1
                    pontos['text'] = score
                    global ja_tem_um_vencedor
                    ja_tem_um_vencedor = False
                    os.system('cls')
                    
                b_np = Button(frame_baixo, command=start, text='NOVAMENTE', width=10, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
                b_np.place(x=85,y=210) 

            global ja_tem_um_vencedor
            ja_tem_um_vencedor = True
                   
        # LINHAS
        app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['vermelho'])
        app_linhaV1.place(x=158,y=2)
        app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['vermelho'])
        app_linhaV2.place(x=90,y=2)
        app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['vermelho'])
        app_linhaH1.place(x=29,y=60)
        app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['vermelho'])
        app_linhaH2.place(x=29,y=125)
        
        # BOTÃO
        b_1 = Button(frame_baixo, command=lambda: controlar(0), text='', width=3, height=1, bg=colors['fundo'], fg=colors['fundo'], font=('Ivy 20 bold'), relief=FLAT, overrelief=RIDGE)
        b_1.place(x=30,y=3)
        b_2 = Button(frame_baixo, command=lambda: controlar(1), text='', width=3, height=1, bg=colors['fundo'], fg=colors['fundo'], font=('Ivy 20 bold'), relief=FLAT, overrelief=RIDGE)
        b_2.place(x=97,y=3)
        b_3 = Button(frame_baixo, command=lambda: controlar(2), text='', width=3, height=1, bg=colors['fundo'], fg=colors['fundo'], font=('Ivy 20 bold'), relief=FLAT, overrelief=RIDGE)
        b_3.place(x=165,y=3)
        b_4 = Button(frame_baixo, command=lambda: controlar(3), text='', width=3, height=1, bg=colors['fundo'], fg=colors['fundo'], font=('Ivy 20 bold'), relief=FLAT, overrelief=RIDGE)
        b_4.place(x=30,y=69)
        b_5 = Button(frame_baixo, command=lambda: controlar(4), text='', width=3, height=1, bg=colors['fundo'], fg=colors['fundo'], font=('Ivy 20 bold'), relief=FLAT, overrelief=RIDGE)
        b_5.place(x=97,y=69)
        b_6 = Button(frame_baixo, command=lambda: controlar(5), text='', width=3, height=1, bg=colors['fundo'], fg=colors['fundo'], font=('Ivy 20 bold'), relief=FLAT, overrelief=RIDGE)
        b_6.place(x=165,y=69)
        b_7 = Button(frame_baixo, command=lambda: controlar(6), text='', width=3, height=1, bg=colors['fundo'], fg=colors['fundo'], font=('Ivy 20 bold'), relief=FLAT, overrelief=RIDGE)
        b_7.place(x=30,y=134)
        b_8 = Button(frame_baixo, command=lambda: controlar(7), text='', width=3, height=1, bg=colors['fundo'], fg=colors['fundo'], font=('Ivy 20 bold'), relief=FLAT, overrelief=RIDGE)
        b_8.place(x=97,y=134)
        b_9 = Button(frame_baixo, command=lambda: controlar(8), text='', width=3, height=1, bg=colors['fundo'], fg=colors['fundo'], font=('Ivy 20 bold'), relief=FLAT, overrelief=RIDGE)
        b_9.place(x=165,y=134)
        
        global lista_botoes
        lista_botoes = [b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9]
    
    def voltar():
        janela.destroy()
        mn.menu_principal()
  
    b_jogar = Button(frame_baixo, command=iniciar_jogo, text='Jogar', width=10, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
    b_jogar.place(x=85,y=210)
    
    b_voltar_menu = Button(frame_cima, command=voltar, text='MENU', width=5, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
    b_voltar_menu.place(x=98,y=3)
    
    janela.mainloop()