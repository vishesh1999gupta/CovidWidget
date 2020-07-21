#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
import requests
import json



# In[2]:


url=requests.get("https://api.covid19india.org/data.json")
json_data=json.loads(url.content)
data=json_data.get("statewise")
def datacall(name):
    def statedata(name):
        flag=0
        for i in range(0,len(data)):
            if data[i]["state"]==name:
                total=data[i]["confirmed"]
                active=data[i]["active"]
                cured=data[i]["recovered"]
                death=data[i]["deaths"]
                flag=1
         
        if flag==1:
            message="State: "+name+"\nConfirmed: "+total+"\nActive: "+active+"\nRecovered: "+cured+"\nDeath: "+death
        else: message="Data Not Found for "+name
        return message
    
    def update_button():
        FindButton["state"]="normal"
        
    notifier=ToastNotifier()
    FindButton["state"]="disabled"
    notifier.show_toast(title="COVID-19 Update",msg=statedata(name),duration=5,icon_path="covid.ico",threaded="True")
    root.after(1000,update_button())
    return


def Indiadata():
    total=data[0]["confirmed"]
    active=data[0]["active"]
    cured=data[0]["recovered"]
    death=data[0]["deaths"]
    
    message="India Update "+"\nConfirmed: "+total+"\nActive: "+active+"\nRecovered: "+cured+"\nDeath: "+death  
    return message
    


# In[3]:


root=Tk()
root.title('Covid19 Update')
root.iconbitmap("covid.ico")
# root.geometry("400x400")


# frame=LabelFrame(root,text="Statewise Data",padx=5,pady=5)
# frame.pack(padx=10,pady=10)
#Creating a drop down menu
ll=['Maharashtra',
 'Tamil Nadu',
 'Delhi',
 'Gujarat',
 'Uttar Pradesh',
 'Rajasthan',
 'West Bengal',
 'Madhya Pradesh',
 'Haryana',
 'Karnataka',
 'Andhra Pradesh',
 'Bihar',
 'Telangana',
 'Jammu and Kashmir',
 'Assam',
 'Odisha',
 'Punjab',
 'Kerala',
 'Uttarakhand',
 'Chhattisgarh',
 'Jharkhand',
 'Tripura',
 'Ladakh',
 'Goa',
 'Himachal Pradesh',
 'Manipur',
 'Chandigarh',
 'Puducherry',
 'Nagaland',
 'Mizoram',
 'Arunachal Pradesh',
 'Sikkim',
 'Dadra and Nagar Haveli and Daman and Diu',
 'Andaman and Nicobar Islands',
 'Meghalaya',
 'Lakshadweep']
clicked=StringVar()
clicked.set("Goa")
drop=OptionMenu(root,clicked,*ll)
Statewise=Label(root,text="Statewise data")
# creating input field
# e=Entry(root,width=50,borderwidth=5)
# e.insert(0,"Enter state name")
status=Label(root,text=Indiadata(),bd=10,relief="groove")


FindButton=Button(root,text="Find",command=lambda: datacall(clicked.get()),padx=50)



QuitButton=Button(root,text="Exit",command=root.destroy,padx=50)

#Griding
Statewise.grid(row=1,columnspan=2,sticky=W+E)
drop.grid(row=2,column=0,columnspan=2,sticky=W+E)
status.grid(row=0,columnspan=2,pady=10,sticky=W+E)
QuitButton.grid(row=3,column=1)
FindButton.grid(row=3,column=0)
#shoving on to the screen


# t = threading.Thread(target=QuitButton)
# t.start()




root.mainloop()



# %%
