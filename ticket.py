from tkinter import*
import tkinter
from tkcalendar import Calendar
import mysql.connector
import random

h_host=input(enter("Enter your mysql host name: "))
u_user=input(enter("Enter your mysql user name: "))
p_pass=input(enter("Enter your mysql password: "))


mydb=mysql.connector.connect(host=h_host,
                             user=u-user,
                             password=p_pass) #localhost root
print("Accessed your mysql")

mycursor=mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Railway")
mydb.database = "Railway"

cursor.execute(
  "CREATE TABLE IF NOT EXISTS Passengers ( \
    SNo INT AUTO_INCREMENT PRIMARY KEY,\
    Coach VARCHAR(100),\
    Cabin VARCHAR(100),\
    SeatNo VARCHAR(100),\
    Name VARCHAR(100),\
    Gender VARCHAR(100),\
    Age CHAR(3),\
    JourneyFrom VARCHAR(100),\
    JourneyUpto VARCHAR(100),\
    BoardingFrom VARCHAR(100),\
    ReservationUpto VARCHAR(100),\
    PNR VARCHAR(100),\
    TicketType VARCHAR(200))")
    

root=Tk()
root.geometry("1100x700")
root.title("Registration Form")
root.configure(bg="pink")
Label(text="RAILWAY BOOKING",bg="black",fg="pink",font="Algerian 17 bold" ,padx=12,pady=12,relief="sunken",width=30).grid(row=0,column=1,columnspan=13)


labelframe=LabelFrame(root,text="Date and time",bg="pink",width=15,height=30)
labelframe.grid(row=1,column=3,padx=20,pady=20,rowspan=10,columnspan=10)

#Label(root,text="Welcome to Chiku railways",font="Algerian 20 ",fg="blue",bg="pink",relief="groove",width=28,padx=8,pady=8).pack()
#Label(root,text="expexted date of departure",bg="pink",fg="black",font="Helvetica 16").grid()

#la=LabelFrame(root,text="Ticket Counter",bg="pink",width=20,height=40)
#la.grid(row=1,column=0,padx=35,pady=35,rowspan=9,columnspan=5)

tkc=Calendar(labelframe,selectmode="day",year=2023,month=1,date=1)
tkc.grid(row=2,column=3,rowspan=5)

def fetch_date():
    date.config(text="Selected date is"+tkc.get_date())

def selection():
    global classv
    Label(root,text="selected "+str(Classvalue.get())).grid(row=4,column=0)
    if Classvalue.get()==1:
        ticket=Label(root,text="Ticket Type",bg="pink",fg="black",font="aharoni 12 underline").grid(row=6,column=0)
        ticketvalue=IntVar()
        scrollbar3=Scrollbar(root)
        scrollbar3.grid(row=4,rowspan=5,column=1,ipady=8,sticky="e")
        mylist=Listbox(root,yscrollcommand=scrollbar3.set,width=30,height=2)
        mylist.insert(END,"EC","1AC","2AC","3AC","FC","CC","SL","2S",)
        mylist.grid(row=4,rowspan=5,column=1)
        scrollbar3.config(command=mylist.yview)
        classv="AC "
    else:
        classv="Non AC"
       
cabins=('Upper Birth','Lower Birth','Side Upper','Side Lower')
rc=random.choice(cabins)
rc1=random.choice(cabins)
rc2=random.choice(cabins)
rc3=random.choice(cabins)
       
coaches=["EC","1AC","2AC","3AC","FC","CC","SL","2S"]                       
gender=['male','female']

ri=random.randint(1,12)

ro=random.randint(30,80)
ro1=random.randint(30,80)
ro2=random.randint(30,80)
ro3=random.randint(30,80)
ro4=random.randint(30,80)
ro5=random.randint(30,80)
rs=int(ro)

