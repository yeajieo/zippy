import tkinter as tk
from utils.makeGUI import InputGUI
from utils.makeExampleFiles import ExampleFileCreator
from utils.makeAppLog import setup_logger
logger = setup_logger()

if __name__ == '__main__':

    # Generate sample log files.
    example = ExampleFileCreator()
    example.load_paths()
    example.load_datetime()
    example.makeSampleFolder()
    example.create_allFiles()

    # Start zippy
    root = tk.Tk()
    gui = InputGUI(root)
    root.mainloop()

    pass

