# GUI para Análise da Saída do Granulometro a Laser Malvern

## 1 - Pré-Requisitos

* Instalar o Anaconda do python;

## 2 - Criar um diretório de trabalho

Criar um diretório de trabalho (Ex.: c:\Users\Cliente\Documentos\Malvern\)
Neste diretório deverá conter:

* O arquivo .txt (Ex.: 11072025_ Tipos de sedimentos.txt) com os dados medidos pelo granulômetro;
* A rotina GUIhistograma.py;

## 3 - Uso da interface GUI

Abrir o terminal do Anaconda, dentro da pasta onde está o seu script, por exemplo:

```python
# cd c:\Users\Cliente\Malvern\
```

Digite:

```python
# python GUIhistograma.py
```

Ao clicar enter, uma janela do GUI vai abrir. Nesta janela, clique na opção 'Selecionar', onde pedirá para localizar e selecionar o arquivo de entrada com dados medidos pelo granulômetro (Ex.: c:\Users\Cliente\Documentos\Malvern\11072025_ Tipos de sedimentos.txt) que deseja analisar.
Caso tenha interesse em salvar o gráficos, habilite também a opção 'Salvar gráficos como PNG'.

## 4 - Dados de saída

Ao clicar em 'Rodar Análise', serão gerados os gráficos do tipo histograma da análise granulométrica individual e comparativa e uma planilha de excel .xlsx com o resumo estatístico (Número de classes, Máximo, Mínimo, Média, Desvio Padrão, D10, D50, D65, D90, Modais) e outra com os dados de entrada. Este produtos serão salvos no diretório de trabalho (Ex.: c:\Users\Cliente\Documentos\Malvern\)
