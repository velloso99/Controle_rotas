from pacotes import *
from tkinter.ttk import Style
from views import*
import sys, os
import tkinter as tk

# Criando Janela
root = Tk()
root.title("Controle de Rotas e Ganhos")
root.geometry("900x600")
root.configure(background=co0)
root.resizable(width=False, height=False)
largura_root= 900
altura_root= 600
#obter tamanho da tela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
# Calcular posição para centralizar
pos_x = ( largura_tela-largura_root )//2
pos_y = (altura_tela - altura_root)//2
# Definir geometria da janela (LxA+X+Y)
root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

style = Style(root)
style.theme_use("clam")



#criando frame
#frame_logo = Frame(root, width=950, height=52, bg=co1)
#frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

#ttk.Separator(root, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=950)

frame_login = Frame(root, width=950, height=750, bg=co1)
frame_login.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

######################################################################################
######################################################################################
#destruir frame login
def cad_usuario():
    for widget in frame_login.winfo_children():
        widget.destroy()
    tela_cadastrar_usuario()


# Abrir painel
#def open_painel():
    #for widget in frame_login.winfo_children():
        #widget.destroy()
        #painel()
    
    
    
########################################################################################
#Tela de Login

    
    #verificar Login e abrir novo arquivo    
def verificar_logion():
    global usuario, senha
    
    usuario = e_user.get() 
    senha = e_senha.get()
    
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("SELECT*FROM login WHERE usuario = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchall()
    if resultado:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        painel()
    else:
        messagebox.showerror("Erro", "Usuario ou senha incorretos!")
    cursor.close()
    
    
    
frame_t_login= Frame(frame_login, width=950, height=750, bg=co1)
frame_t_login.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)
    

l_titulo = Label(frame_login, text="Faça seu login", font=('Ivy 20 bold'), bg=co1, fg=co6)
l_titulo.place(x=450, y=50, anchor=CENTER)

l_user= Label(frame_login,text="Usuario", font=('Ivy 15 bold'), bg=co1, fg=co6)
l_user.place(x=450, y=150, anchor=CENTER)
e_user = Entry(frame_login, width=30, justify=LEFT, font=('ivy 15 bold'), highlightthickness=1, relief="solid")
e_user.place(x=450, y=200, anchor=CENTER)

l_senha = Label(frame_login, text="Senha", font=('Ivy 15 bold'), bg=co1, fg=co6)
l_senha.place(x=450, y=250, anchor=CENTER)
e_senha = Entry(frame_login, width=30, justify=LEFT, font=('Ivy 15 bold'),show="*", highlightthickness=1, relief="solid")
e_senha.place(x=450, y=300,anchor=CENTER)

l_enter= Button(frame_login, command=verificar_logion, text="Enter", font=('Ivy 15 bold'), width=10, overrelief=RIDGE, relief="solid", bg=co1, fg=co6)
l_enter.place(x=450, y=350, anchor=CENTER)

l_cadastro_senha = Button(frame_login,command=cad_usuario, text="Cadastrar Usuario", font=('Ivy 15 bold'), compound=LEFT, width=20, overrelief=RIDGE, relief="solid", bg=co1, fg=co6)
l_cadastro_senha.place(x=450, y=400, anchor=CENTER)

l_rodape = Label(frame_login,text="Desenvolvido por: VellosoDev", font=('Ivy 10 bold'), bg=co1, fg=co6, anchor=CENTER, relief=RAISED)
l_rodape.place(x=450, y=500, anchor=CENTER)



#criar tela de cadastro usuario
def tela_cadastrar_usuario():
    
    def cadastrar_usuario():
        usuario = e_usuario.get()
        senha = e_senha.get()
        
        lista = [usuario, senha]
        
        for i in lista:
            if i == "":
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return
        criar_login(lista)
        
        messagebox.showinfo("Sucesso", "Usuario cadastrado com sucesso!")
        
        e_usuario.delete(0, END)
        e_senha.delete(0, END)
    
    
 
    l_titulo = Label(frame_login, text="Cadastrar novo usuario", font=('Ivy 20 bold'), bg=co1, fg=co6)
    l_titulo.place(x=450, y=50, anchor=CENTER)

    l_usuario= Label(frame_login,text="Usuario", font=('Ivy 15 bold'), bg=co1, fg=co6)
    l_usuario.place(x=450, y=150, anchor=CENTER)
    e_usuario = Entry(frame_login, width=30, justify=LEFT, font=('ivy 15 bold'), highlightthickness=1, relief="solid")
    e_usuario.place(x=450, y=200, anchor=CENTER)

    l_senha = Label(frame_login, text="Senha", font=('Ivy 15 bold'), bg=co1, fg=co6)
    l_senha.place(x=450, y=250, anchor=CENTER)
    e_senha = Entry(frame_login, width=30, justify=LEFT, font=('Ivy 15 bold'),show="*", highlightthickness=1, relief="solid")
    e_senha.place(x=450, y=300,anchor=CENTER)

    l_enter= Button(frame_login,command= cadastrar_usuario, text="Enter", font=('Ivy 15 bold'), width=10, overrelief=RIDGE, relief="solid", bg=co1, fg=co6)
    l_enter.place(x=450, y=350, anchor=CENTER)

    #l_voltar= Button(frame_login, text="Voltar a tela de Login", font=('Ivy 15 bold'), compound=LEFT, width=20, overrelief=RIDGE, relief="solid", bg=co1, fg=co6)
    #l_voltar.place(x=450, y=400, anchor=CENTER)
    
    
def painel():
    global v_mes_var
    v_mes_var = tk.StringVar()
    
    frame_cima = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_cima.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)
    
    frame_botao = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_botao.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)

    frame_baixo = Frame(root, width=900, height=200, bg=co1, relief='flat')
    frame_baixo.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)
    #################---------TITULO------##################################################################################
    l_titulo= Label(frame_cima, text="Controle de Rotas e Ganhos", anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
    l_titulo.place(x=0, y=0, relwidth=1, relheight=1)
    #################---------CONFIGURAÇÃO------##################################################################################
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Pode variar por sistema operaciona   
    
    
    
    
    
    
root.mainloop()