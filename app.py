# Python library imports
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

# Local library imports
import file_manager as fm
import data_processing as pr

df = None
dataset = pr.DataProcessing(df)

# Create a window on which all our widgets will be built
root = tk.Tk()
# Set the dimensions
root.geometry("940x600")
# Set the title of the window
root.title("Python Data Analysis App | Coursework 2")
# root.resizable(width=False, height=False)

# Defining rows in the grid
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=16)
root.grid_rowconfigure(3, weight=10)

# Define columns in the grid
root.grid_columnconfigure(0, weight=6)
root.grid_columnconfigure(1, weight=4)

# Main Window's frames/containers
header_frame = tk.Frame(root, bg="black", bd=1, relief="sunken")
file_frame = tk.Frame(root, bd=1, relief="sunken")
task_frame = tk.Frame(root, bd=1, relief="sunken")
run_frame = tk.Frame(root, bd=1, relief="sunken")
how_to_run_frame = tk.Frame(root, bd=1, relief="sunken")

# Setting the location of these frames in the grid
header_frame.grid(row=0, column=0, columnspan=2, sticky="NSEW", padx=2, pady=2)
file_frame.grid(row=1, column=0, columnspan=2, sticky="NSEW", padx=2, pady=2)
task_frame.grid(row=2, column=0, rowspan=2, sticky="NSEW", padx=2, pady=2)
run_frame.grid(row=2, column=1, rowspan=1, sticky="NSEW", padx=2, pady=2)
how_to_run_frame.grid(row=3, column=1, rowspan=1, sticky="NSEW", padx=2, pady=2)

header_frame.propagate(0)
file_frame.propagate(0)
task_frame.propagate(0)
run_frame.propagate(0)
how_to_run_frame.propagate(0)

# Header label
head_label = tk.Label(header_frame, text="Issuu Data Analysis Tool",
                      justify=tk.LEFT, bg="black", fg="white", padx=14)
head_label.config(font=("Arial", 16, "bold"))
head_label.pack(side=tk.LEFT)

# File manager frame

file_frame.grid_rowconfigure(0, weight=1)
file_frame.grid_columnconfigure(1, weight=1)

curr_dataset_frame = tk.Frame(file_frame, width=100)
data_info_frame = tk.Frame(file_frame, width=250, padx=3)
load_dataset_frame = tk.Frame(file_frame, width=100, padx=3)

curr_dataset_frame.grid(row=0, column=0, sticky="NS")
data_info_frame.grid(row=0, column=1, sticky="NSEW", pady=(14, 0))
load_dataset_frame.grid(row=0, column=2, sticky="NS")

current_dataset_label = tk.Label(curr_dataset_frame, text="No dataset loaded.", justify=tk.LEFT, padx=14)
current_dataset_label.config(font=("Arial", 14, "bold"))
current_dataset_label.pack(side=tk.LEFT)

filepath_label = tk.Label(data_info_frame, text=" ", justify=tk.LEFT, padx=20)
filepath_label.pack(side=tk.TOP, anchor=tk.W)
filesize_label = tk.Label(data_info_frame, text="View the loaded dataset information here.", justify=tk.LEFT,
                          padx=20)
filesize_label.pack(side=tk.TOP, anchor=tk.W)
filelines_label = tk.Label(data_info_frame, text=" ", justify=tk.LEFT, padx=20)
filelines_label.pack(side=tk.TOP, anchor=tk.W)

load_btn = tk.Button(load_dataset_frame, text="Select Dataset", padx=26, pady=7, command=lambda: select_file(),
                     bg="orange", fg="black", bd="1")
load_btn.pack(side=tk.RIGHT, padx=14)

# File types that can be loaded into the app
FILE_TYPES = [("JSON Files", "*.json"), ("All files", "*.*")]

# Initialise variables
df = None
dataset = pr.DataProcessing(df)


def select_file():
    """Lets the user select a file and checks if it is valid"""
    file_frame.filename = filedialog.askopenfilename(initialdir="/dataAnalysis/data", title="Select Dataset",
                                                     filetypes=FILE_TYPES)
    if file_frame.filename:
        f = fm.FileManager(file_frame.filename)
        if f.check_file_format():
            # Check if file selected is of JSON format
            global df
            # Try loading the dataframe, else return messagebox with relevant errors.
            df = f.parse_json_dataframe()
            if not df.empty:
                global dataset
                dataset = pr.DataProcessing(df)
                display_file_info(f)
            else:
                messagebox.showerror("Value Error",
                                     "The JSON file you are trying to load didn't contain valid dictionaries. Please try again")
        else:
            # Display message box in case file is incorrect format
            messagebox.showerror(title="Bad file format", message="Please load JSON file only.")


def display_file_info(f):
    """Displays file information in the file manager frame"""
    current_dataset_label.config(text=f.get_file_name)
    filepath_label.config(text="Filepath: " + f.get_file_path)
    filesize_label.config(text="Filesize: " + f.get_file_size + " MB")
    filelines_label.config(text="Total number of lines: " + f.get_file_lines)


