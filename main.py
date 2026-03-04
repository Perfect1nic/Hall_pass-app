import tkinter as tk
from datetime import datetime
import time
from tkinter import messagebox

def current_time():
    global time_now
    time_now = datetime.now().strftime("%m/%d/%y %H:%M")


with open("log.txt", "a") as file:
        pass

pass_history = []  # In-memory history of passes for the day

def show_frame(frame):
    """Brings the specific frame to the front."""
    frame.tkraise()
    if frame == history_screen:
        refresh_list()

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

    history_btn = tk.Button(nav_container, text="History",
                            command=lambda: show_frame(history_screen))
    history_btn.pack(side="left", padx=10, pady=5)

    past_btn = tk.Button(nav_container, text="Past Passes",
                            command=lambda: show_frame(past_history))
    past_btn.pack(side="left", padx=10, pady=5)

def update_clock():
        time_string = datetime.now().strftime("%I:%M %p")
        clock_label.config(text=time_string, font=("Arial", 35, "bold"))
        clock_label.after(1000, update_clock)


def submit_pass(name, destination):
    now = datetime.now()
    timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    entry_dict = {
        "name": name,
        "dest": destination,
        "departed": timestamp,
        "start_object": now,
        "returned": "Still Out"
    }
    pass_history.append(entry_dict)
    print(f"Logged: {entry_dict}") # For debugging
    show_frame(submit_screen)

    log_entry = f"{name} left for {destination} at {timestamp}"

    with open("log.txt", "a") as f:
        f.write(f"{name} left at {timestamp} -> {destination}\n")  # Refresh the past passes screen to show the new entry

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

def create_history_screen(container):
    frame = tk.Frame(container, bg="white")
    frame.grid(row=0, column=0, sticky="nsew")
    add_navigation(frame)

    tk.Label(frame, text="Active Pass History", font=("Arial", 18), bg="white").pack(pady=10)

    # Scrollable area for history entries
    canvas = tk.Canvas(frame, bg="white")
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="white")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    def sign_in(entry, btn, label):
        end_time = datetime.now()
        ret_string = end_time.strftime("%I:%M %p")
        duration = end_time - entry["start_object"]
        total_minutes = round(duration.total_seconds()/60)
        entry["returned"] = f"{ret_string} ({total_minutes} mins)"
        # Update UI
        btn.pack_forget() # Remove button
        label.config(text=f"Returned: {entry['returned']}", fg="green")
        # Log return to file
        with open("log.txt", "a") as f:
            f.write(f"{entry['name']} returned at {ret_string} (Total: {total_minutes} mins)\n")

    global refresh_list
    def refresh_list():
        for widget in scroll_frame.winfo_children():
            widget.destroy()
       
        if not pass_history:
            tk.Label(scroll_frame, text="No passes logged today.", bg="white").pack(pady=20)
            return

        for entry in pass_history:
            row = tk.Frame(scroll_frame, bg="#f0f0f0", pady=5, padx=10, highlightbackground="gray", highlightthickness=1)
            row.pack(fill="x", pady=2, padx=10)
           
            info = f"{entry['name']} | {entry['dest']} | Left: {entry['departed']}"
            tk.Label(row, text=info, bg="#f0f0f0", font=("Arial", 10)).pack(side="left")
           
            status_label = tk.Label(row, text="", bg="#f0f0f0", font=("Arial", 10, "bold"))
            status_label.pack(side="right", padx=10)

            if entry["returned"] == "Still Out":
                btn = tk.Button(row, text="Stop Timer", bg="#4CAF50", fg="white")
                btn.config(command=lambda e=entry, b=btn, l=status_label: sign_in(e, b, l))
                btn.pack(side="right")
            else:
                status_label.config(text=f"Returned: {entry['returned']}", fg="green")

    tk.Button(frame, text="Refresh List", command=refresh_list).pack(pady=5)
    return frame

def create_past_log_screen(container):
    frame = tk.Frame(container, bg="white")
    frame.grid(row=0, column=0, sticky="nsew")
    add_navigation(frame)

    tk.Label(frame, text="Full Activity Log (log.txt)", font=("Arial", 18), bg="white").pack(pady=10)
   
    log_box = tk.Listbox(frame, font=("Arial", 10), width=80, height=20)
    log_box.pack(pady=10, padx=20)

    def load_logs():
        log_box.delete(0, tk.END)
        try:
            with open("log.txt", "r") as f:
                for line in f:
                    log_box.insert(tk.END, line.strip())
        except FileNotFoundError:
            log_box.insert(tk.END, "No logs found🤔.")

    tk.Button(frame, text="Reload Log File", command=load_logs).pack(pady=5)
    return frame

