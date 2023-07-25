### Created By: Patrick Mathews
### Created On: 11/6/2022
### @ 12:15 AM 


import secrets  
import string
import tkinter
import tkinter.messagebox
import customtkinter #Go to PowerShell and type: pip3 install customtkinter
import pyperclip     #Go to PowerShell and type: pip3 install pyperclip 
import time



customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

main = customtkinter.CTk()

#Center Window When Loading

appWidth = 550
appHeight = 175
screenWidth = main.winfo_screenwidth()
screenHeight = main.winfo_screenheight()
x = (screenWidth / 2) - (appWidth / 2)
y = (screenHeight / 2) - (appHeight / 2)
main.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

main.title('Random Password Generator')
#main.iconbitmap('file location') #Icon for program



#Switch between Dark Mode and Light Mode

def change_mode():
        if switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")


#Copy Password to Clipboard. Minimum Password Length is set to 12 and Maximum Password Length is set to 36

def buttonClick():
    if entry2.get() == "":   #If Password Length box is left empty the default length is 12
        pwd_length = 12
    else:
        pwd_length = int(entry2.get())
    if pwd_length < 12:   #Minimum Password Length
        pwd_length = 12
    if pwd_length > 36:   #Maximum Password Length
        pwd_length = 36
   
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    entry1 = customtkinter.CTkLabel(main, text="" + pwd + "", text_font="Calibri, 18", height=30, width=530, fg_color=("white", "gray25"), justify='left')
    entry1.grid(row=1, column=0, columnspan=4, padx=15, pady=15)
    pyperclip.copy('' + pwd + '')
    text = pyperclip.paste()
    

##### Original Code #####

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation


alphabet = letters + digits + special_chars
#pwd_length = 12

#pwd = ''
#for i in range(pwd_length):
  #pwd += ''.join(secrets.choice(alphabet))

#print(pwd)

##### Original Code #####


#Place label, entry box, button, checkboxes, and switch on window.

entry1 = customtkinter.CTkLabel(main, text="Welcome", text_font="Calibri, 18", height=45, width=530, fg_color=("white", "gray25"), justify='left')
entry1.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

entry2 = customtkinter.CTkEntry(main, placeholder_text="Password Length", text_font="Calibri, 12", height=30, width=150, fg_color=("white", "gray25"), justify='left')
entry2.grid(row=4, column=0, columnspan=1, padx=10, pady=10)


button_1 = customtkinter.CTkButton(text="Randomize & Copy", text_font="Calibri, 12", command=buttonClick)
button_1.grid(row=4, column=1, columnspan=1, pady=10, padx=10, sticky="we")

checkBox1 = customtkinter.CTkCheckBox(main, text='Letters', text_font="Calibri, 14")
checkBox1.grid(row=5, column=0, columnspan=1, sticky="s")
checkBox1.select()

checkBox2 = customtkinter.CTkCheckBox(main, text='Numbers', text_font="Calibri, 14")
checkBox2.grid(row=5, column=1, columnspan=1, sticky="s")
checkBox2.select()

checkBox3 = customtkinter.CTkCheckBox(main, text='Symbols', text_font="Calibri, 14")
checkBox3.grid(row=5, column=2, columnspan=1, sticky="s")
checkBox3.select()

switch_2 = customtkinter.CTkSwitch(text="Dark Mode", text_font="Calibri, 10",command=change_mode)
switch_2.grid(row=4, column=2, pady=10, padx=20, sticky="w")
switch_2.select()


main.mainloop()