from tkinter import *
from tkinter import messagebox
import random

# Initial variables
timer = 0
current_pos = 0
complete = False


# Check if the user has clicked on the lowest value, if yes, disable the button
def disable_btn(btn,num):
    global current_pos, complete
    if numbers[current_pos] == num:
       current_pos+= 1
       btn.config(state=DISABLED)  # Disable the button
       if current_pos == 25:
           messagebox.showinfo("Completed", "Challenge complete!")
           complete = True

       

# update the timer - every second
def update_timer():
    global timer, complete
    if not complete:
        timer += 1
    # Update the label's text
    timer_label.config(text=str(timer))
    # Schedule the update_timer function to be called after 1000ms
    window.after(1000, update_timer)


#create a button and add a lambda function to capture the event and value
def create_button(window, num):
    btn = Button(window, text=num, command=lambda num=num: disable_btn(btn, num))
    return btn

#Calculate numbers
numbers = random.sample(range(1,999),25)

#Create main window
window = Tk()


#create 25 buttons with the value on them
for i in range(5):
    for j in range(5):
        num = numbers[i*5 + j]
        print(num, end="*")
        btn = create_button(window,num)
        btn.grid(row=i, column=j)

#sort the numbers to capture the values properly
numbers.sort()

#Add the label for timer
timer_label = Label(window, text=str(timer))
timer_label.grid(row=6,columnspan=5)
update_timer()

#start
window.mainloop()