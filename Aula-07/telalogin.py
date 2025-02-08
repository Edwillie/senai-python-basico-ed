import customtkinter as ctk

class cEntry(ctk.CTkEntry):
    def __init__(self, txtLabel, txtPlaceholder, pwdFmt=False) -> None:
        self.txtLabel = txtLabel
        self.txtPlaceholder = txtPlaceholder
        self.pwdFmt = pwdFmt

        lblObj = ctk.CTkLabel(app, text=self.txtLabel)

        if self.pwdFmt == True:
            entryObj = ctk.CTkEntry(app, placeholder_text=self.txtPlaceholder, show="*")
        else:    
            entryObj = ctk.CTkEntry(app, placeholder_text=self.txtPlaceholder)

        lblObj.grid()
        entryObj.grid()

def valida_usuario():        
    print(f'usuario: {lblLogin.get()}')
    print(f'senha: {lblPwd.get()}')

ctk.set_appearance_mode("system")
app = ctk.CTk()

app.geometry("300x400")
app.title("Tela de Login")

lblLogin = cEntry('Usuário', 'Quem sou eu?')
lblLogin.pack()
lblPwd = cEntry('Senha', 'Qual a palavra secreta?', True)
lblPwd.pack()
lbtn = ctk.CTkButton(app, text="Validar", command=valida_usuario)
lbtn.grid(pady=10)

app.grid_columnconfigure(0, weight=1)
app.mainloop()