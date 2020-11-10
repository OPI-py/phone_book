#! python3

from tkinter import Tk, Entry, Button, Label, messagebox, END
import sqlite3

win = Tk()
win.title("Database")
win.iconbitmap("favicon.ico")
win.geometry("350x400")
win.resizable(0, 1)


def create_db():
    try:
        con = sqlite3.connect("phone_book.db")
        cc = con.cursor()
        cc.execute("""CREATE TABLE phone_book (
                        first_name,
                        last_name,
                        phone_number
                        )""")
        con.commit()
        con.close()
    except sqlite3.OperationalError:
        pass

create_db()


def submit():
    con = sqlite3.connect("phone_book.db")
    cc = con.cursor()
    
    cc.execute("""INSERT INTO phone_book
                VALUES (:f_name, :l_name, :phone_num)""",
                  {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'phone_num': phone_num.get()
                  })
    con.commit()
    con.close()
    
    f_name.delete(0, END)
    l_name.delete(0, END)
    phone_num.delete(0, END)

def query():
    con = sqlite3.connect('phone_book.db')
    cc = con.cursor()

    cc.execute("SELECT *, oid FROM phone_book")
    records = cc.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + \
                         str(record[1]) + " " + "\t" + str(record[2]) + "\n"

    query_label = Label(win, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    con.commit()
    con.close()

# Create Entry boxes
f_name = Entry(win, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(15, 0))

l_name = Entry(win, width=30)
l_name.grid(row=1, column=1, padx=20, pady=(15, 0))

phone_num = Entry(win, width = 30)
phone_num.grid(row=2, column=1, padx=20, pady=(15, 0))

# Create Labels
f_name_label = Label(win, text="First Name", font=9)
f_name_label.grid(row=0, column=0, pady=(15, 0), padx=(0,15))

l_name_label = Label(win, text="Last Name", font=9)
l_name_label.grid(row=1, column=0, pady=(15, 0), padx=(0,15))

phone_num_label = Label(win, text="Phone number", font=9)
phone_num_label.grid(row=2, column=0, pady=(15, 0), padx=(15,5))

submit_btn = Button(win, text="Submit record", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, ipadx=115)

query_btn = Button(win, text="Show Records", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=10, ipadx=115)

win.mainloop()