from tkinter import *
from crypto_searcher import find_crypto
from playsound import playsound
#----------------------------------------------------------------------------------------------------------------
root =Tk()
root.title("cyrpto price finder")
root.geometry('600x250')
root.resizable(False,False)
root.attributes('-topmost',1)
root.iconbitmap('bitcoin_sim.ico')
#----------------------------------------------------------------------------------------------------------------


def EWantedBuyPricer():
    try:
        global y
        y = int(Eentry.get()) 
        EwantedBuyprice["text"] = f"alarm to BUY is ${y}"
        Eentry.delete(0,END)
    except:
        "entry Syntax Error"


def EWantedSellPricer():
    try:
        global x 
        x = int(Eentry.get())
        EwantedSellprice["text"] = f"alarm to SELL is ${x}"
        Eentry.delete(0,END)
    except:
        "entry Syntax Error"
#----------------------------------------------------------------------------------------------------------------
LastEprice = -1.0              

def FindingPriceLoop():    
    global LastEprice
    
    
    
    eprice = float(find_crypto("ETH"))
    
    if eprice != LastEprice:
        eth_price['text']=f"ETH ${eprice}"
        eth_change['text']="change in price:\n${:.2f}".format(eprice - LastEprice)
        
        LastEprice = eprice
    try:
        if y >= eprice:
            print("BUY BUY BUY BUY")
            sound='bombs.mp3'
            playsound(sound)  

        if x <= eprice:
            print("BUY BUY BUY BUY")
            sound='bombs.mp3'
            playsound(sound)  
    except:
        print("y or x not valid")
    root.after(500,FindingPriceLoop)     
        
 
    

#----------------------------------------------------------------------------------------------------------------

eth_frame = Frame(root,bg="#130E43",bd=3)
eth_frame.place(relheight=1, relwidth=1.0)

eth_price = Label(eth_frame,bg="#64BBD3",font=('losta masta',30),bd=2)
eth_price.place(relheight=0.25,relwidth=0.5)

eth_change= Label(eth_frame,bg="#64BBD3",font=('losta masta',25),bd=2)
eth_change.place(rely=0.26,relheight=0.5,relwidth=0.5)

ethbuybut = Button(eth_frame,text="BUY",bg="#008AB3",font=18,bd=2,relief=GROOVE,command=lambda:EWantedBuyPricer() )
ethbuybut.place(relx=0.9,relwidth=0.1,relheight=0.25)

ethsellbut = Button(eth_frame,text="SELL",bg="#008AB3",font=18,bd=2,relief=GROOVE,command=lambda:EWantedSellPricer() )
ethsellbut.place(relx=0.9,rely=0.25,relwidth=0.1,relheight=0.25)

Eentry = Entry(eth_frame,bg="#64BBD3",font=('losta masta',25),bd=2,relief=GROOVE)
Eentry.place(relx=0.5,relheight=0.5,relwidth=0.4)

EwantedBuyprice = Label(eth_frame,bg="#64BBD3",font=('losta masta',18),bd=4,relief=GROOVE)
EwantedBuyprice.place(rely=0.5,relx=0.5,relheight=0.25,relwidth=0.5)

EwantedSellprice = Label(eth_frame,bg="#64BBD3",font=('losta masta',18),bd=4,relief=GROOVE)
EwantedSellprice.place(rely=0.75,relx=0.5,relheight=0.25,relwidth=0.5)
#----------------------------------------------------------------------------------------------------------------    




FindingPriceLoop()
root.mainloop()