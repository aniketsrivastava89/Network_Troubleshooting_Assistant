import tkinter as tk
from tkinter import messagebox

def troubleshoot_issue():
    # Get the selected problem
    choice = problem_var.get()

    # Display troubleshooting steps based on the selected problem
    if choice == "Slow internet":
        troubleshooting_steps = [
            "Restart your router.",
            "Check for any background downloads or uploads.",
            "Move closer to the router to improve signal strength."
        ]
    elif choice == "Connectivity problems":
        troubleshooting_steps = [
            "Check if other devices can connect to the network.",
            "Restart your computer and router.",
            "Check for any network outages in your area."
        ]
    elif choice == "No internet":
        troubleshooting_steps = [
            "Check if your modem or router is properly connected and powered on.",
            "Restart your modem or router.",
            "Contact your internet service provider for assistance."
        ]
    elif choice == "Limited connectivity":
        troubleshooting_steps = [
            "Check your IP configuration and DNS settings.",
            "Disable and re-enable your network adapter.",
            "Update your network adapter drivers."
        ]
    elif choice == "Missing files or drivers":
        troubleshooting_steps = [
            "Check for updates for your operating system.",
            "Download and install any missing drivers from the manufacturer's website."
        ]
    else:
        troubleshooting_steps = ["Invalid choice. Please select a valid option."]

    # Display the troubleshooting steps in a messagebox with larger font size
    messagebox.showinfo("Troubleshooting Steps", "\n".join(troubleshooting_steps), font=("Arial", 12))

# Create the main window
root = tk.Tk()
root.title("Network Troubleshooting Assistant")
root.geometry("400x300")  # Set the size of the window

# Create a label for the instructions with larger font size
instructions_label = tk.Label(root, text="Please select the problem you are experiencing:", font=("Arial", 14))
instructions_label.pack()

# Create a variable to hold the selected problem
problem_var = tk.StringVar()

# Create a list of problem options
problems = ["Slow internet", "Connectivity problems", "No internet", "Limited connectivity", "Missing files or drivers"]

# Create a dropdown menu to select the problem with larger font size
problem_dropdown = tk.OptionMenu(root, problem_var, *problems)
problem_dropdown.config(font=("Arial", 12))
problem_dropdown.pack()

# Create a button to troubleshoot the selected problem
troubleshoot_button = tk.Button(root, text="Troubleshoot", command=troubleshoot_issue, font=("Arial", 12))
troubleshoot_button.pack()

# Run the main event loop
root.mainloop()
