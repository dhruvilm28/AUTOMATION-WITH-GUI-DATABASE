from tkinter import *
from PIL import Image, ImageTk
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope=  ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
feedback=ServiceAccountCredentials.from_json_keyfile_name("feedback-5884d1f8f24d.json",scope)
client=gspread.authorize(feedback)
sheet=client.open("feed").sheet1
data=sheet.get_all_records()
print(data)
window=Tk()
window.title('Form')
window.geometry('900x800')

load = Image.open("edu2.jpg")
render = ImageTk.PhotoImage(load)
load.resize((2,2))
img = Label( image=render)
img.image = render
img.place(x=15, y=2)



def feed():
    name_info=text1.get()
    contact_info=text2.get()
    purpose_info=text3.get()
    std_info=text4.get()
    school_info=text5.get()
    loacation_info=text6.get()


    print(name_info,contact_info,purpose_info,std_info,school_info,loacation_info)
    insertRow=[name_info,contact_info,purpose_info,std_info,school_info,loacation_info]
    sheet.insert_row(insertRow,2)


heading=Label(text='ENQUIRY FORM',font=("Courier", 20),fg='red',height=3,width=20).place(x='300',y='78')

label1=Label(window,text='NAME : ',font=("verdana", 20),fg='red').place(x='40',y='200',)
text1=StringVar()
ent1=Entry(window,textvariable=text1,width='30').place(x='250',y='210')

label2=Label(window,text='CONTACT : ',font=("verdana", 20),fg='red').place(x='40',y='260',)
text2=StringVar()
ent2=Entry(window,textvariable=text2,width='30').place(x='250',y='270')


label3=Label(window,text='PURPOSE : ',font=("verdana", 20),fg='red').place(x='40',y='320',)
text3=StringVar()
ent3=Entry(window,textvariable=text3,width='30').place(x='250',y='330')
label4=Label(window,text='STD : ',font=("verdana", 20),fg='red').place(x='40',y='380',)
text4=StringVar()
ent4=Entry(window,textvariable=text4,width='30').place(x='250',y='390')


label5=Label(window,text='SCHOOL : ',font=("verdana", 20),fg='red').place(x='40',y='460',)
text5=StringVar()
ent5=Entry(window,textvariable=text5,width='30').place(x='250',y='470')

label6=Label(window,text='LOCATION : ',font=("verdana", 20),fg='red').place(x='40',y='520',)
text6=StringVar()
ent6=Entry(window,textvariable=text6,width='30').place(x='250',y='530')





button=Button(window,text='SUBMIT',font=("Courier", 20),bd='10',command=feed).place(x='270',y='580')







window.mainloop()