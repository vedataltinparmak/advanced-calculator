import tkinter as tk

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

def btn_delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")
window.configure(bg='#e6e6e6')

expression = ""
input_text = tk.StringVar()

brand_label = tk.Label(window, text="GoldeN VedaT CalculatoR", font=('arial', 14, 'bold'), bg='#e6e6e6', fg='#ffbf00')
brand_label.pack(side=tk.TOP, pady=10)

input_frame = tk.Frame(window, bd=5, bg='#ffffff', relief=tk.RIDGE)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=2, width=14, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=20)

btns_frame = tk.Frame(window, bg='#e6e6e6')
btns_frame.pack()

btn_colors = {
    'numbers': '#fff',
    'operations': '#d3d3d3',
    'special': '#f2a65a'
}

buttons = [
    ('7', 1, 0, btn_colors['numbers']), ('8', 1, 1, btn_colors['numbers']), ('9', 1, 2, btn_colors['numbers']), ('/', 1, 3, btn_colors['operations']),
    ('4', 2, 0, btn_colors['numbers']), ('5', 2, 1, btn_colors['numbers']), ('6', 2, 2, btn_colors['numbers']), ('*', 2, 3, btn_colors['operations']),
    ('1', 3, 0, btn_colors['numbers']), ('2', 3, 1, btn_colors['numbers']), ('3', 3, 2, btn_colors['numbers']), ('-', 3, 3, btn_colors['operations']),
    ('C', 4, 0, btn_colors['special']), ('0', 4, 1, btn_colors['numbers']), ('=', 4, 2, btn_colors['special']), ('+', 4, 3, btn_colors['operations']),
    ('Del', 5, 0, btn_colors['special'])
]

for (text, row, col, color) in buttons:
    action = lambda x=text: btn_click(x) if x not in ('=', 'C', 'Del') else (btn_equal() if x == '=' else (btn_clear() if x == 'C' else btn_delete()))
    tk.Button(btns_frame, text=text, fg='black', width=10, height=3, bd=0, bg=color, cursor='hand2', command=action).grid(row=row, column=col, padx=1, pady=1)

window.mainloop()