def cartoon():
    rowcount=0
    num=int(numbervalue.get())
    if num>0:
        sq1="INSERT INTO passengers(Coach,Cabin,SeatNo,Name,Gender,Age,JourneyFrom,JourneyUpto,BoardingFrom,ReservationUpto,PNR,TicketType)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=((str(coache)),str(rc),ro,value.get(),gendervalue.get().title(),agevalue.get(),str(dict1.get(Boardingvalue.get().lower())),str(dict1.get(reservevalue.get().lower())),o,
              p,str(rbb.get()),classv)
        mycursor.execute(sq1,val)
        mydb.commit()
        rowcount+=1
        
    if num>1:
        sq1="INSERT INTO passengers(Coach,Cabin,SeatNo,Name,Gender,Age,JourneyFrom,JourneyUpto,BoardingFrom,ReservationUpto,PNR,TicketType)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=((str(coache)),str(rc1),ro1,value1.get(),gendervalue1.get().title(),agevalue1.get(),str(dict1.get(Boardingvalue.get().lower())),str(dict1.get(reservevalue.get().lower())),o,
              p,str(rbb.get()),classv)
        mycursor.execute(sq1,val)
        mydb.commit()
        rowcount+=1
        
    if num>2:
        sq1="INSERT INTO passengers(Coach,Cabin,SeatNo,Name,Gender,Age,JourneyFrom,JourneyUpto,BoardingFrom,ReservationUpto,PNR,TicketType)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=((str(coache)),str(rc2),ro2,value2.get(),gendervalue2.get().title(),agevalue2.get(),str(dict1.get(Boardingvalue.get().lower())),str(dict1.get(reservevalue.get().lower())),o,
              p,str(rbb.get()),classv)
        mycursor.execute(sq1,val)
        mydb.commit()
        rowcount+=1
       
    if num>3:
        sq1="INSERT INTO passengers(Coach,Cabin,SeatNo,Name,Gender,Age,JourneyFrom,JourneyUpto,BoardingFrom,ReservationUpto,PNR,TicketType)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=((str(coache)),str(rc3),ro3,value3.get(),gendervalue3.get().title(),agevalue3.get(),str(dict1.get(Boardingvalue.get().lower())),str(dict1.get(reservevalue.get().lower())),o,
              p,str(rbb.get()),dk,classv)
        mycursor.execute(sq1,val)
        mydb.commit()
        rowcount+=1
    dk='kid'   
    n=int(number1value.get())
    if n>0:
        sq1="INSERT INTO passengers(Coach,Name,Gender,Age,JourneyFrom,JourneyUpto,BoardingFrom,ReservationUpto,PNR,TicketType)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=((str(coache)),value10.get(),gendervalue10.get().title(),agevalue10.get(),str(dict1.get(Boardingvalue.get().lower())),str(dict1.get(reservevalue.get().lower())),o,
              p,str(rbb.get()),classv)
        mycursor.execute(sq1,val)
        mydb.commit()
        rowcount+=1
       
    if n>1:
        sq1="INSERT INTO passengers(Coach,Name,Gender,Age,JourneyFrom,JourneyUpto,BoardingFrom,ReservationUpto,PNR,TicketType)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=((str(coache)),value20.get(),gendervalue20.get().title(),agevalue20.get(),str(dict1.get(Boardingvalue.get().lower())),str(dict1.get(reservevalue.get().lower())),o,
              p,str(rbb.get()),classv)
        mycursor.execute(sq1,val)
        mydb.commit()
        rowcount+=1
        
    if n>2:
        sq1="INSERT INTO passengers(Coach,Name,Gender,Age,JourneyFrom,JourneyUpto,BoardingFrom,ReservationUpto,PNR,TicketType)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=((str(coache)),value20.get(),gendervalue20.get().title(),agevalue20.get(),str(dict1.get(Boardingvalue.get().lower())),str(dict1.get(reservevalue.get().lower())),o,
              p,str(rbb.get()),classv)
        mycursor.execute(sq1,val)
        mydb.commit()
        rowcount+=1
    print(rowcount,"record inserted")

def coac():
    global coache
    if str(coachval.get()) in coaches:
            if str(coachval.get())== 'EC':
                x='E'
            elif str(coachval.get())=='1AC':
                x='H'
            elif str(coachval.get())=='2AC':
                x='A'
            elif str(coachval.get())=='3AC':
                x='B'
            elif str(coachval.get())=='FC':
                x='FC'
            elif str(coachval.get())=='CC':
                x='C'
            elif str(coachval.get())=='SL':
                x='S'
            elif str(coachval.get())=='2S':
                x='SC'
            coache=str(x)+str(ri)
            Label(new,text="Available seats in "+str(coache) ,fg="white",bg="pink",relief="groove").grid(row=3,column=1,sticky="n")
    
    else:
            print("please select and type coach value from this list")
            for i in coaches:
                print (i)
                



            
list1=['howrah junction' ,
       'sealdah railway station',
       'chhatrapati shivaji terminus',
       'new delhi railway station',
       'chennai central railway station',
       'kanpur central station',
       'allahabad junction',
       'patna junction',
       'ahmedabad junction',
       'vijayawada junction',
       'bangalore city railway station',
       'lucknow charbagh railway station',
       'varanasi junction',
       'mughalsarai junction',
       'kalyan junction',
       'balasore railway station',
       'nagpur railway station',
       'cuttack junction station',
       'jaisalmar railway station',
       'visakhapatnam railway station',
       'ghum railway station',
       'bilaspur railway junction',
       'dudhsagar railway station']

dict1={'howrah junction':'West Bengal' ,
       'sealdah railway station':'West Bengal',
       'chhatrapati shivaji terminus':'Maharashtra',
       'new delhi railway station':'New Delhi',
       'chennai central railway station':'Tamil Nadu',
       'kanpur central station':'Uttar Pradesh',
       'allahabad junction':'Uttar Pradesh',
       'patna junction':'Bihar',
       'ahmedabad junction':'Gujarat',
       'vijayawada junction':'Andhra Pradesh',
       'bangalore city railway station':'Karnataka',
       'lucknow charbagh railway station':'Uttar Pradesh',
       'varanasi junction':'Uttar Pradesh',
       'mughalsarai junction':'Uttar Pradesh',
       'kalyan junction':'Maharashtra',
       'balasore railway station':'Odisha',
       'nagpur railway station':'Maharashtra',
       'cuttack junction station':'Odisha',
       'jaisalmar railway station':'Rajasthan',
       'visakhapatnam railway station':'Andhra Pradesh',
       'ghum railway station':'West Bengal',
       'bilaspur railway junction':'Chhatisgarh',
       'dudhsagar railway station':'Goa'}
PNR=[38801,12905,38703,18013,18011,12343,12377]
ng={}
ng1={}
ng2={}
ng3={}

