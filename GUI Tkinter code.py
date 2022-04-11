#--------------Import Functions---------------------------
from tkinter import * 
from functools import partial #to prevent unwanted windows

import random
#---------------First Class-------------------------------
class Converter:
        def __init__ (self):
                
#---------------Formatting Variables-----------------------------------------------------------------
                background_colour= "light blue" 
                
#---------------Converter Main Screen GUI...---------------------------------------------------------
                self.converter_frame = Frame(width=600, height=600, bg=background_colour,
                                             pady=10)
                self.converter_frame.grid()
                
#---------------Temperature Conversion Heading (row 0)-----------------------------------------------
                self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                                   font=("Arial", "16", "bold" ),
                                                   padx=10, pady=10)
                                                   
                self.temp_converter_label.grid(row=0)
                
#---------------Help Button (row 1)------------------------------------------------------------------
                self.help_button = Button(self.converter_frame, text="Help",
                                          font=("Arial", "16"),
                                          padx=10, pady=10, comman=self.help)
                self.help_button.grid(row=1)
                
        def help(self):
                print("You asked for help")
                get_help = Help(self)
                get-help.help_text.configure(test="Help text goes here")
                
                
                
#---------------Main Routine---------------
if __name__ == "__main__":
        root = Tk()
        root.title("Temperature Converter")
        something = Converter()
        root.mainloop()
