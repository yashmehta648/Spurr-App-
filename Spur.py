from tkinter import *
from tkinter import messagebox
import time
from gtts import gTTS
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.ttk import Progressbar
import os,sys
import playsound
from threading import *

def goto_signup_clicked(destroy_this_window,kill_this_thread):
    destroy_this_window.destroy()
    sign=Tk()
    sign.title("SignUp")
    sign.geometry("500x650") #300x200
    sign.config(background = "black", pady=10)
    load = Image.open("C:/gui/spurpenguin1.jpeg")
    render = ImageTk.PhotoImage(load)
    img = Label(sign, image=render)
    img.image = render
    img.config(height=400, width=300)
    img.place(x=100, y=200)
    global clock
    clock=Label(sign, font=("times", 14), bg= "black",fg="white")
    clock.place(x = 350, y = 5)

    # tick()
    kill_this_thread=Thread(target=ticksmall)
    kill_this_thread.start()

    lbs = Label(sign, text = "SignUp", bg = "black", fg="white", font=20)
    lbs.place(x=210, y=5)

    lb2_s = Label(sign, text = "Username - ", bg="black", fg="white")
    lb2_s2 = Entry(sign)
    lb2_s.place(x=110, y=40)
    lb2_s2.place(x=210, y=40)


    lb2_ps = Label(sign, text = "Password - ", bg="black", fg="white")
    lb2_ps2 = Entry(sign,show="*")
    lb2_ps.place(x=110, y=80)
    lb2_ps2.place(x=210,y=80)
   
    def reg():
        username = lb2_s2.get()
        pas = lb2_ps2.get()
        file =  open("username.txt","a")
        file1= open("password.txt","a")
        score_file= open("score.txt","a")
        fiIn = open('username.txt').readlines()
        fiIn1 = open('password.txt').readlines()
        score_f=open("score.txt").readlines()
        if username=="" or pas=="":
            messagebox.showerror("Error", "Fields are mandatory")
        elif (username+"\n") in fiIn:
            print("Exists")
            messagebox.showerror("Error", "User already exists")
        else:
            print("not Exists")
            if len(pas)>9:
                messagebox.showerror("Error","Password too long")
                lb2_ps2.delete(0,END)
            else:    
                file.write(username+"\n")
                file1.write(pas+"\n")
                score_file.write("0\n")
                lb2_ps2.delete(0,END)
                lb2_s2.delete(0,END)
                messagebox.showinfo("Congratulations", "Registered successfully")
            file.close()
            file1.close()
                
    bts = Button(sign, text="Register", command=reg)
    bts.place(x=210, y=120)
    bts3 = Button(sign, text="Go to Signin", command=lambda:createframelogin("Login",sign))
    bts3.place(x=290, y=120)
    dis.place(x=100, y=150)

def dis():
    user = lb2_u2.get()
    pas = lb2_p2.get()
    filo1 = open('username.txt').readlines()
    filo2 = open('password.txt').readlines()
    if user=="" or pas=="":
        messagebox.showerror("Error", "Enter credentials")
       
    flag=0
    for i in range(0,len(filo1)):
        if((user+"\n")==filo1[i]):
            if ((pas+"\n") ==filo2[i]):
                messagebox.showinfo("Congratulations", "Login successful")
                flag=1
                run_mainframe(user)
                break
            else:
                messagebox.showerror("Error", "Login unsuccessfull!!\nIncorrect password")
                break
    if(flag!=1):
        messagebox.showerror("Error", "Login unsuccessful!!!Try again")
    lb2_u2.delete(0,END)
    lb2_p2.delete(0,END)


