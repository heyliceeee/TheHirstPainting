# 🎨 Hirst Dot Painting – Turtle Graphics Project

Este projeto recria um estilo inspirado nas obras de Damien Hirst, utilizando o módulo **turtle** do Python para desenhar uma grelha de pontos coloridos.  
O resultado é um padrão artístico composto por 100 pontos, cada um com uma cor aleatória retirada de uma paleta pré-definida.

---

## 🐢 Sobre o Projeto

O objetivo deste exercício é praticar:

- Manipulação da biblioteca **turtle**
- Movimentação da tartaruga no ecrã
- Uso de **RGB colors** com `colormode(255)`
- Loops e controlo de fluxo
- Geração de padrões geométricos
- Organização de código com comentários claros

O programa desenha uma grelha de 10x10 pontos, cada um com 20px de diâmetro e espaçados 50px entre si.

---

## ✨ Funcionalidades

- 🎨 Paleta de cores personalizada (lista de RGB extraída de uma imagem)
- 🐢 Movimentação precisa da turtle para criar uma grelha perfeita
- 🔵 Desenho de pontos com `tim.dot()`
- ↕️ Mudança automática de linha após cada 10 pontos
- 🎲 Seleção aleatória de cores para cada ponto
- 👁️ Turtle escondida para um desenho mais limpo

---

## 📂 Estrutura do Código

```
project/
│
├── main.py
└── README.md
```

### **main.py**
Contém:
- Lista de cores RGB
- Configuração da turtle
- Lógica para desenhar a grelha de pontos
- Movimento automático entre linhas

---

## 🧠 Lógica do Desenho

1. A turtle é movida para o canto inferior esquerdo.
2. Desenha um ponto.
3. Avança 50px.
4. Repete até completar 10 pontos.
5. Sobe uma linha, volta para trás 500px e começa a linha seguinte.
6. Repete até desenhar 100 pontos.