from tkinter import filedialog, messagebox
import tkinter as tk

class ConfigBar:
    def __init__(self, app):
        self.app = app

    def novo_arquivo(self):
        self.app.Texto.delete('1.0', tk.END)
        self.app.arquivo_atual = None   

    def abrir_arquivo(self):
        arquivo_selecionado = filedialog.askopenfilename()

        if arquivo_selecionado:
            try:
                with open(arquivo_selecionado, 'r', encoding='utf-8') as arquivo:
                    conteudo = arquivo.read()
                self.app.Texto.delete('1.0', tk.END)
                self.app.Texto.insert('1.0', conteudo)
                self.app.arquivo_atual = arquivo_selecionado

            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")
        
    def salvar_arquivo(self):
        if self.app.arquivo_atual:

        else:    
            self.app.arquivo_atual = 