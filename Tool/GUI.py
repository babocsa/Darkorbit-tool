import tkinter as tk
from tkinter import ttk
import os

autolock_enabled = False  
on_top_enabled = False
autolock_button = None  
on_top_button = None
root = None  

class CustomTitleBar(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.configure(bg="#1E1E1E")

        self.bind("<B1-Motion>", self.move_window)
        self.bind("<Button-1>", self.get_pos)

        self.title_label = ttk.Label(self, text="Seiun no Tappu", style="TLabel")
        self.title_label.pack(side=tk.LEFT, padx=(225, 0))

    def get_pos(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def move_window(self, event):
        deltax = event.x - self.start_x
        deltay = event.y - self.start_y
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay
        self.master.geometry(f"+{x}+{y}")

def button_click():
    print("Nothing for now!")

def toggle_autolock():
    global autolock_enabled, autolock_button
    autolock_enabled = not autolock_enabled  
    if autolock_enabled:
        print("Autolock player enabled")
        autolock_button.config(text="Autolock: On")
    else:
        print("Autolock player disabled")
        autolock_button.config(text="Autolock: Off")

def toggle_on_top():
    global on_top_enabled, on_top_button, root
    on_top_enabled = not on_top_enabled  
    if on_top_enabled:
        print("On Top enabled")
        root.attributes('-topmost', 1)
        on_top_button.config(text="On Top: On")
    else:
        print("On Top disabled")
        root.attributes('-topmost', 0)
        on_top_button.config(text="On Top: Off")

def main():
    global autolock_button, on_top_button, root

    root = tk.Tk()
    root.title("Tool") 
    root.configure(bg="#1E1E1E")


    current_dir = os.path.dirname(__file__)


    icon_path = os.path.join(current_dir, "Resources", "ICON.png")


    root.iconphoto(True, tk.PhotoImage(file=icon_path))

    window_width = 600  
    window_height = 400  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.configure(borderwidth=0, highlightbackground="#1E1E1E")

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("TFrame", background="#1E1E1E")
    style.configure("TLabel", background="#1E1E1E", foreground="#FFFFFF", font=("Helvetica", 16))
    style.configure("TButton", background="#333333", foreground="#FFFFFF", font=("Helvetica", 12))
    style.map("TButton.On", background=[("active", "#008000")])
    style.map("TButton.Off", background=[("active", "#FF0000")])

    title_bar = CustomTitleBar(root)
    title_bar.pack(expand=1, fill=tk.X)

    content_frame = ttk.Frame(root, padding=(150, 150))
    content_frame.pack(expand=1, fill=tk.BOTH)

    label = ttk.Label(content_frame, text="Under developing!", style="TLabel")
    label.pack(padx=10, pady=10)

    autolock_button = ttk.Button(content_frame, text="Autolock: Off", command=toggle_autolock, style="TButton")
    autolock_button.place(x=-140, y=-120)  

    on_top_button = ttk.Button(content_frame, text="On Top: Off", command=toggle_on_top, style="TButton")
    on_top_button.place(x=95, y=100)  

    root.mainloop()

if __name__ == "__main__":
    main()
