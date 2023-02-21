# Pesquisa por Voz Usando Python

## Descrição

Este projeto tem como objetivo desenvolver um aplicativo Python capaz de realizar pesquisas num navegador a partir da fala do utilizador. A captura de áudio é realizada por meio da biblioteca SpeechRecognition, que transcreve a fala em texto. Com o texto transcrito, as bibliotecas de automação de navegador, como o Selenium, são utilizadas para realizar as pesquisas.

O principal benefício do aplicativo é a agilidade e praticidade que a entrada de voz proporciona, permitindo que o utilizador realize pesquisas sem a necessidade de digitar. Além disso, a implementação deste projeto pode ser especialmente útil para pessoas com dificuldades motoras ou deficiências visuais, que podem encontrar dificuldades em realizar a digitação convencional.

## Principais etapas do projeto

- Instalação das bibliotecas necessárias, incluindo o SpeechRecognition e as bibliotecas de automação de navegador, como o Selenium;
- Criação de uma função para capturar a entrada de áudio do utilizador, utilizando a biblioteca SpeechRecognition para transcrever a fala em texto;
- Utilização das bibliotecas de automação de navegador para realizar as pesquisas com base no texto transcrito;
- Testes para avaliar a efetividade e precisão do aplicativo, e ajustes necessários para garantir o seu bom funcionamento.

## Requisitos

- Python 3.11
- Biblioteca SpeechRecognition
- Biblioteca Selenium
- Biblioteca webdriver-manager
- Navegador compatível com o Selenium, como o Chrome ou Firefox

## Instalação

1. Clone o repositório para o seu computador.
2. Instale as bibliotecas necessárias executando o comando `pip install -r requisitos.txt`.
3. Certifique-se de ter um navegador compatível com o Selenium instalado no seu computador.
4. Execute o script `pesquisa_por_voz.py` para iniciar o aplicativo.


## Contribuições

Contribuições são bem-vindas e encorajadas! Sinta-se à vontade para abrir issues e pull requests no repositório.
