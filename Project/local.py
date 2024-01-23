import os
from tkinter import *
import toml
import Project.main as mn

def multiplayer_local():
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
    app_x = Label(frame_cima, text='X', font=('Ivy 40 bold'), bg=colors['preto'], fg=colors['vermelho'])
    app_x.place(x=25,y=10)

    app_x_nome = Label(frame_cima, text='Jogador 1', font=('Ivy 10 bold'), bg=colors['preto'], fg=colors['branco'])
    app_x_nome.place(x=15,y=70)

    app_x_pontos = Label(frame_cima, text='0', font=('Ivy 30 bold'), bg=colors['preto'], fg=colors['branco'])
    app_x_pontos.place(x=80,y=20)

    app_meio= Label(frame_cima, text=':', font=('Ivy 30 bold'), bg=colors['preto'], fg=colors['branco'])
    app_meio.place(x=110,y=15)

    app_o = Label(frame_cima, text='O', height=1, font=('Ivy 40 bold'), bg=colors['preto'], fg=colors['azul'])
    app_o.place(x=165,y=10)

    app_o_nome = Label(frame_cima, text='Jogador 2', height=1,  font=('Ivy 10 bold'), bg=colors['preto'], fg=colors['branco'])
    app_o_nome.place(x=155,y=70)

    app_o_pontos = Label(frame_cima, text='0', font=('Ivy 30 bold'), bg=colors['preto'], fg=colors['branco'])
    app_o_pontos.place(x=130,y=20)

    #LOGICA
    global jogador_1
    global jogador_2
    global score_1
    global score_2
    global jogando
    global jogar
    global contador
    global contador_de_rodada
    
    jogador_1 = 'X'
    jogador_2 = 'O'

    score_1 = 0
    score_2 = 0

    jogando = 'X'
    jogar = ''
    contador = 0
    contador_de_rodada = 0

    #FUNÇÃO
    def iniciar_jogo():
        b_jogar.destroy()
        
        # CONTROLADOR DO JOGO
        def controlar(i):
            global jogando
            global contador 
            global jogar
            global proximo
            
            if lista_botoes[int(i)]['text']=='':
                if jogando == 'X':
                    cor = colors['vermelho']
                    proximo = colors['azul']
                if jogando == 'O':
                    cor = colors['azul']
                    proximo = colors['vermelho']
                
                lista_botoes[int(i)]['fg'] = cor
                lista_botoes[int(i)]['text'] = jogando
                
                # MUDAR DE JOGADOR
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'
                    
                    app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=proximo)
                    app_linhaV1.place(x=158,y=2)
                    app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=proximo)
                    app_linhaV2.place(x=90,y=2)
                    app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=proximo)
                    app_linhaH1.place(x=29,y=60)
                    app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=proximo)
                    app_linhaH2.place(x=29,y=125)
                    
                else:
                    jogando = 'X'
                    jogar = 'jogador 2'
                    
                    app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=proximo)
                    app_linhaV1.place(x=158,y=2)
                    app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=proximo)
                    app_linhaV2.place(x=90,y=2)
                    app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=proximo)
                    app_linhaH1.place(x=29,y=60)
                    app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=proximo)
                    app_linhaH2.place(x=29,y=125)
                    
                # PROXIMA RODADA
                contador += 1
                    
                # VERIFICADOR DE VENCEDOR
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
            global score_1
            global score_2
            global contador
            
            # LIMPA E BLOQUEIA OS BOTÕES
            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''
            b_9['text'] = ''
                
            b_1['state'] = 'disable'
            b_2['state'] = 'disable'
            b_3['state'] = 'disable'
            b_4['state'] = 'disable'
            b_5['state'] = 'disable'
            b_6['state'] = 'disable'
            b_7['state'] = 'disable'
            b_8['state'] = 'disable'
            b_9['state'] = 'disable'
            
            app_vencedor = Label(frame_baixo, text='', width=25, relief='flat', anchor='center', font=('Ivy 14 bold'), bg=colors['fundo'], fg=colors['laranja'])
            app_vencedor.place(x=-20,y=240)
            
            if i == 'X':
                score_1 += 1
                app_vencedor['text'] = 'Jogador 1 venceu'
                app_vencedor['fg'] = colors['vermelho']
                app_x_pontos['text'] = score_1
                
                app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['fundo'])
                app_linhaV1.place(x=158,y=2)
                app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['fundo'])
                app_linhaV2.place(x=90,y=2)
                app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['fundo'])
                app_linhaH1.place(x=29,y=60)
                app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['fundo'])
                app_linhaH2.place(x=29,y=125)

            if i == 'O':
                score_2 += 1
                app_vencedor['text'] = 'Jogador 2 venceu'
                app_vencedor['fg'] = colors['azul']
                app_o_pontos['text'] = score_2
                
                app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['fundo'])
                app_linhaV1.place(x=158,y=2)
                app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['fundo'])
                app_linhaV2.place(x=90,y=2)
                app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['fundo'])
                app_linhaH1.place(x=29,y=60)
                app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['fundo'])
                app_linhaH2.place(x=29,y=125)

            if i == 'EMPATE':
                app_vencedor['text'] = 'PARTIDA EMPATADA'
                
                app_linhaV1 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['fundo'])
                app_linhaV1.place(x=158,y=2)
                app_linhaV2 = Label(frame_baixo, height=30, pady=2, font=('Ivy 4 bold'), bg=colors['fundo'])
                app_linhaV2.place(x=90,y=2)
                app_linhaH1 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['fundo'])
                app_linhaH1.place(x=29,y=60)
                app_linhaH2 = Label(frame_baixo, width=189, padx=2, font=('Ivy 1 bold'), bg=colors['fundo'])
                app_linhaH2.place(x=29,y=125)
                
            def start():
                global contador
                global jogando
                global proximo
                
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
            
                app_vencedor.destroy()
                b_jogar.destroy()
                b_np.destroy()
                b_zerar.destroy()
                
                contador = 0
                jogando = 'X'
                
            def jogo_acabou():
                
                b_np.destroy()
                app_vencedor.destroy()
                b_zerar.destroy()
                
                vencedor_jogo_atual()
                
            # TERMINAR JOGO                     
            def vencedor_jogo_atual():
                global contador_de_rodada
                global contador
                global jogando
                global score_1
                global score_2
                            
                app_fim = Label(frame_baixo, text='', width=25, relief='flat', anchor='center', font=('Ivy 14 bold'), bg=colors['fundo'], fg=colors['laranja'])
                app_fim.place(x=-20,y=240)

                if score_1 > score_2:
                    app_fim['text'] = 'Joagador 1 venceu'
                    app_fim['fg'] = colors['vermelho']
                    
                if score_2 > score_1:
                    app_fim['text'] = 'Joagador 2 venceu'
                    app_fim['fg'] = colors['azul']
                
                if score_1 == score_2:
                    app_fim['text'] = 'PARTIDA  EMPATADA'
                    app_fim['fg'] = colors['laranja']
                    
                contador = 0
                score_1 = 0
                score_2 = 0
                jogando = 'X'
                
                app_x_pontos['text'] = '0'
                app_o_pontos['text'] = '0'
                
                b_1['state'] = 'normal'
                b_2['state'] = 'normal'
                b_3['state'] = 'normal'
                b_4['state'] = 'normal'
                b_5['state'] = 'normal'
                b_6['state'] = 'normal'
                b_7['state'] = 'normal'
                b_8['state'] = 'normal'
                b_9['state'] = 'normal'

                app_fim.destroy()
                
                iniciar_jogo() 

                
            b_np = Button(frame_baixo, command=start, text='NOVAMENTE', width=10, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
            b_np.place(x=10,y=210) 
            
            b_zerar = Button(frame_baixo, command=jogo_acabou, text='ZERAR', width=10, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
            b_zerar.place(x=150,y=210) 
            
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
        
        lista_botoes = [b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9]
    
    def voltar():
        janela.destroy()
        mn.menu_principal()
  
    b_jogar = Button(frame_baixo, command=iniciar_jogo, text='Jogar', width=10, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE)
    b_jogar.place(x=85,y=210)
    
    b_voltar_menu = Button(frame_cima, command=voltar, text='MENU', width=5, height=1, bg=colors['fundo'], fg=colors['branco'],font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
    b_voltar_menu.place(x=98,y=3)
    
    janela.mainloop()