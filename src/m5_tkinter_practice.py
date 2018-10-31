"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jess Thuer.
"""  # DONE 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    window = tkinter.Tk()

    # ------------------------------------------------------------------
    # DONE 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame = ttk.Frame(window, padding = 25)
    frame.grid()

    # ------------------------------------------------------------------
    # DONE 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    button = ttk.Button(frame, text = 'button')
    button.grid()

    # ------------------------------------------------------------------
    # DONE 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    button['command'] = (lambda: say_hello())
    button.grid()

    # ------------------------------------------------------------------
    # DONE 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    entry_box = ttk.Entry(window)
    entry_box.grid()

    entry_button = ttk.Button(window, text = 'Print Entry')
    entry_button['command'] = (lambda: hello_goodbye(entry_box))
    entry_button.grid()

    # ------------------------------------------------------------------
    # DONE 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry2 = ttk.Entry(window)
    entry2.grid()

    button3 = ttk.Button(window, text = 'button3')
    button3['command'] = (lambda: button_press(entry_box, entry2))
    button3.grid()

    # ------------------------------------------------------------------
    # NOT_DONE 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    ####


    window.mainloop()


def say_hello():
    print('Hello')

def hello_goodbye(entry_box):
    contents_of_entry_box = entry_box.get()
    if contents_of_entry_box == 'ok':
        print('Hello')
    else:
        print('Goodbye')

def button_press(entry_box, entry3):
    get_words = entry_box.get()
    get_number = entry3.get()
    n = int(get_number)
    print(get_words*n)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
