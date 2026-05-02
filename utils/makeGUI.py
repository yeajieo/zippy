import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

from utils.makeZip import zipFileCreator
from utils.makeAppLog import setup_logger
logger = setup_logger()

class InputGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Zippy")

        self.folder_path = None
        self.dt = None

        tk.Label(root, text="File path:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.folder_entry = tk.Entry(root, width=40)
        self.folder_entry.grid(row=0, column=1, padx=5, pady=5)
        self.search_button = tk.Button(root, text="Search", command=self.browse_folder)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.date_entry = tk.Entry(root, width=20)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        tk.Label(root, text="Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.time_entry = tk.Entry(root, width=20)
        self.time_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.run_button = tk.Button(
            root,
            text="Run",
            command=self.on_submit,
            width=12,
            height=1,
            font=("", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        )
        self.run_button.grid(row=3, column=0, columnspan=3, pady=(20, 20))

        self.status_label = tk.Label(root, text="", fg="black", font=("", 14, "bold"))
        self.status_label.grid(row=4, column=0, columnspan=3, pady=5)
        self.status_label.config(text="Please enter the folder path, date, and time.")

    def browse_folder(self):
        logger.info("=========== START")
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path = folder
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder)
            self.status_label.config(text="")
        logger.info("=========== END")

    def on_submit(self):
        logger.info("=========== START")
        folder = self.folder_entry.get()
        date_str = self.date_entry.get()
        time_str = self.time_entry.get()

        if not folder:
            logger.debug("Wrong a dir path")
            messagebox.showwarning("Error_Folder", "Choose a folder.")
            self.status_label.config(text="")
            return

        try:
            datetime_str = f"{date_str} {time_str}"
            dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        except ValueError:
            logger.debug("Wrong date")
            messagebox.showerror("Error_DateTime", "Check a format of date and time.")
            self.status_label.config(text="")
            return

        logger.debug("Success input")
        self.folder_path = folder
        self.dt = dt

        self.status_label.config(text="Processing...", font=("", 18, "bold"))
        self.root.update()
        self.search_button.config(state="disabled")
        self.run_button.config(state="disabled")

        logger.debug(f"sample path : {self.folder_path}")
        logger.debug(f"datetime : {self.dt}")

        mz = zipFileCreator(self.folder_path,self.dt)
        mz.makeWorkspaceFolder()
        flag = mz.exporting()
        mz.zipping()

        if flag == True:
            logger.info(f"All process is successfully done.")
            self.status_label.config(text="SUCCESS!\nPlease check the ZIP file in the GMlogger folder.",
                                     font=("", 13, "bold"))
        else:
            logger.info(f"No log files.")
            self.status_label.config(text="FAILED!\nNo log files found for the specified time.", font=("", 13, "bold"))
        self.search_button.config(state="active")
        self.run_button.config(state="active")

        logger.info("=========== END")
