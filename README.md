# Asteroid Run

## Sobre o Projeto
**Asteroid Run** é um jogo 2D desenvolvido em Python utilizando a biblioteca Pygame. O jogador é convocado para uma missão espacial secreta onde o objetivo principal é pilotar uma nave, desviar de uma chuva de asteroides e tentar acumular a maior pontuação possível (com a meta de alcançar 1000 pontos por nível).

Este projeto foi desenvolvido como requisito de avaliação da disciplina de Linguagem de Programação Aplicada do curso de Análise e Desenvolvimento de Sistemas da Uninter. O projeto consiste em uma versão "demo" totalmente jogável, contendo interface gráfica, efeitos sonoros e sistema de persistência de dados.

## Funcionalidades
* **Menu Interativo:** Navegação fluida entre Jogar, Ranking de Pontuação e Sair.
* **Instruções Integradas:** Tela dedicada de introdução e controles apresentada antes das partidas.
* **Customização:** Sistema de escolha de personagem permitindo selecionar entre 5 naves espaciais diferentes.
* **Sistema de Vidas e Colisão:** O jogador inicia com 10 vidas, perdendo uma a cada colisão com os obstáculos dinâmicos gerados aleatoriamente.
* **Ranking de Pontuação (Scoreboard):** Sistema de registro de nome do jogador e salvamento automático das 5 melhores pontuações no banco de dados, incluindo data e hora da partida.

## Controles do Jogo
* **Setas Direcionais (←, ↑, →, ↓):** Movimentam a nave pela tela.
* **ENTER:** Confirma seleções nos menus e avança as telas de diálogo.
* **ESC:** Encerra o jogo.

## Tecnologias Utilizadas
* **Linguagem:** Python 3.13.7
* **Biblioteca Gráfica/Motor do Jogo:** Pygame
* **Banco de Dados:** SQLite (via classe `DBProxy` para salvar o placar)

## Como Executar o Jogo (Versão Compilada)
Para rodar a versão compilada para Windows (sem necessidade de instalar o Python ou Pygame no computador), siga os passos abaixo:

1. Faça a extração (unzip) do arquivo entregue.
2. Certifique-se de que a pasta `asset` (que contém todas as imagens, fontes e músicas) e o banco de dados `DBScore` estejam no **mesmo diretório** do arquivo executável (`.exe`). *Nota: Sem a pasta de assets, o jogo não conseguirá carregar os gráficos e fechará.*
3. Dê um duplo clique no arquivo executável (ex: `main.exe` ou `AsteroidRun.exe`).
4. Caso ocorra algum erro e a janela feche rapidamente, abra o Prompt de Comando (CMD), navegue até a pasta do jogo e execute o `.exe` por lá para ler os logs de erro.
