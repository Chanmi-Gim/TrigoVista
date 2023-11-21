import tkinter as tk
import math

RADIUS = 150
focus = 250
baseX, baseY = 400, 250
arcStart, arcEnd = 235, 265
class canvas(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.start = 0
        self.end = 45
        self.geometry('500x500')
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(expand='yes', fill='both')
        self.canvas.create_oval(100, 100, 400, 400, width = 2) 
        self.canvas.create_line(focus, focus, baseX, baseY, tags = "start_line") 
        self.canvas.create_polygon((focus, focus), (baseX, baseY), (focus, 100), tags = "triangle", fill="white", outline="black", width=2)
        self.canvas.create_arc((arcStart, arcStart), (arcEnd, arcEnd), tags= "arc", width=2, start = 0, extent=90, outline ="red", style= 'arc')
        self.canvas.create_text(270, 230, text=90, anchor="center", tags = "txt_degree", fill = "red")
        self.canvas.tag_bind("triangle", "<B1-Motion>", self.move_triangle_and_arc)
        entry = tk.Entry(self, bg = "white")
        label = tk.Label(self, text= "삼각형 각도")
        button = tk.Button(self, text = "클릭", bg = "white", command=lambda : self.on_btn_click(entry))
        label.pack()
        entry.pack()
        button.pack()


    def move_triangle_and_arc(self, event):
        x, y = event.x, event.y
        curX , curY = x - focus, y - focus
        angle =  math.atan2(curY, curX)
        newX = focus + RADIUS * math.cos(angle)
        newY = focus + RADIUS * math.sin(angle)
        degree = int(math.degrees(angle * -1))
        new_coords = (
            focus, focus,
            baseX, baseY,
            newX,newY
        )
        self.canvas.coords("triangle", new_coords)
        self.canvas.itemconfig("arc", start = 0, extent = degree)
        self.canvas.itemconfig("txt_degree", text = abs(degree))
    
    def on_btn_click(self, entry):
        value = int(entry.get())
        newX = focus + RADIUS * math.cos(math.radians(value*-1))
        newY = focus + RADIUS * math.sin(math.radians(value*-1))
        degree = int(math.degrees(value * -1))
        new_coords = (
            focus, focus,
            baseX, baseY,
            newX,newY
        )
        self.canvas.coords("triangle", new_coords)
        self.canvas.itemconfig("arc", start = 0, extent = value)
        self.canvas.itemconfig("txt_degree", text = abs(value))
        
        
if __name__ == "__main__":
    canvas = canvas()
    canvas.mainloop()