def hungama():
    now=Toplevel(root)
    now.title("Ticket Counter")
    now.geometry("1100x700")
    Label(now,text="soft copy").grid(row=1,column=0)
    now.configure(bg="purple")
    Label(now,text="Tickets Booked Sucessfully ",font="Algerian 20 ",fg="white",bg="black",relief="groove",width=28,padx=8,pady=8).grid(row=0,column=1,columnspan=5)
    if num>0:
        lo=LabelFrame(now,text='details',bg='purple',fg='yellow',width=28)
        lo.grid(sticky='w')
        Label(lo,text='Name: '+str(value.get().title())+'  Gender: '+str(gendervalue.get().title())+' Age: '+str(agevalue.get()),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=3,column=0)  
        Label(lo,text="BoardingFrom: "+str(Boardingvalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=4,column=0)
        Label(lo,text="ReservedUpto: "+str(reservevalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=5,column=0)
        Label(lo,text="Coach: "+str(coache),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=6,column=0)
        Label(lo,text='Cabin: '+str(rc),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=7,column=0)
        Label(lo,text='Seatno: '+str(ro),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=8,column=0)
    if num>1: 
        lo1=LabelFrame(now,text='details',bg='purple',fg='yellow',width=28)
        lo1.grid(sticky='e')
        Label(lo1,text='Name: '+str(value1.get().title())+'  Gender: '+str(gendervalue1.get().title())+' Age: '+str(agevalue1.get()),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=3,column=0)  
        Label(lo1,text="BoardingFrom: "+str(Boardingvalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=4,column=0)
        Label(lo1,text="ReservedUpto: "+str(reservevalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=5,column=0)
        Label(lo1,text="Coach: "+str(coache),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=6,column=0)
        Label(lo1,text='Cabin: '+str(rc1),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=7,column=0)
        Label(lo1,text='Seatno: '+str(ro1),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=8,column=0)
    if num>2:
        lo2=LabelFrame(now,text='details',bg='purple',fg='yellow',width=28)
        lo2.grid(sticky='w')
        Label(lo2,text='Name: '+str(value2.get().title())+'  Gender: '+str(gendervalue2.get().title())+' Age: '+str(agevalue2.get()),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=3,column=0)  
        Label(lo2,text="BoardingFrom: "+str(Boardingvalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=4,column=0)
        Label(lo2,text="ReservedUpto: "+str(reservevalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=5,column=0)
        Label(lo2,text="Coach: "+str(coache),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=6,column=0)
        Label(lo2,text='Cabin: '+str(rc2),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=7,column=0)
        Label(lo2,text='Seatno: '+str(ro2),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=8,column=0)
    if num>3:
        lo3=LabelFrame(now,text='details',bg='purple',fg='yellow',width=28)
        lo3.grid(sticky='e')
        Label(lo3,text='Name: '+str(value3.get().title())+'  Gender: '+str(gendervalue3.get().title())+' Age: '+str(agevalue3.get()),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=3,column=0)  
        Label(lo3,text="BoardingFrom: "+str(Boardingvalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=4,column=0)
        Label(lo3,text="ReservedUpto: "+str(reservevalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=5,column=0)
        Label(lo3,text="Coach: "+str(coache),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=6,column=0)
        Label(lo3,text='Cabin: '+str(rc3),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=7,column=0)
        Label(lo3,text='Seatno: '+str(ro3),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=8,column=0)
    n=int(number1value.get())
    if n==0:
        print("no half ticket")
    if n>0:
        lo10=LabelFrame(now,text='details',bg='purple',fg='yellow',width=28)
        lo10.grid(sticky='w')
        Label(lo10,text='Name: '+str(value10.get().title())+'  Gender: '+str(gendervalue10.get().title())+' Age: '+str(agevalue10.get()),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=3,column=0)  
        Label(lo10,text="BoardingFrom: "+str(Boardingvalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=4,column=0)
        Label(lo10,text="ReservedUpto: "+str(reservevalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=5,column=0)
        Label(lo10,text="Coach: "+str(coache),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=6,column=0)
        Label(lo10,text='Cabin: '+str(rc1),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=7,column=0)
        Label(lo10,text='Seatno: No Seat',font="comicsansms 12 bold",fg='white',bg='purple').grid(row=8,column=0)
    if n>1:
        lo20=LabelFrame(now,text='details',bg='purple',fg='yellow',width=28)
        lo20.grid(sticky='e')
        Label(lo20,text='Name: '+str(value20.get().title())+'  Gender: '+str(gendervalue20.get().title())+' Age: '+str(agevalue20.get()),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=3,column=0)  
        Label(lo20,text="BoardingFrom: "+str(Boardingvalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=4,column=0)
        Label(lo20,text="ReservedUpto: "+str(reservevalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=5,column=0)
        Label(lo20,text="Coach: "+str(coache),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=6,column=0)
        Label(lo20,text='Cabin: '+str(rc2),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=7,column=0)
        Label(lo20,text='Seatno: No Seat',font="comicsansms 12 bold",fg='white',bg='purple').grid(row=8,column=0)
    if n>2:
        lo30=LabelFrame(now,text='details',bg='purple',fg='yellow',width=28)
        lo30.grid()
        Label(lo30,text='Name: '+str(value30.get().title())+'  Gender: '+str(gendervalue30.get().title())+' Age: '+str(agevalue30.get()),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=3,column=0)  
        Label(lo30,text="BoardingFrom: "+str(Boardingvalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=4,column=0)
        Label(lo30,text="ReservedUpto: "+str(reservevalue.get().title()),font="comicsansms 12 bold",bg='purple',fg='white').grid(row=5,column=0)
        Label(lo30,text="Coach: "+str(coache),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=6,column=0)
        Label(lo30,text='Cabin: '+str(rc3),font="comicsansms 12 bold",fg='white',bg='purple').grid(row=7,column=0)
        Label(lo30,text='Seatno: No Seat',font="comicsansms 12 bold",fg='white',bg='purple').grid(row=8,column=0)
    b3=Button(now,text="Done",command=cartoon,bg="black",fg='yellow',width=12)
    b3.grid(row=2,column=2)
    label12=Label(now,text="Press done to confirm ",bg="white",fg="black")
    label12.grid()
          


    
def b1c():
    global num
    num=int(numbervalue.get())
    if num>0:
        if (str(gendervalue.get().lower()) in gender):
           l=[]
           l=[value.get(),gendervalue.get(),str(valu.get()),agevalue.get()]
           ng.setdefault(value.get(),l)
           print(ng)
        else:
            print("Age limit for getting a half ticket is 5yrs to 11yrs")
    if num>1:
        if (str(gendervalue1.get().lower()) in gender):
           l1=[]
           l1=[value1.get().title(),gendervalue1.get(),str(valu1.get()),agevalue1.get()]
           ng1.setdefault(value1.get(),l1)
           print(ng1)
        else:
            print("Age limit for getting a half ticket is 5yrs to 11yrs")
    if num>2:
        if (str(gendervalue2.get().lower()) in gender):
           l2=[]
           l2=[value2.get().title(),gendervalue2.get(),str(valu2.get()),agevalue2.get()]
           ng2.setdefault(value2.get(),l2)
           print(ng2)
        else:
            print("Age limit for getting a half ticket is 5yrs to 11yrs")
    if num>3:
        if (str(gendervalue3.get().lower()) in gender):
           l3=[]
           l3=[value3.get().title(),gendervalue3.get(),str(valu3.get()),agevalue3.get()]
           ng3.setdefault(value3.get(),l3)
           print(ng3)
        else:
            print("Age limit for getting a half ticket is 5yrs to 11yrs")
    else:
        print("Book tickets for maximum 4 adults only")

ht1={}
ht2={}
ht3={}
def b2c():
    global n
    n=int(number1value.get())
    if n>0:
        l10=[]
        if (gendervalue10.get().lower() in gender) & (int(agevalue10.get()))<11& (int(agevalue10.get())>5) :
          l10=[value10.get().title(),gendervalue10.get(),agevalue10.get()]
          ht1.setdefault(value10.get(),l10)
          print(ht1)
        else:
            print("please input gender as 'Male' or 'Female' "
                  "Age limit for getting a half ticket is 5yrs to 11yrs")
    if n>1:
        if (gendervalue20.get().lower() in gender) & (int(agevalue20.get())<11)& (int(agevalue20.get())>5):
           l20=[]
           l20=[value20.get().title(),gendervalue20.get(),agevalue20.get()]
           ht2.setdefault(value20.get(),l20)
           print(ht2)
        else:
            print("please input gender as 'Male' or 'Female' "
                  "Age limit for getting a half ticket is 5yrs to 11yrs")
    if n>2:
        if (gendervalue30.get().lower() in gender) & (int(agevalue30.get())<11)& (int(agevalue30.get())>5):
           l30=[]
           l30=[value30.get().title(),gendervalue30.get(),agevalue30.get()]
           ht3.setdefault(value30.get(),l30)
           print(ht3)
        else:
            print("please input gender as 'Male' or 'Female' "
                  "Age limit for getting a half ticket is 5yrs to 11yrs")
    else:
        print("Book tickets for maximum 3 childern only")


def ticketr():
    global gendervalue
    global value
    global valu
    global agevalue
    global gendervalue1
    global value1
    global valu1
    global agevalue1
    global gendervalue2
    global value2
    global valu2
    global agevalue2
    global gendervalue3
    global value3
    global valu3
    global agevalue3
    global value10
    global gendervalue10
    global agevalue10
    global value20
    global gendervalue20
    global agevalue20
    global value30
    global gendervalue30
    global agevalue30
    global coachval
    global new
    global coache
    new=Toplevel(root)
    new.title("Ticket Counter")
    new.geometry("1100x700")
    Label(new,text="Your Details").grid(row=1,column=0)
    #NEW WINDOW OPERATIONS NOW
    new.configure(bg="sky blue")
    Label(new,text="Welcome ",font="Algerian 20 ",fg="white",bg="black",relief="groove",width=28,padx=8,pady=8).grid(row=0,column=1,columnspan=5)
    Label(new,text="PNR no: "+str(rbb.get()),font="Comicsansms 10").grid(row=1,column=0)
    print("fill the coach first then fill the details")
    
    
    Label(new,text="Fill the details and click on the tick button",fg="black",bg="white",font="Comicsansms 10").grid(row=3,column=0,sticky="s")
   
    if (int(numbervalue.get()) >0)  &(Boardingvalue.get().lower() in list1)&(reservevalue.get().lower() in list1)&(int(numbervalue.get())<5):
            la=LabelFrame(new,text="Full Ticket Counter",bg="sky blue",width=20,height=40,fg='green')
            la.grid(row=4,column=0,padx=60,pady=50,columnspan=10)
            t=0
            z=1
            num=int(numbervalue.get())
            if int(num) >0:
                Label(la,text="Name"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=0,)
                Label(la,text="Mob no."+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=2)
                Label(la,text="Gender"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=4)
                Label(la,text="Age"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=8)
                value=StringVar()
                valu=StringVar()
                gendervalue=StringVar()
                agevalue=StringVar()
                valuentry=Entry(la,textvariable=value).grid(row=16+t,column=1)
                valentry=Entry(la,textvariable=valu).grid(row=16+t,column=3)
                genderentry=Entry(la,textvariable=gendervalue).grid(row=16+t,column=5)
                agentry=Entry(la,textvariable=agevalue).grid(row=16+t,column=9)
                num=num-1
                t=t+1
                z=z+1
                b=Button(new,text="鉁�",bg="black",fg="yellow",font="aharoni 12 underline",command=b1c).grid(row=4,column=12)
                if int(num) >0:
                   Label(la,text="Name"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=0,)
                   Label(la,text="Mob no."+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=2)
                   Label(la,text="Gender"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=4)
                   Label(la,text="Age"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=8)
                   value1=StringVar()
                   valu1=StringVar()
                   gendervalue1=StringVar()
                   agevalue1=StringVar()
                   valuentry1=Entry(la,textvariable=value1).grid(row=16+t,column=1)
                   valentry1=Entry(la,textvariable=valu1).grid(row=16+t,column=3)
                   genderentry1=Entry(la,textvariable=gendervalue1).grid(row=16+t,column=5)
                   agentry1=Entry(la,textvariable=agevalue1).grid(row=16+t,column=9)
                   num=num-1
                   t=t+1
                   z=z+1
                   if int(num) >0:
                       Label(la,text="Name"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=0,)
                       Label(la,text="Mob no."+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=2)
                       Label(la,text="Gender"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=4)
                       Label(la,text="Age"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=8)
                       value2=StringVar()
                       valu2=StringVar()
                       gendervalue2=StringVar()
                       agevalue2=StringVar()
                       valuentry2=Entry(la,textvariable=value2).grid(row=16+t,column=1)
                       valentry2=Entry(la,textvariable=valu2).grid(row=16+t,column=3)
                       genderentry2=Entry(la,textvariable=gendervalue2).grid(row=16+t,column=5)
                       agentry2=Entry(la,textvariable=agevalue2).grid(row=16+t,column=9)
                       num=num-1
                       t=t+1
                       z=z+1
                       if int(num) >0:
                           Label(la,text="Name"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=0,)
                           Label(la,text="Mob no."+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=2)
                           Label(la,text="Gender"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=4)
                           Label(la,text="Age"+str(z),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=16+t,column=8)
                           value3=StringVar()
                           valu3=StringVar()
                           gendervalue3=StringVar()
                           agevalue3=StringVar()
                           valuentry3=Entry(la,textvariable=value3).grid(row=16+t,column=1)
                           valentry3=Entry(la,textvariable=valu3).grid(row=16+t,column=3)
                           genderentry3=Entry(la,textvariable=gendervalue3).grid(row=16+t,column=5)
                           agentry3=Entry(la,textvariable=agevalue3).grid(row=16+t,column=9)
                           num=num-1
                           t=t+1
                           z=z+1
    
    #bl=Boardingvalue.get().lower() 
    if (int(number1value.get()) >0)  &(Boardingvalue.get().lower()in list1)&(reservevalue.get().lower() in list1)&(int(number1value.get())<4):
        lab=LabelFrame(new,text="Half Ticket Counter",bg='sky blue',width=20,height=40)
        lab.grid(row=7,column=0,padx=60,pady=50,columnspan=10,sticky="n")
        ab=0
        pz=1
        n=int(number1value.get())
        b1=Button(new,text="鉁�",bg="black",fg="yellow",font="aharoni 12 underline",command=b2c).grid(row=7,column=9)
        if int(n) >0:
                Label(lab,text="Name"+str(pz),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=17+ab,column=0,)
                Label(lab,text="Gender"+str(pz),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=17+ab,column=4)
                Label(lab,text="Age"+str(pz),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=17+ab,column=8)
                value10=StringVar()
                gendervalue10=StringVar()
                agevalue10=StringVar()
                valuentry10=Entry(lab,textvariable=value10).grid(row=17+ab,column=1)
                genderentry10=Entry(lab,textvariable=gendervalue10).grid(row=17+ab,column=5)
                agentry10=Entry(lab,textvariable=agevalue10).grid(row=17+ab,column=9)
                n=n-1
                ab=ab+1
                pz=pz+1
                if int(n) >0:
                    Label(lab,text="Name"+str(pz),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=17+ab,column=0,)
                    Label(lab,text="Gender"+str(pz),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=17+ab,column=4)
                    Label(lab,text="Age"+str(pz),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=17+ab,column=8)
                    value20=StringVar()
                    gendervalue20=StringVar()
                    agevalue20=StringVar()
                    valuentry20=Entry(lab,textvariable=value20).grid(row=17+ab,column=1)
                    genderentry20=Entry(lab,textvariable=gendervalue20).grid(row=17+ab,column=5)
                    agentry20=Entry(lab,textvariable=agevalue20).grid(row=17+ab,column=9)
                    n=n-1
                    ab=ab+1
                    pz=pz+1
                    if int(n) >0:
                        Label(lab,text="Name"+str(pz),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=17+ab,column=0,)
                        Label(lab,text="Gender"+str(pz),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=17+ab,column=4)
                        Label(lab,text="Age"+str(pz),bg="sky blue",fg='red',font="aharoni 12 underline").grid(row=17+ab,column=8)
                        value30=StringVar()
                        gendervalue30=StringVar()
                        agevalue30=StringVar()
                        valuentry30=Entry(lab,textvariable=value30).grid(row=17+ab,column=1)
                        genderentry30=Entry(lab,textvariable=gendervalue30).grid(row=17+ab,column=5)
                        agentry30=Entry(lab,textvariable=agevalue30).grid(row=17+ab,column=9)
                        n=n-1
                        ab=ab+1
                        pz=pz+1
    button3=Button(new,text="Confirm Ticket",command=hungama,bg="black",fg='yellow',width=12)
    button3.grid(row=14,column=9,sticky="e")
    if (Classvalue.get()==1):
         coachval=StringVar()
         coachentry=Entry(new,textvariable=coachval).grid(row=2,column=1)
         Label(new,text="Coach",fg="black",bg="white",font="Comicsansms 10").grid(row=2,column=0)
         Button(new,text="Search",bg='black',fg='yellow',command=coac).grid(row=2,column=2,sticky="e")
    elif (Classvalue.get()==2):
        Label(new,text="Coach",fg="black",bg="white",font="Comicsansms 10").grid(row=2,column=0)
        Label(new,text="SL"+str(ri)).grid(row=2,column=1)
        coache="SL"+str(ri)
def pogo():
    global rbb
    global num1
    global o
    global p
    if str(Boardingvalue.get().lower()) in list1:
              a=str(Boardingvalue.get().title())
              b=a.split()
              o=''
              k=len(b)
              for i in range(0,k):
                 o+=str(b[i][0])
              print(o)
                
    else:
          print("please select arrival and departure station from the given list: ")
          for x in list1:
            print(x)
          #break            
    
    if str(reservevalue.get().lower()) in list1:
              e=str(reservevalue.get().title())
              d=e.split()
              l=len(d)
              p=''
              for j in range(0,l):
                  p+=str(d[j][0])
              print(p)
    else:
          print("please select arrival and departure station from the given list: ")
          for x in list1:
            print(x)
          #break             
    

    #button2=Button(root,text="Enter",command=ticketr,bg="black",fg="pink",width=12)
    #button2.grid(row=14,column=9,sticky="e")
    Label(root,text="Journeyfrom: "+str(dict1.get(Boardingvalue.get().lower())),bg="pink",fg="white",font="aharoni 12 underline").grid(row=2,column=13)
    Label(root,text="JourneyUpto: "+str(dict1.get(reservevalue.get().lower())),bg="pink",fg="white",font="aharoni 12 underline").grid(row=3,column=13)
    Label(root,text="BoardingFrom: "+str(Boardingvalue.get().title()),bg="pink",fg="white",font="aharoni 12 underline").grid(row=4,column=13)
    Label(root,text="ReservedUpto: "+str(reservevalue.get().title()),bg="pink",fg="white",font="aharoni 12 underline").grid(row=5,column=13)
    jf=str(dict1.get(Boardingvalue.get().lower()))
    rf=str(dict1.get(reservevalue.get().lower()))
    if (Boardingvalue.get().lower())and(reservevalue.get().lower()) in list1:
      if (jf=='West Bengal')& (rf=='West Bengal'):
        rbb=IntVar()
        Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
        r11=Radiobutton(root,text=str(PNR[0])+ " Howrah-Midnapore Fast Local " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
        r12=Radiobutton(root,text=str(PNR[1])+ " Shalimar SF Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
        r13=Radiobutton(root,text=str(PNR[2])+ " Howrah Kharagpur Local " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
        r14=Radiobutton(root,text=str(PNR[3])+ " Bokaro Steel City Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")  
        r15=Radiobutton(root,text=str(PNR[4])+ " Chakradharpur Express " +tkc.get_date() +" 4:45a.m.",variable=rbb,value=PNR[4],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=22,column=0,columnspan=5,sticky="w")
        r16=Radiobutton(root,text=str(PNR[5])+ " Darjeeling Mail " +tkc.get_date() +" 7:35p.m.",variable=rbb,value=PNR[5],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=23,column=0,columnspan=5,sticky="w")  
        r17=Radiobutton(root,text=str(PNR[6])+ " Psdstik Express " +tkc.get_date() +" 12:10p.m.",variable=rbb,value=PNR[6],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=24,column=0,columnspan=5,sticky="w")  
      elif (jf=='West Bengal')& (rf=='Maharashtra') or (rf=='West Bengal')&(jf=='Maharashtra'):
        rbb=IntVar()
        Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
        r11=Radiobutton(root,text=str(PNR[0])+ " Howran Junction Shivaji Math Express " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
        r12=Radiobutton(root,text=str(PNR[1])+ " Saurashtra Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
        r13=Radiobutton(root,text=str(PNR[2])+ " Borivali Express " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
        r14=Radiobutton(root,text=str(PNR[3])+ " Bandra Terminus weekly SF Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")  
        r15=Radiobutton(root,text=str(PNR[4])+ " Kutch SF express " +tkc.get_date() +" 4:45a.m.",variable=rbb,value=PNR[4],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=22,column=0,columnspan=5,sticky="w")
        r16=Radiobutton(root,text=str(PNR[5])+ " Trinuveli Express " +tkc.get_date() +" 7:35p.m.",variable=rbb,value=PNR[5],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=23,column=0,columnspan=5,sticky="w")  
        r17=Radiobutton(root,text=str(PNR[6])+ " Saurashtra Janta Express " +tkc.get_date() +" 12:10p.m.",variable=rbb,value=PNR[6],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=24,column=0,columnspan=5,sticky="w")  
      elif (jf=='West Bengal')& (rf=='New Delhi') or (rf=='New Delhi')&(jf=='west Bengal')or (rf=='West Bengal')&(jf=='Uttar Pradesh')or (rf=='Uttar Pradesh')&(jf=='West Bengal'):
        rbb=IntVar()
        Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
        r11=Radiobutton(root,text=str(PNR[0])+ " Netaji Express " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
        r12=Radiobutton(root,text=str(PNR[1])+ " Sealdah Rajdhani Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
        r13=Radiobutton(root,text=str(PNR[2])+ " Howrah Rajdhani Express " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
        r14=Radiobutton(root,text=str(PNR[3])+ " Poorja Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")  
        r15=Radiobutton(root,text=str(PNR[4])+ " Sealdah AC Duronto Express " +tkc.get_date() +" 4:45a.m.",variable=rbb,value=PNR[4],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=22,column=0,columnspan=5,sticky="w")
      elif (jf=='West Bengal')& (rf=='Rajasthan') or (rf=='West Bengal')&(jf=='Rajasthan')or(jf=='West Bengal')& (rf=='Gujarat') or (rf=='West Bengal')&(jf=='Gujarat'):
        rbb=IntVar()
        Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
        r11=Radiobutton(root,text=str(PNR[0])+ " Ahmedabad SF Express" +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
        r12=Radiobutton(root,text=str(PNR[1])+ " Howrah jn Jaisalmer Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
        r13=Radiobutton(root,text=str(PNR[2])+ "HWH BKN SF Express " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")
      elif (jf=='West Bengal')& (rf=='Tamil Nadu') or (rf=='West Bengal')&(jf=='Tamil Nadu')or (jf=='West Bengal')& (rf=='Karnataka') or (rf=='West Bengal')&(jf=='Karnataka'):
        rbb=IntVar()
        Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
        r11=Radiobutton(root,text=str(PNR[0])+ " Coromandel Express " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
        r12=Radiobutton(root,text=str(PNR[1])+ " MGR Chennai Central Mail " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
        r13=Radiobutton(root,text=str(PNR[2])+ " MGR Chennai CEentral AC SF Express " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")
      elif (jf=='West Bengal')& (rf=='Bihar')or(rf=='Bihar')&(jf=='West Bengal')or (jf=='West Bengal')& (rf=='Chattisgarh')or(jf=='Chattisgarh')&(rf=='West Bengal'):
        rbb=IntVar()
        Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
        r11=Radiobutton(root,text=str(PNR[0])+ "  Poorva Express " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
        r12=Radiobutton(root,text=str(PNR[1])+ " New Delhi Duronto Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
        r13=Radiobutton(root,text=str(PNR[2])+ " Upasana Express " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")
        r14=Radiobutton(root,text=str(PNR[3])+ "  Mumbai CSMT AC Duronto Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")
      elif (jf=='West Bengal')& (rf=='Andhra Pradesh')or(rf=='Andhra Pradesh')&(jf=='West Bengal')or (jf=='West Bengal')& (rf=='Odisha')or(jf=='Odisha')&(rf=='West Bengal'):
        rbb=IntVar()
        Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
        r11=Radiobutton(root,text=str(PNR[0])+ " Howrah-Midnapore Fast Local " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
        r12=Radiobutton(root,text=str(PNR[1])+ " Shalimar SF Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
        r13=Radiobutton(root,text=str(PNR[2])+ " Howrah Kharagpur Local " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
        r14=Radiobutton(root,text=str(PNR[3])+ " Bokaro Steel City Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")
      elif (jf=='West Bengal')& (rf=='Goa')or(rf=='West Bengal')&(jf=='Goa'):
        rbb=IntVar()
        Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
        r11=Radiobutton(root,text=str(PNR[0])+ " Amarvati Express " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
        r12=Radiobutton(root,text=str(PNR[1])+ " VSG Howrah Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
        r13=Radiobutton(root,text=str(PNR[2])+ " Poorna express " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
        r14=Radiobutton(root,text=str(PNR[3])+ " Velakanni Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")       
      elif (jf=='New Delhi')&(rf=='Odisha')or(jf=='odisha')&(rf=='New Delhi'):
            rbb=IntVar()
            Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
            r11=Radiobutton(root,text=str(PNR[0])+ " Hirakud SF Express " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
            r12=Radiobutton(root,text=str(PNR[1])+ " Kalinga Utkal Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
            r13=Radiobutton(root,text=str(PNR[2])+ " Bhubaneshwar Rajdhani Express " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
            r14=Radiobutton(root,text=str(PNR[3])+ " Purushottam Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")  
            r15=Radiobutton(root,text=str(PNR[4])+ " Bhubaneshwar Duronto Express " +tkc.get_date() +" 4:45a.m.",variable=rbb,value=PNR[4],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=22,column=0,columnspan=5,sticky="w")
      elif (jf=='New Delhi')&(rf=='Uttar Pradesh')or(jf=='Uttar Pradesh')&(rf=='New Delhi')or(jf=='New Delhi')&(rf=='Bihar')or(jf=='Bihar')&(rf=='New Delhi'):
            rbb=IntVar()
            Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
            r11=Radiobutton(root,text=str(PNR[0])+ " Yoga Express " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
            r12=Radiobutton(root,text=str(PNR[1])+ " Netaji Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
            r13=Radiobutton(root,text=str(PNR[2])+ " Punjab Mail " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
            r14=Radiobutton(root,text=str(PNR[3])+ " Saharsa Garib Rath Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")  
            r15=Radiobutton(root,text=str(PNR[4])+ " Dibrugarh Rajdhani Express " +tkc.get_date() +" 4:45a.m.",variable=rbb,value=PNR[4],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=22,column=0,columnspan=5,sticky="w")
      elif (jf=='New Delhi')&(rf=='Gujarat')or(jf=='Gujarat')&(rf=='New Delhi')or(jf=='New Delhi')&(rf=='Rajasthan')or(jf=='Rajasthan')&(rf=='New Delhi'):
            rbb=IntVar()
            Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
            r11=Radiobutton(root,text=str(PNR[0])+ " Golden Temple Mail " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
            r12=Radiobutton(root,text=str(PNR[1])+ " Ahmedabad Weekly Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
            r13=Radiobutton(root,text=str(PNR[2])+ " Pooja SF Express " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
            r14=Radiobutton(root,text=str(PNR[3])+ " Sainik Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")  
            r15=Radiobutton(root,text=str(PNR[4])+ " Ranikhet Express " +tkc.get_date() +" 4:45a.m.",variable=rbb,value=PNR[4],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=22,column=0,columnspan=5,sticky="w")
      elif (jf=='New Delhi')&(rf=='Maharashtra')or(jf=='Maharashtra')&(rf=='New Delhi')or(jf=='New Delhi')&(rf=='Chattisgarh')or(jf=='Chattisgarh')&(rf=='New Delhi'):
            rbb=IntVar()
            Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
            r11=Radiobutton(root,text=str(PNR[0])+ " Golden Temple Mail " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
            r12=Radiobutton(root,text=str(PNR[1])+ " Chattisgarh Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
            r13=Radiobutton(root,text=str(PNR[2])+ " Punjab Mail  " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
            r14=Radiobutton(root,text=str(PNR[3])+ " Mewar SF Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")  
            r15=Radiobutton(root,text=str(PNR[4])+ " Chetak Express " +tkc.get_date() +" 4:45a.m.",variable=rbb,value=PNR[4],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=22,column=0,columnspan=5,sticky="w")
      else:
        rbb=IntVar()
        Label(root,text="showing details of trains: ",bg="pink",fg="white",font="aharoni 13 underline").grid(row=14,column=0,columnspan=2)
        r11=Radiobutton(root,text=str(PNR[0])+ " August Kranti Rajdhani Express " +tkc.get_date() +" 9:45a.m.",variable=rbb,value=PNR[0],bg="pink", font="aharoni 15 underline",command=ticketr,pady=7).grid(row=16,column=0,columnspan=5,sticky="w")
        r12=Radiobutton(root,text=str(PNR[1])+ " Avantika Express " +tkc.get_date() +" 2:15p.m.",variable=rbb,value=PNR[1],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=18,column=0,columnspan=5,sticky="w")
        r13=Radiobutton(root,text=str(PNR[2])+ " Azad Hind Express  " +tkc.get_date() +" 8:35p.m.",variable=rbb,value=PNR[2],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=20,column=0,columnspan=5,sticky="w")  
        r14=Radiobutton(root,text=str(PNR[3])+ " Dhauli Express " +tkc.get_date() +" 10:35p.m.",variable=rbb,value=PNR[3],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=21,column=0,columnspan=5,sticky="w")  
        r15=Radiobutton(root,text=str(PNR[4])+ " Dwarka Express " +tkc.get_date() +" 4:45a.m.",variable=rbb,value=PNR[4],bg="pink",font="aharoni 15 underline",command=ticketr,pady=7).grid(row=22,column=0,columnspan=5,sticky="w")
    
            
   
            
button1=Button(labelframe,text="Selected Date",command=fetch_date,bg="black",fg="yellow")
button1.grid(row=2,column=2,sticky="s")

date=Label(labelframe,text="")
date.grid(row=3,column=2,sticky="n")

Boarding=Label(root,text="Boarding from",bg="pink",fg="black",font="aharoni 12 underline").grid(row=1,column=0)
reserved_upto=Label(root,text="Reserved upto",bg="pink",fg="black",font="aharoni 12 underline").grid(row=2,column=0)
Class=Label(root,text="Class",bg="pink",fg="black",font="aharoni 12 underline").grid(row=3,column=0)
number=Label(root,text="Full Tickets",bg="pink",fg="black",font="aharoni 12 underline").grid(row=8,column=0)
number1=Label(root,text="Half Tickets",bg="pink",fg="black",font="aharoni 12 underline").grid(row=9,column=0)

Boardingvalue=StringVar()
reservevalue=StringVar()
Classvalue=IntVar()
numbervalue=StringVar()
number1value=StringVar()


boardentry=Entry(root,textvariable=Boardingvalue)
reserveentry=Entry(root,textvariable=reservevalue)
r1=Radiobutton(root,text="AC Class",variable=Classvalue,value=1,command=selection)
r2=Radiobutton(root,text="Non-AC Class",variable=Classvalue,value=2,command=selection)
numberentry=Entry(root,textvariable=numbervalue)
number1entry=Entry(root,textvariable=number1value)

boardentry.grid(row=1,column=1)
reserveentry.grid(row=2,column=1)
r1.grid(row=3,column=1,sticky="w")
r2.grid(row=3,column=1,sticky="e")
numberentry.grid(row=8,column=1)
number1entry.grid(row=9,column=1)


Button(text="Show more",fg="yellow",bg="black",font="Helvetica 12 bold",command=pogo,width=25).grid(row=12,column=1,columnspan=6)

mydb.close()
mycursor.close()

root.mainloop()
