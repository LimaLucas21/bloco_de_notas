import tkinter as tk
from tkinter import filedialog, messagebox
from Core.config_bar import ConfigBar 

class BlocoNotas:
    def __init__(self):
        self.config_bar = ConfigBar(self)
        
        self.janela = tk.Tk()
        self.janela.title("Bloco de Notas")
        self.janela.geometry("800x600")

        #
        self.frame_principal = tk.Frame(self.janela)
        self.frame_
        #

        self.Menu = tk.Menu(self.janela)

        self.janela.config(menu=self.Menu)

        self.MenuArquivo = tk.Menu(self.Menu, tearoff=0)
        self.MenuEditar = tk.Menu(self.Menu, tearoff=0)

        self.Menu.add_cascade(label="Arquivo", menu=self.MenuArquivo)
        self.Menu.add_cascade(label="Editar", menu=self.MenuEditar)

        self.MenuArquivo.add_command(label="Novo", command=self.config_bar.novo_arquivo)
        self.MenuArquivo.add_command(label="Abrir", command=lambda: self.config_bar.abrir_arquivo())
        self.MenuArquivo.add_command(label="Salvar", command=self.config_bar.salvar_arquivo)
        self.MenuArquivo.add_separator()
        self.MenuArquivo.add_command(label="Sair", command=self.janela.quit)


        self.MenuEditar.add_command(label= 'Desfazer', command=self.Texto.edit_undo)
        self.MenuEditar.add_command(label= 'Refazer', command=self.Texto.edit_redo)
        self.MenuEditar.add_command(label='Recortar', command=lambda: self.config_bar.func_editar("cut"))
        self.MenuEditar.add_command(label='Copiar', command=lambda: self.config_bar.func_editar("copy"))
        self.MenuEditar.add_command(label='Colar', command=lambda: self.config_bar.func_editar("paste"))
        self.MenuEditar.add_separator()
        self.MenuEditar.add_command(label='Selecionar Tudo', command=lambda: self.config_bar.func_editar("select_all"))
        
        # 2. Variável para armazenar caminho do arquivo atual
        self.arquivo_atual = None

        
        # 3. Chamar método para criar interface
        self.criar_interface()
        
    def criar_interface(self):
        # Aqui vamos construir os widgets
        pass
        
    def executar(self):
        # Iniciar loop principal
        self.janela.mainloop()

# Executar aplicação
if __name__ == "__main__":
    app = BlocoNotas()
    app.executar()