import pprint
from tkinter import *
import tkinter as tk
from setuptools import Command
from tkinter import Tk
from tkinter import ttk
import sys

sys.stdout = open('reg.txt', 'w')
c = '#6666ff'
m = Tk()
m.title('Student Registration Form')
m.configure(bg=c)

a=Label(m, text="DATE OF BIRTH", bg=c)
month=StringVar()
year=StringVar()
day=StringVar()
months_name = ["January",
    "February",
    "March",
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December']
day_name = [str(i) for i in range(1, 31)]
dayDrop=OptionMenu(m, day, *day_name)
day.set('Day')
dayDrop.configure(bg=c)

monDrop=OptionMenu(m, month, *months_name)
month.set('Month')
monDrop.configure(bg=c)


year_name = [str(i) for i in range(1980, 2022)]
yearDrop=OptionMenu(m, year, *year_name)
year.set('Year')
yearDrop.configure(bg=c)

genderLabel = Label(m, text='Gender', bg=c)
genderVar = IntVar()
male = Radiobutton(m, text="Male", variable=genderVar, value=1,bg=c)
female = Radiobutton(m, text="Female", variable=genderVar, value=0,bg=c)

#list for contents
names = ['First Name',
         'Last Name',
         'Email ID ',
         'Mobile Number',
         'Address',
         'City',
         'Pincode',
         'State',
         'Country']
n = len(names)+2
labels = []
entry = []
k=0
for i in range(n):
    
    if i==2:
        ip=i+4
        a.grid(row=ip, column=0)
        dayDrop.grid(row=ip, column=1,padx=5)
        monDrop.grid(row=ip, column=2)
        yearDrop.grid(row=ip, column=3)
    elif i==5:
        ip=i+4
        genderLabel.grid(row=ip, column=0)
        male.grid(row=ip,column=1)
        female.grid(row=ip, column=2)
    else:
        labels.append(Label(m, text=names[k], bg=c))
        labels[k].grid(row=i+4, column=0)
        entry.append(Entry(m,width=30, borderwidth=5))
        entry[k].grid(row=i+4, column=2, pady=5)
        k+=1

values = {}


hobies_label = Label(m, text='Hobbies', bg=c)
hobies_label.grid(row=15,column=0)
hobiesNames = ["Drawing", "Singing", "Dancing", "Sketching", "Others"]
hobiesVar = [IntVar() for  p in range(len(hobiesNames))]
hobieschecks = []
for i in range(len(hobiesNames)):
    hobieschecks.append(Checkbutton(m, text=hobiesNames[i], variable=hobiesVar[i],
                 onvalue=1, offvalue=0, bg=c))
    if i!=len(hobiesNames)-1:
        hobieschecks[i].grid(row=15, column=i+1)
    else:
        hobieschecks[i].grid(row=16, column=1)


other_hobbies = Entry(m,width=30, borderwidth=5)
other_hobbies.grid(row=16, column=2)

k=0
classNames = ['Class X', 'Class XII', 'Graduation', 'Masters']
head = ['Oualification','SL No.', 'Examination', 'Board', 'Percentage', 'Year of Passing']

l = [[None]*8 for _ in range(8)]
for i in range(6):
    l[0][i] = Label(m, text=head[k], bg=c)
    l[0][i].grid(row=17, column=k, pady=10)
    k+=1

for i in range(1, 5):
    l[i][0] = Label(m, text='', bg=c)
    l[i][0].grid(row=17+i+1,column=0)
    l[i-1][1] = Label(m, text=i, bg=c).grid(row=17+i+1, column=1)
    l[i][1] = Label(m, text=classNames[i-1], bg=c)
    l[i][1].grid(row=17+i+1, column=2)

for i in range(1, 5):
    for j in range(3, 6):
        l[i][j] = Entry(m,width=25, borderwidth=1)
        l[i][j].grid(row=17+i+1, column=j, padx=5)

# 23
courselabel = Label(m, text='Courses', bg=c).grid(row=23,column=0)
courseVar = IntVar()
courseNames = {"BCA": "1"
                , "B.Com":"2"
                , "Bsc":"3"
                , "BA":"4"}
courseVar = [IntVar() for  _ in range(len(courseNames))]
course = []
z=0
v = StringVar(m, "1")
for (cour_nam, value) in courseNames.items():
    Radiobutton(m, text=cour_nam, variable=v,
                 value=value, bg=c).grid(row=23, column=z+1)
    z+=1

def clear_text():

    day.set('Day')
    month.set('Month')
    year.set('Year')
    v.set(None)
    genderVar.set(None)
    for i in range(len(hobiesNames)):
        hobiesVar[i].set(0)
    for i in range(len(names)):
        entry[i].delete(0, END)
    for i in range(1, 5):
        for j in range(3, 6):
            l[i][j].delete(0, END)
show=["Name:", "Date of Birth:", "Email id:", "Mobile no.:", "Gender:","Address:"
        ,"City:", "Pincode:", "State:","Country:", "Hobbies:", "Qualification:"
        ,"Courses:"]
qual=["Class X: ","Class XII:","Graduation:","Masters:"]
j=0
k=0
def submit_entry():
    global j
    global k
    file = open("test.txt", "w")
    for i in range(18):
        if i==0:
            st=entry[k].get()
            file.write(show[j] + st)
            j=j+1
            k+=1
        elif i==1:
            st=entry[k].get()
            file.write(" "+st+"\n")
            k+=1
        elif i==2:
            st=day.get()
            file.write(show[j]+st)
            j=j+1
        elif i==3:
            st=month.get()
            file.write(" "+st)
        elif i==4:
            st=year.get()
            file.write(" "+st+"\n")
        elif i==5:
            st=entry[k].get()
            file.write(show[j] + st+"\n")
            j=j+1
            k+=1
        elif i==6:
            st=entry[k].get()
            file.write(show[j] + st+"\n")
            j=j+1
            k+=1
        elif i==7:
            ch=genderVar.get()
            file.write(show[j])
            if ch==1:
                file.write(" Male")
            elif ch==0:
                file.write(" Female")
                j=j+1
            file.write("\n")
        elif i==8:
            st=entry[k].get()
            file.write(show[j] + st+"\n")
            j=j+1
            k+=1
        elif i==9:
            st=entry[k].get()
            file.write(show[j] + st+"\n")
            j=j+1
            k+=1
        elif i==10:
            st=entry[k].get()
            file.write(show[j] + st+"\n")
            j=j+1
            k+=1
        elif i==11:
            st=entry[k].get()
            file.write(show[j] + st+"\n")
            j=j+1
            k+=1
        elif i==12:
            st=entry[k].get()
            file.write(show[j] + st+"\n")
            j=j+1
        elif i==13:
            file.write(show[j])
            if hobiesVar[0].get()==1:
                file.write(" Drawing ")
            if hobiesVar[1].get()==1:
                file.write(" Singing")
            if hobiesVar[2].get()==1:
                file.write(" Dancing")
            if hobiesVar[3].get()==1:
                file.write(" Sketching")
            if hobiesVar[4].get()==1:
                file.write(" "+other_hobbies.get())
            j=j+1
        elif i==14:
            st=entry[k].get()
            file.write(show[j] + st+"\n")
            j=j+1
            k+=1
            
    file.close()
Button(m, text='Submit', bg=c, command=submit_entry).grid(row=225, column=0, padx=5, pady=20)
Button(m, text='Reset', bg=c, command=clear_text).grid(row=225, column=1, padx=5)
m.mainloop()