def createframelogin(s,destroy_this_window):
    destroy_this_window.destroy()
    window=Tk()
    window.title(s)
    window.geometry("500x650")   #300x200
    window.config(background = "black", pady=10)
    load = Image.open("C:/gui/spurpenguin1.jpeg")
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render)
    img.image = render
    img.config(height=400, width=300)
    img.place(x=100, y=200)
    global clock
    clock=Label(window, font=("times", 14), bg= "black",fg="white")
    clock.place(x = 350, y = 5)

    # tick()
    tt1=Thread(target=ticksmall)
    tt1.start()
    file =  open("username.txt","a")
    file1= open("password.txt","a")
    global lb2_u
    global lb2_u2
    lb1 = Label(window, text = "Login Form", bg = "black", fg="white", font=20)
    lb1.place(x=210, y=5)

    lb2_u = Label(window, text = "Username - ", bg="black", fg="white")
    lb2_u2 = Entry(window)
    global lb2_p
    global lb2_p2

    lb2_u.place(x=110, y=40)
    lb2_u2.place(x=210, y=40)


    lb2_p = Label(window, text = "Password - ", bg="black", fg="white")
    lb2_p2 = Entry(window,show="*")
    lb2_p.place(x=110, y=80)
    lb2_p2.place(x=210,y=80)
    bt = Button(window, text="Login")                         ## bt=login log
    bt.place(x=210, y=120)                                    ## bt2 =head to signup
    bt.config(command=dis)
    bt2 = Button(window, text="Go to SignUp",command=lambda:goto_signup_clicked(window,tt1))
    bt2.place(x=270, y=120)

    return window
class noneclass:
    def destroy(self):
        pass
    pass

def createframe(s):
    window=Tk()
    window.title(s)
    window.geometry("500x650")
    window.config(background = "black", pady=10)
    return window
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text="Current time:- "+time_string)
    clock.after(1000, tick)
def ticksmall():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text="Current time:- \n"+time_string)
    clock.after(1000, ticksmall)

def start_thread(hr_start,min_start,hr_end,min_end,_goal,hrstart,hrend,minstart,minend,goal,user):
    t2=Thread(target=hclicked,args=(hr_start,min_start,hr_end,min_end,_goal,hrstart,hrend,minstart,minend,goal,user,))
    t2.start()


def hclicked(hr_start,min_start,hr_end,min_end,_goal,hrstart,hrend,minstart,minend,goal,user):
    
    hrstart.delete(0,END)
    hrend.delete(0,END)
    minstart.delete(0,END)
    minend.delete(0,END)
    goal.delete(0,END)
    hrstart.current(0)
    minstart.current(0)
    hrend.current(0)
    minend.current(0)

    language="en"
    outputstart=gTTS(text="Start of "+str(_goal),lang=language,slow=False)
    outputstart.save("start.mp3")
    outputend=gTTS(text="End of "+str(_goal),lang=language,slow=False)
    outputend.save("end.mp3")

    total_timespan=((int(hr_end)-int(hr_start))*60)+(int(min_end)-int(min_start))
    
    filo1 = open('username.txt').readlines()
    # filo2 = open('password.txt').readlines()
    filo3 = open('score.txt').readlines()
    
    for inter in range(0,len(filo1)):
        if((user+"\n")==filo1[inter]):
            total_score=filo3[inter]
            total_score=total_score[::-1]
            total_score=total_score[1:]
            total_score=int(total_score)
            filo3[inter]=str(total_timespan +total_score)+'\n'
    MyFile=open('score.txt','w')
    print(filo3)
    for element in filo3:
        MyFile.write(str(element))
    MyFile.close()




    Set_Alarm = hr_start+":"+min_start+":00"
    Actual_Time = time.strftime("%H:%M:%S")
    while (Actual_Time != Set_Alarm): 
        print ("The time is " + Actual_Time) 
        Actual_Time = time.strftime("%H:%M:%S") 
        # style = ttk.Style()
        # style.theme_use('default')
        # style.configure("black.Horizontal.TProgressbar", background='green')
        # bar = Progressbar(Start_window, length=220, style='black.Horizontal.TProgressbar')
        # bar['value'] = 80
        # bar.grid(column= 60, row=50)
        time.sleep(1)
    if (Actual_Time == Set_Alarm): 
        playsound.playsound("start.mp3",True)


    Set_Alarm_end = hr_end+":"+min_end+":00"
    Actual_Time_end = time.strftime("%H:%M:%S")
    while (Actual_Time_end != Set_Alarm_end): 
        print ("The time is " + Actual_Time_end) 
        Actual_Time_end = time.strftime("%H:%M:%S") 
        style = ttk.Style()
        cur_hr=int(Actual_Time_end[0]+Actual_Time_end[1])
        cur_min=int(Actual_Time_end[3]+Actual_Time_end[4])
        current_timespan=((cur_hr-int(hr_start))*60)+(cur_min-int(min_start))
        k=((current_timespan/total_timespan)*100)
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar", background='green')
        bar = Progressbar(Start_window, length=220, style='black.Horizontal.TProgressbar')
        bar['value'] = k
        print("value of k->"+str(k)+"total timespan->"+str(total_timespan)+"currrent timespan->"+str(current_timespan)+"cur_hr,cur_min->"+str(cur_hr)+" "+str(cur_min))
        # bar.grid(column= 60, row=50)
        bar.place(x= 150, y=300)
        time.sleep(1)
    if (Actual_Time_end == Set_Alarm_end): 
        print ("End of "+str(_goal))
        playsound.playsound("end.mp3",True)
    
