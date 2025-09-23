import ttkbootstrap as ttk
from tkinter import filedialog, messagebox
import threading
import os
from bulk_font_installer import install_all_fonts_in_folder

# Function to choose folder
def choose_folder():
    folder_path = filedialog.askdirectory(title="Select Font Folder")
    if folder_path:
        folder_label.config(text=f"Selected Folder: {folder_path}")
        select_button.config(state="disabled")
        install_fonts_button.config(state="normal")

# Function to show progress bar
def show_progress_bar():
    progress_window = ttk.Toplevel(app)
    progress_window.geometry("400x200")
    progress_window.title("Installing Fonts")

    progress_label = ttk.Label(progress_window, text="Installing fonts... Please wait.", font=("Arial", 12))
    progress_label.pack(pady=20)

    progress_bar = ttk.Progressbar(progress_window, mode="indeterminate")
    progress_bar.pack(pady=20, padx=20, fill="x")
    progress_bar.start()

    return progress_window, progress_bar

# Function to handle success window
def show_success_window():
    success_window = ttk.Toplevel(app)
    success_window.geometry("400x200")
    success_window.title("Success")

    success_label = ttk.Label(success_window, text="Fonts installed successfully!", font=("Arial", 14, "bold"))
    success_label.pack(pady=50)

    close_button = ttk.Button(success_window, text="Close", command=app.quit)
    close_button.pack(pady=10)

# Function to handle error window
def show_error_window(error_message):
    error_window = ttk.Toplevel(app)
    error_window.geometry("400x200")
    error_window.title("Error")

    error_label = ttk.Label(error_window, text=error_message, font=("Arial", 12))
    error_label.pack(pady=50)

    close_button = ttk.Button(error_window, text="Close", command=error_window.destroy)
    close_button.pack(pady=10)

# Start font installation process
def start_installation(folder_path):
    if not os.path.isdir(folder_path):
        show_error_window("Invalid folder selected!")
        return

    progress_window, progress_bar = show_progress_bar()

    def install_in_background():
        try:
            install_all_fonts_in_folder(folder_path)
            progress_window.destroy()
            show_success_window()
        except Exception as e:
            progress_window.destroy()
            show_error_window(str(e))

    # Run the installation in a separate thread to avoid freezing the UI
    threading.Thread(target=install_in_background, daemon=True).start()

# Main window setup
app = ttk.Window()
app.geometry("600x500")
app.title("Bulk Font Installer")

# Main label
label = ttk.Label(app, text="Bulk Font Installer")
label.pack(pady=30)
label.config(font=("Arial", 20, "bold"))

# Folder selection interface
folder_frame = ttk.Frame(app)
folder_frame.pack(pady=10, fill="x")
folder_label = ttk.Label(folder_frame, text="No folder selected", font=("Arial", 12))
folder_label.pack(pady=5)

select_button = ttk.Button(folder_frame, text="Select Folder", command=choose_folder)
select_button.pack(pady=5)

# Button to start font installation
install_fonts_button = ttk.Button(app, text="Install Fonts", state="disabled", command=lambda: start_installation(folder_label.cget("text").replace("Selected Folder: ", "")))
install_fonts_button.pack(pady=20)

# Run the application
app.mainloop()
