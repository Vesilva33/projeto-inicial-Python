from  PySimpleGUI import PySimpleGUI as sg
#Layout
sg.theme('reddit')
layout = [
    [sg.Text('usuario'),sg.Input(key ='usuario',size=(20,1))],
    [sg.Text('senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('salvar o login?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de login',layout)
#ler os eventos
while True:
   eventos,valores = janela.read()
   if eventos == sg.WINDOW_CLOSED:
    break
   if eventos =='Entrar': 
    if valores['usuario'] =='verusca'and valores['senha'] == '225523':
        print('bem-vinda ao python')
        