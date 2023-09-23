# Nazwa skryptu: kody_payday.py
# Autor: Piotr G. / Paczek
# Data utworzenia: 23 września 2023
# Opis: Skrypt Daje Kazdą Mozliwą Kombinacje Kodów Do Sejfu W Grze PayDay.


import itertools
import tkinter as tk
from tkinter import ttk
import os
import sys

def reset_script():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def generate_combinations(odciski):
    odciski = [int(x) for x in odciski]
    combinacje = itertools.product(odciski, repeat=4)
    filtered = list(filter(lambda c: set(c) == set(odciski), combinacje))
    filtered.sort()
    return filtered

def display_combinations():
    odciski = entry.get()
    combinations = generate_combinations(odciski)

    section_count = 0
    first_number = -1

    result_text.delete(1.0, tk.END)  # Wyczyść pole tekstowe

    for i, unique_result in enumerate(combinations):
        if unique_result[0] != first_number:
            section_count += 1
            result_text.insert(tk.END, f"--- section {section_count} ---\n")
            first_number = unique_result[0]

        result_text.insert(tk.END, f"{i + 1}:\t{unique_result}\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Generator Kombinacji")

    label = ttk.Label(root, text="Typ odciskow (np. 123 lub 1234):")
    label.pack(pady=10)

    entry = ttk.Entry(root)
    entry.pack()

    generate_button = ttk.Button(root, text="Generuj Kombinacje", command=display_combinations)
    generate_button.pack()

    result_text = tk.Text(root, height=15, width=40)
    result_text.pack()

    reset_button = ttk.Button(root, text="Zresetuj Skrypt", command=reset_script)
    reset_button.pack()

    root.mainloop()