# Task frame
available_label = tk.Label(task_frame, text="Select a task to run it.", justify=tk.LEFT)
available_label.config(font=("Arial", 16))
available_label.pack(side=tk.TOP, anchor=tk.W, pady=(14, 2), padx=14)

subtitle_label = tk.Label(task_frame, text="Select a task to read about it or to run it", justify=tk.LEFT)
subtitle_label.pack(side=tk.TOP, anchor=tk.W, pady=(0, 6), padx=14)

# ttkinter Int variable to store the value of the selected radio button
val = tk.IntVar(task_frame)

# Store info of a particular in a dictionary with task id as a key and its title and into a pair, as the value.
TASK_DATA = {
    1: ("Task 2a",
        "Displays a histogram of the countries a specific document has been viewed in."),
    2: ("Task 2b",
        "Displays a histogram of the continents a specific document has been viewed in."),
    3: ("Task 3a",
        "Displays a histogram of browsers the documents have been read in (however it's verbose and not formatted)."),
    4: ("Task 3b",
        "Displays a histogram of browsers the documents have been read in."),
    5: ("Task 4",
        "Displays the top 10 readers in the dataset with the most amount of reading time with their read times."),
    6: ("Task 5",
        "Displays the top 10 also-like (read) documents of readers who have read a specific document."),
    7: ("Task 6",
        "Displays a graph of the relationship between the reader(s) and the also like documents."),
}

# Loop to create radio buttons
for (value, text) in TASK_DATA.items():
    tk.Radiobutton(task_frame, text=text[0], variable=val, value=value,
                   command=lambda: display_task_info(), font="1"
                   ).pack(side=tk.TOP, anchor=tk.W, ipadx=14, ipady=2)

# About and run frame
task_name_label = tk.Label(run_frame, text="Select task to run", justify=tk.LEFT, padx=10)
task_name_label.config(font=("Arial", 16))
task_name_label.pack(side=tk.TOP, anchor=tk.W, pady=(14, 2))
task_desc_label = tk.Message(run_frame, text="Selected task details will appear here", justify=tk.LEFT, width="280")
task_desc_label.pack(side=tk.TOP, anchor=tk.W, padx=(6, 0), pady=(0, 2))
run_task_btn = tk.Button(run_frame, text="Run task", padx=24, pady=6,
                         command=lambda: run_selected_task(val.get()),
                         state=tk.NORMAL,
                         bg="spring green", fg="black", bd="1", width=1000)
run_task_btn.pack(padx=10, pady=(20, 20), side=tk.BOTTOM)


def display_task_info():
    """Function which prints the information for a selected task"""
    task_name = TASK_DATA.get(val.get())[0]  # Gets the name of the task from the task data map
    task_name_label.config(text="Selected: " + task_name)  # set task data to task name label

    task_desc = TASK_DATA.get(val.get())[1]  # Gets the description of the task from the task data map
    task_desc_label.config(text=task_desc, font=8)  # set task desc to task desc label


def get_input(keyword, label):
    """
    Get a user input based on label and returns it back.
    :param keyword:
    :param label:
    :return: The user input

    """
    # Label defines which dialog box message do we want. 0 is for document ID, 1 is for visitor ID.
    if label == 0:
        uuid = "Enter the document ID of the document you want to check."
    else:
        uuid = "Enter the visitor ID of the visitor you want to check."
    # Get user input in result variable using simple dialog (a part of tkinter module in python to get user inputs from
    # dialog boxes
    result = simpledialog.askstring(TASK_DATA.get(keyword)[0], uuid)
    if not result or result.isspace():
        # Return false if no value is input or if user has pressed cancel on the input box.
        return ""
    else:
        # Strip away for any leading or trailing whitespaces as part of input validation.
        return result.strip()


def display_result_task_4(keyword, result):
    """
    Displays the results for a task.
    :param keyword:
    :param result:
    """
    result_window = tk.Tk()
    result_window.title("Result for " + TASK_DATA.get(keyword)[0])
    result_window.resizable(width=False, height=False)

    results_label = tk.Label(result_window, text="Reader profiles", justify=tk.LEFT)
    results_label.config(font=("Arial", 16))
    results_label.pack(side=tk.TOP, anchor=tk.W, pady=(20, 14), padx=14)

    sub_label = tk.Label(result_window, text="Top 10 readers identified are", justify=tk.LEFT)
    sub_label.pack(side=tk.TOP, anchor=tk.W, padx=14, pady=(2, 14))

    counter = 1
    for k, v in result.items():
        key_label = tk.Label(result_window, text=str(counter) + ". Reader: " + k, justify=tk.LEFT)
        key_label.config(font=("Arial", 10))
        key_label.pack(side=tk.TOP, anchor=tk.W, padx=14, pady=(0, 1))

        value_label = tk.Label(result_window, text="   Read time: " + v, justify=tk.LEFT)
        value_label.config(font=("Arial", 10, "bold"))
        value_label.pack(side=tk.TOP, anchor=tk.W, padx=14, pady=(0, 14))
        counter += 1

    result_window.mainloop()


