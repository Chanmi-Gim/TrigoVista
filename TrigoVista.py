import tkinter as tk
import math

RADIUS = 150
FOCUS = 250
HORIZONTAL = 400
VERTICAL = 100
ARC_START, ARC_END = 235, 265
X = 450
Y = 50
class canvas(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.start = 0
        self.end = 45
        self.geometry('500x500')
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(expand='yes', fill='both')
        self.canvas.create_oval(100, 100, 400, 400, width = 2) 
        self.canvas.create_line(FOCUS, FOCUS, HORIZONTAL, FOCUS, tags = "start_line") 
        self.canvas.create_line(Y, FOCUS, X, FOCUS, width = 2) 
        self.canvas.create_line(FOCUS, Y, FOCUS, X, width = 2) 
        self.canvas.create_text(X, FOCUS+10, text="x", anchor="center", fill = "black")
        self.canvas.create_text(FOCUS-10, Y, text="y", anchor="center", fill = "black")
        self.canvas.create_text(FOCUS, FOCUS+10, text="O(250,250)", anchor="center", fill = "black")
        self.canvas.create_polygon((FOCUS, FOCUS), (HORIZONTAL, FOCUS), (FOCUS, 100), tags = "triangle", fill="white", outline="blue", width=2)
        self.canvas.create_text(FOCUS, VERTICAL-10, text=f"({FOCUS},{VERTICAL})", anchor="center", tags = "xy1", fill = "black")
        self.canvas.create_text(HORIZONTAL-10, FOCUS, text=f"({HORIZONTAL},{FOCUS})", anchor="center", tags = "xy2", fill = "black")
        self.canvas.create_arc((ARC_START, ARC_START), (ARC_END, ARC_END), tags= "arc", width=1.5, start = 0, extent=90, outline ="red", style= 'arc')
        self.canvas.create_text(270, 230, text=90, anchor="center", tags = "txt_degree", fill = "blue")
        self.canvas.create_text(FOCUS, FOCUS, text="A", anchor="center", state ="hidden", tags = "A", fill = "red")
        self.canvas.create_text(FOCUS, FOCUS, text="B", anchor="center", state ="hidden", tags = "B", fill = "red")
        self.canvas.create_text(FOCUS, FOCUS, text="C", anchor="center", state ="hidden", tags = "C", fill = "red")
        self.canvas.tag_bind("triangle", "<B1-Motion>", self.move_triangle_and_arc)
        frame = tk.Frame(self)
        frame.pack()
        
        btn_30 = tk.Button(frame, text = "θ = 30", bg = "white", command=lambda : self.on_btn_click(30) )
        btn_45 = tk.Button(frame, text = "θ = 45", bg = "white", command=lambda : self.on_btn_click(45) )
        btn_60 = tk.Button(frame, text = "θ = 60", bg = "white", command=lambda : self.on_btn_click(60) )
        btn_30.grid(row =0, column=0)
        btn_45.grid(row =0, column=1)
        btn_60.grid(row =0, column=2)
        label = tk.Label(frame, text= "각도 입력: ")
        label.grid(row =1, column=0)
        entry = tk.Entry(frame, bg = "white")
        entry.grid(row =1, column=1)
        btn_click = tk.Button(frame, text = "클릭", bg = "white", command=lambda : self.on_btn_click(entry.get()))
        btn_click.grid(row=1, column=2)
        # self.theta = tk.Label(frame, text= "sinθ: -, cosθ: -, tanθ: -", )
        # self.theta.grid(row=2, column=0)

    def move_triangle_and_arc(self, event):
        x, y = event.x, event.y
        curX , curY = x - FOCUS, y - FOCUS
        angle =  math.atan2(curY, curX)
        newX = FOCUS + RADIUS * math.cos(angle)
        newY = FOCUS + RADIUS * math.sin(angle)
        degree = int(math.degrees(angle * -1))
        new_coords = (
            FOCUS, FOCUS,
            newX, FOCUS,
            newX,newY
        )
        self.update(newX, newY, new_coords, degree)
    
    def on_btn_click(self, value):
        value = int(value)
        newX = FOCUS + RADIUS * math.cos(math.radians(value*-1))
        newY = FOCUS + RADIUS * math.sin(math.radians(value*-1))
        new_coords = (
            FOCUS, FOCUS,
            newX, FOCUS,
            newX,newY
        )
        self.update(newX, newY, new_coords, value)
        
    def update(self, newX, newY, new_coords, value):
        self.canvas.coords("triangle", new_coords)
        self.canvas.itemconfig("arc", start = 0, extent = value)
        self.canvas.itemconfig("txt_degree", text = abs(value))
        self.canvas.coords("xy1", newX+10, newY+10)
        self.canvas.itemconfig("xy1", text =f"({int(newX)},{int(newY)})")
        self.canvas.coords("xy2", newX+10, FOCUS)
        self.canvas.itemconfig("xy2", text =f"({int(newX)},{FOCUS})")
        C = FOCUS - newY
        B = newX - FOCUS
        A = math.sqrt((newX-FOCUS)**2+(newY-FOCUS)**2)
        C_RATIO = int(abs((C/(A+B+C))*100))
        B_RATIO = int(abs((B/(A+B+C))*100))
        A_RATIO = int(abs((A/(A+B+C))*100))
        self.canvas.coords("C",abs(newX+10), abs(((FOCUS+(newY+10))/2)))
        self.canvas.itemconfig("C", text =f"{int(C)}({C_RATIO}) ", state="normal")
        
        self.canvas.coords("B", abs((FOCUS+ (newX+10))/2), abs(FOCUS))
        self.canvas.itemconfig("B", text =f"{int(B)}({B_RATIO})", state="normal")
        
        self.canvas.coords("A", abs((FOCUS+(newX+10))/2), abs((FOCUS+(newY+10))/2))
        self.canvas.itemconfig("A", text =f"{int(A)}({A_RATIO})", state="normal")
        # self.theta.config(text= f"sinθ: {math.sin(value+250)}, cosθ: {math.cos(math.radians(value+250))}, tanθ: {math.tan(value+250)}")
if __name__ == "__main__":
    canvas = canvas()
    canvas.mainloop()

