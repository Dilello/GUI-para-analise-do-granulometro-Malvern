# GUI para Análise da Saída do Granulometro a Laser Malvern

## 1 - Pré-Requisitos

* Instalar Excel;
* Instalar o Anaconda do python;

## 2 - Criar uma planilha.xlsx de input

Nesta planilha, a primeira coluna conterá as classes de diâmetros, em mícrons, discretizados pelo granulômetro Malvern. As demais colunas deverão conter o percentual de cada classe diâmetros, onde o cabeçalho de cada coluna deve ser o nome ou código da amostra. 
Aqui segue uma planilha teste de referência (Ex.: amostra_teste.xlsx).

## 3 - Criar um diretório de trabalho

Criar um diretório de trabalho (Ex.: c:\Users\Cliente\Documentos\Malvern\)
Neste diretório deverá conter:

* A planilha (Ex.: amostra_teste.xlsx) com os dados medidos pelo granulômetro;
* A rotina GUIhistograma.py;

## 4 - Uso da interface GUI

Abrir o terminal do Anaconda, dentro da pasta onde está o seu script:

cd c:\Users\Cliente\Malvern\

Depois, digite:

python GUIhistograma.py

Ao dar enter, uma janela do GUI vai abrir. Nesta janela, clique na opção 'Selecionar', onde pedirá para localizar e selecionar o arquivo de entrada com dados medidos pelo granulômetro (Ex.: c:\Users\Cliente\Documentos\Malvern\amostra_teste.xlsx) que deseja analisar.
Caso tenha interesse em salvar o gráficos, habilite também a opção 'Salvar gráficos como PNG'.

## 5 - Dados de saída

Ao clicar em 'Rodar Análise', serão gerados os gráficos da análise granulométrica e uma planilha de excel .xlsx com o resumo estatístico (Número de classes, Máximo, Mínimo, Média, Desvio Padrão, D10, D50, D65, D90, Modais). Este produtos serão salvos no diretório de trabalho (Ex.: c:\Users\Cliente\Documentos\Malvern\)
