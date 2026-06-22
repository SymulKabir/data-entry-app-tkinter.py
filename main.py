import tkinter as tk
from app.ui.formView import FormView

class ABQDataEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ABQ Data Entry Application")
         
        window_width = 750
        window_height = 700
        screen_width = self.root.winfo_screenwidth() 
        x_position = screen_width - window_width
        y_position = 0 
        
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        FormView(self.root)
 



if __name__ == "__main__":
    root = tk.Tk()
    app = ABQDataEntryApp(root)
    root.mainloop()