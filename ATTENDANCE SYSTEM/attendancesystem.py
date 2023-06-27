# GROUP 12 - CLARIN, PARAGOSO, REPE
from tkinter import *
import customtkinter
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = customtkinter.CTk()
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
win.title("Student Attendance System")
win.geometry("1350x760+0+0")
win.resizable(False, False)

def homecom():
#**************************************************************** HOME ****************************************************************#
    homeframe = tk.Frame(mainframe,width=1150,height=810,background="gray1")
    homeframe.place(x=65,y=100)
# MENU BUTTONS
    homebtn = customtkinter.CTkButton(mainframe,text="HOME",text_color="white",font=("Tahoma",15),width=100,height=35,fg_color="gray5",hover_color="gray13",command=homecom)
    homebtn.place(x=50,y=30)
    eventbtn = customtkinter.CTkButton(mainframe,text="EVENTS",text_color="white",font=("Tahoma",15),width=100,height=35,fg_color="gray5",hover_color="gray13",command=eventcom)
    eventbtn.place(x=170,y=30)
    studentbtn = customtkinter.CTkButton(mainframe,text="STUDENTS",text_color="white",font=("Tahoma",15),width=100,height=35,fg_color="gray5",hover_color="gray13",command=studentcom)
    studentbtn.place(x=290,y=30)
    coursebtn = customtkinter.CTkButton(mainframe,text="COURSE",text_color="white",font=("Tahoma",15),width=100,height=35,fg_color="gray5",hover_color="gray13",command=coursecom)
    coursebtn.place(x=410,y=30)
# DISPLAY LABELS
    label2 =customtkinter.CTkLabel(mainframe,text="Embrace the Digital Wave, Track Your Event Journey Today!",text_color="papaya whip",font=("Helvetica",30,"bold"))
    label2.place(x=55,y=120)
    label3 =customtkinter.CTkLabel(mainframe,text="College of Computer Studies Attendance System",text_color="white",font=("Helvetica",25,"bold"))
    label3.place(x=55,y=170)

def tablestyle():
    style = ttk.Style()
    style.configure("Treeview",background="light yellow2",fg="lightgoldenrod4",rowheight=35,fieldbackground="lightgoldenrod4")
    style.configure("Treeview.Heading", font=('Calibri', 15,'bold'),height=50) 
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 14)) 
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 
    style.map("Treeview",background=[("selected","lightgoldenrod4")])

def eventcom():
#**************************************************************** ADD EVENT TABVIEW ****************************************************************#
    eventframe = tk.Frame(mainframe,width=1150,height=810,background="gray1")
    eventframe.place(x=65,y=100)
    tabview = customtkinter.CTkTabview(master=eventframe,width=900,height=555)
    tabview.place(x=5,y=25)
    tabview.configure(text_color="black",fg_color="light yellow",segmented_button_fg_color="lightgoldenrod3",segmented_button_selected_color="light yellow",segmented_button_unselected_color="lightgoldenrod3",segmented_button_unselected_hover_color="light yellow",segmented_button_selected_hover_color="light yellow")
    tabview.add("ADD EVENT")  
    tabview.add("EVENTS LIST") 
    tabview.set("EVENTS LIST") 
# LABELS
    elabel1 =customtkinter.CTkLabel(tabview.tab("ADD EVENT"),text="EVENT INFORMATION:",text_color="black",font=("Helvetica",16,"bold"))
    elabel1.place(x=45,y=45)
    elabel2 =customtkinter.CTkLabel(tabview.tab("ADD EVENT"),text="EVENT ID:",text_color="black",font=("Helvetica",15))
    elabel2.place(x=45,y=120)
    elabel3 =customtkinter.CTkLabel(tabview.tab("ADD EVENT"),text="EVENT NAME:",text_color="black",font=("Helvetica",15))
    elabel3.place(x=45,y=205)
    elabel3 =customtkinter.CTkLabel(tabview.tab("ADD EVENT"),text="START DATE:",text_color="black",font=("Helvetica",15))
    elabel3.place(x=45,y=295)
    elabel4 =customtkinter.CTkLabel(tabview.tab("ADD EVENT"),text="SCHOOL YEAR:",text_color="black",font=("Helvetica",15))
    elabel4.place(x=535,y=120)
    elabel5 =customtkinter.CTkLabel(tabview.tab("ADD EVENT"),text="END DATE:",text_color="black",font=("Helvetica",15))
    elabel5.place(x=45,y=380)
    elabel6 =customtkinter.CTkLabel(tabview.tab("ADD EVENT"),text="SEMESTER:",text_color="black",font=("Helvetica",15))
    elabel6.place(x=535,y=205)
