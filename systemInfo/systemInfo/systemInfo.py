### System Infomation Gathering Tool ###
### By: Patrick Mathews II ###
### Started On: 10/1/2022 ###



import os
from pathlib import Path
import tkinter
import tkinter.messagebox
import customtkinter  #pip3 install customtkinter      Make sure to install the library to your system.
import socket
import platform
import requests
import smtplib


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

main = customtkinter.CTk()

#Center Window When Loading

appWidth = 400
appHeight = 400
screenWidth = main.winfo_screenwidth()
screenHeight = main.winfo_screenheight()
x = (screenWidth / 2) - (appWidth / 2)
y = (screenHeight / 2) - (appHeight / 2)
main.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

main.title('System Information')
#main.iconbitmap('file location') #Load a favicon here and uncomment the line.



def change_mode():
        if switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

#def buttonClick(): 
    
        #e1 = (entry1.get())
        #sender_add='testmail@mathewscustoms.com' #storing the sender's mail id
        #receiver_add='' + str(e1) + '' #storing the receiver's mail id
        #password='testmail' #storing the password to log in
   
        #creating the SMTP server object by giving SMPT server address and port number
        #smtp_server=smtplib.SMTP("https://mail.mathewscustoms.com",456)
        #smtp_server.ehlo() #setting the ESMTP protocol
        #smtp_server.starttls() #setting up to TLS connection
        #smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()
        #smtp_server.login(sender_add,password) #logging into out email id
    
        #msg_to_be_sent ='''
        #This Is a Test
        #This Is a Test
        #This Is a Test
        #''' + text5.get() + "\n" + text6.get() + "\n" + text7.get() +""
    
        #sending the mail by specifying the from and to address and the message 
        #smtp_server.sendmail(sender_add,receiver_add,msg_to_be_sent)
        #priting a message on sending the mail
    
        #smtp_server.quit()#terminating the server
    

hostname = socket.gethostname()
ipAdd = requests.get('https://api.ipify.org').text
location = requests.get('http://ip-api.com/json/' + ipAdd + '').json()
lon = location['lon']
lat = location['lat']


if location['status'] == 'success':
    connected = ('Yes')


text0 = customtkinter.CTkLabel(main, text="Connected To Internet: " + connected + "", text_font=('calibri', '16'))
text0.grid(row=0, column=0)
text1 = customtkinter.CTkLabel(main, text="Computer Name: " + platform.node() + "", text_font=('calibri', '16'))
text1.grid(row=1, column=0)
text2 = customtkinter.CTkLabel(main, text="Machine Type: " + platform.machine() + "", text_font=('calibri', '16'))
text2.grid(row=2, column=0)
text3 = customtkinter.CTkLabel(main, text="ISP: " + location['isp'] + "", text_font=('calibri', '16'))
text3.grid(row=7, column=0)
text4 = customtkinter.CTkLabel(main, text="Operating System: " + platform.system() + " " + platform.release() + " " + platform.version() + "", text_font=('calibri', '16'))
text4.grid(row=3, column=0)
text5 = customtkinter.CTkLabel(main, text="Username: " + os.getlogin() + "", text_font=('calibri', '16'))
text5.grid(row=4, column=0)
text6 = customtkinter.CTkLabel(main, text="Local IPv4 Address: " + socket.gethostbyname(hostname) + "", text_font=('calibri', '16'))
text6.grid(row=5, column=0)
text7 = customtkinter.CTkLabel(main, text="Public IPv4 Address: " + ipAdd + "", text_font=('calibri', '16'))
text7.grid(row=6, column=0)
text8 = customtkinter.CTkLabel(main, text="Location: " + location['city'] + ", " + location['region'] + ". " + location['zip'], text_font=('calibri', '16'))
text8.grid(row=8, column=0)
text9 = customtkinter.CTkLabel(main, text="" + location['country'] + "", text_font=('calibri', '16'))
text9.grid(row=9, column=0)
text10 = customtkinter.CTkLabel(main, text="Longitude: " + str(lon) + " Lattitude: " + str(lat), text_font=('calibri', '16'))
text10.grid(row=10, column=0)




print(location)
#entry1 = customtkinter.CTkEntry(main, text_font=('calibri', '14'), placeholder_text="Enter Your Email Address", height=40, width=350, fg_color=("white", "gray25"), justify='center')
#entry1.grid(row=14, column=0, columnspan=2, padx=10, pady=10)

#button1 = customtkinter.CTkButton(main, text = "Email Results", text_font=('calibri', '16'), command=buttonClick())
#button1.grid(row=15, column=0, pady=10, padx=20, sticky='s')


switch_2 = customtkinter.CTkSwitch(main, text="Dark Mode", text_font=('calibri', '10'), command=change_mode)
switch_2.grid(row=16, column=0, padx=20, sticky="s")
switch_2.select()




main.mainloop()