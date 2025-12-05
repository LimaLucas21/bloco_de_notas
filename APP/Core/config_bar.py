from tkinter import filedialog, messagebox
import tkinter as tk
import os

class ConfigBar:
    def __init__(self, app):
        self.app = app

    def func_editar(self, operacao):
        if operacao == "cut":
            self.app.Texto.event_generate("<<Cut>>")
        elif operacao == "copy":
            self.app.Texto.event_generate("<<Copy>>")
        elif operacao == "paste":
            self.app.Texto.event_generate("<<Paste>>")
        elif operacao == "select_all":
            self.app.Texto.tag_add('sel', '1.0', 'end')

    def novo_arquivo(self):
        self.app.Texto.delete('1.0', tk.END)
        self.app.arquivo_atual = None   
        self.app.janela.tittle('Bloco de Notas - Novo Arquivo')

    def abrir_arquivo(self):
        arquivo_selecionado = filedialog.askopenfilename()

        if arquivo_selecionado:
            try:
                with open(arquivo_selecionado, 'r', encoding='utf-8') as arquivo:
                    conteudo = arquivo.read()
                self.app.Texto.delete('1.0', tk.END)
                self.app.Texto.insert('1.0', conteudo)
                self.app.arquivo_atual = arquivo_selecionado
                self.app.janela.title(f"Bloco de Notas - {os.path.basename(arquivo_selecionado)}")

            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")
        
    def salvar_arquivo(self):
        arquivo_atual = self.app.arquivo_atual
        if not arquivo_atual:
            self.salvar_arquivo_como()
        else:
            try:
                conteudo = self.app.Texto.get('1.0', tk.END)
                with open(arquivo_atual, 'w', encoding='utf-8') as arquivo:
                    arquivo.write(conteudo)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar o arquivo: {e}")

    def salvar_arquivo_como(self):
        arquivo_selecionado = filedialog.asksaveasfilename(defaultextension='.txt',filetypes=[("Descrição", "*.extensão"), ("Outra descrição", "*.*")])
        if arquivo_selecionado:
            try:
                conteudo = self.app.Texto.get('1.0', tk.END)
                with open(arquivo_selecionado, 'w', encoding='utf-8') as arquivo:
                    arquivo.write(conteudo)
                    self.app.arquivo_atual = arquivo_selecionado
                    self.app.janela.title(f"Bloco de Notas - {os.path.basename(arquivo_selecionado)}")

            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível salvar o arquivo: {e}")
