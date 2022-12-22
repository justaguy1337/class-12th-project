import random

def arrival():
    lmao="drop table arrival"
    cursor.execute(lmao)

    table = "create table arrival(Time time NOT NULL,\
                                FlightNo char(20) NOT NULL UNIQUE ,\
                                Flight char(20) NOT NULL,\
                                Depart char(30) NOT NULL,\
                                Status char(20) NOT NULL);"
    cursor.execute(table)
    fly = "INSERT INTO arrival(Time,FlightNo,Flight, Depart,Status)VALUES(%s, %s, %s, %s, %s)"
    rows = [('063000','AI23', 'Air India','Bhopal',"On-Time")
            ,('143000','SJ12','Spice Jet','Bhopal',"On-Time")
            ,('200000','UK20','Vistara','Bhopal',"On-Time")
            ,('204500','AA01','Air Asia','Mumbai',"Delay")
            ,('170000','AI11','Air India','Mumbai',"On-Time")
            ,('084500','SJ10', 'Spice Jet', 'Mumbai',"Delay")
            ,('233000','SJ01','Spice Jet','Bengaluru',"Delay")
            ,('135000','6E67', 'Indigo','Chennai',"On-Time")
            ,('000000','6E04','Indigo','Chennai',"On-Time")
            ,('112000','AA72','Air Asia','Chennai',"On-Time")
            ,('161000','SJ33', 'Spice Jet','Lucknow ',"On-Time")
            ,('193300','6E56', 'Indigo','Ahmedabad',"Delay")
            ,('122000','AA91','Air Asia','Ahmedabad',"Delay")
            ,('073000','UK31','Vistara','Ahmedabad',"On-Time")
            ,('214500','AA55','Air Asia','Kolkata',"On-Time")
            ,('100000','AI12','Air India','Kolkata',"On-Time")
            ,('220000','AI27','Air India','Kolkata',"On-Time")
            ,('002400','SJ29','Spice Jet','Varanasi',"Delay")
            ,('113000','UK41','Vistara','Varanasi',"On-Time")
            ,('184500','AA43','Air Asia','Varanasi',"On-Time")
            ,('045600','AI22','Air India','Hyderabad',"Delay")
            ,('170800','AA98', 'Air Asia','Lucknow ',"On-Time")]
    cursor.executemany(fly,rows)
    mcon.commit()

    print('-'*80)
    print('Time\t\tFlightNo\tFlight\t\tDepart\t\tStatus')
    print('-'*80)
    query = "select * from arrival order by time"
    cursor.execute(query)
    record = cursor.fetchall()
    for col in record:
        print(col[0],'\t' , col[1], '\t\t', col[2], '\t', col[3],'\t',col[4])
    print('-'*80)
        
    
def departure():
    lol="drop table departure"
    cursor.execute(lol)
    
    table = "create table departure(Time time NOT NULL,\
                                FlightNo char(20) NOT NULL UNIQUE ,\
                                Flight char(20) NOT NULL,\
                                Departure char(30) NOT NULL,\
                                GateNo char(2) NOT NULL, \
                                Status char(20) NOT NULL);"
    cursor.execute(table)
    cmd = "insert into departure(Time, FlightNo, Flight,Departure, GateNo, Status) VALUES(%s , %s , %s , %s , %s , %s);"
    val = [('130000','6E01','Indigo','Bengaluru',3,'Boarding')
          ,('132000','UK86','Vistara','Bengaluru',6,'Boarding')
          ,('134400','6E32','Indigo','Lucknow ',7,'Boarding')]
    cursor.executemany(cmd,val)
    mcon.commit()
    print('-'*80)
    print('Time\t\tFlightNo\tFlight\t\tDepart\t\tGateNo')
    print('-'*80)
    query = "select * from departure order by time"
    cursor.execute(query)
    record = cursor.fetchall()
    for col in record:
        print(col[0],'\t' , col[1], '\t\t', col[2], '\t', col[3],'\t',col[4])
    print('-'*80) 


def heading1():
    print('\n')
    print("\t\t\tYour Boarding Pass")
    print('_'*80)
    print("\t Name\t\t\t Age\t\t SeatNo")


def heading2():
    print("\n\n")
    print("\t FlightNo\t Flight\t\t\t Destination\t\t Time")

    
