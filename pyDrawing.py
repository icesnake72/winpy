import tkinter as tk
from PIL import Image, ImageDraw
import time

class DrawingApp:
    def __init__(self, root):
        self.root = root
        
        self.button = tk.Button(self.root,
                                text='save',
                                command=self.OnSave,
                                width=30,
                                height=1,
                                bd=1)
        self.button.pack(fill='x')
        
        self.canvas = tk.Canvas(self.root, 
                                bg='white',
                                width=self.root.winfo_width(), 
                                height=self.root.winfo_height())
        self.canvas.pack(fill='both', expand=True)
        
        self.root.bind('<Configure>', self.OnSize())

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.drawing = False
        self.last_x = 0
        self.last_y = 0
        
    def OnSave(self):
      im = Image.open('test.ps')
      print(im)
      
      # Image 객체 생성
      image = Image.new("RGBA", (im.width, im.height), "white")
      draw = ImageDraw.Draw(image)
      
      image.paste(im, (0,0))
      image.save('save.png', 'PNG')
      
      # im.show()
      # with Image.open("test.ps") as im:
        # im.show()
        # im.rotate(45).show()
      # self.canvas.postscript(file='test.ps', colormode='color')    
      # time.sleep(5)
      # image = Image.open('test.ps')
      # image.save('canvas.png', 'PNG')
        
    def OnSize(self):
      self.canvas.configure(width=self.root.winfo_width() , height=self.root.winfo_height())

    def start_drawing(self, event):
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def stop_drawing(self, event):
        self.drawing = False

    def draw(self, event):
        if self.drawing:            
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=5)
            self.last_x = event.x
            self.last_y = event.y            
            

if __name__ == "__main__":
    root = tk.Tk()
    root.title("그림판")
    app = DrawingApp(root)
    root.mainloop()

# import tkinter as tk
# from tkinter import colorchooser

# class ColorPickerApp:
#     def __init__(self, root):
#         self.root = root
#         self.color_button = tk.Button(self.root, text="색상 선택", command=self.pick_color)
#         self.color_button.pack()

#     def pick_color(self):
#         color = colorchooser.askcolor(title="색상 선택")
#         if color[1]:
#             self.root.configure(background=color[1])

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("컬러픽커")
#     app = ColorPickerApp(root)
#     root.mainloop()
