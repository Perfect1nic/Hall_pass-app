import tkinter as tk

def show_frame(frame):
    """Brings the specified frame to the front."""
    frame.tkraise()

def add_navigation(parent):
    """Adds a row of navigation buttons to a parent frame."""
    nav_container = tk.Frame(parent, bg="white", height=50)
    nav_container.pack(side="top", fill="x")

    # Navigation Buttons placed next to each other
    home_btn = tk.Button(nav_container, text="Home", 
                         command=lambda: show_frame(home_screen))
    home_btn.pack(side="left", padx=10, pady=5)
    
    about_btn = tk.Button(nav_container, text="About", 
                            command=lambda: show_frame(about_screen))
    about_btn.pack(side="left", padx=10, pady=5)

def create_home_screen(container):
    frame = tk.Frame(container, bg="lightblue")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Where to?", font=("Arial", 18), bg="lightblue")
    label.pack(pady=50)

    bathroom_btn = tk.Button(frame, text = "Bathroom", font=("Arial", 12),
                             command=lambda: show_frame(bathroom_screen))
    bathroom_btn.pack(pady=5)

    office_btn = tk.Button(frame, text = "Main Office", font=("Arial", 12),
                             command=lambda: show_frame(office_screen))
    office_btn.pack(pady=5)

    nurse_btn = tk.Button(frame, text = "Nurse", font=("Arial", 12),
                             command=lambda: show_frame(nurse_screen))
    nurse_btn.pack(pady=5)

    classroom_btn = tk.Button(frame, text = "Another Classroom", font=("Arial", 12),
                             command=lambda: show_frame(classroom_screen))
    classroom_btn.pack(pady=5)
    return frame

def create_about_screen(container):
    frame = tk.Frame(container, bg="white")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="About This App", font=("Arial", 18), bg="white")
    label.pack(pady=50)

    about = tk.Label(frame, text = "This program allows teachers to keep track of who is out of the classroom and start a timer stopwatch.\n First the student enters their name and id and then they select their destination and start the timer. \n Then when the student returns they will stop the stopwatch and do what they got to do. \n If the student does not return, the teacher has to stop the stopwatch.", font=("Arial", 18), bg="white")
    about.pack(pady=10)
    return frame

def create_bathroom_screen(container):
    frame = tk.Frame(container, bg="#C4A484")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Bathroom", font=("Arial", 18), bg="#C4A484")
    label.pack(pady=(50, 0))

    name_label = tk.Label(frame, text="Enter Your Name", font=("Arial", 15), bg="#C4A484")
    name_label.pack(pady=(10, 0))

    name_entry = tk.Entry(frame, text="", font=("Arial", 12))
    name_entry.pack(pady=10)

    name_label = tk.Label(frame, text="Enter the time", font=("Arial", 15), bg="#C4A484")
    name_label.pack(pady=(10, 0))

    name_entry = tk.Entry(frame, text="", font=("Arial", 12))
    name_entry.pack(pady=10)

    submit_btn = tk.Button(frame, text = "Submit", font=("Arial", 12),
                             command=lambda: show_frame(nurse_screen))
    submit_btn.pack(pady=10)
    return frame

def create_office_screen(container):
    frame = tk.Frame(container, bg="lightgreen")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Main Office", font=("Arial", 18), bg="lightgreen")
    label.pack(pady=50)

    name_label = tk.Label(frame, text="Enter Your Name", font=("Arial", 15), bg="lightgreen")
    name_label.pack(pady=(10, 0))

    name_entry = tk.Entry(frame, text="", font=("Arial", 12))
    name_entry.pack(pady=10)

    name_label = tk.Label(frame, text="Enter the time", font=("Arial", 15), bg="lightgreen")
    name_label.pack(pady=(10, 0))

    name_entry = tk.Entry(frame, text="", font=("Arial", 12))
    name_entry.pack(pady=10)

    submit_btn = tk.Button(frame, text = "Submit", font=("Arial", 12),
                             command=lambda: show_frame(nurse_screen))
    submit_btn.pack(pady=10)
    return frame

def create_nurse_screen(container):
    frame = tk.Frame(container, bg="lightcoral")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Nurse", font=("Arial", 18), bg="lightcoral")
    label.pack(pady=50)

    name_label = tk.Label(frame, text="Enter Your Name", font=("Arial", 15), bg="lightcoral")
    name_label.pack(pady=(10, 0))

    name_entry = tk.Entry(frame, text="", font=("Arial", 12))
    name_entry.pack(pady=10)

    name_label = tk.Label(frame, text="Enter the time", font=("Arial", 15), bg="lightcoral")
    name_label.pack(pady=(10, 0))

    name_entry = tk.Entry(frame, text="", font=("Arial", 12))
    name_entry.pack(pady=10)

    submit_btn = tk.Button(frame, text = "Submit", font=("Arial", 12),
                             command=lambda: show_frame(nurse_screen))
    submit_btn.pack(pady=10)
    return frame

def create_classroom_screen(container):
    frame = tk.Frame(container, bg="lightgreen")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Another Classroom", font=("Arial", 18), bg="lightgreen")
    label.pack(pady=50)

    name_label = tk.Label(frame, text="Enter Your Name", font=("Arial", 15), bg="lightgreen")
    name_label.pack(pady=(10, 0))

    name_entry = tk.Entry(frame, text="", font=("Arial", 12))
    name_entry.pack(pady=10)

    name_label = tk.Label(frame, text="Enter the time", font=("Arial", 15), bg="lightgreen")
    name_label.pack(pady=(10, 0))

    name_entry = tk.Entry(frame, text="", font=("Arial", 12))
    name_entry.pack(pady=10)

    submit_btn = tk.Button(frame, text = "Submit", font=("Arial", 12),
                             command=lambda: show_frame(nurse_screen))
    submit_btn.pack(pady=10)
    return frame

# --- Main Application Setup ---
root = tk.Tk()
root.title("Hall-pass App")
root.state('zoomed')

main_container = tk.Frame(root)
main_container.pack(fill="both", expand=True)

main_container.grid_rowconfigure(0, weight=1)
main_container.grid_columnconfigure(0, weight=1)

# Initialize all screens
home_screen = create_home_screen(main_container)
about_screen = create_about_screen(main_container)
bathroom_screen = create_bathroom_screen(main_container)
office_screen = create_office_screen(main_container)
nurse_screen = create_nurse_screen(main_container)
classroom_screen = create_classroom_screen(main_container)

# Show initial frame
show_frame(home_screen)

root.mainloop()
