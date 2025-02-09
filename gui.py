import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from query_books import export_books_to_csv, get_all_categories

def export_all():
    export_books_to_csv("books_all.csv")
    messagebox.showinfo("Export CSV", "✅ Tous les livres ont été exportés !")
    
def export_by_category():
    selected_category = category_var.get()
    if selected_category == "Choisir une catégorie":
        messagebox.showwarning("Erreur ⚠️", "Veuillez sélectionner une catégorie valide pour l'export !")
        return
    export_books_to_csv(f"books_{selected_category}.csv", category=selected_category)
    messagebox.showinfo("Export CSV", f"✅ Livres de '{selected_category}' exportés !")

def export_by_price():
    export_books_to_csv("books_price_10_20.csv", min_price=10, max_price=20)
    messagebox.showinfo("Export CSV", "✅ Livres entre 10 et 20 £ exportés !")
    
root = tk.Tk()
root.title("Export CSV de livres")

categories = ["Choisir une catégorie"] + sorted(get_all_categories())
category_var = tk.StringVar(root)
category_var.set(categories[0])

tk.Label(root, text="Sélectionner une catégories :").pack(pady=10)
category_menu = ttk.Combobox(root, textvariable=category_var, values=categories, state="readonly")
category_menu.pack(pady=5)
category_menu.config(width=40)

tk.Button(root, text="Exporter tout les livres", command=export_all).pack(pady=5)
tk.Button(root, text="Exporter de la catégorie :", command=export_by_category).pack(pady=5)
tk.Button(root, text="Exporter les livres entre 10 et 20 £", command=export_by_price).pack(pady=5)

root.mainloop()

