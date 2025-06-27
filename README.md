# GUI para Análise da Saída do Granulometro a Laser Malvern

## 1 - Criar uma planilha.xlsx de input

Nesta planilha, a primeira coluna conterá as classes de diâmetros, em mícrons, discretizados pelo granulômetro Malvern. As demais colunas deverão conter o percentual de cada classe diâmetros, onde o cabeçalho de cada coluna deve ser o nome ou código da amostra. 
Aqui segue uma planilha teste de referência (amostra_teste.xlsx).

## 2 - Criar um diretório de trabalho

Criar um diretório de trabalho (Ex.: c:\Users\Cliente\Documentos\Malvern\)
Neste diretório deverá conter:

* A planilha com os dados medidos pelo granulômetro;
* O executável GUIhistograma.exe;

## 3 - Uso da interfaca GUI

Ao clicar no executável GUIhistograma.exe, uma janela vai abrir, onde se pede para inserir o caminho até o arquivo de entrada com dados medidos pelo granulômetro (Ex.: c:\Users\Cliente\Documentos\Malvern\amostra_teste.xlsx).
Caso tenha interesse em salvar o gráficos, abilite a opção 'Slvar gráficos como PNG'.

## 4 - Dados de saída

Ao clicar em Rodar Análise, serão gerados os gráficos da análise granulométrica e uma planilha de excel .xlsx com o resumo estatístico (Número de classes, Máximo, Mínimo, Média, Desvio Padrão, D10, D50, D65, D90, Modais). Este produtos serão salvos no diretório de trabalho (Ex.: c:\Users\Cliente\Documentos\Malvern\)
