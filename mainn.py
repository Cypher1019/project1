from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
#Functions
def reset():
    textReceipt.delete(1.0,END)
    e_burger.set('0')
    e_pasta.set('0')
    e_pizza.set('0')
    e_fries.set('0')
    e_wings.set('0')
    e_seafood.set('0')
    e_sandwich.set('0')
    e_rolls.set('0')
    e_friedchicken.set('0')

    e_soda.set('0')
    e_coffee.set('0')
    e_tea.set('0')
    e_icedtea.set('0')
    e_milkshakes.set('0')
    e_beer.set('0')
    e_whiskey.set('0')
    e_wine.set('0')
    e_tequila.set('0')

    e_donut.set('0')
    e_pastries.set('0')
    e_icecream.set('0')
    e_smoothies.set('0')
    e_popsicles.set('0')
    e_frozenyogurt.set('0')
    e_cheesecake.set('0')
    e_cookies.set('0')
    e_candies.set('0')

    textburger.config(state=DISABLED)
    textpasta.config(state=DISABLED)
    textpizza.config(state=DISABLED)
    textfries.config(state=DISABLED)
    textwings.config(state=DISABLED)
    textseafood.config(state=DISABLED)
    textsandwich.config(state=DISABLED)
    textrolls.config(state=DISABLED)
    textfriedchicken.config(state=DISABLED)

    textsoda.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    texttea.config(state=DISABLED)
    texticedtea.config(state=DISABLED)
    textmilkshakes.config(state=DISABLED)
    textbeer.config(state=DISABLED)
    textwhiskey.config(state=DISABLED)
    textwine.config(state=DISABLED)
    texttequila.config(state=DISABLED)

    textdonut.config(state=DISABLED)
    textpastries.config(state=DISABLED)
    texticecream.config(state=DISABLED)
    textsmoothies.config(state=DISABLED)
    textpopsicles.config(state=DISABLED)
    textfrozenyogurt.config(state=DISABLED)
    textcheesecake.config(state=DISABLED)
    textcandies.config(state=DISABLED)
    textcookies.config(state=DISABLED)

    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')   
    var8.set('0')   
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')
    var13.set('0')
    var14.set('0')
    var15.set('0')
    var16.set('0')
    var17.set('0')
    var18.set('0')
    var19.set('0')
    var20.set('0')
    var21.set('0')
    var22.set('0')
    var23.set('0')
    var24.set('0')
    var25.set('0')
    var26.set('0')
    var27.set('0')

    costoffoodvar.set('')
    
    costofdrinksvar.set('')
        
    costofdessertvar.set('')
        
    subtotalvar.set('')
        
    servicetaxvar.set('')
        
    totalcostvar.set('')





