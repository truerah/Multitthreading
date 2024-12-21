import tkinter as tk
import  time, random as r
import threading


# Function to generate random numbers and update the label with a given refresh time
def task(label,lb,ub,refreshTime):
    while True:
        num=r.randint(lb,ub)
        label.config(text=f"{num}\n[{lb}, {ub}]\nrefresh time = {refreshTime}")
        time.sleep(refreshTime)
    return
# Function to create the dashboard
def create_dashboard():
    # Create the main window
    root = tk.Tk()
    root.title("Random Number Dashboard")

    # Define number ranges and refresh times for each label
    ranges_and_times = [
        (10,20, 10, "lightcoral"),
        (-10, 10, 20, "lightblue"),
        (-100, 0, 8, "lightgreen"),
        (0, 20, 12, "yellow"),
        (-40, 40, 16, "lightsteelblue"),
        (100, 200, 14, "lightgray")
    ]

    # Create 6 labels with different ranges and refresh times
    labels = []
    for i, (lb,ub, refresh_time, color) in enumerate(ranges_and_times):
        label = tk.Label(root, text="0", font=("Helvetica", 16), width=15, height=5, bg=color)
        label.grid(row=i//2, column=i%2, padx=20, pady=20)
        labels.append((label,lb,ub, refresh_time))

    # Create and start a thread for each label to update random numbers
    for label,lb,ub, refresh_time in labels:
        thread = threading.Thread(target=task, args=(label,lb,ub, refresh_time))
        thread.daemon = True
        thread.start()

    # Start the GUI event loop
    root.mainloop()

# Run the dashboard
if __name__ == "__main__":
    create_dashboard()
