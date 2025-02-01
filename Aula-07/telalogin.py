import customtkinter as ctk

class cEntry():
    def __init__(self) -> None:
        pass

    def create(self, txtLabel, txtPlaceholder):
        lblObj = ctk.CTkLabel(app, text=txtLabel)
        entryObj = ctk.CTkEntry(app, placeholder_text=txtPlaceholder)
        lblObj.grid()
        entryObj.grid()


ctk.set_appearance_mode("system")
app = ctk.CTk()

app.geometry("300x400")
app.title("Tela de Login")

lblLogin = cEntry()
lblLogin.create('Usuário', 'Quem sou eu?')

lblPwd = cEntry()
lblPwd.create('Senha', 'Qual a palavra secreta?')

app.grid_columnconfigure(0, weight=1)
#dialog = ctk.CTkInputDialog(text="Type in a number:", title="Test")
#text = dialog.get_input()  # waits for input


app.mainloop()