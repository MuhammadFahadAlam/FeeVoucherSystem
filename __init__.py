import UserInterface
from tkinter import * 
from tkinter import ttk            #  ttk provides access to the Tk themed widget set
import Voucher
import Database

if __name__ == "__main__":                              #  program runs if we are accessing it directly( without import )
    """Condition which be satisfied if file is accessed directly."""

    obj = UserInterface.MainView( )

    obj.mainloop()