def create_past_passes_screen(container):
    frame = tk.Frame(container, bg="white")
    frame.grid(row=0, column=0, sticky="nsew")
   
    # Add the navigation bar
    add_navigation(frame)

    past_listbox = tk.Listbox(frame, font=("Arial", 12), height=15, width=70)
    past_listbox.pack(pady=10, padx=10)

    def past_refresh():
        past_listbox.delete(0, tk.END)
        try:
            with open("log.txt", "r") as f:
                lines = f.readlines()
                if lines:
                    for line in lines:
                        past_listbox.insert(tk.END, line.strip())
                else:
                    past_listbox.insert(tk.END, "No past passes found 🤔")
        except FileNotFoundError:
            past_listbox.insert(tk.END, "No past passes found 🤔")
    past_refresh_btn = tk.Button(frame, text="Load Past Passes", command=past_refresh)
    past_refresh_btn.pack(pady=10)

    label = tk.Label(frame, text="Past Passes", font=("Arial", 18), bg="white")
    label.pack(pady=50)

    return frame

def create_past_passes_screen(container):
    frame = tk.Frame(container, bg="white")
    frame.grid(row=0, column=0, sticky="nsew")
   
    # Add the navigation bar
    add_navigation(frame)

    past_listbox = tk.Listbox(frame, font=("Arial", 12), height=15, width=70)
    past_listbox.pack(pady=10, padx=10)

    def past_refresh():
        past_listbox.delete(0, tk.END)
        try:
            with open("log.txt", "r") as f:
                lines = f.readlines()
                if lines:
                    for line in lines:
                        past_listbox.insert(tk.END, line.strip())
                else:
                    past_listbox.insert(tk.END, "No past passes found 🤔")
        except FileNotFoundError:
            past_listbox.insert(tk.END, "No past passes found 🤔")
    past_refresh_btn = tk.Button(frame, text="Load Past Passes", command=past_refresh)
    past_refresh_btn.pack(pady=10)

    label = tk.Label(frame, text="Past Passes", font=("Arial", 18), bg="white")
    label.pack(pady=50)

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
    global name_bath
    frame = tk.Frame(container, bg="#C4A484")
    frame.grid(row=0, column=0, sticky="nsew")
   
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Bathroom", font=("Arial", 18), bg="#C4A484")
    label.pack(pady=(50, 0))

    name_label = tk.Label(frame, text="Enter Your Name", font=("Arial", 15), bg="#C4A484")
    name_label.pack(pady=(10, 0))


    name_bath = tk.Entry(frame, text="", font=("Arial", 12))
    name_bath.pack(pady=10)

    submit_btn = tk.Button(frame, text = "Submit", font=("Arial", 12),
                             command=process_bathroom_submit)
    submit_btn.pack(pady=10)


    return frame

def create_office_screen(container):
    global name_office
    frame = tk.Frame(container, bg="lightgreen")
    frame.grid(row=0, column=0, sticky="nsew")
   
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Main Office", font=("Arial", 18), bg="lightgreen")
    label.pack(pady=(50,0))

    name_box_office = tk.Label(frame, text="Enter Your Name", font=("Arial", 15), bg="lightgreen")
    name_box_office.pack(pady=(10, 0))

    name_office = tk.Entry(frame, text="", font=("Arial", 12))
    name_office.pack(pady=10)

    submit_btn = tk.Button(frame, text = "Submit", font=("Arial", 12),
                             command=process_office_submit)
    submit_btn.pack(pady=10)
    return frame

def create_nurse_screen(container):
    global name_nurse
    frame = tk.Frame(container, bg="lightcoral")
    frame.grid(row=0, column=0, sticky="nsew")
   
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Nurse", font=("Arial", 18), bg="lightcoral")
    label.pack(pady=(50,0))

    name_box_nurse = tk.Label(frame, text="Enter Your Name", font=("Arial", 15), bg="lightcoral")
    name_box_nurse.pack(pady=(10, 0))

    name_nurse = tk.Entry(frame, text="", font=("Arial", 12))
    name_nurse.pack(pady=10)

    submit_btn = tk.Button(frame, text = "Submit", font=("Arial", 12),
                             command=process_nurse_submit)
    submit_btn.pack(pady=10)
    return frame

def create_classroom_screen(container):
    global name_classroom
    global num_classroom
    frame = tk.Frame(container, bg="beige")
    frame.grid(row=0, column=0, sticky="nsew")
   
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Another Classroom", font=("Arial", 18), bg="beige")
    label.pack(pady=(50,0))

    name_box_classroom = tk.Label(frame, text="Enter Your Name", font=("Arial", 15), bg="beige")
    name_box_classroom.pack(pady=(10, 0))

    name_classroom = tk.Entry(frame, text="", font=("Arial", 12))
    name_classroom.pack(pady=10)

    num_box_classroom = tk.Label(frame, text="Enter the Room Number", font=("Arial", 15), bg="beige")
    num_box_classroom.pack(pady=(10, 0))

    num_classroom = tk.Entry(frame, text="", font=("Arial", 12))
    num_classroom.pack(pady=10)

    submit_btn = tk.Button(frame, text = "Submit", font=("Arial", 12),
                             command=process_classroom_submit)
    submit_btn.pack(pady=10)

   
    return frame


