from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk
from ttkthemes import themed_tk as tk
import sqlite3
from PIL import Image, ImageTk
from tkinter import messagebox
#NOTE: SET THEME TO NEWELY ADDED ELEMENTS! 

conn = sqlite3.connect('bloodbank.db')
c = conn.cursor()



#Root window configuration
root = tk.ThemedTk()
root.get_themes()
root.set_theme('plastik')
# root.set_theme('winxpblue')


root.title("Blood Banking System")
root.geometry("700x400")
root.iconbitmap("hospital-1_icon-icons.com_66068.ico")
root.resizable(height=False, width=False)
root_back = ImageTk.PhotoImage(Image.open("Root_background.png"))
root_back_label = Label(root,image=root_back)
root_back_label.place(x=0, y=0, relheight=1, relwidth=1)

def delete_record_func():
	entered_rowid = delete_record_entry.get()
	conn = sqlite3.connect('bloodbank.db')
	c = conn.cursor()
	c.execute("DELETE FROM donar_table WHERE rowid = ?",entered_rowid)
	conn.commit()
	adminlogin_window_data.destroy()
	response6 = messagebox.showinfo("DELETED","RECORD DELETED")


def search_donar():
	if blood_selected.get() == '-':
		finddonor_window.destroy()
		response3 = messagebox.showerror("Error","No Blood Group Selected")
	else:
		needed_bloodtype = blood_selected.get()
		finddonor_window.destroy()
		avail_donar_window = Toplevel()
		avail_donar_window.geometry("570x600")
		avail_donar_window.title("Available Donors")
		avail_donar_window.resizable(height = False, width = False)
		avail_donar_window.iconbitmap("hospital-1_icon-icons.com_66068.ico") #finddonor_back.png
		avail_donar_back = ImageTk.PhotoImage(Image.open("admin_db_back.png"))
		avail_donar_back_label = Label(avail_donar_window,image=avail_donar_back)
		avail_donar_back_label.place(x=0, y=0, relheight=1, relwidth=1)
		
		conn = sqlite3.connect('bloodbank.db')
		c = conn.cursor()
		c.execute("SELECT * FROM donar_table WHERE blood_type = ?", (needed_bloodtype,))
		list2 = c.fetchall()
		if len(list2)==0:
			avail_donar_window.destroy()
			response5 = messagebox.showerror("Error","No Data Available")
		else:
			i = 0
			for item in list2: # this loop works each tuple
				for j in range(len(item)): # this loop works for each item in each tupel
					e = ttk.Entry(avail_donar_window , width=10) 
					e.grid(row=i, column=j,padx=8,pady=5) 
					e.insert(END, item[j])
				i=i+1 # we switch to new row after printing each attribute of a tuple
		
		avail_donar_window.mainloop()

def adminloginsubmit():
	if admin_username_entry.get() != 'admin' and admin_pass_entry != 'admin':
		adminlogin_window.destroy()
		response1 = messagebox.showerror("Error","No Input")
	else:
		adminlogin_window.destroy()
		global adminlogin_window_data
		adminlogin_window_data =  Toplevel() # admin_db_back.png

		
		
		adminlogin_window_data.geometry("570x600")
		adminlogin_window_data.title("DATABASE")
		adminlogin_window_data.resizable(height = False, width = False)
		adminlogin_window_data.iconbitmap("admin_login_logo.ico")

		#NOTE: BACKGROUND IS NOT VISIBLE ON THE ADMIN DATABASE VIEW PAGE
		admin_data_back = ImageTk.PhotoImage(Image.open("admin_db_back.png"))
		back_label_data = Label(adminlogin_window_data,image=admin_data_back)
		back_label_data.place(x=0, y=0, relheight=1, relwidth=1)
		conn = sqlite3.connect('bloodbank.db')
		c = conn.cursor()
		c.execute("SELECT rowid,* FROM donar_table LIMIT 15")
		list1 = c.fetchall()
		if len(list1)==0:
			adminlogin_window_data.destroy()
			response4 = messagebox.showerror("Error","No Data Available")
		else:
			i = 0
			for item in list1: # this loop works each tuple
				for j in range(len(item)): # this loop works for each item in each tupel
					e = Entry(adminlogin_window_data, width=10, fg='blue') 
					e.grid(row=i, column=j,padx=8,pady=3) 
					e.insert(END, item[j])
				i=i+1 # we switch to new row after printing each attribute of a tuple
		global delete_record_entry
		
		delete_record_entry = ttk.Entry(adminlogin_window_data)
		delete_record_button = ttk.Button(adminlogin_window_data, text="DELETE",command=delete_record_func)
		delete_record_entry.place(x=150,y=570)
		delete_record_button.place(x=300,y=570)
		adminlogin_window_data.mainloop()

def add_entry():
	
	name1 = donorsname_entry.get()
	blood_type = blood.get()
	donate_organ= organ.get()
	
	ph_number = phone_no_entry.get()
	email1 = email_entry.get()
	address1 = address_text.get()
	if name1 !="":
		conn = sqlite3.connect('bloodbank.db')
		c = conn.cursor()

		c.execute("INSERT INTO donar_table VALUES(:name12,:blood_type12,:donate_organ12,:ph_number12,:email12,:address12)",
			{
			'name12' :name1,
			'blood_type12' :blood_type,
			'donate_organ12' :donate_organ,
			'ph_number12' :ph_number,
			'email12' :email1,
			'address12' :address1
			})
		conn.commit()
		conn.close()
		donateblood_window.destroy()
	else:
		donateblood_window.destroy()
		response = messagebox.showerror("Error","No Input")
		

