import tkinter as tk

# Create a function to be called when the button is clicked
def button_click():
    print("Button clicked!")

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example")

# Create a button widget
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()  # Add the button to the window

# Start the Tkinter event loop
root.mainloop()