def get_text1():
    text1 = name_bath.get()
    result1_label.config(text=f"Bathroom: {text1} -  {time_now}")
   
def get_text2():
    text2 = name_office.get()
    result2_label.config(text=f"Office: {text2} -  {time_now}")

def get_text3():
    text3 = name_nurse.get()
    result3_label.config(text=f"Nurse: {text3} -  {time_now}")

def get_text4():
    text4 = name_classroom.get()
    numb = num_classroom.get()
    result4_label.config(text=f"Another classroom: {text4} - class# {numb} - {time_now}")


def create_submit_screen1(container):
    global result1_label
    global result2_label
    global result3_label
    global result4_label
    frame = tk.Frame(container, bg="lightgreen")
    frame.grid(row=0, column=0, sticky="nsew")
   
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Pass Submitted 👍", font=("Arial", 18), bg="lightgreen")
    label.pack(pady=50)

    info_label = tk.Label(frame, text="Your pass has been submitted. Please return to the classroom as soon as possible.", font=("Arial", 14), bg="lightgreen")
    info_label.pack(pady=10)

    result1_label = tk.Label(frame, text= "", font=("Arial", 18), bg="lightgreen" )
    result1_label.pack(pady=10)

    result2_label = tk.Label(frame, text= "", font=("Arial", 18), bg="lightgreen" )
    result2_label.pack(pady=10)

    result3_label = tk.Label(frame, text= "", font=("Arial", 18), bg="lightgreen" )
    result3_label.pack(pady=10)

    result4_label = tk.Label(frame, text= "", font=("Arial", 18), bg="lightgreen" )
    result4_label.pack(pady=10)
   
    return frame

def check_submit(entry_widget):
    content = entry_widget.get().strip()
    if not content:
        messagebox.showerror("Error", "You must enter a name into the text box!")
        return False
    elif entry_widget.get().isdigit():
        messagebox.showerror("Error", "You must enter an alphabetical value into the text box!")
        return False
    else:
        print(f"Success! You entered: {content}")
        return True


def check_roomnumb():
    global num_classroom
    if not num_classroom.get().strip():
        messagebox.showerror("Error", "You must enter a room number!")
        return False
    else:
        print("Success! You entered")
        return True

def process_nurse_submit():
    # The code only continues if soemone enters something into the entry box.
    if check_submit(name_nurse):
        current_time()
        get_text3()
        submit_pass(name_nurse.get(), "Nurse")
        show_frame(submit_screen)

def process_office_submit():
    # The code only continues if soemone enters something into the entry box.
    if check_submit(name_office):
        current_time()
        get_text2()
        submit_pass(name_office.get(), "Office")
        show_frame(submit_screen)

def process_bathroom_submit():
    # The code only continues if soemone enters something into the entry box.
    if check_submit(name_bath):
        current_time()
        get_text1()
        submit_pass(name_bath.get(), "Bathroom")
        show_frame(submit_screen)

def process_classroom_submit():
    # The code only continues if soemone enters something into the entry box.
    if check_submit(name_classroom) and check_roomnumb():
        current_time()
        get_text4()
        submit_pass(name_classroom.get(), "Classroom" + num_classroom.get())
        show_frame(submit_screen)

def process_classroom_both():
    if check_submit(name_classroom) and check_roomnumb():
        current_time()
        get_text4()
        submit_pass(name_classroom.get(), "Classroom" + num_classroom.get())
        show_frame(submit_screen)
# --- Main Application Setup ---
root = tk.Tk()
root.title("Hall-pass App")
root.state('zoomed')

main_container = tk.Frame(root)
main_container.pack(fill="both", expand=True)

clock_label = tk.Label(root)
clock_label.pack(pady=10)
update_clock()

main_container.grid_rowconfigure(0, weight=1)
main_container.grid_columnconfigure(0, weight=1)

# Initialize all screens
home_screen = create_home_screen(main_container)
history_screen = create_history_screen(main_container)
past_history = create_past_passes_screen(main_container)
about_screen = create_about_screen(main_container)
bathroom_screen = create_bathroom_screen(main_container)
office_screen = create_office_screen(main_container)
nurse_screen = create_nurse_screen(main_container)
classroom_screen = create_classroom_screen(main_container)
submit_screen = create_submit_screen1(main_container)

# Show initial frame
show_frame(home_screen)

root.mainloop()