# VARIABLES
    monthOM1_var = customtkinter.StringVar(value="Month")
    dayOM1_var = customtkinter.StringVar(value="Day")
    yearOM1_var = customtkinter.StringVar(value="Year")
    monthOM2_var = customtkinter.StringVar(value="Month")  
    dayOM1_var = customtkinter.StringVar(value="Day")
    yearOM2_var = customtkinter.StringVar(value="Year")
    schoolyearOM_var = customtkinter.StringVar(value="Select")
    semesterOM_var = customtkinter.StringVar(value="Select")
# ENTRIES
    eIDentry = customtkinter.CTkEntry(tabview.tab("ADD EVENT"),placeholder_text="e.g. DEVCON",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=295,height=35)
    eIDentry.place(x=180,y=120)
    eNameentry = customtkinter.CTkEntry(tabview.tab("ADD EVENT"),placeholder_text="e.g. DEVCON SUMMIT",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=295,height=35)
    eNameentry.place(x=180,y=205)
    monthOM1 = customtkinter.CTkOptionMenu(tabview.tab("ADD EVENT"),variable=monthOM1_var,values=["01","02","03","04","05","06","07","08","09","10","11","12"],text_color="black",dynamic_resizing=TRUE,width=90,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    monthOM1.place(x=180,y=295)
    dayOM1 = customtkinter.CTkOptionMenu(tabview.tab("ADD EVENT"),variable=dayOM1_var,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],text_color="black",dynamic_resizing=FALSE,width=75,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    dayOM1.place(x=295,y=295)
    yearOM1 = customtkinter.CTkOptionMenu(tabview.tab("ADD EVENT"),variable=yearOM1_var,values=["2023","2024","2025","2026","2027","2028","2029","2030"],text_color="black",dynamic_resizing=TRUE,width=85,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    yearOM1.place(x=390,y=295)
    monthOM2 = customtkinter.CTkOptionMenu(tabview.tab("ADD EVENT"),variable=monthOM2_var,values=["01","02","03","04","05","06","07","08","09","10","11","12"],text_color="black",dynamic_resizing=TRUE,width=90,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    monthOM2.place(x=180,y=380)
    dayOM2 = customtkinter.CTkOptionMenu(tabview.tab("ADD EVENT"),variable=dayOM1_var,values=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"],text_color="black",dynamic_resizing=FALSE,width=75,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    dayOM2.place(x=295,y=380)
    yearOM2 = customtkinter.CTkOptionMenu(tabview.tab("ADD EVENT"),variable=yearOM2_var,values=["2022","2023","2024","2025","2026","2027","2028","2029","2030"],text_color="black",dynamic_resizing=TRUE,width=85,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    yearOM2.place(x=390,y=380)
    schoolyearOM = customtkinter.CTkOptionMenu(tabview.tab("ADD EVENT"),variable=schoolyearOM_var,values=["2022-2023","2023-2024","2024-2025","2025-2026","2026-2027","2027-2028","2028-2029","2029-2030","2030-2031"],text_color="black",dynamic_resizing=FALSE,width=160,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    schoolyearOM.place(x=680,y=120)
    semesterOM = customtkinter.CTkOptionMenu(tabview.tab("ADD EVENT"),variable=semesterOM_var,values=["1ST SEMESTER","2ND SEMESTER"],text_color="black",dynamic_resizing=TRUE,width=160,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    semesterOM.place(x=680,y=205)
# SAVE BUTTON
    esavebtn = customtkinter.CTkButton(tabview.tab("ADD EVENT"),text="ADD EVENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover=True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
    esavebtn.place(x=640,y=295)

#**************************************************************** EVENTS LIST TABVIEW ****************************************************************#
    elabel7 =customtkinter.CTkLabel(tabview.tab("EVENTS LIST"),text="EVENTS LIST:",text_color="black",font=("Helvetica",16,"bold"))
    elabel7.place(x=50,y=45)
# SEARCH
    elabel8 =customtkinter.CTkLabel(tabview.tab("EVENTS LIST"),text="SEARCH:",text_color="black",font=("Helvetica",13))
    elabel8.place(x=610,y=45)
    eIDentry = customtkinter.CTkEntry(tabview.tab("EVENTS LIST"),placeholder_text="e.g. DEVCON",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
    eIDentry.place(x=680,y=45)
# TABLE
    tablestyle()
    table_frame = tk.Frame(tabview.tab("EVENTS LIST"),bg="white")
    table_frame.place(x=55,y=125,width=1000,height=360)
    y_scroll = customtkinter.CTkScrollbar(table_frame,orientation=VERTICAL,button_color="lightgoldenrod4",button_hover_color="lightgoldenrod3")
    y_scroll.pack(side=RIGHT,fill=Y)
    etable = ttk.Treeview(table_frame,yscrollcommand=y_scroll.set)
    y_scroll.configure(command=etable.yview)
    etable["columns"] = ("EVENT ID","EVENT NAME","START DATE","END DATE","SCHOOL YEAR","SEMESTER")
    etable.column("#0", width=0, stretch=NO)  
    etable.column("EVENT ID", width=100,anchor=CENTER)
    etable.column("EVENT NAME", width=200,anchor=CENTER)
    etable.column("START DATE", width=150,anchor=CENTER)
    etable.column("END DATE", width=150,anchor=CENTER)
    etable.column("SCHOOL YEAR", width=150,anchor=CENTER)
    etable.column("SEMESTER", width=150,anchor=CENTER)
    etable.heading("EVENT ID", text="EVENT ID")
    etable.heading("EVENT NAME", text="EVENT NAME")
    etable.heading("START DATE", text="START DATE")
    etable.heading("END DATE", text="END DATE")
    etable.heading("SCHOOL YEAR", text="SCHOOL YEAR")
    etable.heading("SEMESTER", text="SEMESTER")
    etable.insert("", tk.END, text="1", values=("DEVCON","DEVCON SUMMIT", "JUNE 26,2023","June 26,2023","2023-2024","1ST SEMESTER"))
    etable.insert("", tk.END, text="2", values=("PALAKASAN","FOUNDATION DAY", "JUNE 26,2023","June 27,2023","2023-2024","1ST SEMESTER"))
    etable.pack(fill=BOTH,expand=True)
# BUTTONS
    eviewbtn = customtkinter.CTkButton(tabview.tab("EVENTS LIST"),text="VIEW ATTENDANCE",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
    eviewbtn.place(x=45,y=405)
    eeditbtn = customtkinter.CTkButton(tabview.tab("EVENTS LIST"),text="EDIT EVENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
    eeditbtn.place(x=625,y=405)
    edeletebtn = customtkinter.CTkButton(tabview.tab("EVENTS LIST"),text="delete event",font=("Helvetica",14),text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=100,height=35)
    edeletebtn.place(x=745,y=405)

def studentcom():
#**************************************************************** ADD STUDENT TABVIEW ****************************************************************#
    studentframe = tk.Frame(mainframe,width=1150,height=810,background="gray1")
    studentframe.place(x=65,y=100)
    tabview = customtkinter.CTkTabview(master=studentframe,width=900,height=560)
    tabview.place(x=5,y=25)
    tabview.configure(text_color="black",fg_color="light yellow",segmented_button_fg_color="lightgoldenrod3",segmented_button_selected_color="light yellow",segmented_button_unselected_color="lightgoldenrod3",segmented_button_unselected_hover_color="light yellow",segmented_button_selected_hover_color="light yellow")
    tabview.add("ADD STUDENT")  
    tabview.add("STUDENTS LIST") 
    tabview.set("STUDENTS LIST") 
# LABELS
    slabel1 =customtkinter.CTkLabel(tabview.tab("ADD STUDENT"),text="STUDENT INFORMATION:",text_color="black",font=("Helvetica",16,"bold"))
    slabel1.place(x=45,y=45)
    slabel2 =customtkinter.CTkLabel(tabview.tab("ADD STUDENT"),text="LAST NAME:",text_color="black",font=("Helvetica",15))
    slabel2.place(x=45,y=120)
    slabel3 =customtkinter.CTkLabel(tabview.tab("ADD STUDENT"),text="FIRST NAME:",text_color="black",font=("Helvetica",15))
    slabel3.place(x=45,y=205)
    slabel3 =customtkinter.CTkLabel(tabview.tab("ADD STUDENT"),text="MIDDLE NAME:",text_color="black",font=("Helvetica",15))
    slabel3.place(x=45,y=295)
    slabel4 =customtkinter.CTkLabel(tabview.tab("ADD STUDENT"),text="STUDENT ID:",text_color="black",font=("Helvetica",15))
    slabel4.place(x=480,y=120)
    slabel5 =customtkinter.CTkLabel(tabview.tab("ADD STUDENT"),text="COURSE:",text_color="black",font=("Helvetica",15))
    slabel5.place(x=480,y=205)
    slabel6 =customtkinter.CTkLabel(tabview.tab("ADD STUDENT"),text="YEAR LEVEL:",text_color="black",font=("Helvetica",15))
    slabel6.place(x=480,y=295)
# VARIABLES
    scourse_var = customtkinter.StringVar(value="Select")
    syearlevel_var = customtkinter.StringVar(value="Select")
# ENTRIES
    slNameent = customtkinter.CTkEntry(tabview.tab("ADD STUDENT"),placeholder_text="e.g. PARAGOSO",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
    slNameent.place(x=180,y=120)
    sfNameent = customtkinter.CTkEntry(tabview.tab("ADD STUDENT"),placeholder_text="e.g. EDA GRACE",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
    sfNameent.place(x=180,y=205)
    smNameent = customtkinter.CTkEntry(tabview.tab("ADD STUDENT"),placeholder_text="e.g. JUTBA",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
    smNameent.place(x=180,y=295)
    sIDent = customtkinter.CTkEntry(tabview.tab("ADD STUDENT"),placeholder_text="e.g. 2021-1574",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
    sIDent.place(x=610,y=120)
    scourseOM = customtkinter.CTkOptionMenu(tabview.tab("ADD STUDENT"),variable=scourse_var,values=["BSCS","BSIT","BSCA","BSIS"],text_color="black",dynamic_resizing=TRUE,width=230,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    scourseOM.place(x=610,y=205)
    syearlevelOM = customtkinter.CTkOptionMenu(tabview.tab("ADD STUDENT"),variable=syearlevel_var,values=["1ST YEAR","2ND YEAR","3RD YEAR","4TH YEAR"],text_color="black",dynamic_resizing=TRUE,width=230,fg_color="lightgoldenrod2",button_color="lightgoldenrod4",button_hover_color="lightgoldenrod4",dropdown_fg_color="lightgoldenrod2",dropdown_hover_color="lightgoldenrod3")
    syearlevelOM.place(x=610,y=295)
# SAVE BUTTON
    ssavebtn = customtkinter.CTkButton(tabview.tab("ADD STUDENT"),text="ADD STUDENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover=True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
    ssavebtn.place(x=400,y=390)

#**************************************************************** STUDENTS LIST TABVIEW ****************************************************************#
    elabel7 =customtkinter.CTkLabel(tabview.tab("STUDENTS LIST"),text="STUDENTS LIST:",text_color="black",font=("Helvetica",16,"bold"))
    elabel7.place(x=45,y=45)
# SEARCH
    elabel8 =customtkinter.CTkLabel(tabview.tab("STUDENTS LIST"),text="SEARCH:",text_color="black",font=("Helvetica",13))
    elabel8.place(x=610,y=45)
    eIDentry = customtkinter.CTkEntry(tabview.tab("STUDENTS LIST"),placeholder_text="e.g. 2021-1574",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
    eIDentry.place(x=680,y=45)
# TABLE
    tablestyle()
    table_frame = tk.Frame(tabview.tab("STUDENTS LIST"),bg="white")
    table_frame.place(x=55,y=125,width=1000,height=360)
    y_scroll = customtkinter.CTkScrollbar(table_frame,orientation=VERTICAL,button_color="lightgoldenrod4",button_hover_color="lightgoldenrod3")
    y_scroll.pack(side=RIGHT,fill=Y)
    stable = ttk.Treeview(table_frame,yscrollcommand=y_scroll.set)
    y_scroll.configure(command=stable.yview)
    stable["columns"] = ("STUDENT ID","LAST NAME","FIRST NAME","MIDDLE NAME","COURSE","YEAR LEVEL")
    stable.column("#0", width=0, stretch=NO)  
    stable.column("STUDENT ID", width=120,anchor=CENTER)
    stable.column("LAST NAME", width=200,anchor=CENTER)
    stable.column("FIRST NAME", width=200,anchor=CENTER)
    stable.column("MIDDLE NAME", width=200,anchor=CENTER)
    stable.column("COURSE", width=130,anchor=CENTER)
    stable.column("YEAR LEVEL", width=130,anchor=CENTER)
    stable.heading("STUDENT ID", text="STUDENT ID")
    stable.heading("LAST NAME", text="LAST NAME")
    stable.heading("FIRST NAME", text="FIRST NAME")
    stable.heading("MIDDLE NAME", text="MIDDLE NAME")
    stable.heading("COURSE", text="COURSE")
    stable.heading("YEAR LEVEL", text="YEAR LEVEL")
    stable.insert("", tk.END, text="1", values=("2021-1574","PARAGOSO", "EDA GRACE","JUTBA","BSCS","2ND YEAR"))
    stable.insert("", tk.END, text="2", values=("2021-0622","SAYSON", "NANCY","MAHINAY","BSCS","2ND YEAR"))
    stable.pack(fill=BOTH,expand=True)
# BUTTONS
    eeditbtn = customtkinter.CTkButton(tabview.tab("STUDENTS LIST"),text="EDIT STUDENT",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
    eeditbtn.place(x=585,y=405)
    edeletebtn = customtkinter.CTkButton(tabview.tab("STUDENTS LIST"),text="delete student",font=("Helvetica",14),text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=100,height=35)
    edeletebtn.place(x=730,y=405)

def coursecom():
#**************************************************************** ADD COURSE TABVIEW ****************************************************************#
    courseframe = tk.Frame(mainframe,width=1150,height=810,background="gray1")
    courseframe.place(x=65,y=100)
    tabview = customtkinter.CTkTabview(master=courseframe,width=900,height=500)
    tabview.place(x=5,y=25)
    tabview.configure(text_color="black",fg_color="light yellow",segmented_button_fg_color="lightgoldenrod3",segmented_button_selected_color="light yellow",segmented_button_unselected_color="lightgoldenrod3",segmented_button_unselected_hover_color="light yellow",segmented_button_selected_hover_color="light yellow")
    tabview.add("ADD COURSE")  
    tabview.add("COURSES LIST") 
    tabview.set("COURSES LIST") 
# LABELS
    clabel1 =customtkinter.CTkLabel(tabview.tab("ADD COURSE") ,text="COURSE INFORMATON:",text_color="black",font=("Helvetica",16,"bold"))
    clabel1.place(x=45,y=45)
    clabel2 =customtkinter.CTkLabel(tabview.tab("ADD COURSE") ,text="COURSE CODE:",text_color="black",font=("Helvetica",15))
    clabel2.place(x=45,y=120)
    clabel3 =customtkinter.CTkLabel(tabview.tab("ADD COURSE") ,text="COURSE NAME:",text_color="black",font=("Helvetica",15))
    clabel3.place(x=45,y=190)
# ENTRIES
    ccodeent = customtkinter.CTkEntry(tabview.tab("ADD COURSE"),placeholder_text="e.g. BSCS",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=230,height=35)
    ccodeent.place(x=180,y=120)
    cnameent = customtkinter.CTkEntry(tabview.tab("ADD COURSE"),placeholder_text="e.g. BACHELOR OF SCIENCE IN COMPUTER SCIENCE",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=660,height=35)
    cnameent.place(x=180,y=190)
# SAVE BUTTON
    ssavebtn = customtkinter.CTkButton(tabview.tab("ADD COURSE"),text="ADD COURSE",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover=True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
    ssavebtn.place(x=400,y=260)

#**************************************************************** COURSES LIST TABVIEW ****************************************************************#
    elabel7 =customtkinter.CTkLabel(tabview.tab("COURSES LIST"),text="COURSES LIST:",text_color="black",font=("Helvetica",16,"bold"))
    elabel7.place(x=45,y=45)
# SEARCH
    elabel8 =customtkinter.CTkLabel(tabview.tab("COURSES LIST"),text="SEARCH:",text_color="black",font=("Helvetica",13))
    elabel8.place(x=610,y=45)
    eIDentry = customtkinter.CTkEntry(tabview.tab("COURSES LIST"),placeholder_text="e.g. BSCS",placeholder_text_color="lightgoldenrod4",border_color="lightgoldenrod2",fg_color="lightgoldenrod2",width=160,height=35)
    eIDentry.place(x=680,y=45)
# TABLE
    tablestyle()
    table_frame = tk.Frame(tabview.tab("COURSES LIST"),bg="white")
    table_frame.place(x=55,y=120,width=1000,height=290)
    y_scroll = customtkinter.CTkScrollbar(table_frame,orientation=VERTICAL,button_color="lightgoldenrod4",button_hover_color="lightgoldenrod3")
    y_scroll.pack(side=RIGHT,fill=Y)
    ctable = ttk.Treeview(table_frame,yscrollcommand=y_scroll.set)
    y_scroll.configure(command=ctable.yview)
    ctable["columns"] = ("COURSE CODE","COURSE NAME")
    ctable.column("#0", width=0, stretch=NO)  
    ctable.column("COURSE CODE", width=50,anchor=CENTER)
    ctable.column("COURSE NAME", width=400,anchor=CENTER)
    ctable.heading("COURSE CODE", text="COURSE CODE")
    ctable.heading("COURSE NAME", text="COURSE NAME")
    ctable.insert("", tk.END, text="1", values=("BSCS","BACHELOR OF SCIENCE IN COMPUTER SCIENCE"))
    ctable.insert("", tk.END, text="2", values=("BSCA","BACHELOR OF SCIENCE IN COMPUTER APPLICATIONS"))
    ctable.insert("", tk.END, text="3", values=("BSIS","BACHELOR OF SCIENCE IN INFORMATION SYSTEM"))
    ctable.insert("", tk.END, text="4", values=("BSIT","BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY"))
    ctable.pack(fill=BOTH,expand=True)
# BUTTONS
    eeditbtn = customtkinter.CTkButton(tabview.tab("COURSES LIST"),text="EDIT COURSE",font=("Helvetica",14),text_color="black",fg_color="lightgoldenrod2",border_width=2,hover= True,hover_color= "lightgoldenrod1",corner_radius=10,border_color= "lightgoldenrod2",width=100,height=35)
    eeditbtn.place(x=595,y=345)
    edeletebtn = customtkinter.CTkButton(tabview.tab("COURSES LIST"),text="delete course",font=("Helvetica",14),text_color="white",fg_color="red2",border_width=2,hover= True,hover_color= "red",corner_radius=10,border_color= "red2",width=100,height=35)
    edeletebtn.place(x=730,y=345)

#**************************************************************** MAIN SCREEN ****************************************************************#
# BACKGROUND 
mainframe = tk.Frame(win,width=1000,height=1000,bg="gray1")
mainframe.pack(fill="both")
bg_img = customtkinter.CTkImage(light_image=Image.open("C:\\Users\\User\\Desktop\\ATTENDANCE SYSTEM\\Wolf16.jpg"),size=(500,800))
label1 = customtkinter.CTkLabel(master=mainframe,text= "",image=bg_img,anchor='e')
label1.pack(fill="x")
homecom()

win.mainloop()
