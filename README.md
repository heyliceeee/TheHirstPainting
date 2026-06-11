# 🎨 Hirst Dot Painting – Turtle Graphics Project

This project recreates a style inspired by Damien Hirst’s artwork, using Python’s **turtle** module to draw a grid of colorful dots.  
The result is an artistic pattern made of 100 dots, each with a random color selected from a predefined palette.

---

## 🐢 About the Project

The goal of this exercise is to practice:

- Working with the **turtle** graphics library  
- Moving the turtle around the screen  
- Using **RGB colors** with `colormode(255)`  
- Loops and control flow  
- Generating geometric patterns  
- Writing clean, well‑commented code  

The program draws a 10×10 grid of dots, each 20px in diameter and spaced 50px apart.

---

## ✨ Features

- 🎨 Custom color palette (RGB list extracted from an image)  
- 🐢 Precise turtle movement to create a perfect grid  
- 🔵 Dot drawing using `tim.dot()`  
- ↕️ Automatic line breaks after every 10 dots  
- 🎲 Random color selection for each dot  
- 👁️ Hidden turtle for a cleaner drawing  

---

## 📂 Code Structure

```
project/
│
├── main.py
└── README.md
```

### **main.py**
Includes:
- RGB color list  
- Turtle configuration  
- Logic for drawing the dot grid  
- Automatic movement between rows  

---

## 🧠 Drawing Logic

1. The turtle moves to the bottom‑left corner.  
2. Draws a dot.  
3. Moves forward 50px.  
4. Repeats until completing 10 dots.  
5. Moves up one row, goes back 500px, and starts the next line.  
6. Repeats until all 100 dots are drawn.  
