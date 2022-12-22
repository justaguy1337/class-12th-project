import pickle
import os
import time


print("\n\n\t\t\tWelcome to Maruti Showrooms\n")
print("What service of ours would you like to try?")


#METHOD FOR SELLING CARS

def sell_heading():  #METHOD FOR SELLING CARS HEADING
    print('-'*76)
    print('Car Name\t','Manufacture Year','\tCondtion','\tExpected Price')
    print('-'*76)

def sell_file_write():   #METHOD FOR SELLING CARS WRITING
    f=open('sell.txt','w')
    cr= input("Enter you car name: ")
    try:
        mft=int(input("Enter manufacture year: "))
    except ValueError:
        print("Please use Integers only")
        mft=int(input("Enter manufacture year: "))
    cnd=input("Enter your car's condition(Good/Avg/Bad): ")
    cnd=cnd.lower()
    exp='good'
    if cnd == 'good':
        exp= 'Rs.5L-Max'
    elif cnd=='avg':
        exp= 'Rs.2L-Rs.3.5L'
    elif cnd== 'bad':
        exp = 'Rs.50K-Rs.1.8L'
    f.write('\n'+cr+'\t\t'+str(mft)+'\t\t'+cnd+'\t\t'+exp+'\n')
    f.close()

def sell_file_read():    #METHOD FOR SELLING CARS READING
    sell_heading()
    f=open('sell.txt','r')
    c = f.read()
    word = c.split()
    for i in word :
        if i[0].islower() :
            x =i.capitalize() 
            print (x,end= "\t\t")
            time.sleep(.5)
        else :
            print (i,end= "\t\t\t")
            time.sleep(.1)
    f.close()
    print("\n")
    print('-'*76)                

def sell():
    print('\n\n')
    sell_file_write()
    sell_file_read()




#METHOD FOR BUYING CARS

f = open("buy.dat","wb")            #METHOD FOR BUYING CARS WRITING
rec = []
rec.append([int(201),"Alto\t",int(350000),int(5)])
pickle.dump(rec,f)
rec = []
rec.append([int(202),"Ertiga",int(600000),int(5)])
pickle.dump(rec,f)
rec = []
rec.append([int(203),"Baleno",int(700000),int(5)])
pickle.dump(rec,f)
rec = []
rec.append([int(204),"Dzire\t",int(650000),int(5)])
pickle.dump(rec,f)
rec = []
rec.append([int(205),"Ciaz\t",int(1200000),int(5)])
pickle.dump(rec,f)
rec = []
rec.append([int(206),"Vitara",int(1000000),int(5)])
pickle.dump(rec,f)
rec = []
rec.append([int(207),"S-Cross",int(900000),int(5)])
pickle.dump(rec,f)
rec = []
rec.append([int(208),"Brezza",int(800000),int(5)])
pickle.dump(rec,f)
f.close()

def heading( ) :    #METHOD FOR BUYING CARS DISPLAY HEADING
    print("-"*70)
    print("Car Code","\t","Model","\t\t\t","Price","\t\t","Quantity")
    print("-"*70)

def bill_heading( ) :    #METHOD FOR BUYING CARS BILL HEADING
    print("\n")
    print("-"*40)
    print("Code","\t\t","Name","\t\t","Price")
    print("-"*40)
    

def buy_car_file_read( ):    #METHOD FOR BUYING CARS READING
    print("Available cars in Showroom")
    heading( )
    f = open("buy.dat","rb")
    rec=pickle.load(f)
    try:
        while True:
            for re in rec:
                code= re[0]
                model=re[1]
                price=re[2]
                quantity=re[3]
                print(code,"\t\t",model,"\t\t",price,"\t",quantity)
                time.sleep(.1)
            rec=pickle.load(f)
    except EOFError:
             print("-"*70)
    f.close()
def bill():             #METHOD FOR BUYING CARS BILL WITH LOGIC
    f=open("buy.dat","rb")
    g=open("temp.dat","wb")
    pc=int(input("Enter the Car Code which you want to buy: "))
    try:
        rec= pickle.load(f)
        while True:
            for record in rec:
                if record[0]!= pc :
                    pickle.dump(rec,g)
                else:
                    record[3]=record[3]-1
                    pickle.dump(rec,g)
            rec= pickle.load(f)
    except EOFError:
        print()
    f.close()
    g.close()
    os.remove("buy.dat")
    os.rename("temp.dat","buy.dat")


    na=input("Enter your Name : ")          #METHOD FOR BUYING CARS USERS'S DATA
    na=na.upper()
    add=input("Enter your Address : ")
    add=add.upper()
    pno=int(input("Enter your phone number : "))
    adh=int(input("Enter your Adhar No : "))
    pan=int(input("Enter your Pan No : "))
    print("\n")
    print("\t\tFinal Bill")
    print("\n")
    print("*"*40)
    print("Billing Details")
    print("*"*40)
    print("Name : ",na)
    print("Address : ",add)
    print("Phone No : ",pno)
    print("Adhar No : ",adh)
    print("Pan No : ",pan)
    print("*"*40)

    
    bill_heading( )
    f=open("buy.dat","rb")        #METHOD FOR BUYING CARS BILL DISPLAY
    try:
        rec= pickle.load(f)
        while True:
            for i in rec:
                if i[0]== pc :
                    print(i[0],"\t\t",i[1],"\t",i[2])
                else:
                    continue
            rec= pickle.load(f)
    except EOFError:
        print("-"*40)
    

def buy():
    print('\n\n')
    print("\t\t\tMaruti Showrooms\n")
    buy_car_file_read()
    bill()
#METHOD FOR CAR SERVICING

def service_heading():       #METHOD FOR CAR SERVICING HEADING
    print('-'*55)
    print('Car Name','\tManufacture Year','\tExpected Price')
    print('-'*55)

def service_file_write():       #METHOD FOR CAR SERVICING WRITING
    f=open('service.txt','w')
    cr= input("Enter you car name: ")
    try:
        mft=int(input("Enter manufacture year: "))
    except ValueError:
        print("Please use Integers only")
    exp=0
    if mft <= 2000:
        exp = exp+30000
    elif mft == 2001 and mft <=2010:
        exp = exp+20000
    else:
        exp = exp+10000
    f.write('\n'+cr+'\t\t'+str(mft)+'\t\t'+'Rs.'+str(exp)+'\n')
    f.close()

def service_file_read():       #METHOD FOR CAR SERVICING READING
    service_heading()
    f=open('service.txt','r')
    c = f.read()
    word = c.split()
    for i in word :
        if i[0].islower() :
            x =i.capitalize() 
            print (x,end= "\t\t")
            time.sleep(.5)
        else :
            print (i,end= "\t\t\t")
            time.sleep(.1)
    f.close()
    print("\n")
    print('-'*55)

def service():
    print('\n\n')
    service_file_write()
    service_file_read()

    
dict = {1:sell, 2:buy, 3:service}
choice = 0
ans = 'y'
while ans == 'y' :
    print('\n1.Sell your old car')
    print('2.Buy a new car')
    print('3.Service your vehicle')
    choice = int(input('\nPlease enter your choice: '))
    dict.get(choice)()
    ans = input('\nDo you want to do something else?\n(y/n)--->')
    ans=ans.lower()

if ans != 'y':
    print('\n\t\t\tThank You, Have a nice day')
