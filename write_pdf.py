from fillpdf import fillpdfs
from tkinter import filedialog


def choise_newdir():
    global path_out
    path_out = filedialog.askdirectory()

def save_newpdf():
    # a = fillpdfs.write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict, flatten=False)
    print(str(path_out))