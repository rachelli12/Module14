import sys
from anagram import anagram_functions as af
from anagram.anagram_database import *
import tkinter as tk
from tkinter import messagebox

class GUI(tk.Tk):
    DATABASE = 'anagram_database.db'
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Anagram Generator")

        self.start_label = tk.Label(self, text='Enter your word here', width=25).grid(row=2, column=0)
        self.start_enter = tk.Entry(self).grid(row=2, column=1)
        self.enter_button = tk.Button(self, text='Enter', command=self.create_database).grid(row=3)

        self.exit_button = tk.Button(self, text='Exit', width=25, command=self.destroy).grid(row=5)

    def create_database(self):
        create_tables(self.DATABASE)

    def add_anagram(self):
        conn = create_connection(self.DATABASE)
        with conn:
            anagram = (self.start_enter.get())
            create_anagram(conn, anagram)

    def view_anagram(self):
        conn = create_connection(self.DATABASE)
        anagrams = select_all_anagrams(conn)
        for anagram in anagrams:
            print(anagram)

if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