def adminlogin_function():
	global admin_username_entry
	global admin_pass_entry
	global adminlogin_window
	adminlogin_window =  Toplevel()
	
	adminlogin_window.title("Admin Login")
	adminlogin_window.geometry("700x400")
	adminlogin_window.resizable(height=False, width=False)
	adminlogin_window.iconbitmap("admin_login_logo.ico")
	admin_background = ImageTk.PhotoImage(Image.open("admin_login_background123.jpg"))
	admin_background_label = Label(adminlogin_window, image=admin_background)
	admin_background_label.place(x=0, y=0, relheight=1, relwidth=1)

	# Widgets on adminlogin_window
	admin_username_label = ttk.Label(adminlogin_window, text="Username")
	admin_username_label.place(x=388, y=135)
	admin_username_entry = ttk.Entry(adminlogin_window)
	admin_username_entry.place(x =490 , y =135, width = 85)
	admin_pass_label = ttk.Label(adminlogin_window, text="Password")
	admin_pass_label.place(x = 388, y= 180)
	admin_pass_entry = ttk.Entry(adminlogin_window, show="*")
	admin_pass_entry.place(x =490 , y =180, width = 85)
	admin_login_button = ttk.Button(adminlogin_window, text="Login", command=adminloginsubmit)
	admin_login_button.place(x = 430, y= 230, width=100)
	adminlogin_window.mainloop()

def donate_function():
	global donorsname_entry
	global blood
	global organ
	global phone_no_entry
	global email_entry
	global address_text
	global donateblood_window
	#donateblood_window configuration
	donateblood_window = Toplevel()
	donateblood_window.geometry("500x500")
	donateblood_window.title("Donate Blood")
	donateblood_window.resizable(height = False, width = False)
	donateblood_window.iconbitmap("hospital-1_icon-icons.com_66068.ico")
	donateblood_background = ImageTk.PhotoImage(Image.open("donate_blood_back_2.png"))
	donateblood_background_label = Label(donateblood_window, image = donateblood_background)
	donateblood_background_label.place(x=0, y=0, relheight=1, relwidth=1)

	#donateblood_window widgets
	donorsname_label = ttk.Label(donateblood_window, text = "Donor's name:",  width=18)
	donorsname_label.place(x = 100, y = 110)
	donorsname_entry = ttk.Entry(donateblood_window)
	donorsname_entry.place(x = 300, y = 110)
	bloodtype_label = ttk.Label(donateblood_window, text="Blood Type:",  width=18)
	bloodtype_label.place(x = 100, y = 150)
	bloodtype_list = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
	blood = StringVar(value='Select blood type')
	bloodtype_dropdown = ttk.OptionMenu(donateblood_window, blood, *bloodtype_list)
	bloodtype_dropdown.place(x=300,y=150)
	donate_organ_option = ttk.Label(donateblood_window, text = "Donate organs after death?")
	donate_organ_option.place(x = 100, y = 190)
	organ = StringVar(value=0)
	donate_organ_option_yes = ttk.Radiobutton(donateblood_window, text='Yes', variable=organ,value=1)
	donate_organ_option_no = ttk.Radiobutton(donateblood_window, text='No', variable=organ, value =0)
	donate_organ_option_yes.place(x = 300, y = 190)
	donate_organ_option_no.place(x = 350, y = 190)
	phone_no_label = ttk.Label(donateblood_window, text="Phone number:")
	phone_no_label.place(x = 100, y = 230)
	phone_no_entry = ttk.Entry(donateblood_window)
	phone_no_entry.place(x = 300, y = 230)
	email_label = ttk.Label(donateblood_window, text='Email Address:')
	email_label.place(x = 100, y = 270)
	email_entry = ttk.Entry(donateblood_window)
	email_entry.place(x = 300, y = 270)
	address_label = ttk.Label(donateblood_window, text='Address:')
	address_label.place(x =100, y = 310)
	address_text = ttk.Entry(donateblood_window)
	address_text.place(x = 300, y = 310)
	submit_button = ttk.Button(donateblood_window, text="Submit",  width=20, command=add_entry)
	submit_button.place(x = 180, y = 390)
	donateblood_window.mainloop()

def finddonor_function():
	global blood_selected
	global finddonor_window

	#finddonor_window configuration
	finddonor_window = Toplevel()
	finddonor_window.geometry("600x400")
	finddonor_background  = ImageTk.PhotoImage(Image.open('find_donor_background.png'))
	finddonor_window.iconbitmap("hospital-1_icon-icons.com_66068.ico")
	finddonor_label = Label(finddonor_window, image= finddonor_background)
	finddonor_label.place(x = 0, y = 0, relheight=1, relwidth=1)

	# finddonor_window widgets
	bloodtype_list2 = ['-','A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
	blood_selected = StringVar(value='Select a blood group')
	blood_dropdown = ttk.OptionMenu(finddonor_window, blood_selected, *bloodtype_list2)
	blood_dropdown.place(x=134,y=150)
	search_donor_button =ttk. Button(finddonor_window, text='Search',width=10,command=search_donar)
	search_donor_button.place(x = 123, y = 200)
	
	finddonor_window.mainloop()

# Root window widgets
adminlogin_button = ttk.Button(root, text="Admin Login", command = adminlogin_function)
adminlogin_button.place(x=250, y=160, width = 200)
donate_button = ttk.Button(root, text="Donate Blood", command = donate_function)
donate_button.place(x=250, y=195, width = 200) 
finddonor_button = ttk.Button(root, text="Find Donar", command = finddonor_function)
finddonor_button.place(x = 250, y = 230 , width = 200)
quit_button = ttk.Button(root, text="Quit", command = quit)
quit_button.place(x = 250, y = 265, width = 200)

conn.commit()
conn.close()

root.mainloop()