def save():
    url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    
    bill_data= textReceipt.get(1.0, END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information', 'Your Bill is Successfully Saved')




def receipt():
    global billnumber, date
    textReceipt.delete(1.0, END)
    x = random.randint(1001,100100)
    billnumber = "BILL" + str(x)
    date = time.strftime('%d/%m/%Y')
    textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber+'\t\t' + date + '\n' )
    textReceipt.insert(END, '******************************************')
    textReceipt.insert(END, 'Items:\t\t Cost of Items(Rs)\n')
    textReceipt.insert(END, '******************************************')
    if e_burger.get()!='0':
        textReceipt.insert(END, f'Burger\t\t\t{int(e_burger.get())*500}\n\n')
    if e_pasta.get()!='0':
        textReceipt.insert(END, f'Pasta\t\t\t{int(e_pasta.get())*450}\n\n')
    if e_pizza.get()!='0':
        textReceipt.insert(END, f'Pizza\t\t\t{int(e_pizza.get())*700}\n\n')
    if e_fries.get()!='0':
        textReceipt.insert(END, f'Fries\t\t\t{int(e_fries.get())*250}\n\n')
    if e_wings.get()!='0':
        textReceipt.insert(END, f'Wings\t\t\t{int(e_wings.get())*350}\n\n')
    if e_seafood.get()!='0':
        textReceipt.insert(END, f'Seafood\t\t\t{int(e_seafood.get())*400}\n\n')
    if e_sandwich.get()!='0':
        textReceipt.insert(END, f'Sandwich\t\t\t{int(e_sandwich.get())*300}\n\n')
    if e_rolls.get()!='0':
        textReceipt.insert(END, f'Rolls\t\t\t{int(e_rolls.get())*250}\n\n')
    if e_friedchicken.get()!='0':
        textReceipt.insert(END, f'FriedChicken\t\t\t{int(e_friedchicken.get())*600}\n\n')
    if e_soda.get()!='0':
        textReceipt.insert(END, f'Soda\t\t\t{int(e_soda.get())*80}\n\n')
    if e_coffee.get()!='0':
        textReceipt.insert(END, f'Coffee\t\t\t{int(e_burger.get())*150}\n\n')
    if e_tea.get()!='0':
        textReceipt.insert(END, f'Burger\t\t\t{int(e_tea.get())*120}\n\n')
    if e_icedtea.get()!='0':
        textReceipt.insert(END, f'IcedTea\t\t\t{int(e_icedtea.get())*250}\n\n')
    if e_milkshakes.get()!='0':
        textReceipt.insert(END, f'Milkshakes\t\t\t{int(e_milkshakes.get())*250}\n\n')
    if e_beer.get()!='0':
        textReceipt.insert(END, f'Beer\t\t\t{int(e_beer.get())*550}\n\n')
    if e_whiskey.get()!='0':
        textReceipt.insert(END, f'Whiskey\t\t\t{int(e_whiskey.get())*750}\n\n')
    if e_wine.get()!='0':
        textReceipt.insert(END, f'Wine\t\t\t{int(e_wine.get())*900}\n\n')
    if e_tequila.get()!='0':
        textReceipt.insert(END, f'Tequila\t\t\t{int(e_tequila.get())*1000}\n\n')
    if e_donut.get()!='0':
        textReceipt.insert(END, f'Donut\t\t\t{int(e_donut.get())*150}\n\n')
    if e_pastries.get()!='0':
        textReceipt.insert(END, f'Pastries\t\t\t{int(e_pastries.get())*150}\n\n')
    if e_icecream.get()!='0':
        textReceipt.insert(END, f'Icecream\t\t\t{int(e_icecream.get())*180}\n\n')
    if e_smoothies.get()!='0':
        textReceipt.insert(END, f'Smoothies\t\t\t{int(e_smoothies.get())*250}\n\n')
    if e_popsicles.get()!='0':
        textReceipt.insert(END, f'Popsicles\t\t\t{int(e_popsicles.get())*100}\n\n')
    if e_frozenyogurt.get()!='0':
        textReceipt.insert(END, f'Frozenyogurt\t\t\t{int(e_frozenyogurt.get())*200}\n\n')
    if e_cookies.get()!='0':
        textReceipt.insert(END, f'Cookies\t\t\t{int(e_cookies.get())*250}\n\n')
    if e_candies.get()!='0':
        textReceipt.insert(END, f'Candies\t\t\t{int(e_candies.get())*250}\n\n')

    textReceipt.insert(END, '******************************************')
    if costoffoodvar.get()!=' 0 RS':
        textReceipt.insert(END, f'Cost of Food\t\t\t{priceofFood}Rs\n\n')
    if costofdrinksvar.get()!=' 0 RS':
        textReceipt.insert(END, f'Cost of Drinks\t\t\t{priceofDrinks}Rs\n\n')
    if costofdessertvar.get()!=' 0 RS':    
        textReceipt.insert(END, f'Cost of Dessert\t\t\t{priceofDessert}Rs\n\n')

    textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}RS\n\n')
    textReceipt.insert(END, f'ServiceTax\t\t\t{250}RS\n\n')
    textReceipt.insert(END, f'TotalCost\t\t\t{subtotalofItems + 250}RS\n\n')
    textReceipt.insert(END, '******************************************')




