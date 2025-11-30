import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")
        self.master.geometry("600x800")
        root.configure(bg="black") 
        self.display = tk.Entry(master, font=("Italian", 24), borderwidth=5, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            'sqrt', 'sin', 'cos', 'tan',
            'pow','C','/','*','-','%','+','=',
            '7', '8', '9', 
            '4', '5', '6', 
            '1', '2', '3', 
            '0' 
            
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.master, text=button, width=10, height=3, command=action,bg="black",fg="white").grid(row=row_val, column=col_val)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.display.get()
                if 'sqrt' in expression:
                    expression = expression.replace('sqrt', 'math.sqrt')
                elif 'pow' in expression:
                    expression = expression.replace('pow', '**')
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
