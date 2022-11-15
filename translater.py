from tkinter import *
import pandas
from googletrans import *

data=pandas.read_csv('data.csv')
dic_data=data.to_dict(orient='records')
language_list=[i['language'] for i in dic_data]
color='#F9F9F9'
style=('Candara Light',15,'bold')
#function
def translate_text():
    trans=Translator()
    global language
    input_text=input_box.get("1.0","end-1c")
    lang=language.get()
    for i in dic_data:
        if i['language']==lang:
            code=i['code']
    translated_text=trans.translate(text=input_text,dest=code)
    output_box.delete('1.0','end')
    output_box.insert(INSERT,translated_text.text)
#window 
window=Tk()
window.title('Language Translater')
window.config(padx=15,pady=30,bg=color)
img=PhotoImage(file='img (1).png')
#canvas
canvas=Canvas(width=450,height=163)
canvas.create_image(225,82,image=img)
canvas.config(highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=3)
#labels
input=Label(text='Enter Text:',
            font=style,
            highlightthickness=0,background=color)
input.grid(column=0,row=1)
translated=Label(text='Translated text:',
                 font=style,
                 highlightthickness=0,background=color)
translated.grid(column=0,row=2)
language_to_translate=Label()
#entry
input_box=Text(window,width=20,height=3,font=style)
input_box.grid(column=1,row=1,columnspan=2)

output_box=Text(window,width=20,height=3,font=style)
output_box.grid(column=1,row=2,columnspan=2)
#button
global language
language=StringVar(window)
language.set('Language')

option_button=OptionMenu(window,language,*language_list)
option_button.config(font=style,background=color)
option_button.grid(column=3,row=1)

translate=Button(text='Translate',
                 font=style,
                 highlightthickness=0,background=color,
                 command=translate_text)
translate.grid(column=3,row=2)

    
window.mainloop()