def totalcost():
    global priceofFood,priceofDrinks,priceofDessert,subtotalofItems
   




    item1 = int(e_burger.get())
    item2 = int(e_pasta.get())
    item3 = int(e_pizza.get())
    item4 = int(e_fries.get())
    item5 = int(e_wings.get())
    item6 = int(e_seafood.get())
    item7 = int(e_sandwich.get())
    item8 = int(e_rolls.get())
    item9 = int(e_friedchicken.get())


    item10 = int(e_soda.get())
    item11 = int(e_coffee.get())
    item12 = int(e_tea.get())
    item13 = int(e_icedtea.get())
    item14 = int(e_milkshakes.get())
    item15 = int(e_beer.get())
    item16 = int(e_whiskey.get())
    item17 = int(e_wine.get())
    item18 = int(e_tequila.get())

    item19 = int(e_donut.get())
    item20 = int(e_pastries.get())
    item21 = int(e_icecream.get())
    item22 = int(e_smoothies.get())
    item23 = int(e_popsicles.get())
    item24 = int(e_frozenyogurt.get())
    item25 = int(e_cheesecake.get())
    item26 = int(e_cookies.get())
    item27 = int(e_candies.get())


    priceofFood=(item1*500)+(item2*450)+(item3*700)+(item4*250)+(item5*350)+(item6*400)+(item7*300)+(item8*250)+(item9*600)
    priceofDrinks=(item10*80)+(item11*150)+(item12*120)+(item13*250)+(item14*250)+(item15*550)+(item16*750)+(item17*900)+(item18*1000)
    priceofDessert=(item19*150)+(item20*150)+(item21*180)+(item22*250)+(item23*100)+(item24*200)+(item25*200)+(item26*250+(item27*250))

    costoffoodvar.set(str(priceofFood)+ ' Rs')
    costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
    costofdessertvar.set(str(priceofDessert)+ ' Rs')

    subtotalofItems = priceofFood + priceofDrinks + priceofDessert
    subtotalvar.set(str(subtotalofItems) + ' Rs')

    servicetaxvar.set(' 250 Rs')

    totalcost = subtotalofItems + 250 
    totalcostvar.set(str(totalcost) + ' Rs')





def burger():
    if var1.get()==1:
        textburger.config(state = NORMAL)
        textburger.delete(0, END)
        textburger.focus()
    else :
        textburger.config(state = DISABLED)
        e_burger.set('0')

def pasta():
    if var2.get()==1:
        textpasta.config(state = NORMAL)
        textpasta.delete(0, END)
        textpasta.focus()
    else :
        textpasta.config(state = DISABLED)
        e_pasta.set('0')

def pizza():
    if var3.get()==1:
        textpizza.config(state = NORMAL)
        textpizza.delete(0, END)
        textpizza.focus()
    else :
        textpizza.config(state = DISABLED)
        e_pizza.set('0')
        ('0')

def fries():
    if var4.get()==1:
        textfries.config(state = NORMAL)
        textfries.delete(0, END)
        textfries.focus()
    else :
        textfries.config(state = DISABLED)
        e_fries.set('0')

def wings():
    if var5.get()==1:
        textwings.config(state = NORMAL)
        textwings.delete(0, END)
        textwings.focus()
    else :
        textwings.config(state = DISABLED)
        e_wings.set('0')

def seafood():
    if var6.get()==1:
        textseafood.config(state = NORMAL)
        textseafood.delete(0, END)
        textseafood.focus()
    else :
        textseafood.config(state = DISABLED)
        e_seafood.set('0')

def sandwich():
    if var7.get()==1:
        textsandwich.config(state = NORMAL)
        textsandwich.delete(0, END)
        textsandwich.focus()
    else :
        textsandwich.config(state = DISABLED)
        e_sandwich.set('0')

def rolls():
    if var8.get()==1:
        textrolls.config(state = NORMAL)
        textrolls.delete(0, END)
        textrolls.focus()
    else :
        textrolls.config(state = DISABLED)
        e_rolls.set('0')

def friedchicken():
    if var9.get()==1:
        textfriedchicken.config(state = NORMAL)
        textfriedchicken.delete(0, END)
        textfriedchicken.focus()
    else :
        textfriedchicken.config(state = DISABLED)
        e_friedchicken.set('0')

def soda():
    if var10.get()==1:
        textsoda.config(state = NORMAL)
        textsoda.delete(0, END)
        textsoda.focus()
    else :
        textsoda.config(state = DISABLED)
        e_soda.set('0')

