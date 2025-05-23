from pacotes import *
from views import*
from tkcalendar import Calendar


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


frame_login = Frame(root, width=950, height=750, bg=co1)
frame_login.place(x=0, y=0)


######################################################################################
################Login#################################################################
######################################################################################


def login():
    

    #destruir frame login
    def cad_usuario():
        for widget in frame_login.winfo_children():
            widget.destroy()
        tela_cadastrar_usuario()
    def abrir_painel():
        for widget in frame_login.winfo_children():
            widget.destroy()
        painel()
    

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
            abrir_painel()
        else:
            messagebox.showerror("Erro", "Usuario ou senha incorretos!")
            cursor.close()
    

    frame_t_login= Frame(frame_login, width=900, height=600, bg=co1)
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
        login()
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

    l_voltar = Button(frame_login,command=login, text="Voltar", font=('Ivy 15 bold'), compound=LEFT, width=20, overrelief=RIDGE, relief="solid", bg=co1, fg=co6)
    l_voltar.place(x=450, y=400, anchor=CENTER)

############################################################################################################################################
###################################### PAINEL PRINCIPAL ##################################################################################
############################################################################################################################################# 

def painel():
    
    def abrir_ml():
        for widget in frame_titulo.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_botao.winfo_children():
            widget.destroy()
        ml_rota()


    global v_mes_var
    v_mes_var = tk.StringVar()
    
    frame_titulo = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_titulo.grid(row=0, column=0, sticky="nsew")

    frame_botao = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_botao.grid(row=1, column=0, sticky="nsew")

    frame_baixo = Frame(root, width=900, height=200, bg=co1, relief='flat')
    frame_baixo.grid(row=2, column=0, sticky="nsew")

    frame_tabela = Frame(root, width=900, height=300, bg=co1, relief='flat')
    frame_tabela.grid(row=3, column=0, sticky="nsew")
    #################---------TITULO------##################################################################################
    l_titulo= Label(frame_titulo, text="Controle de Rotas e Ganhos", anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
    l_titulo.place(x=0, y=0, relwidth=1, relheight=1)
    #################---------CONFIGURAÇÃO------##################################################################################
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Pode variar por sistema operaciona   
    #################---------BOTÕES------##################################################################################
    bt_ml = Button(frame_botao, command=abrir_ml, text="Mercado Livre", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_ml.grid(row=0, column=0, padx=1, pady=1)

    bt_sp = Button(frame_botao, command=sp_rota, text="Shopee", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_sp.grid(row=0, column=1, padx=1, pady=1)

    bt_euentrego = Button(frame_botao, command=ee_rota, text="Eu Entrego", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_euentrego.grid(row=0, column=2, padx=1, pady=1)

    bt_abast = Button(frame_botao, command=None, text="Abastecimento", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_abast.grid(row=0, column=3, padx=1, pady=1)

    bt_lucroanual = Button(frame_botao, command=None, text="Lucro Anual", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_lucroanual.grid(row=0, column=4, padx=1, pady=1)

    bt_lucpormes = Button(frame_botao, command=None, text="Lucro por Mês", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_lucpormes.grid(row=0, column=5, padx=1, pady=1)

    bt_contas = Button(frame_botao, command=None, text="Contas", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_contas.grid(row=0, column=6, padx=1, pady=1)

    bt_contaml = Button(frame_botao, command=None, text="Conta Mercado Livre", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_contaml.grid(row=0, column=7, padx=1, pady=1)


############################################################################################################################################
###################################### ROTA MERCADO LIVRE ##################################################################################
#############################################################################################################################################
def ml_rota():
    
    frame_titulo = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_titulo.grid(row=0, column=0, sticky="nsew")
    
    frame_botao = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_botao.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)

    frame_baixo = Frame(root, width=900, height=200, bg=co1, relief='flat')
    frame_baixo.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)

    frame_tabela = Frame(root, width=900, height=350, bg=co1, relief='flat')
    frame_tabela.grid(row=3, column=0, padx=0, pady=0, sticky=NSEW)

    #################---------TITULO------##################################################################################
    l_titulo= Label(frame_titulo, text="Rota Mercado Livre", anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
    l_titulo.place(x=0, y=0, relwidth=1, relheight=1)
    #################---------CONFIGURAÇÕES BOTÕES------##################################################################################
    def voltar_painel():
        for widget in frame_cima.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_botao.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        painel()

    ################---------CONFIGURAÇÃO DE DADOS------##################################################################################
    v_mes_var = tk.StringVar()
    #################---------CONFIGURAÇÕES GERAL   ------##################################################################################
    def calcular_media_combustivel():
        try:
            valor_rota = float(e_valor_rota.get())
            km = float(e_km.get())
            valor_bomba = float(e_v_comb.get())
            entregue = int(e_entregas.get())
            devolvidas = int(e_dev.get())

            # Calcula total de entregas realizadas
            total_entregas = entregue - devolvidas
            e_Total_entregas.delete(0, END)
            e_Total_entregas.insert(0, str(total_entregas))

            # Calcula o gasto com combustível (média de 10 km por litro)
            gasto_combustivel = (km / 10) * valor_bomba
            # Calcula o lucro: valor da rota - gasto com combustível
            lucro = valor_rota - gasto_combustivel

            # Mostra o lucro no campo de lucro
            e_lucro.delete(0, END)
            e_lucro.insert(0, f"{lucro:.2f}")

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
            
    def cadastrar_dados():
        data = e_data.get()
        dia_semana = e_d_semana.get()

        # Verifica campos obrigatórios de texto antes de conversões
        if not all([data, dia_semana, e_valor_rota.get(), e_km.get(), e_v_comb.get(), e_lucro.get(), e_entregas.get(), e_dev.get(), e_Total_entregas.get()]):
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            valor_rota = float(e_valor_rota.get())
            km = float(e_km.get())
            valor_bomba = float(e_v_comb.get())
            lucro = float(e_lucro.get())
            entregas = int(e_entregas.get())
            devolvidas = int(e_dev.get())
            total = float(e_Total_entregas.get())
        except ValueError:
            messagebox.showerror("Erro", "Verifique se os valores numéricos estão corretos.")
            return

        lista = [data, dia_semana, valor_rota, km, valor_bomba, lucro, entregas, devolvidas, total]

        # Inserindo no banco de dados
        criar_dados_ml(lista)

        messagebox.showinfo("Sucesso", "Dados cadastrados com sucesso!")

        # Limpa os campos após o cadastro
        for campo in [e_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas]:
            campo.delete(0, END)

    def calcular_total_valor_rota():
        try:
            with con:
                cur = con.cursor()
                cur.execute('SELECT SUM(valor_rota) FROM Rota_Mercado_Livre')
                resultado = cur.fetchone()[0]
                return resultado if resultado is not None else 0
        except Exception as e:
            print(f"Erro ao calcular total de valor_rota: {e}")
            return 0

    def atualizar_entry_valor_rota():
        total = calcular_total_valor_rota()
        v_mes_var.set(f"R$ {total:.2f}")

    def update_dados():
        try:
            tree_itens = tree_lucro.focus()
            tree_dicionario = tree_lucro.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

        # Limpando campos
            for campo in [e_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas]:
                campo.delete(0, END)

            # Preenchendo os campos com os valores selecionados
            e_data.insert(0, tree_lista[1])
            e_d_semana.insert(0, tree_lista[2])
            e_valor_rota.insert(0, tree_lista[3])
            e_km.insert(0, tree_lista[4])
            e_v_comb.insert(0, tree_lista[5])
            e_lucro.insert(0, tree_lista[6])
            e_entregas.insert(0, tree_lista[7])
            e_dev.insert(0, tree_lista[8])
            e_Total_entregas.insert(0, tree_lista[9])

            # Função para salvar alterações
            def update():
                # Coleta de dados
                dados = [
                    e_data.get(),
                    e_d_semana.get(),
                    e_valor_rota.get(),
                    e_km.get(),
                    e_v_comb.get(),
                    e_lucro.get(),
                    e_entregas.get(),
                    e_dev.get(),
                    e_Total_entregas.get(),
                    valor_id
                ]

                if not all(dados[:-1]):
                    messagebox.showerror('Erro', 'Preencha todos os campos!')
                    return

                try:
                    atualizar_dados_ml(dados)
                    messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

                    for campo in [e_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas]:
                        campo.delete(0, END)

                    mostrar_ml()

                    if 'bt_update' in globals() and bt_update.winfo_exists():
                        bt_update.destroy()

                except Exception as e:
                    messagebox.showerror('Erro', f'Erro ao atualizar: {e}')

            # Botão de salvar alterações
            bt_update = Button(frame_botao, command=update, text="Salvar Atualizações", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
            bt_update.grid(row=0, column=8)

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela')

    def excluir_dados():
        try:
            tree_itens = tree_lucro.focus()
            tree_dicionario = tree_lucro.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Excluindo os dados
            excluir_dados_ml(valor_id)

            messagebox.showinfo('Sucesso', 'Os dados foram excluídos com sucesso!')

            # Atualizando a tabela
            mostrar_ml()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela')

    def calendario():
        def pegar_data():
            data_selecionada = cal.selection_get()
            e_data.delete(0, END)
            e_data.insert(0, data_selecionada.strftime("%d/%m/%Y"))

            # Mapear o dia da semana
            dias_traduzidos = {
                0: "Segunda-feira",
                1: "Terça-feira",
                2: "Quarta-feira",
                3: "Quinta-feira",
                4: "Sexta-feira",
                5: "Sábado",
                6: "Domingo"
            }

            dia_semana_num = data_selecionada.weekday()  # 0=Segunda, ..., 6=Domingo
            dia_semana_pt = dias_traduzidos[dia_semana_num]

            e_d_semana.delete(0, END)
            e_d_semana.insert(0, dia_semana_pt)

            calendario_root.destroy()

        calendario_root = Toplevel()
        calendario_root.title("Selecionar Data")
        calendario_root.resizable(width=False, height=False)
        largura_root = 200
        altura_root = 270
        largura_tela = calendario_root.winfo_screenwidth()
        altura_tela = calendario_root.winfo_screenheight()
        pos_x = (largura_tela - largura_root) // 2
        pos_y = (altura_tela - altura_root) // 2
        calendario_root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

        cal = Calendar(calendario_root, selectmode="day", date_pattern="dd/mm/yyyy")
        cal.pack(pady=20)

        Button(calendario_root, text="Selecionar", command=pegar_data).pack(pady=10)
    #################---------BOTÕES------##################################################################################
    bt_adicionar = Button(frame_botao, command=cadastrar_dados, text="Adicionar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_adicionar.place(x=10, y=10)

    bt_excluir = Button(frame_botao, command=excluir_dados, text="Excluir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_excluir.place(x=100, y=10)

    bt_imprimir = Button(frame_botao, command=None, text="Imprimir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_imprimir.place(x=200, y=10)

    bt_calc = Button(frame_botao, command=calcular_media_combustivel, text="Calcular", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_calc.place(x=300, y=10)

    bt_rela = Button(frame_botao, command=None, text="Relatório", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_rela.place(x=400, y=10)

    bt_atualizar = Button(frame_botao, command=update_dados, text="Atualizar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_atualizar.place(x=500, y=10)

    bt_voltar = Button(frame_botao, command=voltar_painel, text="Painel", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_voltar.place(x=600, y=10)

    #################--------LABEL------##################################################################################
    bt_calendario = Button(frame_baixo, text="Data", command=calendario)
    bt_calendario.place(x=10, y=10)
    e_data = Entry(frame_baixo, width=10, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_data.place(x=70, y=10)  

    l_d_semana = Label(frame_baixo, text="Dia da Semana:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_d_semana.place(x=190, y=10)
    e_d_semana = Entry(frame_baixo, width=12, justify=CENTER, font=('Ivy 10 bold'), relief='solid')
    e_d_semana.place(x=305, y=10)

    l_v_comb = Label(frame_baixo, text="Valor da Bomba R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_v_comb.place(x=390, y=10)
    e_v_comb = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_v_comb.place(x=520, y=10)

    l_v_mês = Label(frame_baixo, text="Valor Mensal R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_v_mês.place(x=390, y=40)
    e_v_mês = Entry(frame_baixo,textvariable=v_mes_var, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_v_mês.place(x=510, y=40)

    l_valor_rota = Label(frame_baixo, text="Valor Rota:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_valor_rota.place(x=10, y=40)
    e_valor_rota= Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_valor_rota.place(x=90, y=40)

    l_km = Label(frame_baixo, text="KM:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_km.place(x=10, y=70)
    e_km= Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_km.place(x=90, y=70)

    l_lucro = Label(frame_baixo, text="Lucro R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_lucro.place(x=10, y=100)
    e_lucro = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_lucro.place(x=90, y=100)

    l_entregas = Label(frame_baixo, text="Entregas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_entregas.place(x=170, y=40)
    e_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_entregas.place(x=240, y=40)

    l_dev = Label(frame_baixo, text="Devolvidas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_dev.place(x=170, y=70)
    e_dev = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_dev.place(x=250, y=70)

    l_Total_entregas = Label(frame_baixo, text="Total:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_Total_entregas.place(x=190, y=100)
    e_Total_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_Total_entregas.place(x=260, y=100)
    
    #Tabela Mercado Livre
    def mostrar_ml():
        
        # Atualizar os valores totais nos Entry
        atualizar_entry_valor_rota()
        # atualizar_e_v_mes()  # Removed as it is not defined

        # Atualizar os valores totais nos Entry
        atualizar_entry_valor_rota()
        # atualizar_e_v_mes()  # Removed as it is not defined

        app_nome = Label(frame_tabela, text="Registros de Rotas", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co6)
        app_nome.place(x=10, y=10)

        # Definição do cabeçalho
        list_header = ['id', 'Data', 'Dia da Semana', 'Valor R$', 'KM', 'Valor Bomba R$', 'Lucro R$', 'Entregas', 'Devolvidas', 'Total Entregas']
    
        # Obtém os dados do estoque
        df_list = ver_dados_ml() # Certifique-se de que essa função retorna os dados corretamente

        global tree_registro

        # Criando a Treeview
        tree_registro = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

        # Barras de rolagem
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_registro.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_registro.xview)  # Corrigido aqui

        tree_registro.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    
        # Posicionando os widgets
        tree_registro.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')

        frame_tabela.grid_rowconfigure(0, weight=12)

        # Configuração das colunas
        hd = ["nw", "center", "center", "center", "center", "center", "center", "center", "center", "center"]
        h = [40, 80, 100, 100, 100, 100, 100, 80, 80, 80]
    
        for n, col in enumerate(list_header):
            tree_registro.heading(col, text=col.title(), anchor=NW)
            tree_registro.column(col, width=h[n], anchor=hd[n])

        # Inserindo os dados
        if df_list:
            for item in df_list:
                    tree_registro.insert("", "end", values=item)

    mostrar_ml()

############################################################################################################################################
###################################### ROTA SHOPPEE ##################################################################################
#############################################################################################################################################
def sp_rota():
  
    frame_cima = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_cima.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)
    
    frame_botao = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_botao.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)

    frame_baixo = Frame(root, width=900, height=200, bg=co1, relief='flat')
    frame_baixo.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)
    
    frame_tabela = Frame(root, width=900, height=350, bg=co1, relief='flat')
    frame_tabela.grid(row=3, column=0, padx=0, pady=0, sticky=NSEW)
    #################---------TITULO------##################################################################################
    l_titulo=Label(frame_cima, text="Rota da Shoppee",anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
    l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

    #################---------CONFIGURAÇÕES BOTÕES------##################################################################################
    def voltar_painel():
        for widget in frame_cima.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_botao.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        painel()

    ################---------CONFIGURAÇÃO DE DADOS------#################################################################################
    v_mes_var = tk.StringVar()


    def calcular_media_combustivel():
        try:
            valor_rota = float(e_valor_rota.get())
            km = float(e_km.get())
            valor_bomba = float(e_v_comb.get())
            entregue = int(e_entregas.get())
            devolvidas = int(e_dev.get())

            # Calcula total de entregas realizadas
            total_entregas = entregue - devolvidas
            e_Total_entregas.delete(0, END)
            e_Total_entregas.insert(0, str(total_entregas))

            # Calcula o gasto com combustível (média de 10 km por litro)
            gasto_combustivel = (km / 10) * valor_bomba

            # Calcula o lucro: valor da rota - gasto com combustível
            lucro = valor_rota - gasto_combustivel

            # Mostra o lucro no campo de lucro
            e_lucro.delete(0, END)
            e_lucro.insert(0, f"{lucro:.2f}")

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

    def cadastrar_dados():
        data = e_data.get()
        dia_semana = e_d_semana.get()
        valor_rota = e_valor_rota.get()
        km = e_km.get()
        valor_bomba = e_v_comb.get()
        lucro = e_lucro.get()
        entregas = e_entregas.get()
        devolvidas = e_dev.get()
        total = e_Total_entregas.get()

        lista = [data,dia_semana, valor_rota, km, valor_bomba, lucro, entregas, devolvidas, total]

        # Verifica se algum campo está vazio
        for i in lista:
            if i == "":
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return

        # Inserindo no banco de dados
        criar_dados_s(lista)

        messagebox.showinfo("Sucesso", "Dados cadastrados com sucesso!")

        # Limpa os campos após o cadastro
        e_data.delete(0, END)
        e_d_semana.delete(0, END)
        e_valor_rota.delete(0, END)
        e_km.delete(0, END)
        e_v_comb.delete(0, END)           # <<< adicionado
        e_lucro.delete(0, END)
        e_entregas.delete(0, END)
        e_dev.delete(0, END)
        e_Total_entregas.delete(0, END)

    def calcular_total_valor_rota():
        try:
            with con:
                cur = con.cursor()
                cur.execute('SELECT SUM(valor_rota) FROM Rota_Shoppee')
                resultado = cur.fetchone()[0]
                return resultado if resultado is not None else 0
        except Exception as e:
            print(f"Erro ao calcular total de valor_rota: {e}")
            return 0

    def atualizar_entry_valor_rota():
        total = calcular_total_valor_rota()
        v_mes_var.set(f"R$ {total:.2f}")

    def update_dados():
        try:
            tree_itens = tree_lucro.focus()
            tree_dicionario = tree_lucro.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Limpando campos
            for campo in [e_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas]:
                campo.delete(0, END)

            # Preenchendo os campos com os valores selecionados
            e_data.insert(0, tree_lista[1])
            e_d_semana.insert(0, tree_lista[2])
            e_valor_rota.insert(0, tree_lista[3])
            e_km.insert(0, tree_lista[4])
            e_v_comb.insert(0, tree_lista[5])
            e_lucro.insert(0, tree_lista[6])
            e_entregas.insert(0, tree_lista[7])
            e_dev.insert(0, tree_lista[8])
            e_Total_entregas.insert(0, tree_lista[9])

            # Tentando carregar a imagem
            def update():
                # Pegando os dados atualizados
                entry_data = entry_data.get()
                e_d_semana = e_d_semana.get()
                e_valor_rota = e_valor_rota.get()
                e_km = e_km.get()
                e_v_comb = e_v_comb.get()
                e_lucro = e_lucro.get()
                e_entregas = e_entregas.get()
                e_dev = e_dev.get()
                e_Total_entregas = e_Total_entregas.get()
            
            
                lista = [entry_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas, valor_id]

                # Verificação de campos vazios
                if not all(lista[:-1]):  # Exclui o ID da verificação
                    messagebox.showerror('Erro', 'Preencha todos os campos!')
                    return

                try:
                    atualizar_dados_s(lista)
                    messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

                    # Limpa os campos
                    for campo in [entry_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas]:
                        campo.delete(0, END)

                    mostrar_s()

                    if 'botao_update' in globals() and bt_update.winfo_exists():
                        bt_update.destroy()

                except Exception as e:
                    messagebox.showerror('Erro', f'Erro ao atualizar: {e}')

            # Botão de salvar alterações
            bt_update = Button(frame_botao, command=update, text="Salvar Atualizações", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
            bt_update.grid(row=0, column=8)
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela')

    def excluir_dados():
        try:
            tree_itens = tree_lucro.focus()
            tree_dicionario = tree_lucro.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Excluindo os dados
            excluir_dados_s(valor_id)

            messagebox.showinfo('Sucesso', 'Os dados foram excluídos com sucesso!')

            # Atualizando a tabela
            mostrar_s()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela')

    def calendario():
        def pegar_data():
            data_selecionada = cal.selection_get()
            e_data.delete(0, END)
            e_data.insert(0, data_selecionada.strftime("%d/%m/%Y"))

            # Mapear o dia da semana
            dias_traduzidos = {
                0: "Segunda-feira",
                1: "Terça-feira",
                2: "Quarta-feira",
                3: "Quinta-feira",
                4: "Sexta-feira",
                5: "Sábado",
                6: "Domingo"
            }

            dia_semana_num = data_selecionada.weekday()  # 0=Segunda, ..., 6=Domingo
            dia_semana_pt = dias_traduzidos[dia_semana_num]

            e_d_semana.delete(0, END)
            e_d_semana.insert(0, dia_semana_pt)

            calendario_root.destroy()

        calendario_root = Toplevel()
        calendario_root.title("Selecionar Data")
        calendario_root.resizable(width=False, height=False)
        largura_root = 200
        altura_root = 270
        largura_tela = calendario_root.winfo_screenwidth()
        altura_tela = calendario_root.winfo_screenheight()
        pos_x = (largura_tela - largura_root) // 2
        pos_y = (altura_tela - altura_root) // 2
        calendario_root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

        cal = Calendar(calendario_root, selectmode="day", date_pattern="dd/mm/yyyy")
        cal.pack(pady=20)

        Button(calendario_root, text="Selecionar", command=pegar_data).pack(pady=10)



    #################---------BOTÕES------##################################################################################
    bt_adicionar = Button(frame_botao, command=cadastrar_dados, text="Adicionar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_adicionar.grid(row=0, column=1)

    bt_excluir = Button(frame_botao, command=excluir_dados, text="Excluir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_excluir.grid(row=0, column=2)

    bt_imprimir = Button(frame_botao, command=None, text="Imprimir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_imprimir.grid(row=0, column=3)

    bt_calc = Button(frame_botao, command=calcular_media_combustivel, text="Calcular", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_calc.grid(row=0, column=4)

    bt_rela = Button(frame_botao, command=None, text="Relatório", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_rela.grid(row=0, column=5)

    bt_atualizar = Button(frame_botao, command=update_dados, text="Atualizar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_atualizar.grid(row=0, column=6)

    bt_voltar = Button(frame_botao, command=voltar_painel, text="Painel", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_voltar.grid(row=0, column=7)
    
    #################--------LABEL------##################################################################################
    bt_calendario = Button(frame_baixo, text="Data", command=calendario)
    bt_calendario.place(x=10, y=10)
    e_data = Entry(frame_baixo, width=10, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_data.place(x=70, y=10) 

    l_d_semana = Label(frame_baixo, text="Dia da Semana:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_d_semana.place(x=190, y=10)
    e_d_semana = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_d_semana.place(x=305, y=10)

    l_v_comb = Label(frame_baixo, text="Valor da Bomba R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_v_comb.place(x=390, y=10)
    e_v_comb = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_v_comb.place(x=520, y=10)

    l_v_mês = Label(frame_baixo, text="Valor Mensal R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_v_mês.place(x=390, y=40)
    e_v_mês = Entry(frame_baixo,textvariable=v_mes_var, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_v_mês.place(x=510, y=40)

    l_valor_rota = Label(frame_baixo, text="Valor Rota:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_valor_rota.place(x=10, y=40)
    e_valor_rota= Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_valor_rota.place(x=90, y=40)

    l_km = Label(frame_baixo, text="KM:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_km.place(x=10, y=70)
    e_km= Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_km.place(x=90, y=70)

    l_lucro = Label(frame_baixo, text="Lucro R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_lucro.place(x=10, y=100)
    e_lucro = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_lucro.place(x=90, y=100)

    l_entregas = Label(frame_baixo, text="Entregas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_entregas.place(x=170, y=40)
    e_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_entregas.place(x=240, y=40)

    l_dev = Label(frame_baixo, text="Devolvidas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_dev.place(x=170, y=70)
    e_dev = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_dev.place(x=250, y=70)

    l_Total_entregas = Label(frame_baixo, text="Total:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_Total_entregas.place(x=190, y=100)
    e_Total_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_Total_entregas.place(x=260, y=100)


    #Tabela Shoppee
    def mostrar_s():
    
        # Atualizar os valores totais nos Entry
        atualizar_entry_valor_rota()
        # atualizar_e_v_mes()  # Removed as it is not defined

        # Atualizar os valores totais nos Entry
        atualizar_entry_valor_rota()
        # atualizar_e_v_mes()  # Removed as it is not defined

        app_nome = Label(frame_tabela, text="Registros de Rotas", height=1, pady=0, padx=0,relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
    
        # Cabeçalhos da tabela
        list_header = ['id', 'Data', 'Dia da Semana', 'Valor de Rota', 'Km', 'Valor Bomba', 'Lucro', 'Entregas', 'Devolvidas', 'Total']

        # Buscar dados
        df_list = ver_dados_s()

        # Criar Treeview
        global tree_lucro
        tree_lucro = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

        # Scrollbars
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_lucro.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_lucro.xview)
        tree_lucro.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Posicionar Treeview e Scrolls
        tree_lucro.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')

        # Expandir corretamente o grid
        frame_tabela.grid_rowconfigure(1, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        # Configurar colunas
        align = ["center"] * len(list_header)
        largura = [40, 100, 120, 100, 60, 100, 100, 100, 100, 100]

        for n, col in enumerate(list_header):
            tree_lucro.heading(col, text=col.title(), anchor="center")
            tree_lucro.column(col, width=largura[n], anchor=align[n])

        # Inserir dados
        for item in df_list:
            try:
                tree_lucro.insert("", "end", values=item)
            except Exception as e:
                print(f"Erro ao inserir item na tabela: {e}")
    mostrar_s()   
    
############################################################################################################################################    
###################################### ROTA EU ENTREGO ##################################################################################
#############################################################################################################################################
def ee_rota():
  
    frame_cima = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_cima.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)
    
    frame_botao = Frame(root, width=900, height=50, bg=co1, relief='flat')
    frame_botao.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)

    frame_baixo = Frame(root, width=900, height=200, bg=co1, relief='flat')
    frame_baixo.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)
    
    frame_tabela = Frame(root, width=900, height=350, bg=co1, relief='flat')
    frame_tabela.grid(row=3, column=0, padx=0, pady=0, sticky=NSEW)
    #################---------TITULO------##################################################################################
    l_titulo=Label(frame_cima, text="Rota da Shoppee",anchor=CENTER, font=('Ivy 13 bold'), bg=co6, fg=co0)
    l_titulo.place(x=0, y=0, relwidth=1, relheight=1)

    #################---------CONFIGURAÇÕES BOTÕES------##################################################################################
    def voltar_painel():
        for widget in frame_cima.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_botao.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        painel()

    ################---------CONFIGURAÇÃO DE DADOS------#################################################################################
    v_mes_var = tk.StringVar()


    def calcular_media_combustivel():
        try:
            valor_rota = float(e_valor_rota.get())
            km = float(e_km.get())
            valor_bomba = float(e_v_comb.get())
            entregue = int(e_entregas.get())
            devolvidas = int(e_dev.get())

            # Calcula total de entregas realizadas
            total_entregas = entregue - devolvidas
            e_Total_entregas.delete(0, END)
            e_Total_entregas.insert(0, str(total_entregas))

            # Calcula o gasto com combustível (média de 10 km por litro)
            gasto_combustivel = (km / 10) * valor_bomba

            # Calcula o lucro: valor da rota - gasto com combustível
            lucro = valor_rota - gasto_combustivel

            # Mostra o lucro no campo de lucro
            e_lucro.delete(0, END)
            e_lucro.insert(0, f"{lucro:.2f}")

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

    def cadastrar_dados():
        data = e_data.get()
        dia_semana = e_d_semana.get()
        valor_rota = e_valor_rota.get()
        km = e_km.get()
        valor_bomba = e_v_comb.get()
        lucro = e_lucro.get()
        entregas = e_entregas.get()
        devolvidas = e_dev.get()
        total = e_Total_entregas.get()

        lista = [data,dia_semana, valor_rota, km, valor_bomba, lucro, entregas, devolvidas, total]

        # Verifica se algum campo está vazio
        for i in lista:
            if i == "":
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return

        # Inserindo no banco de dados
        criar_dados_ee(lista)

        messagebox.showinfo("Sucesso", "Dados cadastrados com sucesso!")

        # Limpa os campos após o cadastro
        e_data.delete(0, END)
        e_d_semana.delete(0, END)
        e_valor_rota.delete(0, END)
        e_km.delete(0, END)
        e_v_comb.delete(0, END)           # <<< adicionado
        e_lucro.delete(0, END)
        e_entregas.delete(0, END)
        e_dev.delete(0, END)
        e_Total_entregas.delete(0, END)

    def calcular_total_valor_rota():
        try:
            with con:
                cur = con.cursor()
                cur.execute('SELECT SUM(valor_rota) FROM Rota_Eu_Entrego')
                resultado = cur.fetchone()[0]
                return resultado if resultado is not None else 0
        except Exception as e:
            print(f"Erro ao calcular total de valor_rota: {e}")
            return 0

    def atualizar_entry_valor_rota():
        total = calcular_total_valor_rota()
        v_mes_var.set(f"R$ {total:.2f}")

    def update_dados():
        try:
            tree_itens = tree_lucro.focus()
            tree_dicionario = tree_lucro.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Limpando campos
            for campo in [e_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas]:
                campo.delete(0, END)

            # Preenchendo os campos com os valores selecionados
            e_data.insert(0, tree_lista[1])
            e_d_semana.insert(0, tree_lista[2])
            e_valor_rota.insert(0, tree_lista[3])
            e_km.insert(0, tree_lista[4])
            e_v_comb.insert(0, tree_lista[5])
            e_lucro.insert(0, tree_lista[6])
            e_entregas.insert(0, tree_lista[7])
            e_dev.insert(0, tree_lista[8])
            e_Total_entregas.insert(0, tree_lista[9])

            # Tentando carregar a imagem
            def update():
                # Pegando os dados atualizados
                e_data = e_data.get()
                e_d_semana = e_d_semana.get()
                e_valor_rota = e_valor_rota.get()
                e_km = e_km.get()
                e_v_comb = e_v_comb.get()
                e_lucro = e_lucro.get()
                e_entregas = e_entregas.get()
                e_dev = e_dev.get()
                e_Total_entregas = e_Total_entregas.get()
            
            
                lista = [e_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas, valor_id]

                # Verificação de campos vazios
                if not all(lista[:-1]):  # Exclui o ID da verificação
                    messagebox.showerror('Erro', 'Preencha todos os campos!')
                    return

                try:
                    atualizar_dados_ee(lista)
                    messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso!')

                    # Limpa os campos
                    for campo in [e_data, e_d_semana, e_valor_rota, e_km, e_v_comb, e_lucro, e_entregas, e_dev, e_Total_entregas]:
                        campo.delete(0, END)

                    mostrar_e()

                    if 'botao_update' in globals() and bt_update.winfo_exists():
                        bt_update.destroy()

                except Exception as e:
                    messagebox.showerror('Erro', f'Erro ao atualizar: {e}')

            # Botão de salvar alterações
            bt_update = Button(frame_botao, command=update, text="Salvar Atualizações", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
            bt_update.grid(row=0, column=8)
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela')

    def excluir_dados():
        try:
            tree_itens = tree_lucro.focus()
            tree_dicionario = tree_lucro.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            # Excluindo os dados
            excluir_dados_ee(valor_id)

            messagebox.showinfo('Sucesso', 'Os dados foram excluídos com sucesso!')

            # Atualizando a tabela
            mostrar_e()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos alunos na tabela')

    def calendario():
        def pegar_data():
            data_selecionada = cal.selection_get()
            e_data.delete(0, END)
            e_data.insert(0, data_selecionada.strftime("%d/%m/%Y"))

            # Mapear o dia da semana
            dias_traduzidos = {
                0: "Segunda-feira",
                1: "Terça-feira",
                2: "Quarta-feira",
                3: "Quinta-feira",
                4: "Sexta-feira",
                5: "Sábado",
                6: "Domingo"
            }

            dia_semana_num = data_selecionada.weekday()  # 0=Segunda, ..., 6=Domingo
            dia_semana_pt = dias_traduzidos[dia_semana_num]

            e_d_semana.delete(0, END)
            e_d_semana.insert(0, dia_semana_pt)

            calendario_root.destroy()

        calendario_root = Toplevel()
        calendario_root.title("Selecionar Data")
        calendario_root.resizable(width=False, height=False)
        largura_root = 200
        altura_root = 270
        largura_tela = calendario_root.winfo_screenwidth()
        altura_tela = calendario_root.winfo_screenheight()
        pos_x = (largura_tela - largura_root) // 2
        pos_y = (altura_tela - altura_root) // 2
        calendario_root.geometry(f"{largura_root}x{altura_root}+{pos_x}+{pos_y}")

        cal = Calendar(calendario_root, selectmode="day", date_pattern="dd/mm/yyyy")
        cal.pack(pady=20)

        Button(calendario_root, text="Selecionar", command=pegar_data).pack(pady=10)

    #################---------BOTÕES------##################################################################################
    bt_adicionar = Button(frame_botao, command=cadastrar_dados, text="Adicionar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_adicionar.grid(row=0, column=1)

    bt_excluir = Button(frame_botao, command=excluir_dados, text="Excluir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_excluir.grid(row=0, column=2)

    bt_imprimir = Button(frame_botao, command=None, text="Imprimir", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_imprimir.grid(row=0, column=3)

    bt_calc = Button(frame_botao, command=calcular_media_combustivel, text="Calcular", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_calc.grid(row=0, column=4)

    bt_rela = Button(frame_botao, command=None, text="Relatório", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_rela.grid(row=0, column=5)

    bt_atualizar = Button(frame_botao, command=update_dados, text="Atualizar", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_atualizar.grid(row=0, column=6)

    bt_voltar = Button(frame_botao, command=voltar_painel, text="Painel", bd=9, bg=co1, fg=co6, font=('verdana', 9, 'bold'))
    bt_voltar.grid(row=0, column=7)
    
    #################--------LABEL------##################################################################################
    bt_calendario = Button(frame_baixo, text="Data", command=calendario)
    bt_calendario.place(x=10, y=10)
    e_data = Entry(frame_baixo, width=10, justify=LEFT, font=('Ivy 10 bold'),  relief='solid')
    e_data.place(x=70, y=10) 

    l_d_semana = Label(frame_baixo, text="Dia da Semana:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_d_semana.place(x=190, y=10)
    e_d_semana = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_d_semana.place(x=305, y=10)

    l_v_comb = Label(frame_baixo, text="Valor da Bomba R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_v_comb.place(x=390, y=10)
    e_v_comb = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_v_comb.place(x=520, y=10)

    l_v_mês = Label(frame_baixo, text="Valor Mensal R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_v_mês.place(x=390, y=40)
    e_v_mês = Entry(frame_baixo,textvariable=v_mes_var, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_v_mês.place(x=510, y=40)

    l_valor_rota = Label(frame_baixo, text="Valor Rota:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_valor_rota.place(x=10, y=40)
    e_valor_rota= Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_valor_rota.place(x=90, y=40)

    l_km = Label(frame_baixo, text="KM:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_km.place(x=10, y=70)
    e_km= Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_km.place(x=90, y=70)

    l_lucro = Label(frame_baixo, text="Lucro R$:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_lucro.place(x=10, y=100)
    e_lucro = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_lucro.place(x=90, y=100)

    l_entregas = Label(frame_baixo, text="Entregas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_entregas.place(x=170, y=40)
    e_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_entregas.place(x=240, y=40)

    l_dev = Label(frame_baixo, text="Devolvidas:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_dev.place(x=170, y=70)
    e_dev = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid')
    e_dev.place(x=250, y=70)

    l_Total_entregas = Label(frame_baixo, text="Total:", font=('Ivy 10 bold'), bg=co1, fg=co6)
    l_Total_entregas.place(x=190, y=100)
    e_Total_entregas = Entry(frame_baixo, width=10, justify=CENTER, font=('Ivy 10 bold'),  relief='solid', bg=co1, fg=co6)
    e_Total_entregas.place(x=260, y=100)


    #Tabela Shoppee
    def mostrar_e():
        
        # Atualizar os valores totais nos Entry
        atualizar_entry_valor_rota()
        # atualizar_e_v_mes()  # Removed as it is not defined

        # Atualizar os valores totais nos Entry
        atualizar_entry_valor_rota()
        # atualizar_e_v_mes()  # Removed as it is not defined

        app_nome = Label(frame_tabela, text="Registros de Rotas", font=('Ivy 12 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, sticky="nsew")

        list_header = ['id', 'Data', 'Dia da Semana', 'Valor de Rota', 'Km', 'Valor Bomba', 'Lucro', 'Entregas', 'Devolvidas', 'Total']
        df_list = ver_dados_ee()

        tree_lucro = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_lucro.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_lucro.xview)
        tree_lucro.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree_lucro.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')

        frame_tabela.grid_rowconfigure(1, weight=1)
        frame_tabela.grid_columnconfigure(0, weight=1)

        align = ["center"] * len(list_header)
        largura = [40, 100, 120, 100, 60, 100, 100, 100, 100, 100]

        for n, col in enumerate(list_header):
            tree_lucro.heading(col, text=col.title(), anchor="center")
            tree_lucro.column(col, width=largura[n], anchor=align[n])

        for item in df_list:
            try:
                tree_lucro.insert("", "end", values=item)
            except Exception as e:
                print(f"Erro ao inserir item na tabela: {e}")
    mostrar_e()


login()
root.mainloop()


#root.mainloop()