def display_result_task_5(keyword, result, input_doc):
    """
    Displays the results for a task 5.
    :param input_doc:
    :param keyword:
    :param result:
    """
    result_window = tk.Tk()
    result_window.title("Result for " + TASK_DATA.get(keyword)[0])
    result_window.resizable(width=False, height=False)

    results_label = tk.Label(result_window, text="Readers & Also like documents", justify=tk.LEFT)
    results_label.config(font=("Arial", 16))
    results_label.pack(side=tk.TOP, anchor=tk.W, pady=(20, 14), padx=14)

    sub_label = tk.Label(result_window, text="Top 10 readers identified are:", justify=tk.LEFT)
    sub_label.pack(side=tk.TOP, anchor=tk.W, padx=14, pady=(14, 2))

    readers, output = result
    for reader in readers:
        key_label = tk.Label(result_window, text=reader[-4:], justify=tk.LEFT)
        key_label.config(font=("Arial", 10))
        key_label.pack(side=tk.TOP, anchor=tk.W, padx=14, pady=(0, 1))

    sub_label = tk.Label(result_window, text="The also like documents are:", justify=tk.LEFT)
    sub_label.pack(side=tk.TOP, anchor=tk.W, padx=14, pady=(14, 2))

    for documents, count in output.items():
        if documents[-4:] == input_doc[-4:]:
            key_label = tk.Label(result_window, text=documents[-4:] + " (*) read " + str(count) + " times",
                                 justify=tk.LEFT)
            key_label.config(font=("Arial", 10, "bold"))
            key_label.pack(side=tk.TOP, anchor=tk.W, padx=14, pady=(0, 1))
        else:
            key_label = tk.Label(result_window, text=documents[-4:] + " read " + str(count) + " times",
                                 justify=tk.LEFT)
            key_label.config(font=("Arial", 10))
            key_label.pack(side=tk.TOP, anchor=tk.W, padx=14, pady=(0, 1))

    tk.Label(result_window, text="Where the (*) is the input document", pady=20).pack()
    result_window.mainloop()


def run_selected_task(keyword):
    """
    Runs a task based on the entered.

    If the keyword is,
    1, run task 2a
    2, run task 2b,
    3, run task 3a,
    4, run task 3b,
    5, run task 4,
    6, run task 5
    7, run task 6

    :param keyword:

    Returns:
    The output of a task entered. Displays error message if no dataset is loaded of if no task is selected.
    """
    # First check if a dataset is passed in the app or not by using the dataset.is_none() method which gives us
    # this information. If not none, then enter the if loop. Else, display the relevant error message
    if dataset.is_not_none():
        if keyword == 1:
            doc_id = get_input(keyword, 0)
            if doc_id:
                dataset.histogram_country(doc_id)
        elif keyword == 2:
            doc_id = get_input(keyword, 0)
            if doc_id:
                dataset.histogram_continent(doc_id)
        elif keyword == 3:
            dataset.histogram_browsers_a()
        elif keyword == 4:
            dataset.histogram_browsers_b()
        elif keyword == 5:
            result = dataset.visitor_readtimes()
            display_result_task_4(keyword, result)
        elif keyword == 6:
            doc_id = get_input(keyword, 0)
            user_id = get_input(keyword, 1)
            if doc_id:
                result = dataset.run_task_5(doc_id, user_id)
                display_result_task_5(keyword, result, doc_id)
        elif keyword == 7:
            doc_id = get_input(keyword, 0)
            user_id = get_input(keyword, 1)
            if doc_id:
                dataset.run_task_6(doc_id, user_id)
        else:
            messagebox.showinfo("Select task to run", "Please select a task in the Tasks panel.")
    else:
        messagebox.showerror("No dataset given", "Please load a dataset to run the task")
        # If dataset not selected, then prompt user to select the dataset after that.
        select_file()


# How to run tasks frame
how_to_label = tk.Label(how_to_run_frame, text="Instructions to run tasks", justify=tk.LEFT, padx=10)
how_to_label.config(font=("Arial", 16))
how_to_label.pack(side=tk.TOP, anchor=tk.W, pady=(14, 4))

# Instructions to run the program seperated by comma values.
STEPS = "1. Load the desired JSON dataset.,2. Select Task on the Available tasks panel.,3. Run the selected task on the right side panel.,4. Enter document ID and user ID if prompted."

# Print the steps in the frame
for step in STEPS.split(","):
    tk.Label(how_to_run_frame, text=step).pack(side=tk.TOP, anchor=tk.W, pady=(0, 2), padx=10)

root.mainloop()


def main():
    """When executed, runs the App"""
    root.mainloop()


if __name__ == '__main__':
    main()
