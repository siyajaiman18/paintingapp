import tkinter as tk
from tkinter import ttk

class PaintingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Painting App")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.pen_color = "black"
        self.pen_size = 2

        self.init_ui()

    def init_ui(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        color_menu = tk.Menu(menu_bar, tearoff=0)
        color_menu.add_command(label="Black", command=lambda: self.change_color("black"))
        color_menu.add_command(label="Red", command=lambda: self.change_color("red"))
        color_menu.add_command(label="Green", command=lambda: self.change_color("green"))
        color_menu.add_command(label="Blue", command=lambda: self.change_color("blue"))
        menu_bar.add_cascade(label="Colors", menu=color_menu)

        size_menu = tk.Menu(menu_bar, tearoff=0)
        size_menu.add_command(label="Small", command=lambda: self.change_size(2))
        size_menu.add_command(label="Medium", command=lambda: self.change_size(5))
        size_menu.add_command(label="Large", command=lambda: self.change_size(10))
        menu_bar.add_cascade(label="Pen Size", menu=size_menu)

        clear_button = ttk.Button(self.root, text="Clear Canvas", command=self.clear_canvas)
        clear_button.pack()

        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.stop_paint)

    def start_paint(self, event):
        self.last_x, self.last_y = event.x, event.y

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.pen_color, width=self.pen_size)
        self.last_x, self.last_y = x, y

    def stop_paint(self, event):
        pass

    def change_color(self, color):
        self.pen_color = color

    def change_size(self, size):
        self.pen_size = size

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintingApp(root)
    root.mainloop()
