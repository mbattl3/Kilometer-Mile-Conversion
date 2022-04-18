#Conversion Km --> Mi
#Formula: mi = Km * 0.62137
#Labels:3
#textboxes: 3 (1 is an error message)
#Buttons: 2
#wrap in try and except
#lambda function for calc button

from tkinter import*


def calc(txtbx, txtbx2, txtbx3):
   # Mi= 0
   msg = ''
   a = ''

   try:
        indata = txtbx.get()
        a = str(indata)
        print ("Kilometers Entered: ", indata)
        Mi = float(indata) * 0.62137
        

        if float(indata) < 0:
            raise TypeError
        else: pass
        
        if float(indata) == 0:
            msg = "Value cannot be 0"
            print (msg)
            txtbx3.insert(0,msg)
        else:
            pass
           

   except TypeError:
        msg = "Entry cannot be negative"
        print (msg)
        txtbx3.insert(0, msg)
        

   #except TypeError:
    #    msg = "Value cannot be 0"
    #    txtbx3.insert(0,msg)
   
   except Exception:
       if len(indata) == 0:
           msg = "Entry cannot be blank"
           print (msg)
           txtbx3.insert(0, msg)
       elif a.isspace():
           msg = "No spaces are allowed" 
           print (msg) 
           txtbx3.insert(0, msg)    
       elif a.isalpha():
            msg = "Entry must be numeric"
            print (msg)
            txtbx3.insert(0, msg)
       else:
            pass
       #msg = e

   else:
        txtbx2.insert(0, Mi)
        print ("Miles: ", Mi)





def clear(txtbx, txtbx2,txtbx3):
    txtbx.delete(0, "end")
    txtbx2.delete(0, "end")
    txtbx3.delete(0, "end")  
    print ("Field has been cleared")
    


def main():
    window = Tk()
    window.geometry("800x600")
    window.title("Program 18: GUI")
    window.minsize (500,200)
    window.maxsize (600,300)
    window.configure (bg= "#F0A868")

    lbl = Label(window,
                    text = "Kilometers to Miles",
                    font = ("Arial Bold", 20),
                     fg= "#FFE8C2",
                    bg= "#F0A868")

    lbl2 = Label(window,
                    text = "Kilometers",
                    fg= "#FFE8C2",
                    bg= "#F0A868",
                    font = ("Arial Bold", 18))

    lbl3 = Label(window,
                    text = "Miles",
                    fg= "#FFE8C2",
                    bg= "#F0A868",
                    font = ("Arial Bold", 18))

        #Kilo Input
    txtbx =  Entry(window,
                        width = 15,
                        #borderwidth = 3,
                        fg= "#FFE8C2",
                        bg = "#F0A868",
                        font = ("Arial Bold", 16))
        
        #Miles Output
    txtbx2 = Entry(window,
                        width = 15,
                        #borderwidth = 3,
                        fg= "#FFE8C2",
                        bg = "#F0A868",
                        font = ("Arial Bold", 16))
    
        #Error
    txtbx3 = Entry(window,
                        width = 30,
                        #borderwidth = 3,
                        fg= "#FFE8C2",
                        bg = "#F0A868",
                        font = ("Arial Bold", 16))
        

        #Calculate 
    button = Button(window,
                        text = "Calculate",
                        borderwidth = 3,
                        fg= "#F0A868",
                        bg = "#FFE8C2",
                        font = ("Arial, 12"),
                        #command = calc,
                        command = lambda: calc(txtbx,txtbx2, txtbx3))


        #Clear Field
    button2 = Button (window,
                        text = "Clear",
                        borderwidth = 3,
                        relief = "raised",
                        fg= "#F0A868",
                        bg = "#FFE8C2",
                        font = ("Arial, 12"),
                        command = lambda: clear(txtbx,txtbx2,txtbx3))
        
        
        #for labels
    lbl.grid (column = 2, row =0)
    lbl2.grid (column = 1, row =1)
    lbl3.grid (column = 1, row =2)


    txtbx.grid (column = 2, row =1)
    txtbx2.grid (column = 2, row =2)
    txtbx3.grid (column = 2, row =3)
        
        #for Buttons
    button.grid (column = 2, row = 5)
    button2.grid (column = 3, row = 5)

#-------------------------------------------------------

    window.mainloop()

main()
    