def coffee():
    if var11.get()==1:
        textcoffee.config(state = NORMAL)
        textcoffee.delete(0, END)
        textcoffee.focus()
    else :
        textcoffee.config(state = DISABLED)
        e_coffee.set('0')

def tea():
    if var12.get()==1:
        texttea.config(state = NORMAL)
        texttea.delete(0, END)
        texttea.focus()
    else :
        texttea.config(state = DISABLED)
        e_tea.set('0')

def icedtea():
    if var13.get()==1:
        texticedtea.config(state = NORMAL)
        texticedtea.delete(0, END)
        texticedtea.focus()
    else :
        texticedtea.config(state = DISABLED)
        e_icedtea.set('0')

def milkshakes():
    if var14.get()==1:
        textmilkshakes.config(state = NORMAL)
        textmilkshakes.delete(0, END)
        textmilkshakes.focus()
    else :
        textmilkshakes.config(state = DISABLED)
        e_milkshakes.set('0')

def beer():
    if var15.get()==1:
        textbeer.config(state = NORMAL)
        textbeer.delete(0, END)
        textbeer.focus()
    else :
        textbeer.config(state = DISABLED)
        e_beer.set('0')

def whiskey():
    if var16.get()==1:
        textwhiskey.config(state = NORMAL)
        textwhiskey.delete(0, END)
        textwhiskey.focus()
    else :
        textwhiskey.config(state = DISABLED)
        e_whiskey.set('0')

def wine():
    if var17.get()==1:
        textwine.config(state = NORMAL)
        textwine.delete(0, END)
        textwine.focus()
    else :
        textwine.config(state = DISABLED)
        e_wine.set('0')

def tequila():
    if var18.get()==1:
        texttequila.config(state = NORMAL)
        texttequila.delete(0, END)
        texttequila.focus()
    else :
        texttequila.config(state = DISABLED)
        e_tequila.set('0')

def donut():
    if var19.get()==1:
        textdonut.config(state = NORMAL)
        textdonut.delete(0, END)
        textdonut.focus()
    else :
        textdonut.config(state = DISABLED)
        e_donut.set('0')

def pastries():
    if var20.get()==1:
        textpastries.config(state = NORMAL)
        textpastries.delete(0, END)
        textpastries.focus()
    else :
        textpastries.config(state = DISABLED)
        e_pastries.set('0')

def icecream():
    if var21.get()==1:
        texticecream.config(state = NORMAL)
        texticecream.delete(0, END)
        texticecream.focus()
    else :
        texticecream.config(state = DISABLED)
        e_icecream.set('0')

def smoothies():
    if var22.get()==1:
        textsmoothies.config(state = NORMAL)
        textsmoothies.delete(0, END)
        textsmoothies.focus()
    else :
        textsmoothies.config(state = DISABLED)
        e_smoothies.set('0')

def popsicles():
    if var23.get()==1:
        textpopsicles.config(state = NORMAL)
        textpopsicles.delete(0, END)
        textpopsicles.focus()
    else :
        textpopsicles.config(state = DISABLED)
        e_popsicles.set('0')

def frozenyogurt():
    if var24.get()==1:
        textfrozenyogurt.config(state = NORMAL)
        textfrozenyogurt.delete(0, END)
        textfrozenyogurt.focus()
    else :
        textfrozenyogurt.config(state = DISABLED)
        e_frozenyogurt.set('0')

def cheesecake():
    if var25.get()==1:
        textcheesecake.config(state = NORMAL)
        textcheesecake.delete(0, END)
        textcheesecake.focus()
    else :
        textcheesecake.config(state = DISABLED)
        e_cheesecake.set('0')

def cookies():
    if var26.get()==1:
        textcookies.config(state = NORMAL)
        textcookies.delete(0, END)
        textcookies.focus()
    else :
        textcookies.config(state = DISABLED)
        e_cookies.set('0')

def candies():
    if var27.get()==1:
        textcandies.config(state = NORMAL)
        textcandies.delete(0, END)
        textcandies.focus()
    else :
        textcandies.config(state = DISABLED)
        e_candies.set('0')







root = Tk()

root.geometry('1270x690+0+0')



root.title("BILLING MANAGEMENT SYSTEM")

root.config(bg ='#FFFFC0')

