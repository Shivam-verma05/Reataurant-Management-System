# USE GIVEN BELLOW ID AND PASSWORD TO USE THE RESTAURANT MANAGEMENT SYSTEM
# Manager ID = manager@123
# Password = 12345

# IMPORTING MODULES
from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox


# MAIN FUNCTION
def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()



# MAKING A CLASS WINDOW2 FOR BILL GENERATION 
class Window2:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1300x750+100+6")
        self.win.resizable(False,False)
        self.win.title("Restaurant Management System") 
        
        self.title_label = Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        
        bill_no = random.randint(1000,10000)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)
        calc_var= StringVar()

        # DECLARING VARIABLES
        cust_nm=StringVar()
        cust_cot=StringVar()
        date_pr=StringVar()
        item_pur=StringVar()
        item_qty=StringVar()
        cone=StringVar()

        # ACCESSING CURRENT DATE AND TIME USING MODULE
        date_pr.set(datetime.now())
        
        # CREATING A EMPTY LIST TO APPEND ITEMS PURCHASED FOR FURTHER CALCULATION
        total_list=[]
        self.grd_total=0


     
        # CREATING FRAMES,BUTTON,LABELS AND ENTRY FIELDS USING TKINTER
        self.entry_frame = LabelFrame(self.win,text="Enter Details",background="lightgrey",font=('Arial',20,'bold'),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)
        
        self.bill_no_lbl = Label(self.entry_frame,text="Bill Number: ",font=('Arial',15,'bold'),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)
        
        self.bill_no_ent = Entry(self.entry_frame,font=('Arial',15,'bold'),bd=5,textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")
        
        self.cust_nm_lbl = Label(self.entry_frame,text="Customer Name: ",font=('Arial',15,'bold'),bg="lightgrey")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)
        
        self.cust_nm_ent = Entry(self.entry_frame,font=('Arial',15,'bold'),bd=5,textvariable=cust_nm)
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)
        
        self.cust_cot_lbl = Label(self.entry_frame,text="Customer Contact: ",font=('Arial',15,'bold'),bg="lightgrey")
        self.cust_cot_lbl.grid(row=2,column=0,padx=2,pady=2)
        
        self.cust_cot_ent = Entry(self.entry_frame,font=('Arial',15,'bold'),bd=5,textvariable=cust_cot)
        self.cust_cot_ent.grid(row=2,column=1,padx=2,pady=2)
        
        self.date_lbl = Label(self.entry_frame,text="Date: ",font=('Arial',15,'bold'),bg="lightgrey")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)
        
        self.date_ent = Entry(self.entry_frame,font=('Arial',15,'bold'),bd=5,textvariable=date_pr)
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)
        
        self.item_pur_lbl = Label(self.entry_frame,text="Item Purchased: ",textvariable="item_pur",font=('Arial',15,'bold'),bg="lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)
        
        self.item_pur_ent = Entry(self.entry_frame,font=('Arial',15,'bold'),bd=5,textvariable=item_pur)
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)
        
        self.item_qty_lbl = Label(self.entry_frame,text="Item Quantity: ",font=('Arial',15,'bold'),bg="lightgrey")
        self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)
        
        self.item_qty_ent = Entry(self.entry_frame,font=('Arial',15,'bold'),bd=5,textvariable=item_qty)
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)
        
        self.cost_one_lbl = Label(self.entry_frame,text="Cost of One: ",font=('Arial',15,'bold'),bg="lightgrey")
        self.cost_one_lbl.grid(row=6,column=0,padx=2,pady=2)
        
        self.cost_one_ent = Entry(self.entry_frame,font=('Arial',15,'bold'),bd=5,textvariable=cone)
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)

        

        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\tSwad Restaurant")
            self.bill_txt.insert(END,"\n\t\t\t7Street,Near Railway Lines,Badaun")
            self.bill_txt.insert(END,"\n\t\t\t      Phone:+916203401099")
            self.bill_txt.insert(END,"\n==============================================================================\n")
            self.bill_txt.insert(END,f"Bill  Number{bill_no.get()}")        

        def genbill():
            self.bill_txt.insert(END,f"\nCustomer Name : {cust_nm.get()}")
            self.bill_txt.insert(END,f"\nCustomer Contact : {cust_cot.get()}")
            self.bill_txt.insert(END,f"\nCustomer Name : {date_pr.get()}")
            self.bill_txt.insert(END,"\n==============================================================================\n")
            self.bill_txt.insert(END,"Product Name\t\t\t\tQuantity\t\tPerCost\t\tTotal") 
            self.bill_txt.insert(END,"\n==============================================================================\n")
            
            # AS BILL IS GENERATED THIS BUTTONS GETS ACTIVATED
            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")
            self.save_btn.config(state="normal")

        # FUNCTION OF CLEAR BUTTON TO EMPTY THE ENTRY FIELDS
        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")

        # FUNCTION OF RESET BUTTON TO DELETE ENTRY AND GENERATED BILL
        def  reset_func():
            self.bill_txt.delete("1.0,END")
            default_bill()
        
        # ADD FUNCTION TO CALCULATE AMOUNTS TO BE PAID
        def add_func():
            qty=int(item_qty.get())
            cones=int(cone.get())
            total=qty*cones
            total_list.append(total)
            self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t\t{item_qty.get()}\t\tRs.{cone.get()}\t\tRs.{total}") 

 
        # TO CALULATE TOTAL AMOUNT TO BE PAID
        def total_func():
            # global grd_total
            for item in total_list:
                self.grd_total=self.grd_total + item
            self.bill_txt.insert(END,"\n==============================================================================\n")
            self.bill_txt.insert(END,f"\n\t\t\t\tGrand Total : {self.grd_total}\n")
            self.bill_txt.insert(END,"\n==============================================================================\n")

        def reset_func():
            total_list.clear()
            self.grd_total=0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_txt.delete("1.0",END)
        
        def save_func():
            user_choice=messagebox.askyesno("confirm?",f"Do you want to save the bill: {bill_no_tk.get()}")
            if user_choice>0:
                self.bill_content=self.bill_txt.get("1.0",END)
                can=open(str(bill_no_tk.get())+".txt","a")
                can.write(self.bill_content)
                can.close()
                messagebox.showinfo("success!",f"Bill{bill_no_tk.get()} has been saved successfully!",parent=self.win)
            else:
               return
            
        
        # VARIOUS BUTTONS 
        self.button_frame = LabelFrame(self.entry_frame,text="Options",bd=5,font=('Arial',15,'bold'),bg="lightgrey")
        self.button_frame.place(x=20,y=280,width=430,height=300)
        
        self.add_btn = Button(self.button_frame,text="Add",font=('Arial',12,'bold'),bd=3,width=12,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)
        
        self.generate_btn = Button(self.button_frame,text="Generate",font=('Arial',12,'bold'),bd=3,width=12,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)
        
        self.clear_btn = Button(self.button_frame,text="Clear",font=('Arial',12,'bold'),bd=3,width=12,height=3,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)
        
        self.total_btn = Button(self.button_frame,text="Total",font=('Arial',12,'bold'),bd=3,width=12,height=3,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)
        
        self.reset_btn = Button(self.button_frame,text="Reset",font=('Arial',12,'bold'),bd=3,width=12,height=3,command=reset_func)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)
        
        self.save_btn = Button(self.button_frame,text="Save",font=('Arial',12,'bold'),bd=3,width=12,height=3,command=save_func)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)
        
        
        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")

        

        # CREATING A CALCULATOR FRAME TO CROSS CHECK CALCULATION
        self.calc_frame=Frame(self.win,bd=8,background="lightgrey",relief=GROOVE)
        self.calc_frame.place(x=570,y=110,width=680,height=295)

        def press_btn(event):
            button_text = event.widget.cget("text")  # Get the text of the clicked button

            if button_text == "=":  # If the clicked button is the equal sign
                try:
            # Evaluate the expression entered in the display
                    expression = display.get()
                    result = eval(expression)
                    display.delete(0, END)  # Clear the display
                    display.insert(END, str(result))  # Display the result
                except Exception as e:
                     display.delete(0, END)  # Clear the display
                     display.insert(END, "Error")  # Display error message

            else:  # For other buttons (digits and operators)
                    display.insert(END, button_text)  # Append the clicked button text to the display

        display = Entry(self.calc_frame, font=("Arial", 15),width=58,justify='right')
        display.grid(row=0, column=0, columnspan=11, padx=10, pady=10)
        

       # Create the buttons
        buttons = [
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "0", ".", "=", "+"
        ]

        row = 1
        col = 0
        for button_text in buttons:
            button = Button(self.calc_frame,bg="lightgrey",text=button_text,bd=8,width=12,height=1,font=("Arial",15,"bold"))
            button.grid(row=row, column=col, padx=1, pady=2)
            button.bind("<Button-1>", press_btn)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        self.bill_frame=LabelFrame(self.win,text="Bill Area",font=("Arial",18,"bold"),bd=8,background="lightgrey",relief=GROOVE)
        self.bill_frame.place(x=585,y=420,width=650,height=320)
        
        self.bill_txt=Text(self.bill_frame,bg="white")
        self.bill_txt.pack(fill=BOTH,expand=TRUE)
        
        default_bill()

