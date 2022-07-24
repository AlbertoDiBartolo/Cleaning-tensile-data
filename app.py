# import
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfilename
import pandas as pd
from clean import *


# instantiate Tk
root = Tk()
root.geometry("100x100")
root.eval("tk::PlaceWindow . center")


def clean_file():
    # cleans, formats and saves the data

    # file selection
    loadfile = askopenfile(mode="r", filetypes=[("Excel files", ".csv")])

    # the selected file is converted to a pandas dataframe
    df = pd.read_csv(
        loadfile,
        encoding="ISO-8859-1",
        names=[
            "info",
            "dL (mm)",
            "F (kN)",
            "specimen",
            "strain (%)",
            "stress (MPa)",
            "thickness (mm)",
        ],
    )

    # clean the dataframe
    # cleaning() retunrs the clean dataframe and the number of specimens
    df, n_specimens = cleaning(df)

    # save the file as a worksheet
    savefile = asksaveasfilename(filetypes=[("Excel files", ".xlsx")])
    with pd.ExcelWriter(savefile + ".xlsx") as writer:
        df.to_excel(
            writer, sheet_name="Data", index=False
        )  # save the whole dataframe to the first sheet
        for i in range(
            n_specimens
        ):  # the data for each specimen are saved to separate sheets
            df[df["specimen"] == i + 1].to_excel(
                writer, sheet_name=f"specimen{i+1}", index=False
            )


Button(root, text="Clean File", command=clean_file).pack()


root.mainloop()
