#Yazan yiğit

import tkinter as tk
from os import system
ekran = tk.Tk()
ekran.maxsize(500,700)
ekran.minsize(500,700)
ekran.title("PYGUI - zypper")

def install():
    ins = paket.get()
    system(f"sudo zypper install {ins}")
def upgrade():
    system("sudo zypper dist-upgrade")
def update():
    system("sudo zypper update")

title2 = tk.Label(
    ekran,
    text="Paket Yöneticisi GUI",
    font="italic 25",
    fg="blue",
    ).pack()

os = tk.Label(
    ekran,
    text="DNF\n",
    font="italic 25",
    fg="blue",
    ).pack()

title3 = tk.Label(
    ekran,
    text="kuruluacak paketler:",
    font="italic 15",
    ).pack()

paket = tk.Entry(ekran)
paket.pack()

paket_b = tk.Button(
    ekran,
    text="Kur",
    font="italic 15",
    command=install
    ).pack()

bos32 = tk.Label(
    ekran,
    text="",
    font="italic 25",
    ).pack()

upgrade_b = tk.Button(
    ekran,
    text="Upgrade",
    font="italic 20",
    fg="blue",
    command=upgrade,
    ).pack()

bos3 = tk.Label(
    ekran,
    text="",
    font="italic 25",
    ).pack()

update_b = tk.Button(
    ekran,
    text="Update",
    font="italic 20",
    fg="blue",
    command=update,
    ).pack()

imza = tk.Label(
    ekran,
    text="\nHazırlayan Yiğit",
    font="italic 25",
    ).pack()

ekran.mainloop()