topFrame=Frame(root, bd = 10, relief = RIDGE, bg ='#FFFFC0')
topFrame.pack(side = TOP)

labelTitle = Label(topFrame, text = 'VH BISTRO', font = ('arial', 20, 'bold'), fg='black',bd = 9, bg ='#FFFFC0', width = 51) 
labelTitle.grid(row = 0, column = 0)

#frames

menuFrame = Frame(root, bd = 10, relief = RIDGE, bg = '#FFFFC0', pady = 10)
menuFrame.pack(side = LEFT)

costFrame = Frame(menuFrame, bd = 4, relief = RIDGE, bg = '#FFFFC0' )
costFrame.pack(side = BOTTOM)

foodFrame = LabelFrame(menuFrame, text = 'Food', font = ('arial', 15, 'bold'), bd = 8, relief=RIDGE, fg = 'Black')
foodFrame.pack(side = LEFT)

drinksFrame= LabelFrame(menuFrame, text = 'Drinks', font = ('arial', 15, 'bold'), bd = 8, relief=RIDGE)
drinksFrame.pack(side = LEFT)

dessertFrame= LabelFrame(menuFrame, text = 'Dessert', font = ('arial', 15, 'bold'), bd = 8, relief=RIDGE)
dessertFrame.pack(side = LEFT)

rightFrame = Frame(root, bd = 15, relief= RIDGE, bg = '#FFFFC0')
rightFrame.pack(side = RIGHT)

calculatorFrame = Frame(rightFrame, bd = 1, relief= RIDGE, bg = '#FFFFC0')
calculatorFrame.pack()

receiptFrame = Frame(rightFrame, bd = 4, relief= RIDGE, bg = '#FFFFC0')
receiptFrame.pack()

buttonFrame = Frame(rightFrame, bd = 8, relief= RIDGE, bg = '#FFFFC0')
buttonFrame.pack()

#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()



e_burger = StringVar()
e_pasta = StringVar()
e_pizza = StringVar()
e_fries = StringVar()
e_wings = StringVar()
e_seafood = StringVar()
e_sandwich = StringVar()
e_rolls = StringVar()
e_friedchicken = StringVar()

e_soda = StringVar()
e_coffee = StringVar()
e_tea = StringVar()
e_icedtea = StringVar()
e_milkshakes = StringVar()
e_beer = StringVar()
e_whiskey = StringVar()
e_wine = StringVar()
e_tequila = StringVar()

e_donut = StringVar()
e_pastries = StringVar()
e_icecream = StringVar()
e_smoothies = StringVar()
e_popsicles = StringVar()
e_frozenyogurt = StringVar()
e_cheesecake = StringVar()
e_cookies = StringVar()
e_candies = StringVar()


costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofdessertvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()



e_burger.set('0')
e_pasta.set('0')
e_pizza.set('0')
e_fries.set('0')
e_wings.set('0')
e_seafood.set('0')
e_sandwich.set('0')
e_rolls.set('0')
e_friedchicken.set('0')

e_soda.set('0')
e_coffee.set('0')
e_tea.set('0')
e_icedtea.set('0')
e_milkshakes.set('0')
e_beer.set('0')
e_whiskey.set('0')
e_wine.set('0')
e_tequila.set('0')

e_donut.set('0')
e_pastries.set('0')
e_icecream.set('0')
e_smoothies.set('0')
e_popsicles.set('0')
e_frozenyogurt.set('0')
e_cheesecake.set('0')
e_cookies.set('0')
e_candies.set('0')

#Food

burger = Checkbutton(foodFrame, text = 'Burger', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var1, command = burger)
burger.grid(row = 0, column = 0, sticky = W)
pasta = Checkbutton(foodFrame, text = 'Pasta', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var2, command = pasta)
pasta.grid(row = 1, column = 0, sticky = W)
pizza = Checkbutton(foodFrame, text = 'Pizza', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var3, command = pizza)
pizza.grid(row = 2, column = 0, sticky = W)
fries = Checkbutton(foodFrame, text = 'Fries', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var4, command = fries)
fries.grid(row = 3, column = 0, sticky = W)
wings = Checkbutton(foodFrame, text = 'Wings', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var5, command = wings)
wings.grid(row = 4, column = 0, sticky = W)
seafood = Checkbutton(foodFrame, text = 'Seafood', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var6, command = seafood)
seafood.grid(row = 5, column = 0, sticky = W)
sandwich = Checkbutton(foodFrame, text = 'Sandwich', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var7, command =  sandwich)
sandwich.grid(row = 6, column = 0, sticky = W)
rolls = Checkbutton(foodFrame, text = 'Rolls', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var8, command = rolls)
rolls.grid(row = 7, column = 0, sticky = W)
friedchicken = Checkbutton(foodFrame, text = 'Fried Chicken', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var9, command = friedchicken)
friedchicken.grid(row = 8, column = 0, sticky = W)

