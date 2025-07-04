#GUI histograma

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# === FUNÇÃO PRINCIPAL ===
def gerar_histogramas_para_multiplas_amostras(df, sigma=1.5, prominence=1.0, distance=3,
                                              salvar_png=False, salvar_estatisticas=False,
                                              arquivo_saida_estatisticas=None):
    unidade = 'μm'
    num_bins = 100
    estatisticas = []

    if df.shape[1] < 2:
        raise ValueError("O DataFrame deve ter ao menos duas colunas (diâmetro + uma amostra).")

    diametros = df.iloc[:, 0].values
    nomes_amostras = df.columns[1:]

    for nome_amostra in nomes_amostras:
        percentuais = df[nome_amostra].values
        mask_validos = (percentuais > 0) & (diametros > 0)
        diametros_validos = diametros[mask_validos]
        percentuais_validos = percentuais[mask_validos]

        if len(diametros_validos) == 0:
            print(f"⚠️ Nenhum valor válido para a amostra '{nome_amostra}'. Pulando.")
            continue

        media = np.average(diametros_validos, weights=percentuais_validos)
        desvio_padrao = np.sqrt(np.average((diametros_validos - media)**2, weights=percentuais_validos))
        minimo_pct = np.min(diametros_validos)
        maximo_pct = np.max(diametros_validos)

        def percentil_ponderado(valores, pesos, percentil):
            ordem = np.argsort(valores)
            valores_ord = valores[ordem]
            pesos_ord = pesos[ordem]
            cumul = np.cumsum(pesos_ord) / np.sum(pesos_ord)
            return np.interp(percentil / 100, cumul, valores_ord)

        p10 = percentil_ponderado(diametros_validos, percentuais_validos, 10)
        p50 = percentil_ponderado(diametros_validos, percentuais_validos, 50)
        p65 = percentil_ponderado(diametros_validos, percentuais_validos, 65)
        p90 = percentil_ponderado(diametros_validos, percentuais_validos, 90)

        bins = np.logspace(np.log10(0.01), np.log10(10000), num_bins)
        counts, edges = np.histogram(diametros, bins=bins, weights=percentuais)
        centros = (edges[:-1] + edges[1:]) / 2

        smoothed = gaussian_filter1d(counts, sigma=sigma)
        peaks, _ = find_peaks(smoothed, prominence=prominence, distance=distance)
        modais_diametros = centros[peaks]
        modais_str = ', '.join([f'{d:.2f}' for d in modais_diametros]) if len(modais_diametros) > 0 else "Nenhum detectado"

        texto_legenda = (
            f"Amostra: {nome_amostra}\n"
            f"N° Classes: {len(diametros_validos)}\n"
            f"Min.: {minimo_pct:.2f} {unidade}\n"
            f"Máx.: {maximo_pct:.2f} {unidade}\n"
            f"Média: {media:.2f} {unidade}\n"
            f"Desv. Padrão: ±{desvio_padrao:.2f} {unidade}\n"
            f"D10: {p10:.2f} {unidade}\n"
            f"D50: {p50:.2f} {unidade}\n"
            f"D65: {p65:.2f} {unidade}\n"
            f"D90: {p90:.2f} {unidade}\n"
            f"Modais: {modais_str} {unidade}"
        )

        # Plot
        plt.figure(figsize=(11, 5))
        plt.hist(diametros, bins=bins, weights=percentuais, edgecolor='black', color='cornflowerblue')
        plt.xscale('log')
        plt.xlabel(f'Tamanho das partículas ({unidade}) [escala log]')
        plt.ylabel('Percentual (%)')
        plt.title(nome_amostra)
        plt.grid(True, which='both', linestyle='--', alpha=0.6)

        plt.gca().text(1.05, 0.5, texto_legenda, transform=plt.gca().transAxes,
                       fontsize=9, verticalalignment='center',
                       bbox=dict(boxstyle="round", facecolor='whitesmoke', edgecolor='gray'))

        plt.tight_layout(rect=[0, 0, 0.85, 1])

        if salvar_png:
            nome_fig = f"{nome_amostra}.png".replace(" ", "_")
            plt.savefig(nome_fig, dpi=300)

        plt.show()

        estatisticas.append({
            'Amostra': nome_amostra,
            'Min': minimo_pct,
            'Max': maximo_pct,
            'Média': media,
            'Desvio Padrão': desvio_padrao,
            'D10': p10,
            'D50': p50,
            'D65': p65,
            'D90': p90,
            'Modais': modais_str
        })

    if salvar_estatisticas and arquivo_saida_estatisticas:
        df_stats = pd.DataFrame(estatisticas)
        df_stats.to_excel(arquivo_saida_estatisticas, index=False)

# === INTERFACE GRÁFICA ===
class InterfaceAnaliseAmostras:
    def __init__(self, master):
        self.master = master
        master.title("Análise de Amostras Granulométricas")

        self.label_entrada = tk.Label(master, text="Arquivo Excel de entrada:")
        self.label_entrada.grid(row=0, column=0, sticky="w")
        self.entrada_entry = tk.Entry(master, width=50)
        self.entrada_entry.grid(row=0, column=1, padx=5)
        self.entrada_btn = tk.Button(master, text="Selecionar", command=self.selecionar_arquivo)
        self.entrada_btn.grid(row=0, column=2)

        self.salvar_png_var = tk.IntVar()
        self.salvar_png_check = tk.Checkbutton(master, text="Salvar gráficos como PNG", variable=self.salvar_png_var)
        self.salvar_png_check.grid(row=2, column=1, sticky="w", pady=5)

        self.rodar_btn = tk.Button(master, text="Rodar Análise", command=self.rodar_analise, bg="green", fg="white")
        self.rodar_btn.grid(row=3, column=1, pady=15)

    def selecionar_arquivo(self):
        caminho = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if caminho:
            self.entrada_entry.delete(0, tk.END)
            self.entrada_entry.insert(0, caminho)

    def rodar_analise(self):
        caminho_entrada = self.entrada_entry.get()
        salvar_png = self.salvar_png_var.get()

        if not os.path.exists(caminho_entrada):
            messagebox.showerror("Erro", "Arquivo de entrada inválido.")
            return

        try:
            df = pd.read_excel(caminho_entrada)

            # Criar caminho de saída automático
            nome_entrada = os.path.basename(caminho_entrada)
            nome_base = os.path.splitext(nome_entrada)[0]
            diretorio = os.path.dirname(caminho_entrada)
            caminho_saida = os.path.join(diretorio, f"estatisticas_{nome_base}.xlsx")

            gerar_histogramas_para_multiplas_amostras(
                df,
                salvar_png=bool(salvar_png),
                salvar_estatisticas=True,
                arquivo_saida_estatisticas=caminho_saida
            )

            messagebox.showinfo("Sucesso", f"Análise concluída!\nArquivo salvo em:\n{caminho_saida}")
        except Exception as e:
            messagebox.showerror("Erro durante execução", str(e))
            
    # === RODAR APP ===
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceAnaliseAmostras(root)
    root.mainloop()