# import tkinter as tk

# class DrawingApp:
#     def __init__(self, root):
#         self.root = root
#         self.canvas = tk.Canvas(self.root, width=500, height=500)
#         self.canvas.pack()

#         self.canvas.bind("<B1-Motion>", self.draw)
#         self.canvas.bind("<Button-1>", self.start_drawing)
#         self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

#         self.drawing = False
#         self.last_x = 0
#         self.last_y = 0

#     def start_drawing(self, event):
#         self.drawing = True
#         self.last_x = event.x
#         self.last_y = event.y

#     def stop_drawing(self, event):
#         self.drawing = False

#     def draw(self, event):
#         if self.drawing:
#             self.canvas.create_line(self.last_x, self.last_y, event.x, event.y)
#             self.last_x = event.x
#             self.last_y = event.y

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("그림판")
#     app = DrawingApp(root)
#     root.mainloop()

import tkinter as tk
from tkinter import colorchooser

class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.color_button = tk.Button(self.root, text="색상 선택", command=self.pick_color)
        self.color_button.pack()

    def pick_color(self):
        color = colorchooser.askcolor(title="색상 선택")
        if color[1]:
            self.root.configure(background=color[1])

if __name__ == "__main__":
    root = tk.Tk()
    root.title("컬러픽커")
    app = ColorPickerApp(root)
    root.mainloop()
