#Ayushi Patel
#MadLibs Game

#Imported Tkinter from library to use for buttons
from tkinter import *

#Its for font style, and font size for the display windowss and text.
top = Tk()
top.geometry("500x500")
Label(top, text= 'Mad Libs Generator \n Lets Have Fun!' , font = 'Times 20 bold').pack()
Label(top, text = 'Choose One :', font = 'Times 25 bold').place(x=40, y=80)

#Once user will chose the category the sentences and inputs will display according to the category
def life():

    Noun= input('Enter a noun: ')
    Family= input('Enter a member: ')
    Things=input('Enter a thing: ')
    Place=input('Enter a place: ')
    Verb=input('Enter a verb: ')
    Name=input('Enter a name: ')
    Adjective=input('Enter a adjective: ')
    Color=input('Enter a color: ')

    print('Listen to the people who love ' + Noun+ '. Believe that they ' +Verb+ 'worth living for ' +Family+ ' even when you don’t believe' +Adjective+ '. Seek out the ' +Things+ 'memories depression takes away and ' +Place+ 'project them into the future. Be' +Adjective+ '; be strong; take your' +Things+ '. Exercise because it’s good for you ' +Noun+ '.')

def song():
   
    Noun= input('Enter a noun: ')
    Family= input('Enter a member: ')
    Things=input('Enter a thing: ')
    Place=input('Enter a place: ')
    Verb=input('Enter a verb: ')
    Name=input('Enter a name: ')
    Adjective=input('Enter a adjective: ')
    Color=input('Enter a color: ')

    print('Baby Im falling head over heels' +Noun+ 'Looking for ways to let ' +Things+ ',know just how I feel' +Place+ ' I wish I was holding you by my side ' +Verb+ 'I wouldnt change a '+Thing+ 'cause finally its' +Adjective+ 'Im tryinto hold back,' +Family+ 'you ought to know that ' +Noun+ ' the one thats on my mind ' +Place+ 'Im falling too fast deeply in love. Its ' +Family+ 'You, its you')

def kid():

    Noun= input('Enter a noun: ')
    Family= input('Enter a member: ')
    Things=input('Enter a thing: ')
    Place=input('Enter a place: ')
    Verb=input('Enter a verb: ')
    Name=input('Enter a name: ')
    Adjective=input('Enter a adjective: ')
    Color=input('Enter a color: ')
   
    print('I never saw a ' +Color+ ' cow,I never hope ' +Verb+ ' see one, But I can tell ' +Adjective+ ', anyhow,I’d ' +Verb+ 'rather see than be one!')

#Button will be used when they want to click on category instead of writing it out
B = Button(top, text = "Life Inspiration", command = life)
B.place(x = 60,y = 120)
B = Button(top, text = "Its You Song", command = song)
B.place(x = 70,y = 180)
B = Button(top, text = "The Purple Cow Poem", command = kid)
B.place(x = 80,y = 240)

#Final statement for program to know it ready to run
top.mainloop()

