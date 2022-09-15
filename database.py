import mariadb
conn=mariadb.connect(user="root",password="991227",host="localhost",port=3306,database="empExample")
cur1=conn.cursor()
c=0
while c!=7:
    fname = input("Enter Your Name: ")
    c=c+1
    if(len(fname) >0 and fname.isalpha()):
        surname=input("Enter your surname: ")
        c=c+1
        if(len(surname)>0 and surname.isalpha()):
            phone=input("Enter contact number: ")
            c=c+1
            if(len(phone)>0):
                if(len(phone)>9 and phone.isnumeric()):
                    age=int(input("Enter your age: "))
                    c=c+1
                    if(age>=20 and age<=101):
                            city=input("Enter your city: ")
                            c=c+1
                            if(len(city)>0):
                                salary=int(input("Enter your salary: "))
                                c=c+1
                                if( salary>0):
                                    dep=input("Enter department name: ")
                                    c=c+1
                                    if(len(dep)>0):
                                            print("Name: ",fname)
                                            print("Surname: ",surname)
                                            print("phone : ",phone)
                                            print("age : ",age)
                                            print("city: ",city)
                                            print("salary: ",salary)
                                            print("dep. name: ",dep)

                                            break
                                    else:
                                        print("Enter valid department name")
                                else:
                                    print("Enter valid salary amount")
                                    
                            else:
                                print("Enter valid city")
                                
                    else:
                            print("Enter valid age")
                            
                    

                else:
                    print("Enter valid phone")
                    
            else:
                print("Enter valid phone")
                
        else:
            print("Enter valid surname")
            
    else:
        print("Enter Valid name")

try:
    cur1.execute("create table employeetable17(fname varchar(25),surname varchar(25),phone varchar(12),age int,city varchar(250),salary int,dep varchar(25))")
except Exception as y:
    print(y)
sql="insert into employeetable17(fname,surname,phone,age,city,salary,dep) values(%s,%s,%s,%d,%s,%d,%s)"
values=(fname,surname,phone,age,city,salary,dep)
cur1.execute(sql,values)
cur1.execute("select * from employeetable17")
for (fname,surname,phone,age,city,salary,dep) in cur1:
    print("Name:",fname,"SurName: ",surname,"Phone:",phone,"Age:",age,"City:",city,"Salary:",salary,"Department:",dep,)

conn.commit()





        
