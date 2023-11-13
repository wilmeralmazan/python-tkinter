
from tkinter import *
from tkinter import messagebox


def calcular():
    try:
        number1 = float(number1_str.get())
        number2 = float(number2_str.get())
    
        total = 0
        match sym.get():
            case "+": total = number1 + number2
            case "-": total = number1 - number2
            case "*": total = number1 * number2
            case "/": total = number1 / number2
        result_str.set(round(total,2))
    except ZeroDivisionError:
        messagebox.showerror("Zero Division Error", "Division by 0 is not allowed")
        entry2.focus_set()
    except:
        messagebox.showerror("Incorrect Data Type", "Check your input. You must provide numbers")
        entry1.focus_set()
    

#Main Window
window = Tk()
window.geometry("300x200")

# let us create a Tkinter string variable 
# that is able to store any string value 
sym = StringVar(window, "1") 
number1_str = StringVar(window,"")
number2_str = StringVar(window,"")

result_str = StringVar(window,"")

# here is a Dictionary to create multiple buttons 
options = { 
            "+": "+",
			"-": "-",
			"*": "*",
			"/": "/",
		} 

# We will use a Loop just to create multiple 
# Radiobuttons instaed of creating each button separately
radio_sum = Radiobutton(window, text="+", variable=sym, value="+").grid(row=0,column=1)
radio_sub = Radiobutton(window, text="-", variable=sym, value="-").grid(row=1,column=1)
radio_mul = Radiobutton(window, text="*", variable=sym, value="*").grid(row=2,column=1)
radio_div = Radiobutton(window, text="/", variable=sym, value="/").grid(row=3,column=1)



#Textbox
entry1 = Entry(window,textvariable=number1_str).grid(row=1,column=0)
entry2 = Entry(window,textvariable=number2_str).grid(row=1,column=2)

#Button
btn = Button(text="Evaluate", command=calcular).grid(row=4,column=1)

#Result
result = Label(window, text = "Result: ").grid(row=5,column=1)
result_value = Label(window, text = "----", textvariable=result_str).grid(row=5,column=2)  

#Run the app
window.mainloop()