#Entry Fields for Food Items

textburger=Entry(foodFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_burger)
textburger.grid(row= 0, column = 1)
textpasta=Entry(foodFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_pasta)
textpasta.grid(row= 1, column = 1)
textpizza=Entry(foodFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_pizza)
textpizza.grid(row= 2, column = 1)
textfries=Entry(foodFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_fries)
textfries.grid(row= 3, column = 1)
textwings=Entry(foodFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_wings)
textwings.grid(row= 4, column = 1)
textseafood=Entry(foodFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_seafood)
textseafood.grid(row= 5, column = 1)
textsandwich=Entry(foodFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_sandwich)
textsandwich.grid(row= 6, column = 1)
textrolls=Entry(foodFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_rolls)
textrolls.grid(row= 7, column = 1)
textfriedchicken=Entry(foodFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_friedchicken)
textfriedchicken.grid(row= 8, column = 1)


#Drinks

soda = Checkbutton(drinksFrame, text = 'Soda', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var10, command = soda )
soda.grid(row = 0, column = 0, sticky = W)
coffee = Checkbutton(drinksFrame, text = 'Coffee', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var11, command = coffee)
coffee.grid(row = 1, column = 0, sticky = W)
tea = Checkbutton(drinksFrame, text = 'Tea', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var12, command = tea)
tea.grid(row = 2, column = 0, sticky = W)
icedtea = Checkbutton(drinksFrame, text = 'Iced Tea', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var13, command = icedtea)
icedtea.grid(row = 3, column = 0, sticky = W)
milkshakes = Checkbutton(drinksFrame, text = 'Milkshakes', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var14, command = milkshakes)
milkshakes.grid(row = 4, column = 0, sticky = W)
beer = Checkbutton(drinksFrame, text = 'Beer', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var15, command = beer)
beer.grid(row = 5, column = 0, sticky = W)
whiskey = Checkbutton(drinksFrame, text = 'Whiskey', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var16, command = whiskey)
whiskey.grid(row = 6, column = 0, sticky = W)
wine = Checkbutton(drinksFrame, text = 'Wine', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var17, command = wine)
wine.grid(row = 7, column = 0, sticky = W)
tequila = Checkbutton(drinksFrame, text = 'Tequila', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var18, command = tequila)
tequila.grid(row = 8, column = 0, sticky = W)

#Entry fields for drink item

textsoda=Entry(drinksFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_soda)
textsoda.grid(row= 0, column = 1)
textcoffee=Entry(drinksFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_coffee)
textcoffee.grid(row= 1, column = 1)
texttea=Entry(drinksFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_tea)
texttea.grid(row= 2, column = 1)
texticedtea=Entry(drinksFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_icedtea)
texticedtea.grid(row= 3, column = 1)
textmilkshakes=Entry(drinksFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_milkshakes)
textmilkshakes.grid(row= 4, column = 1)
textbeer=Entry(drinksFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_beer)
textbeer.grid(row= 5, column = 1)
textwhiskey=Entry(drinksFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_whiskey)
textwhiskey.grid(row= 6, column = 1)
textwine=Entry(drinksFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_wine)
textwine.grid(row= 7, column = 1)
texttequila=Entry(drinksFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_tequila)
texttequila.grid(row= 8, column = 1)