# CREATING CLASS FOR LOGIN WINDOW  
class LoginPage:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1300x750+100+6")
        self.win.resizable(False,False)
        self.win.title("Restaurant Management System")
        
        self.title_label = Label(self.win,text="Restaurant Management System",font=('Arial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        
        self.main_frame = Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=450)
        
        self.login_lbl = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="lightgrey",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)
        
        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif',18))
        self.entry_frame.pack(fill=BOTH,expand=True)
        
        self.entus_lbl = Label(self.entry_frame,text="Manager ID: ",bg="lightgrey",font=('sans-serif',15),bd=6)
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)
        
    
        # VARIABLES FOR THE LOGIN WINDOW
        username= StringVar()
        password = StringVar()
        
        self.entus_ent = Entry(self.entry_frame,font=('sans-serif',15),textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)
        
        self.entpass_lbl = Label(self.entry_frame,text="Password: ",bg="lightgrey",font=('sans-serif',15),bd=6)
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)
        
        self.entpass_ent = Entry(self.entry_frame,font=('sans-serif',15),show="*",textvariable=password)
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)
        
        #LOGIN VALIDATION
        
        def check_login():
            if username.get()=="manager@123" and password.get()=="12345":
                self.billing_btn.config(state="normal")
            else:
                pass
        
        def reset():
            username.set("")
            password.set("")
        
        def billing_sect():
            self.newWindow=Toplevel(self.win)
            self.app= Window2(self.newWindow)
        
        self.button_frame = LabelFrame(self.entry_frame,text="Options",bd=7,relief=GROOVE,bg="lightgrey",font=('Arial',15))
        self.button_frame.place(x=20,y=100,width=730,height=85)
        
        self.login_btn = Button(self.button_frame,text="Login",bd=5,font=('Arial',12),width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)
        
        self.billing_btn = Button(self.button_frame,text="Billing",bd=5,font=('Arial',12),width=15,command=billing_sect)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")
        
        self.reset_btn = Button(self.button_frame,text="Reset",bd=5,font=('Arial',12),width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)

        # default_bill()
    
        
if __name__ == "__main__":
    main()