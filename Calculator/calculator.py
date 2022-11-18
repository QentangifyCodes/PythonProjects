from xml.dom import XMLNS_NAMESPACE
import button

class Calculator:
    def __init__(self):
        self.buttons = []

        self.GenerateButtons()

    def GenerateButtons(self):
        x, y = 0, 100
        i = 1

        while y < 300:
            while x < 300:
                butt = button.NumButton((x,y), str(i))

                if y == 250:
                    if i == 10:
                        butt = button.OppButton((x,y), "=")
                    elif i == 11:
                        butt = button.NumButton((x,y), "0")
                    else:
                        butt = button.OppButton((x,y), "C")

                self.buttons.append(butt)
                i+=1
                x+=100
            x = 0
            y+=50

        yy = 100

        while yy < 300:
            if yy==100:
                butt = button.OppButton((300,yy), "+")
            if yy==150:
                butt = button.OppButton((300,yy), "-")
            if yy==200:
                butt = button.OppButton((300,yy), "X")
            if yy==250:
                butt = button.OppButton((300,yy), "/")
            
            self.buttons.append(butt)
            yy+=50

    
    def Update(self):
        for button in self.buttons:
            button.Update()