#Dessert
donut = Checkbutton(dessertFrame, text = 'Donut', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var19, command = donut)
donut.grid(row = 0, column = 0, sticky = W)
pastries = Checkbutton(dessertFrame, text = 'Pastries', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var20, command = pastries)
pastries.grid(row = 1, column = 0, sticky = W)
icecream = Checkbutton(dessertFrame, text = 'Ice Cream', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var21, command = icecream)
icecream.grid(row = 2, column = 0, sticky = W)
smoothies = Checkbutton(dessertFrame, text = 'Smoothies', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var22, command = smoothies)
smoothies.grid(row = 3, column = 0, sticky = W)
popsicles = Checkbutton(dessertFrame, text = 'Popsicles', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var23, command = popsicles)
popsicles.grid(row = 4, column = 0, sticky = W)
frozenyogurt = Checkbutton(dessertFrame, text = 'Frozen Yogurt', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var24, command = frozenyogurt)
frozenyogurt.grid(row = 5, column = 0, sticky = W)
cheesecake = Checkbutton(dessertFrame, text = 'Cheesecake', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var25, command = cheesecake)
cheesecake.grid(row = 6, column = 0, sticky = W)
cookies = Checkbutton(dessertFrame, text = 'Cookies', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var26, command = cookies)
cookies.grid(row = 7, column = 0, sticky = W)
candies = Checkbutton(dessertFrame, text = 'Candies', font =('arial', 18, 'bold'), onvalue =1, offvalue =0, variable= var27, command = candies)
candies.grid(row = 8, column = 0, sticky = W)


#Entry fields for desserts

textdonut=Entry(dessertFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_donut)
textdonut.grid(row= 0, column = 1)
textpastries=Entry(dessertFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_pastries)
textpastries.grid(row= 1, column = 1)
texticecream=Entry(dessertFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_icecream)
texticecream.grid(row= 2, column = 1)
textsmoothies=Entry(dessertFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_smoothies)
textsmoothies.grid(row= 3, column = 1)
textpopsicles=Entry(dessertFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_popsicles)
textpopsicles.grid(row= 4, column = 1)
textfrozenyogurt=Entry(dessertFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_frozenyogurt)
textfrozenyogurt.grid(row= 5, column = 1)
textcheesecake=Entry(dessertFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_cheesecake)
textcheesecake.grid(row= 6, column = 1)
textcookies=Entry(dessertFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_cookies)
textcookies.grid(row= 7, column = 1)
textcandies=Entry(dessertFrame, font = ('arial', 18, 'bold'), bd = 7, width = 6, state = DISABLED, textvariable = e_candies)
textcandies.grid(row= 8, column = 1)


#Cost labels & Entry fields
LabelCostofFood = Label(costFrame, text = 'Cost of Food', font =('arial', 12, 'bold'), bg = '#FFFFC0',)
LabelCostofFood.grid(row = 0, column = 0)
textCostofFood = Entry(costFrame, font = ('arial', 12, 'bold'), bd = 5, width = 12, state = 'readonly', textvariable = costoffoodvar)
textCostofFood.grid(row = 0, column = 1, padx = 30)

LabelCostofDrinks = Label(costFrame, text = 'Cost of Drinks', font =('arial', 12, 'bold'), bg = '#FFFFC0',)
LabelCostofDrinks.grid(row = 1, column = 0)
textCostofDrinks = Entry(costFrame, font = ('arial', 16, 'bold'), bd = 6, width = 12, state = 'readonly', textvariable = costofdrinksvar)
textCostofDrinks.grid(row = 1, column = 1, padx = 30)

LabelCostofDessert = Label(costFrame, text = 'Cost of Dessert', font =('arial', 12, 'bold'), bg = '#FFFFC0',)
LabelCostofDessert.grid(row = 2, column = 0)
textCostofDessert = Entry(costFrame, font = ('arial', 12, 'bold'), bd = 5, width = 12, state = 'readonly', textvariable = costofdessertvar)
textCostofDessert.grid(row = 2, column = 1, padx = 30)

LabelSubTotal= Label(costFrame, text = 'Sub Total', font =('arial', 12, 'bold'), bg = '#FFFFC0',)
LabelSubTotal.grid(row = 0, column = 2)
textSubTotal = Entry(costFrame, font = ('arial', 12, 'bold'), bd = 5, width = 12, state = 'readonly', textvariable = subtotalvar)
textSubTotal.grid(row = 0, column = 3, padx = 30)