def available():
    print("\n\t\tList of Available Flights Today\n")
    lmao="drop table available"
    cursor.execute(lmao)
    c = "create table available(FlightNo char(20) NOT NULL unique ,\
                                Flight char(20) NOT NULL,\
                                Destination char(30) NOT NULL,\
                                Time time NOT NULL,\
                                Price integer NOT NULL)"
    cursor.execute(c)
    fly = "INSERT INTO available(FlightNo,Flight, Destination, Time, Price)VALUES(%s, %s, %s, %s, %s)"
    rows = [('AI23', 'Air India','Bhopal','063000',9000)
            ,('SJ12','Spice Jet','Bhopal','143000',14000)
            ,('UK20','Vistara','Bhopal','200000',10000)
            ,('AA01','Air Asia','Mumbai','204500',9000)
            ,('AI11','Air India','Mumbai','170000',12000)
            ,('SJ10', 'Spice Jet', 'Mumbai','084500',10000)
            ,('UK86', 'Vistara','Bengaluru','132000',15000)
            ,('SJ01','Spice Jet','Bengaluru','233000',11000)
            ,('6E01','Indigo','Bengaluru','130000',16000)
            ,('6E67', 'Indigo','Chennai','135000',13000)
            ,('6E04','Indigo','Chennai','000000',15000)
            ,('AA72','Air Asia','Chennai','112000',9000)
            ,('SJ33', 'Spice Jet','Lucknow ','161000',20000)
            ,('6E56', 'Indigo','Ahmedabad','193300',17000)
            ,('AA91','Air Asia','Ahmedabad','122000',17000)
            ,('UK31','Vistara','Ahmedabad','073000',11000)
            ,('AA55','Air Asia','Kolkata','214500',8500)
            ,('AI12','Air India','Kolkata','100000',9500)
            ,('AI27','Air India','Kolkata','220000',9750)
            ,('SJ29','Spice Jet','Varanasi','002400',11000)
            ,('UK41','Vistara','Varanasi','113000',11000)
            ,('AA43','Air Asia','Varanasi','184500',12000)
            ,('AI22','Air India','Hyderabad','045600',9750)
            ,('6E32', 'Indigo','Lucknow ','134400',15600)
            ,('AA98', 'Air Asia','Lucknow ','170800',23500)]
    cursor.executemany(fly,rows)
    mcon.commit()
    print('-'*80)
    print('FlightNo\tFlight\t\t\tDestination\t  Time\t\t Price')
    print('-'*80)
    query = "select * from available order by time"
    cursor.execute(query)
    record = cursor.fetchall()
    for col in record:
        print(col[0],'\t\t' , col[1], '\t\t', col[2], '\t', col[3],'\t',col[4])
    print('-'*80)
    pc=input("\nEnter FlightNo you want to book: ")
    pc=pc.upper()
    lmao="drop table booking"
    cursor.execute(lmao)
    c = "create table booking(name char(30) not null, age integer not null,seat integer not null unique);"
    cursor.execute(c)
    list = []
    rec = int(input('\nHow many tickets do you want book?: '))
    for i in range (0,rec):
        a = []
        name = input('\nEnter your name : ') ; a.append(name)
        age = int(input('\nEnter your age number: ')) ; a.append(age)
        seat = random.randrange(1,50) ; a.append(seat)
        list.append(a)
        for rec in record:
            if rec[0] == pc:
                heading1()
                print('\t',name,'\t\t',age,'\t\t',seat)
                heading2()
                print('\t',rec[0],'\t\t',rec[1],'\t\t',rec[2],'\t\t',rec[3])
                print('_'*80)
    stmt = "insert into booking(name,age,seat)values(%s,%s,%s)"
    cursor.executemany(stmt, list)
    mcon.commit()
    
    




import mysql.connector as msql
pas = input("Enter Your Mysql Password Here -> ")
mcon = msql.connect(host='localhost', user='root',passwd=pas,database='board') 
cursor = mcon.cursor()

dict = {1:arrival, 2:departure, 3:available}
choice=0
ans = 'y'
while ans == 'y' :
    print('\n1.Check the Arrival of Planes')
    print('2.Check the Departure of Planes')
    print('3.Book a Ticket')
    choice = int(input('\nPlease enter your choice: '))
    dict.get(choice)()
    ans = input('\nDo you want to do something else?\n(y/n)--->')
    ans=ans.lower()

if ans != 'y':
    print('\n\t\t\tThank You, Have a nice day')
