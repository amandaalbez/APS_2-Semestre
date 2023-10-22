# Bibliotecas
import customtkinter
from tkinter import *
import tkinter as tk

# Criação da tela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

screen = customtkinter.CTk()
screen.geometry("700x450")
screen.title("Encrypther")
screen.resizable(False, False)

# Código de criptografia
def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_message += encrypted_char
        else:
            encrypted_message += "§"  # Use um caractere especial para separar as palavras
    return encrypted_message

#Código de Descriptografia
def decrypt(encrypted_message, key):
    decrypted_message = ""
    current_word = ""
    for char in encrypted_message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            current_word += decrypted_char
        elif char == "§":  # Caractere especial usado para separar as palavras
            if current_word:
                if decrypted_message:
                    decrypted_message += " "  # Adicione um espaço antes da próxima palavra
                decrypted_message += current_word
                current_word = ""
    if current_word:
        if decrypted_message:
            decrypted_message += " "
        decrypted_message += current_word
    return decrypted_message

# Função para criptografar e atualizar a saída
def criptografar():
    message = text1.get("1.0", "end-1c")
    key = int(code.get())
    encrypted_message = encrypt(message, key)
    text2.delete("1.0", "end")
    text2.insert("1.0", encrypted_message)

# Função para descriptografar e atualizar a saída
def descriptografar():
    encrypted_message = text2.get("1.0", "end-1c")
    key = int(code_des.get())
    decrypted_message = decrypt(encrypted_message, key)
    text3.delete("1.0", "end")
    text3.insert("1.0", decrypted_message)

# Limitação de caracteres
def limitar_caracteres(event):
    texto_atual = text1.get("1.0", "end-1c")
    if len(texto_atual) >= limite_caracteres:
        return "break"
limite_caracteres = 128

#Função de Limpar
def clear():
    text1.delete("1.0", "end")
    text2.delete("1.0", "end")
    text3.delete("1.0", "end")
    code.set("")
    code_des.set("")

# Interface Gráfica
# Lado da Criptografia
#1- Titulo
label_titulo1 = customtkinter.CTkLabel(master=screen, text="Criptografar", font=customtkinter.CTkFont(family='Arial]', size=20))
label_titulo1.place(x=25, y=25) 
#2- Digitar Frase
label1 = customtkinter.CTkLabel(master=screen, text="Digite a frase: ",text_color="blue", font=customtkinter.CTkFont(family='Roboto', size=12)).place(x=25, y=58)
text1 = tk.Text(master=screen,font="12",bd=2,width=30, height=3,bg="#1F1F1F",fg="white")
text1.place(x=25,y=105)
label2 = customtkinter.CTkLabel(master=screen, text="Campo frase, Obrigatorio*",text_color="white", font=customtkinter.CTkFont(family='Roboto', size=9)).place(x=25, y=145)
#3-  Digitar Chave
code = StringVar()
chave = Entry(master=screen,textvariable=code,bd=2,font="20",show="*",bg="#1F1F1F",fg="white",width="30").place(x=25,y=252)
label3 = customtkinter.CTkLabel(master=screen, text="Digite a chave: ",text_color="blue", font=customtkinter.CTkFont(family='Roboto', size=12)).place(x=25, y=173)
label4 = customtkinter.CTkLabel(master=screen, text="Campo Chave, Obrigatorio*",text_color="white", font=customtkinter.CTkFont(family='Roboto', size=9)).place(x=25, y=228)
#4 - Saída
label5 = customtkinter.CTkLabel(master=screen, text="Frase Criptografada: ",text_color="blue", font=customtkinter.CTkFont(family='Roboto', size=12)).place(x=25, y=256)
text2 = Text(master=screen,font="12",bd=2,width=30, height=3,bg="#1F1F1F",fg="white")
text2.place(x=25,y=350)
label6 = customtkinter.CTkLabel(master=screen, text="Campo frase, Obrigatorio*",text_color="white", font=customtkinter.CTkFont(family='Roboto', size=9)).place(x=25, y=340)
#5- Botão
customtkinter.CTkButton(master=screen, text='Criptografar',command=criptografar).place(x=15, y=380)

# Lado da Descriptografia
#Frame
frame = customtkinter.CTkFrame(master=screen, width=350, height=447)
frame.pack(side=RIGHT)
#1- Titulo
label_titulo2 = customtkinter.CTkLabel(master=frame, text="Descriptografar", font=customtkinter.CTkFont(family='Roboto', size=20))
label_titulo2.place(x=25, y=25)
#2- Digitar Chave Novamente
code_des = StringVar()
chave_des = Entry(master=frame, textvariable=code_des, bd=2, font="20", show="*", bg="#1F1F1F", fg="white", width="30")
chave_des.place(x=25, y=110)
label3 = customtkinter.CTkLabel(master=frame, text="Digite a chave: ",text_color="blue", font=customtkinter.CTkFont(family='Roboto', size=12)).place(x=25, y=58)
label4 = customtkinter.CTkLabel(master=frame, text="Campo Chave, Obrigatorio*",text_color="white", font=customtkinter.CTkFont(family='Roboto', size=9)).place(x=25, y=115)
#3- Saída
label5 = customtkinter.CTkLabel(master=frame, text="Frase Descriptografada: ",text_color="blue", font=customtkinter.CTkFont(family='Roboto', size=12)).place(x=25, y=150)
text3 = Text(master=frame,font="12",bd=2,width=30, height=3,bg="#1F1F1F",fg="white")
text3.place(x=25,y=220)
label6 = customtkinter.CTkLabel(master=frame, text="Campo frase, Obrigatorio*",text_color="white", font=customtkinter.CTkFont(family='Roboto', size=9)).place(x=25, y=240)
#4- Botões
customtkinter.CTkButton(master=frame, text='Descriptografar', command=descriptografar).place(x=15, y=290)
customtkinter.CTkButton(master=frame, text='Limpar', command=clear).place(x=15, y=340)

# Vincula o evento <Key> ao callback limitar_caracteres
text1.bind("<Key>", limitar_caracteres)

screen.mainloop()
