#! python3

from tkinter import Tk, Entry, Button, Label, messagebox, END
import sqlite3

wnd = Tk()
wnd.title("Database")
wnd.iconbitmap("favicon.ico")
wnd.geometry("350x400")
wnd.resizable(0, 1)


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
        print_records += str(record[3]) + " " + \
                         str(record[0]) + " " + \
                         "\t" + str(record[1]) + str(record[2]) + "\n"

    query_label = Label(wnd, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    con.commit()
    con.close()

def delete():
    con = sqlite3.connect('phone_book.db')
    cc = con.cursor()
    
    try:
        cc.execute("DELETE FROM phone_book WHERE oid = " + delete_box.get())
    except sqlite3.OperationalError:
        print(sqlite3.OperationalError)
        messagebox.showwarning(title="Warning",
                                message="Select ID field is empty")
    con.commit()
    con.close()

# Create Entry boxes
f_name = Entry(wnd, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(15, 0))

l_name = Entry(wnd, width=30)
l_name.grid(row=1, column=1, padx=20, pady=(15, 0))

phone_num = Entry(wnd, width = 30)
phone_num.grid(row=2, column=1, padx=20, pady=(15, 0))

delete_box = Entry(wnd, width=30)
delete_box.grid(row=7, column=1, pady=15)

# Create Labels
f_name_label = Label(wnd, text="First Name", font=9)
f_name_label.grid(row=0, column=0, pady=(15, 0), padx=(0,15))

l_name_label = Label(wnd, text="Last Name", font=9)
l_name_label.grid(row=1, column=0, pady=(15, 0), padx=(0,15))

phone_num_label = Label(wnd, text="Phone number", font=9)
phone_num_label.grid(row=2, column=0, pady=(15, 0), padx=(15,5))

delete_box_info = Label(wnd, 
            text="Please enter record ID and press 'Delete Record'")
delete_box_info.grid(row=6, column=0, columnspan=2)

delete_box_label = Label(wnd, text="Select ID", font=9)
delete_box_label.grid(row=7, column=0, pady=15)

#Create Buttons
submit_btn = Button(wnd, text="Submit record", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, ipadx=115)

query_btn = Button(wnd, text="Show Records", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=10, ipadx=115)

delete_btn = Button(wnd, text="Delete Record", command=delete)
delete_btn.grid(row=8, column=0, columnspan=2, pady=10, ipadx=115)

wnd.mainloop()