
from tkinter import *
def display_quiz(quiz):
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
