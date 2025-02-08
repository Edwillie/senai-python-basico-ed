import customtkinter as ctk
import sqlite3 as sql

class DialogWindow(ctk.CTkToplevel):
    def __init__(self, msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text=msg)
        self.label.pack(padx=20, pady=20)

def enviar_bd():
    lDictCliente = {}
    lDictCliente['Nome'] = box_nome.get()
    lDictCliente['Endereco'] = box_endereco.get()
    lDictCliente['CEP'] = box_cep.get()
    lDictCliente['Bairro'] = box_bairro.get()
    lDictCliente['UF'] = op_estado.get()

    print(lDictCliente)

    conexao = sql.connect('Aula-08\\bd_teste.db')
    lcursor = conexao.cursor()

    try:
        lcursor.execute(''' CREATE TABLE tb_clientes (
                                nome          TEXT (255),
                                endereco      TEXT (255),
                                cep           TEXT (8),
                                bairro        TEXT (255),
                                estado        TEXT (255)
                        );''')
    except:
        pass

    try:
        lvazio = 0
        for campo, valor in lDictCliente.items():
            if not valor.strip():
                print(f'O campo {campo} não pode estar vazio')
                lvazio += 1

        if lvazio == 0:
            lcursor.execute('insert into tb_clientes(nome, endereco, cep, bairro, estado) values(?, ?, ?, ?, ?)', \
                            (lDictCliente['Nome'], lDictCliente['Endereco'], lDictCliente['CEP'], lDictCliente['Bairro'], lDictCliente['UF'])) 
       
            conexao.commit()

            diag = DialogWindow('Dados Cadastrados').wm_transient(main)
    except: 
        print('Ooops, deu ruim')

#cores
fundo_box = '#BA8E7A'
text_lable = 'white'
fg_lable = 'black'
fg_entrybox = '#E7E8E7'
texto_box = '#FFFFFF'
cor_texto_entrybox = 'Black'
border_box_color = 'white'
btn_fundo = 'white'

main = ctk.CTk(fg_color=fundo_box)
main.geometry("700x360")

config_Entrybox = {
    'fg_color': fg_entrybox, 
    'text_color': cor_texto_entrybox, 
    'border_color': border_box_color,
    'border_color': 'black'
}

main.grid_columnconfigure(0, weight=0)
main.grid_columnconfigure(1, weight=1)
main.grid_columnconfigure(2, weight=1)
main.grid_columnconfigure(3, weight=1)
main.grid_columnconfigure(4, weight=1)
main.grid_columnconfigure(5, weight=1)
main.grid_rowconfigure(0, weight=1)

frame_titulo = ctk.CTkFrame(main, fg_color=fundo_box, border_color='#66796B',border_width=2, corner_radius=12)
frame_titulo.grid(column=0, row=0, padx=160, pady=10, columnspan=6,  sticky='we')

frame_dados = ctk.CTkFrame(main, fg_color=fundo_box, border_color='#66796B',border_width=2, corner_radius=12)
frame_dados.grid(column=0, row=2,padx=5, pady=5, columnspan=6, rowspan=5, sticky='nswe')

titulo_cadastro = ctk.CTkLabel(main,text="CADASTRO DE CLIENTES",fg_color=fundo_box, text_color=text_lable, font=('Verdana',22))
titulo_cadastro.grid(column=0, row=0, padx=180, pady=30, columnspan=6, sticky='nswe')

quebra_de_linhas = ctk.CTkLabel(main, text=" ")
quebra_de_linhas.grid(column=0, row=1, padx=2, pady=2)

label_nome = ctk.CTkLabel(main, text='Nome:',fg_color=fundo_box,text_color=text_lable, font=('Arial',12))
label_nome.grid(column=0, row=2, padx=5, pady=5, stick='e')

box_nome = ctk.CTkEntry(main, **config_Entrybox)
box_nome.grid(column=1, row=2, padx=10, pady=10, columnspan=5, sticky='we')

label_endereco = ctk.CTkLabel(main, text='Endereço:',fg_color=fundo_box,text_color=text_lable, font=('Arial',12))
label_endereco.grid(column=0, row=3, padx=10, pady=10, sticky='e')

box_endereco = ctk.CTkEntry(main,  **config_Entrybox)
box_endereco.grid(column=1, row=3, padx=10, pady=10, columnspan=5, sticky='we')

label_cep = ctk.CTkLabel(main, text='CEP:',fg_color=fundo_box,text_color=text_lable, font=('Arial',12))
label_cep.grid(column=0, row=4, padx=10, pady=10, stick='e')

box_cep = ctk.CTkEntry(main,  **config_Entrybox)
box_cep.grid(column=1, row=4, padx=10, pady=10,  stick='we')

label_bairro = ctk.CTkLabel(main, text='Bairro:',fg_color=fundo_box,text_color=text_lable, font=('Arial',12))
label_bairro.grid(column=2, row=4, padx=10, pady=10, stick='e')

box_bairro = ctk.CTkEntry(main,  **config_Entrybox)
box_bairro.grid(column=3, row=4, padx=10, pady=10, stick='we')

label_estado = ctk.CTkLabel(main, text='Estado', fg_color=fundo_box, text_color=text_lable, font=('Arial',12))
label_estado.grid(column=4, row=4, padx=10, pady=10, stick='e')

op_estado = ctk.CTkOptionMenu(main,fg_color=text_lable, text_color=cor_texto_entrybox, button_color=btn_fundo, values=[' ','SP','RJ','PR','ES','MG'])
op_estado.grid(column=5, row=4, padx=10, pady=10,  stick='we')

btn_enviar = ctk.CTkButton(main, text="ENVIAR",fg_color=btn_fundo, text_color='black', hover_color='#FF2CDC', command=enviar_bd)
btn_enviar.grid(column=0, row=5, padx=10, pady=30, columnspan=6, stick='ns')

main.mainloop()