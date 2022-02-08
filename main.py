from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Km to Mile Converter")
window.minsize(width=400, height=100)
window.config(padx=50, pady=20)  # To make more space between the framework window and the text

# Labels
label_km = Label(text="Km", font=("Arial", 17))
label_km.grid(column=2, row=0)

# Labels
label_miles = Label(text="Miles", font=("Arial", 17))
label_miles.grid(column=2, row=1)

# Labels
label_equal = Label(text="is equal to", font=("Arial", 17))
label_equal.grid(column=0, row=1)

# Labels
label_result = Label(text=0, font=("Arial", 17))
label_result.grid(column=1, row=1)

# Entry
km = Entry(width=10)
km.grid(column=1, row=0)


# Buttons
def action():
    miles = float(km.get()) * 0.621
    # Labels
    label_result.config(text=miles)


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)

window.mainloop()
