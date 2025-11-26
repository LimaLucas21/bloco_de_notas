import tkinter as tk
from tkinter import filedialog, messagebox
from Core.config_bar import ConfigBar

class BlocoNotas:
    def __init__(self):
        self.config_bar = ConfigBar(self)
        
        self.janela = tk.Tk()
        self.janela.title("Bloco de Notas")
        self.janela.geometry("800x600")
        self.Texto = tk.Text(self.janela, wrap='word', undo=True)
        self.Texto.pack(expand=True, fill='both')
        self.Menu = tk.Menu(self.janela)
        self.janela.config(menu=self.Menu)
        self.MenuArquivo = tk.Menu(self.Menu, tearoff=0)
        self.MenuEditar = tk.Menu(self.Menu, tearoff=0)
        self.Menu.add_cascade(label="Arquivo", menu=self.MenuArquivo)
        self.Menu.add_cascade(label="Editar", menu=self.MenuEditar)
        self.MenuArquivo.add_command(label="Novo", command=ConfigBar.novo_arquivo)
        self.MenuArquivo.add_command(label="Abrir", command=lambda: self.config_bar.abrir_arquivo())
        self.MenuArquivo.add_command(label="Salvar", command=ConfigBar.menu_arquivo)
        self.MenuArquivo.add_separator()
        self.MenuArquivo.add_command(label="Sair", command=self.janela.quit)
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