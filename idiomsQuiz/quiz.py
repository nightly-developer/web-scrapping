#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs
import requests
import random
from tkinter import *
#import idioms_gui
def quiz_maker(Q=5):
  category = 'common-english-idioms'
  # category = 'Common-English-Idioms'
  # category = 'Familiar-English-Idioms'
  # category = 'Idioms-About-Age'
  #category = 'Idioms-About-Art'
  print(category)

  category = 'common-english-idioms'
  website = requests.get(f'https://www.wordscoach.com/idioms?category={category}').text
  soup  = bs(website,'lxml')

  idioms_list = soup.find_all('div', class_ = 'list-content')
  idioms = {}

  for idiom in idioms_list:
    for index, element in enumerate(idiom.p):
      if index == 1:
        idioms[idiom.a['title'].strip()] = element.strip()

  keys = list(idioms.keys())
  dict_values = list(idioms.values())
  quiz = {}
  for _ in range(Q):
    item = random.randrange(len(keys))
    options = {}
    values = []
    answer = idioms[keys[item]]
    while len(values) != 3:
      value = random.choice(dict_values)
      if value != answer:
        values.append(value)
    values.append(answer)
    random.shuffle(values)
    for index, letter in enumerate('ABCD'):
      options.update({letter:values[index]})
    quiz.update({keys[item]:options})
    del keys[item]
  
  root = Tk()
  root.title('Quiz')
  width = 1000
  height = 600
  #root.config()

  root.geometry(str(width)+'x'+str(height))

  #frame3
  LabelFrame(root, bg='gray50',relief = RAISED,width=20, height=500, bd=4).pack(fill = BOTH,side='right')

  frame1 = LabelFrame(root, bg='#845EC2',relief = RAISED,bd=4)
  frame1.pack(fill = BOTH, expand = True)

  frame2 = LabelFrame(root, bg='#D5CABD',relief = RAISED,width=500, height=30, bd=4)
  frame2.pack(fill = BOTH, expand = True)

  class Display():
    #class variables
    answers = []

    def __init__(self,Qnumber,options) -> None:
      self.Qnumber = Qnumber
      self.options = options
      self.answer = StringVar()

      def call():
        #print((self.answer).get())
        Display.answers[int((Qnumber-1)/4)] = (self.answer).get()

      for Onumber, option in enumerate(options,start=1):
        #display options
        if Onumber < 3:
          Radiobutton(frame1, text=options[option],variable=self.answer,value =option,wraplength=450,justify=LEFT,command=call,bg='#4E8397',borderwidth=5,padx=3).grid(row=self.Qnumber+1,column=(Onumber+1)%2,sticky=W,padx=10,pady=5)
        else:
          Radiobutton(frame1, text=options[option],variable=self.answer,value =option,wraplength=450,justify=LEFT,command=call,bg='#4E8397',borderwidth=5,padx=3).grid(row=self.Qnumber+2,column=(Onumber+1)%2,sticky=W,padx=10,pady=5)

  for Qnumber, (question,options) in enumerate(quiz.items()):
    Qnumber = Qnumber*4+1
    Display.answers.append(None)
    Label(frame1,text=question).grid(row=Qnumber,column=0,sticky=W,padx=10,pady=5)
    Display(Qnumber,options)
    Label(frame1,bg='#845EC2').grid(row=Qnumber+3,columnspan=2)

  #frame2 buttons Functions
  def score():
    print(Display.answers)
    root.destroy()
    
  #frame2 buttomns
  Button(frame2,text='previous').place(relx=0.03,rely=0.5)
  Button(frame2,text='submit',command=score).place(relx=0.45,rely=0.5)
  Button(frame2,text='next').place(relx=0.91,rely=0.5)

  root.mainloop()
quiz_maker(3)