from tkinter import *
import stock_price_tracker as sptracker

app_window = Tk()
app_window.title("Stock Price Tracker")
app_window.minsize(width= 600, height= 400)

stock_list= []

def update_listbox():
    listbox.delete(0, END)
    for stock in stock_list:
        listbox.insert(END, stock)
        
def show_stock_info(ticker, open_price, close_price):
    info_window = Toplevel(app_window)
    info_window.title(f"{ticker}")
    info_window.geometry("300x200")
    
    Label(
        info_window, text=f"Stock Name: {ticker}", 
        font=("Times New Roman", 12)
        ).pack(pady=10)
    Label(
        info_window, text=f"Open Price: {open_price}", 
        font=("Times New Roman", 12)
        ).pack(pady=10)
    Label(
        info_window, text=f"Close Price: {close_price}", 
        font=("Times New Roman", 12)
        ).pack(pady=10)

def activate_remove():
    add_button.config(bg= "red")
    entry= user_stock_input.get()
    if len(entry) > 1:
        if entry in stock_list:
            if len(stock_list) >= 1:
                current_stock.config(
                    text= f"Removed: {entry}", 
                    fg= "red"
                    )
                stock_list.remove(entry)
                update_listbox()
            else:
                current_stock.config(
                    text= "No Stocks To Remove", 
                    fg= "red"
                    )
                raise Exception("Under Limit")
        else:
            current_stock.config(
                text= "Stock Not Tracked!", 
                fg= "red"
                )
            raise Exception("Stock Not Present In List")  

def activate_add():
    add_button.config(bg= "green")
    entry= user_stock_input.get()
    if len(entry) > 1 and entry not in stock_list:
        if len(stock_list) <= 20 and entry not in stock_list:
            current_stock.config(
                text=f"Added: {entry}", 
                fg= "green"
                )
            stock_list.append(entry)
            update_listbox()
        else:
            current_stock.config(
                text= "Limit Reached, Cannot Add More Stocks!", 
                fg= "red"
                )
            raise Exception("Limit Reached")
    else:
        current_stock.config(
            text= "Invalid Entry!", 
            fg= "red"
            )
        raise Exception("Invalid Entry")
    
def listbox_used(event):
    selection= listbox.curselection()
    if selection:
        selected_stock= listbox.get(selection[0])
        stockData= sptracker.get_stock(selected_stock)
        ticker= stockData[0]
        open_price= stockData[1]
        close_price= stockData[2]
        show_stock_info(ticker, open_price, close_price)    
    
add_button= Button(
    text= "+ ADD STOCK", 
    font= ("Times New Roman", 18, "bold"),
    width= 15,
    command= activate_add,
    )
add_button.place(x= 0, y= 0)

remove_button= Button(
    text= "- REMOVE STOCK", 
    font= ("Times New Roman", 18, "bold"),
    width= 15,
    command= activate_remove,
    )
remove_button.place(x= 0, y= 30)

user_stock_input= Entry(width= 18)
user_stock_input.place(x= 0, y= 60)

current_stock= Label(
    text= "No Stock Added",
    font= ("Times New Roman", 12, "bold"),
    fg= "red" # burns my eyes, CHANGE colour later
    )
current_stock.place(x= 40, y= 90)

listbox = Listbox()
listbox.place(
    x=0,
    y=120,
    width=170,
    height=270,
)
listbox.bind("<<ListboxSelect>>", listbox_used)

app_window.mainloop()