
from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES
from langdetect import detect


root = Tk()
root.geometry('1080x400')
root.resizable(0,0)
root.title("All Language Translator")
root.config(bg = 'powderblue')

#heading
Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()
Label(root,text ="Get your all language translated here...", font = 'arial 20 bold', bg ='white smoke' , width = '60').pack(side = 'bottom')


#INPUT AND OUTPUT TEXT WIDGET
Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)


Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)


language = list(LANGUAGES.values())

#Define function
# def autodetection():

language_var = StringVar()
language_var.set("English")  # default selected language

languages = ["English", "French", "Spanish", "German", "Hindi", "Marathi"]
dropdown = OptionMenu(root, language_var, *languages)
dropdown.pack()


def Translate():
    translator = Translator()
    input_text = Input_text.get("1.0", "end-1c")
    dest_lang = language_var.get()  # assuming you're selecting the target language from a dropdown

    # Translate
    translated = translator.translate(input_text, dest=dest_lang)

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
   

#Translate Button
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')
trans_btn.place(x = 490, y = 180)


root.mainloop()