LabelServiceTax= Label(costFrame, text = 'Service Tax', font =('arial', 12, 'bold'), bg = '#FFFFC0',)
LabelServiceTax.grid(row = 1, column = 2)
textServiceTax = Entry(costFrame, font = ('arial', 12, 'bold'), bd = 5, width = 12, state = 'readonly', textvariable = servicetaxvar)
textServiceTax.grid(row = 1, column = 3, padx = 30)

LabelTotalCost= Label(costFrame, text = 'Total Cost', font =('arial', 12, 'bold'), bg = '#FFFFC0',)
LabelTotalCost.grid(row =2, column = 2)
textTotalCost = Entry(costFrame, font = ('arial', 12, 'bold'), bd = 5, width = 12, state = 'readonly', textvariable = totalcostvar)
textTotalCost.grid(row = 2, column = 3, padx = 30)


#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',10,'bold'),fg='white',bg='black',bd=2, command = totalcost)
buttonTotal.grid(row=0,column=0)
buttonReceipt=Button(buttonFrame, text = 'Receipt', font = ('arial', 10, 'bold'), fg = 'white', bg = 'black',bd = 2, command = receipt)
buttonReceipt.grid(row=0,column=1)
buttonSave=Button(buttonFrame, text = 'Save', font = ('arial', 10, 'bold'), fg = 'white', bg = 'black', bd = 2, command = save )
buttonSave.grid(row=0,column=2)

buttonReset=Button(buttonFrame, text = 'Reset', font = ('arial', 10, 'bold'), fg = 'white', bg = 'black', bd = 2, command = reset)
buttonReset.grid(row=0,column=4)



#textarea for receipt

textReceipt = Text(receiptFrame, font = ('arial', 12, 'bold'), bd = 3, width = 28, height = 18)
textReceipt.grid(row = 0, column = 0)

#Calculator
operator = ''
def buttonClick(numbers):
    global operator
    operator = operator + numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)

def clear():
    global operator
    operator = ''
    calculatorField.delete(0, END)

def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0, result)
    operator = ''

calculatorField = Entry(calculatorFrame, font = ('arila',10, 'bold'), width = 32, bd = 4)
calculatorField.grid(row = 0, column = 0, columnspan = 4)
button7 = Button(calculatorFrame, text = '7', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('7'))
button7.grid(row = 1, column = 0)
button8 = Button(calculatorFrame, text = '8', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6 ,command = lambda:buttonClick('8'))
button8.grid(row = 1, column = 1) 
button9 = Button(calculatorFrame, text = '9', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('9'))
button9.grid(row = 1, column = 2)
buttonPlus = Button(calculatorFrame, text = '+', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('+'))
buttonPlus.grid(row = 1, column = 3)
button4 = Button(calculatorFrame, text = '4', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('4'))
button4.grid(row = 2, column = 0)
button5 = Button(calculatorFrame, text = '5', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('5'))
button5.grid(row = 2, column = 1)
button6 = Button(calculatorFrame, text = '6', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('6'))
button6.grid(row = 2, column = 2)
buttonMinus = Button(calculatorFrame, text = '-', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('-'))
buttonMinus.grid(row = 2, column = 3)
button1 = Button(calculatorFrame, text = '1', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('1'))
button1.grid(row = 3, column = 0)
button2 = Button(calculatorFrame, text = '2', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('2'))
button2.grid(row = 3, column = 1)
button3 = Button(calculatorFrame, text = '3', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('3'))
button3.grid(row = 3, column = 2)
buttonMult = Button(calculatorFrame, text = '*', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('*'))
buttonMult.grid(row = 3, column = 3)
buttonAns = Button(calculatorFrame, text = 'Ans', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = answer )
buttonAns.grid(row = 4, column = 0)
buttonClear = Button(calculatorFrame, text = 'Clear', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = clear)
buttonClear.grid(row = 4, column = 1)
button0 = Button(calculatorFrame, text = '0', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('0'))
button0.grid(row = 4, column = 2)
buttonDiv = Button(calculatorFrame, text = '/', font = ('arial', 8 , 'bold'), fg ='white', bg = 'black', bd = 4, width= 6, command = lambda:buttonClick('/'))
buttonDiv.grid(row = 4, column = 3)



















root.mainloop()