from tkinter import *
import datetime, re

class NewYear:
    def __init__(self):
        self.window = Tk()
        self.window.title("Contador do Ano Novo")
        self.window.resizable(False,False)
        self.create_widgets()
        self.month = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
                      "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        self.window.after(10,self.update)
        self.window.mainloop()
    
    def create_widgets(self):
        self.labelCounter = Label(self.window, text="00:00:00", justify=CENTER, font=("Arial",100))
        self.labelCounter.grid(row=0,column=0)
        self.labelDate = Label(self.window,text="Hoje é DIA de MÊS de ANO", justify=LEFT, font=("Arial",18))
        self.labelDate.grid(row=1,column=0)


    def update(self):
        self.labelCounter['text'] = self.calcTime()
        self.labelDate["text"] = self.show_day()
        self.window.after(1000, self.update)

    def calcTime(self):
        today = datetime.datetime.now()
        year = today.year + 1
        new_year = datetime.datetime(year,1,1)
        regressive = new_year - today
        text = str(regressive).split(".")[0]
        new = re.sub("day[s]?","dias",text)
        if re.search("^1",new) != None:
            new = re.sub("dias","dia",new)
        return new

    def show_day(self):
        today = datetime.datetime.now()
        return "Hoje é {} de {} de {}".format(today.day, self.month[today.month - 1], today.year)

if __name__=="__main__":
    App = NewYear()
