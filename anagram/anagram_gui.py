"""
Program: anagram_gui.py
Author: Rachel Li
Last date modified: 31/07/2020

The purpose of this program is to create GUI with Database
and produce GUI of anagram that displays output of anagram.
"""
import sys
from anagram.anagram_class import *
from anagram.anagram_functions import *
from anagram.anagram_database import *
import tkinter as tk
from tkinter import messagebox

class entry_GUI(tk.Tk):
    DATABASE = 'anagram_database.db'

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Anagram Generator")

        self.start_label = tk.Label(self, text='Enter your word here', width=25).grid(row=1, column=0)
        self.start_enter = tk.Entry(self).grid(row=1, column=1)
        self.enter_button = tk.Button(self, text='Enter', command=main(), width= 25).grid(row=1, column=2)

        self.display_result_label = tk.Label(self, text='Results', command=main()).grid(row=2, column=0)

        self.exit_button = tk.Button(self, text='Exit', width=25, command=self.destroy).grid(row=3)

    def create_database(self):
        main()
        create_tables(self.DATABASE)

    def add_anagram(self):
        conn = create_connection(self.DATABASE)
        with conn:
            an = (self.start_enter.get())
            create_anagram(conn, an)

    def view_anagram(self):
        conn = create_connection(self.DATABASE)
        ans = select_all_anagrams(conn)
        for a in ans:
            print(ans)

if __name__ == '__main__':
    entry_GUI().mainloop()