def run_mainframe(user):
    global Start_window
    global clock
    hr_list=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"
    ,"21","22","23","24"]
    min_list=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"
    ,"21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42"
    ,"43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]

    total_score=0
    filo1 = open('username.txt').readlines()
    filo2 = open('password.txt').readlines()
    filo3 = open('score.txt').readlines()
    for inter in range(0,len(filo1)):
        if((user+"\n")==filo1[inter]):
            total_score=filo3[inter]
            total_score=total_score[::-1]
            total_score=total_score[1:]
            total_score=int(total_score)

    Start_window=createframe("Spur!!!")
    
    t="Hello "+user+" Your current score is "+str(total_score)
    greet=Label(Start_window,bg="black",fg="white",text=t, font=("arial", 18))
    greet.place(x = 0, y = 30)
    greet1=Label(Start_window,bg="black",fg="white",text="Enter The time and goal ", font=("arial", 18))
    greet1.place(x = 0, y = 65)
    clock=Label(Start_window, font=("times", 15), bg= "black",fg="white")
    clock.place(x = 300, y = 5)

    # tick()
    t1=Thread(target=tick)
    t1.start()

    hr_l=Label(Start_window,bg="black",fg="white",text="Start Time:--> hrs:                    min:",font=("times", 16))
    hr_l.place(x = 10, y = 150 )

    hrstart = ttk.Combobox(Start_window, values=hr_list,state="readonly",width=5)
    hrstart.place(x = 180, y = 150 )

    minstart = ttk.Combobox(Start_window, values=min_list,state="readonly",width=5)
    minstart.place(x = 310, y = 150 )

    hrend=Label(Start_window,bg="black",fg="white",text="End Time:--> hrs:                     min:",font=("times", 16))
    hrend.place(x = 10, y = 190 )

    hrend = ttk.Combobox(Start_window, values=hr_list,state="readonly",width=5)
    hrend.place(x = 180, y = 190 )

    minend = ttk.Combobox(Start_window, values=min_list,state="readonly",width=5)
    minend.place(x = 310, y = 190 )

    glabel=Label(Start_window,bg="black",fg="white",text="Enter the note: ",font=("times", 16))
    glabel.place(x = 10, y = 230 )
    goal=Entry(Start_window,width=40)
    goal.place(x = 170, y = 230 )

    log=Button(Start_window,font=("times", 16),text="Log Goal",command=lambda:start_thread(hrstart.get(),minstart.get(),hrend.get(),minend.get(),goal.get(),hrstart,hrend,minstart,minend,goal,user)) #hclicked(hrstart.get(),minstart.get(),hrend.get(),minend.get(),goal.get(),hrstart,hrend,minstart,minend,goal))
    log.place(x = 200, y = 400 )
    Start_window.mainloop()

Start_window=None
clock=None








a=noneclass()
login_window=createframelogin("Login",a)

login_window.mainloop()
