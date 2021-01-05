
#brightness_4
# Program to make a simple  
# login screen   
  
from instapy import InstaPy  
import tkinter as tk 
   
root=tk.Tk() 
root.title('Instagram Bot')  
# setting the windows size 
root.geometry("350x250") 
   
# declaring string variable 
# for storing name and password 
name_var=tk.StringVar() 
passw_var=tk.StringVar() 
tag_var=tk.StringVar()   
com_var=tk.StringVar()     
# defining a function that will 
# get the name and password and  
# print them on the screen 
def submit(): 
  
    #name=name_entry.get() 
    #password=ptag_varassw_var.get() 
   
       session =InstaPy(username = name_entry.get()  ,password = passw_var.get() )
       session.login()

       session.set_relationship_bounds(enabled = True,max_followers = 300)

       session.set_do_follow(True,percentage=100,times=5)
       session.like_by_tags([tag_entry.get()],amount = 5)

       session.set_do_comment(enabled=True, percentage=25)

       session.set_comments([com_entry.get()])
      
      
# creating a label for  
# name using widget Label 
name_label = tk.Label(root, text = 'Username', 
                      font=('calibre', 
                            12, 'bold')) 
   
# creating a entry for input 
# name using widget Entry 
tag_entry = tk.Entry(root, 
                      textvariable = tag_var,
                      font = ('calibre',12,'normal')) 
   
# creating a label for password 
tag_label = tk.Label(root, text = 'tag', 
                      font=('calibre', 
                            12, 'bold')) 
   

name_entry = tk.Entry(root, 
                      textvariable = name_var,
                      font = ('calibre',12,'normal')) 
passw_label = tk.Label(root, 
                       text = 'Password', 
                       font = ('calibre',12,'bold')) 
   

com_entry = tk.Entry(root, 
                      textvariable = com_var,
                      font = ('calibre',12,'normal')) 
com_label = tk.Label(root, 
                       text = 'Comment Text', 
                       font = ('calibre',12,'bold'))  
empty_label = tk.Label(root, 
                       text = '', 
                       font = ('calibre',12,'bold'))  

# creating a entry for password 
passw_entry=tk.Entry(root, 
                     textvariable = passw_var, 
                     font = ('calibre',12,'normal'), 
                     show = '*') 
   
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(root,text = 'Submit', 
                  command = submit) 



   
name_label.grid(row=0,column=4) 
name_entry.grid(row=0,column=5) 
passw_label.grid(row=2,column=4) 
passw_entry.grid(row=2,column=5) 
tag_label.grid(row=4,column=4) 
tag_entry.grid(row=4,column=5) 
com_label.grid(row=6,column=4) 
com_entry.grid(row=6,column=5) 
empty_label.grid(row=7,column=5)
empty_label.grid(row=8,column=5)
sub_btn.grid(row=12,column=5) 
   
# performing an infinite loop  
# for the window to display 
root.mainloop() 