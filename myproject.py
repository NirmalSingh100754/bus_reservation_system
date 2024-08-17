from tkinter import *
class obp:
    variable = -1
    def title(self):
        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        img = PhotoImage(file="starbus.png")
        Label(root, image=img).grid(row=0, column=0, padx=550, pady=15)
        Label(
            root,
            text="Online Bus Booking System",
            font="Ariel 23 bold",
            fg="red",
            bg="light blue",
            relief="ridge",
        ).grid(row=1, column=0)
        Label(root, text="\n\nName: Nirmal Singh", fg="blue", font="Ariel 15", pady=20).grid(
            row=2, column=0
        )
        Label(root, text="Er: 221B252", fg="blue", font="Ariel 15").grid(row=3, column=0)
        Label(root, text="Mobile: 9565469972\n", fg="blue", font="Ariel 15", pady=20).grid(
            row=4, column=0
        )
        Label(
            root,
            text="Submitted To: Dr.Mahesh Kumar",
            fg="red",
            bg="light blue",
            font="Ariel 18 bold",
            relief="ridge",
        ).grid(row=7, column=0)
        Label(root, text="Project Based Learning", fg="red", font="Ariel 10 bold").grid(
            row=8, column=0
        )
        def n():
            root.destroy()
            self.page1()
        Button(root,text=" Next ",font="Ariel 10 bold",bg="OliveDrab1",command=n).grid(row=9,column=0,columnspan=20)
        root.mainloop()
    def page1(self):
        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        fr = Frame(root)
        fr.grid(row=0, column=0)
        img = PhotoImage(file="starbus.png")
        fr1 = Frame(root)
        fr2 = Frame(root)
        fr1.grid(row=1, column=0, pady=20)
        fr2.grid(row=2, column=0, pady=40)
        Label(fr, image=img).grid(row=0, column=0, padx=550, pady=20, columnspan=100)
        Label(
            fr1,
            text="Online Bus Booking System",
            font="Ariel 25 bold",
            fg="red",
            bg="light blue",
        ).grid(row=1, column=0)


        def SeatBooking():
            root.destroy()
            self.book_your_seats()
        def CheckBookedSeats():
            root.destroy()
            self.check_booked_seats()
        def AddBusDetails():
            root.destroy()
            self.new_details()
        Button(fr2, text="Seat Booking", font="Ariel 10 bold", bg="springgreen2",command=SeatBooking).grid(
            row=2, column=0, padx=30
        )
        Button(fr2, text="Check Booked Seats", font="Ariel 10 bold", bg="springgreen2",command=CheckBookedSeats).grid(
            row=2, column=1, padx=30
        )
        Button(fr2, text="Add Bus Details", font="Ariel 10 bold", bg="springgreen2",command=AddBusDetails).grid(
            row=2, column=2, padx=30
        )
        Label(fr2, text="For Admin Only", font="Ariel 8 bold", fg="red").grid(
            row=3, column=2, pady=20
        )
        root.mainloop()
    def new_details(self):
        import sqlite3
        con = sqlite3.Connection("bus")
        cur = con.cursor()
        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        fr = Frame(root)
        fr.grid(row=0, column=0)
        fr1 = Frame(root)
        fr2 = Frame(root)
        fr1.grid(row=1, column=0, pady=20)
        fr2.grid(row=3, column=0)
        img = PhotoImage(file="starbus.png")
        Label(fr, image=img).grid(row=0, column=0, padx=550, pady=20, columnspan=100)
        Label(
            fr1,
            text="Online Bus Booking System",
            font="Ariel 25 bold",
            fg="red",
            bg="light blue",
        ).grid(row=1, column=0, columnspan=20)
        Label(
            fr1,
            text="Add New Details To DataBase",
            fg="green",
            bg="light green",
            relief="ridge",
            font="Areil 15 bold",
        ).grid(row=2, column=0, pady=20, columnspan=20)


        def new_operator():
            root.destroy()
            self.New_Operator()

        def new_bus():
            root.destroy()
            self.New_Bus()      


        def new_route():
            root.destroy()
            self.New_Route()       


        def new_run():
            root.destroy()
            self.New_Run()       


        Button(
            fr2,
            text="New Operator",
            bg="light green",
            font="Areil 10 bold",
            command=new_operator,
        ).grid(row=3, column=0, padx=10)
        Button(fr2, text="New Bus", bg="orange", font="Areil 10 bold", command=new_bus).grid(
            row=3, column=1, padx=10
        )
        Button(fr2, text="New Route", bg="blue", font="Areil 10 bold", command=new_route).grid(
            row=3, column=2, padx=10
        )
        Button(fr2, text="New Run", bg="brown", font="Areil 10 bold", command=new_run).grid(
            row=3, column=3, padx=10
        )
        root.mainloop()
    def check_booked_seats(self):
        from tkinter import messagebox
        from tkinter.messagebox import askyesno
        import sqlite3
        con = sqlite3.Connection('Bus')
        cur = con.cursor()
        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        img = PhotoImage(file="starbus.png")
        Label(root, image=img).grid(row=0, column=0, padx=550)
        Label(root, text="Online Bus Booking System", font="Ariel 25 bold",
            fg="red", bg="light blue", relief="ridge").grid(row=1, column=0)
        Label(root, text="Check Your Booking", font="Ariel 15 bold",
            fg="red", bg="yellow2", relief="ridge").grid(row=2, column=0, pady=10)
        fr = Frame()
        fr.grid(row=3, column=0)
        fr1 = Frame(root, relief="groove", bd=5)
        fr1.grid(row=4, column=0, columnspan=10, pady=10)


        Label(fr, text="Enter Your Mobile No : ",
            font="Ariel 12 bold").grid(row=0, column=0, padx=10)
        phone_no = Entry(fr, font="Ariel 12 bold")
        phone_no.grid(row=0, column=1, padx=10)


        def check():
            try:

                Number = phone_no.get()
                if len(str(Number)) != 10:
                    raise Exception(messagebox.showerror(
                        "Incorrect Number", "phone number must be of 10 numbers"))

                cur.execute(
                    "select * from booking_history where phone = ?  ", (int(Number),))
                passenger_info = cur.fetchall()
                if passenger_info == []:
                    answer = askyesno(title='No Booking Record',
                                    message='Do you want to seat book now ?')
                    if answer == True:
                        root.destroy()
                        self.book_your_seats()
                    else:
                        exit()

                passenger_info = passenger_info[0]
                cur.execute("select * from bus_details where busid = ?",
                            (passenger_info[8],))
                passenger_Bus_info = cur.fetchall()
                passenger_Bus_info = passenger_Bus_info[0]
                cur.execute("select * from operators where operator_id = ?",
                            (passenger_Bus_info[4],))
                passenger_operator_info = cur.fetchall()
                passenger_operator_info = passenger_operator_info[0]
                cur.execute("select * from route_details where route_id = ?",
                            (passenger_Bus_info[5],))
                passenger_route_info = cur.fetchall()
                passenger_route_info = passenger_route_info[0]
                print(passenger_info)
                print(passenger_Bus_info)
                print(passenger_operator_info)
                print(passenger_route_info)
                total_fare = int(passenger_info[3])*int(passenger_Bus_info[3])
                Label(fr1, text="Passenger : " + passenger_info[1],
                    font="Ariel 12 bold").grid(row=0, column=0)
                Label(fr1, text="Gender : " + passenger_info[2],
                    font="Ariel 12 bold").grid(row=0, column=1)
                Label(fr1, text="No of seats : " + str(passenger_info[3]),
                    font="Ariel 12 bold").grid(row=1, column=0)
                Label(fr1, text="Phone : "+str(passenger_info[4]),
                    font="Ariel 12 bold").grid(row=1, column=1)
                Label(fr1, text="Age : " +
                    str(passenger_info[5]), font="Ariel 12 bold").grid(row=2, column=0)
                Label(fr1, text="Fare Rs : "+str(total_fare),
                    font="Ariel 12 bold").grid(row=2, column=1)
                Label(fr1, text="Booking ref : "+str(passenger_info[0]),
                    font="Ariel 12 bold").grid(row=3, column=0)
                Label(fr1, text="Bus Details : "+passenger_operator_info[1],
                    font="Ariel 12 bold").grid(row=3, column=1)
                Label(fr1, text="Travel on : "+str(passenger_info[7]),
                    font="Ariel 12 bold").grid(row=4, column=0)
                Label(fr1, text="Booked on : "+str(passenger_info[6]),
                    font="Ariel 12 bold").grid(row=4, column=1)
                Label(fr1, text="Operator contact : "+str(passenger_operator_info[3]),
                    font="Ariel 12 bold").grid(row=5, column=0)
                Label(fr1, text="Boarding Point : "+passenger_route_info[1],
                    font="Ariel 12 bold").grid(row=5, column=1)
                Label(fr1, text="•Total amount Rs " + str(total_fare) + " to be paid at the time of boarding the bus.",
                    fg="red", font="Ariel 10 bold").grid(row=6, column=0, columnspan=4)
            except ValueError:
                messagebox.showerror(
                    "Incorrect Number", "Incorrect Phone Number !")
            except TypeError:
                messagebox.showerror(
                    "Incorrect Number", "Incorrect Phone Number !")
            except IndexError:
                messagebox.showerror(
                    "No Record", "No Record Found!")


        Button(fr, text="Check Booking", command=check,
            font="Ariel 13 bold").grid(row=0, column=3, padx=10)
        root.mainloop()
    def book_your_seats(self):
        from tkcalendar import DateEntry
        from tkinter import messagebox
        from tkinter.messagebox import askyesno
        import datetime
        import sqlite3
        global details1
        con = sqlite3.Connection('bus')
        cur = con.cursor()
        cur.execute('create table if not exists booking_history(booking_ref INTEGER PRIMARY KEY AUTOINCREMENT,name varchar(20),gender varchar(10),no_of_seat int,phone big int,age int,booking_date date,travel_date date,bus_id int,CONSTRAINT fk1 foreign key(bus_id) references bus(busid) ON DELETE CASCADE)')
        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        fr = Frame(root)
        fr.grid(row=0, column=0)
        img = PhotoImage(file="starbus.png")
        fr1 = Frame(root)
        fr2 = Frame(root)
        fr1.grid(row=1, column=0)
        fr2.grid(row=2, column=0)
        fr3 = Frame(root, pady=20)
        fr3.grid(row=3, column=0)
        fr4 = Frame(root)
        fr4.grid(row=4, column=0)
        fr5 = Frame(root)
        fr5.grid(row=5, column=0)
        Label(fr, image=img).grid(row=0, column=0, padx=550, columnspan=100)
        Label(fr1, text="Online Bus Booking System", font="Ariel 25 bold",
            fg="red", bg="light blue").grid(row=1, column=0)
        Label(fr1, text="Enter Journey Details", fg="green", bg="light green",
            relief="ridge", font="Areil 15 bold").grid(row=2, column=0, pady=20)
        Label(fr2, text="To", font="Ariel 10 bold").grid(row=3, column=0)
        t = Entry(fr2)
        t.grid(row=3, column=1)
        Label(fr2, text="From", font="Ariel 10 bold").grid(row=3, column=2)
        f = Entry(fr2)
        f.grid(row=3, column=3)
        Label(fr2, text="Journey Date", font="Ariel 10 bold").grid(row=3, column=4)
        jd = DateEntry(fr2, date_pattern="yyyy-mm-dd")
        jd.grid(row=3, column=5)

        # function global variable

        


        def make_something(value):
            global variable
            variable = value
        # set_passenger_details


        def set_passenger_details():
            try:
                details2 = details1[variable]
                print(details2)
                Name = name.get()
                Gen = gen.get()
                Seat = seat.get()
                Mobail = mobail.get()
                Age = age.get()
                Booking_date = datetime.datetime.now()
                Booking_date = Booking_date.date()
                Seat_avl = details2[2]-int(Seat)
                print(Seat_avl)
                if (Seat_avl < 0):
                    raise Exception(messagebox.showerror(
                        "No Seats Available", "Sorry Only " + str(details2[2]) + " Seats Are Available"))

                if Name == "" or Gen == "Gender" or Seat == "" or int(Seat) == 0 or Mobail == "" or Age == "":
                    raise Exception(messagebox.showerror(
                        "blank_field", "no field can be blank"))
                if len(str(Mobail)) != 10:
                    raise Exception(messagebox.showerror(
                        "Invalid phone no.", "phone number must be of 10 numbers"))

            # Operator_name,Bus_Type,Seat_avl,seat_cap,fare,travle date,bus id
            # name varchar(20),gender varchar(10),no_of_seat int,phone big int,age int,booking_ref int not null primary key,booking_date date,travel_date date,bus_id int,CONSTRAINT fk1 foreign key(bus_id) references bus(busid) ON DELETE CASCADE)
                info = ((str(Name), str(Gen), int(Seat), int(Mobail),
                        int(Age), Booking_date, details2[5], details2[6]))
                Total_Amount = int(Seat) * int(details2[4])
                answer = askyesno(title='confirmation',
                                message='Total Amount To be Paid Rs '+str(Total_Amount))
                if answer == True:
                    cur.execute(
                        'insert into booking_history (name,gender,no_of_seat,phone,age,booking_date,travel_date,bus_id) values(?,?,?,?,?,?,?,?)', info)
                    cur.execute("select * from booking_history")
                    print(cur.fetchall())
                    cur.execute(
                        "update run_details set seat_avl = ? where bus_id = ? ", (Seat_avl, details2[6]))
                    con.commit()
                    root.destroy()
                    self.bus_ticket()
            except sqlite3.IntegrityError:
                messagebox.showerror("insertion error", "record already exist")
            except ValueError:
                messagebox.showerror(
                    "wrong entry", "please check input and try again")


        # function get passenger_details


        def get_passenger_details():
            print(variable)
            if (variable == -1):
                raise Exception(messagebox.showerror(
                    "Select Bus", "Please select bus !"))
            Label(fr4, text="Fill passenger details to book the bus", fg="green", bg="light blue",
                relief="ridge", font="Areil 15 bold").grid(row=0, column=0, pady=20)
            global gen
            global seat
            global mobail
            global age
            global name
            Label(fr5, text="Name ").grid(row=0, column=0)
            name = Entry(fr5)
            name.grid(row=0, column=1)
            Label(fr5, text="Gender ").grid(row=0, column=2)
            options = ['Male', 'Female', 'Other']
            gen = StringVar()
            gen.set("Gender")
            drop = OptionMenu(fr5, gen, *options)
            drop.grid(row=0, column=3)
            Label(fr5, text="No of seats ").grid(row=0, column=4)
            seat = Entry(fr5)
            seat.grid(row=0, column=5)
            Label(fr5, text="Mobile No ").grid(row=0, column=6)
            mobail = Entry(fr5)
            mobail.grid(row=0, column=7)
            Label(fr5, text="Age ").grid(row=0, column=8)
            age = Entry(fr5)
            age.grid(row=0, column=9)
            Button(fr5, text="Book Seat", bg="springgreen2", font="Ariel 10 bold",
                command=set_passenger_details).grid(row=0, column=10, padx=10)


        # Show Bus Function
        details1 = []


        def show_bus():
            To = t.get()
            To = To.upper()
            From = f.get()
            From = From.upper()
            date = jd.get()
            if str(To) == "" or str(From) == "" or date == "":
                raise Exception(messagebox.showerror(
                    "blank_field", "any field cannot be blank"))
            cur.execute(
                "select * from route_details where station_Name = ? order by route_id", (From,))
            From_details = cur.fetchall()
            print(From_details)
            To_details = []

            for i in From_details:
                cur.execute(
                    "select * from route_details where station_Name = ? and Route_id = ? order by route_id", (To, i[0]))
                To_details.append(cur.fetchall())
            if (To_details == []):
                raise Exception(messagebox.showerror(
                    "No Bus", "No bus available !"))
            print("To details : ", To_details)
            From_details = []

            for i in To_details:
                for j in i:
                    cur.execute(
                        "select * from route_details where station_Name = ? and Route_id = ? order by route_id", (From, j[0]))
                    From_details.append(cur.fetchall())
            print("From details : ", From_details)

            A = From_details[0]
            A = A[0]
            B = To_details[0]
            B = B[0]
            temp = 0
            rid = []
            if (A[2] < B[2]):
                for i in From_details:
                    for j in i:
                        if (temp % 2 == 0):
                            rid.append(j[0])
                        temp = temp+1
            else:
                for i in From_details:
                    for j in i:
                        if (temp % 2 != 0):
                            rid.append(j[0])
                        temp = temp+1
            print(rid)
            Bus_details = []
            for i in rid:
                cur.execute("select * from bus_details where route_id = ?", (i,))
                Bus_details.append(cur.fetchall())
                print(Bus_details)

            flag = 1
            run_detail = []
            for i in Bus_details:
                for j in i:
                    cur.execute(
                        "select * from run_details where bus_id = ? and running_date = ?", (j[0], date))
                    Run_detail = cur.fetchall()
                    if (Run_detail != []):
                        run_detail.append(Run_detail)
                        flag = 0
            print(run_detail)
            if (flag):
                raise Exception(messagebox.showerror(
                    "No Bus", "No bus available !"))

            Label(fr3, text="Select Bus", fg="red",
                font="Areil 12 bold").grid(row=0, column=0, padx=30)
            Label(fr3, text="Operator", fg="red",
                font="Areil 10 bold").grid(row=0, column=1, padx=30)
            Label(fr3, text="Bus Type", fg="red",
                font="Areil 10 bold").grid(row=0, column=2, padx=30)
            Label(fr3, text="Available/Capacity", fg="red",
                font="Areil 10 bold").grid(row=0, column=3, padx=30)
            Label(fr3, text="Fare", fg="red", font="Areil 10 bold").grid(
                row=0, column=4, padx=30)
            Label(fr3, text="", fg="red", font="Areil 10 bold").grid(
                row=0, column=5, padx=30)
            temp1 = 0
            Bus_Button = {}
            for i in range(0, len(run_detail)):
                Run_detail = run_detail[i]
                Run_detail = Run_detail[i]
                for j in Bus_details:
                    for k in j:
                        if Run_detail[0] == k[0]:
                            op_id = k[4]
                            cur.execute(
                                "select name from operators where operator_id = ? ", (op_id,))
                            operator_detail = cur.fetchall()
                            operator_detail = operator_detail[0]
                            operator_detail = operator_detail[0]
                            temp2 = ()

                            def call_make_something(val=temp1):
                                return make_something(val)
                            Bus_Button[temp1] = Button(fr3, text="Bus"+str(temp1+1), command=call_make_something, bg="springgreen2", activebackground='blue',
                                                    font="Ariel 10 bold")
                            Bus_Button[temp1].grid(row=temp1+1, column=0, padx=30)
                            Label(fr3, text=operator_detail, fg="blue",
                                font="Areil 10 bold").grid(row=temp1+1, column=1, padx=30)
                            temp2 = temp2 + (operator_detail,)  # operator details
                            Label(fr3, text=k[1], fg="blue",
                                font="Areil 10 bold").grid(row=temp1+1, column=2, padx=30)
                            temp2 = temp2 + (k[1],)  # Bus type
                            Label(fr3, text=str(Run_detail[2]) + "/" + str(k[2]), fg="blue",
                                font="Areil 10 bold").grid(row=temp1+1, column=3, padx=30)
                            temp2 = temp2 + (Run_detail[2], k[2])  # Seat avl.
                            Label(fr3, text=k[3], fg="blue", font="Areil 10 bold").grid(
                                row=temp1+1, column=4, padx=30)
                            temp2 = temp2 + (k[3],)  # Fare
                            Button(fr3, text="Proceed to Book", bg="springgreen2",
                                font="Ariel 10 bold", command=get_passenger_details).grid(row=temp1+1, column=5, padx=30)
                            temp2 = temp2 + (date,)
                            temp2 = temp2 + (k[0],)
                            temp1 = temp1+1
                            details1.append(temp2)
                            # print(details1)


        Button(fr2, text="Show Bus", command=show_bus, bg="springgreen2",
            font="Ariel 10 bold").grid(row=3, column=6, padx=10)
        im = PhotoImage(file="home.png")


        def hom():
            root.destroy()
            self.page1()


        Button(fr2, image=im, bg="springgreen2", command=hom).grid(row=3, column=7)
        root.mainloop()
    def bus_ticket(self):
        from tkinter import messagebox
        import sqlite3
        con = sqlite3.Connection('Bus')
        cur = con.cursor()
        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        # Entry(Text)
        img = PhotoImage(file="starbus.png")
        Label(root, image=img).grid(row=0, column=0, padx=550)
        Label(root, text="Online Bus Booking System", font="Ariel 25 bold",
            fg="red", bg="light blue", relief="ridge").grid(row=1, column=0)
        Label(root, text="Bus Ticket", font="Ariel 15 bold",
            fg="red", bg="yellow2", relief="ridge").grid(row=2, column=0, pady=10)
        fr1 = Frame(root, relief="groove", bd=5)
        fr1.grid(row=3, column=0, columnspan=10)
        cur.execute("select * from booking_history order by booking_ref desc limit 1 ")
        passenger_info = cur.fetchall()
        passenger_info = passenger_info[0]
        cur.execute("select * from bus_details where busid = ?", (passenger_info[8],))
        passenger_Bus_info = cur.fetchall()
        passenger_Bus_info = passenger_Bus_info[0]
        cur.execute("select * from operators where operator_id = ?",
                    (passenger_Bus_info[4],))
        passenger_operator_info = cur.fetchall()
        passenger_operator_info = passenger_operator_info[0]
        cur.execute("select * from route_details where route_id = ?",
                    (passenger_Bus_info[5],))
        passenger_route_info = cur.fetchall()
        passenger_route_info = passenger_route_info[0]
        print(passenger_info)
        print(passenger_Bus_info)
        print(passenger_operator_info)
        print(passenger_route_info)
        total_fare = int(passenger_info[3])*int(passenger_Bus_info[3])
        Label(fr1, text="Passenger : " + passenger_info[1],
            font="Ariel 10 bold").grid(row=0, column=0)
        Label(fr1, text="Gender : " + passenger_info[2],
            font="Ariel 10 bold").grid(row=0, column=1)
        Label(fr1, text="No of seats : " + str(passenger_info[3]),
            font="Ariel 10 bold").grid(row=1, column=0)
        Label(fr1, text="Phone : "+str(passenger_info[4]),
            font="Ariel 10 bold").grid(row=1, column=1)
        Label(fr1, text="Age : " +
            str(passenger_info[5]), font="Ariel 10 bold").grid(row=2, column=0)
        Label(fr1, text="Fare Rs : "+str(total_fare),
            font="Ariel 10 bold").grid(row=2, column=1)
        Label(fr1, text="Booking ref : "+str(passenger_info[0]),
            font="Ariel 10 bold").grid(row=3, column=0)
        Label(fr1, text="Bus Details : "+passenger_operator_info[1],
            font="Ariel 10 bold").grid(row=3, column=1)
        Label(fr1, text="Travel on : "+str(passenger_info[7]),
            font="Ariel 10 bold").grid(row=4, column=0)
        Label(fr1, text="Booked on : "+str(passenger_info[6]),
            font="Ariel 10 bold").grid(row=4, column=1)
        Label(fr1, text="Operator contact : "+str(passenger_operator_info[3]),
            font="Ariel 10 bold").grid(row=5, column=0)
        Label(fr1, text="Boarding Point : "+passenger_route_info[1],
            font="Ariel 10 bold").grid(row=5, column=1)
        Label(fr1, text="•Total amount Rs " + str(total_fare) + " to be paid at the time of boarding the bus.",
            fg="red").grid(row=6, column=0, columnspan=4)
        messagebox.showinfo("Success", "Seat Booked...")
        root.mainloop()
    def New_Operator(self):
        from tkinter import messagebox
        import sqlite3

        con = sqlite3.Connection("bus")
        cur = con.cursor()
        cur.execute(
            "create table if not exists operators(operator_id int,name varchar(30),address varchar(50),phone bigint,email varchar(50),CONSTRAINT operators_pk PRIMARY KEY(operator_id))"
        )
        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        fr = Frame(root)
        fr.grid(row=0, column=0)
        fr1 = Frame(root)
        fr2 = Frame(root)
        fr1.grid(row=1, column=0, pady=20)
        fr2.grid(row=3, column=0, pady=20)
        img = PhotoImage(file="starbus.png")
        Label(fr, image=img).grid(row=0, column=0, padx=550, pady=20, columnspan=100)
        Label(
            fr1,
            text="Online Bus Booking System",
            font="Ariel 25 bold",
            fg="red",
            bg="light blue",
        ).grid(row=1, column=0, columnspan=20)
        Label(
            fr1,
            text="Add Bus Operator Details",
            fg="green",
            bg="light green",
            relief="ridge",
            font="Areil 15 bold",
        ).grid(row=2, column=0, pady=20, columnspan=20)
        Label(fr2, text="Operator id").grid(row=3, column=0)
        Opid = Entry(fr2)
        Opid.grid(row=3, column=1)
        Label(fr2, text="Name").grid(row=3, column=2)
        Name = Entry(fr2)
        Name.grid(row=3, column=3)
        Label(fr2, text="Address").grid(row=3, column=4)
        Address = Entry(fr2)
        Address.grid(row=3, column=5)
        Label(fr2, text="Phone").grid(row=3, column=6)
        Phone = Entry(fr2)
        Phone.grid(row=3, column=7)
        Label(fr2, text="Email").grid(row=3, column=8)
        Email = Entry(fr2)
        Email.grid(row=3, column=9)
        im = PhotoImage(file="home.png")


        def go_home():
            root.destroy()
            self.page1()


        Button(fr2, image=im, bg="springgreen2", command=go_home).grid(row=3, column=12, padx=5)
        Label(
            fr2,
        )
        oid = StringVar()
        n = StringVar()
        adr = StringVar()
        p = StringVar()
        e = StringVar()


        def ad():
            oid = Opid.get()
            n = Name.get().upper()
            adr = Address.get().upper()
            p = Phone.get()
            e = Email.get()
            if n == "" or adr == "" or e == "" or oid == "" or p == "":
                raise Exception(messagebox.showerror("blank_field", "no field can be blank"))
            if len(p) != 10:
                raise Exception(
                    messagebox.showerror(
                        "Invalid phone no.", "phone number must be of 10 numbers"
                    )
                )
            try:
                cur.execute(
                    "insert into operators values(?,?,?,?,?)", (int(oid), n, adr, int(p), e)
                )
                messagebox.showinfo("operator entry", "operator added successfully")
                Label(fr2, text=oid + " " + n + " " + adr + " " + p + " " + e).grid(
                    row=5, column=0, columnspan=15
                )
            except sqlite3.IntegrityError:
                messagebox.showinfo("insertion error", "record already exists")
            Opid.delete(0, END)
            Name.delete(0, END)
            Address.delete(0, END)
            Phone.delete(0, END)
            Email.delete(0, END)
            con.commit()


        Button(fr2, text="Add", bg="springgreen2", font="Areil 10 bold", command=ad).grid(
            row=3, column=10, padx=5
        )


        def edit():
            oid = Opid.get()
            n = Name.get()
            adr = Address.get()
            p = Phone.get()
            e = Email.get()
            if n == "" or adr == "" or e == "" or p == "" or oid == "":
                raise Exception(messagebox.showerror("blank_field", "no field can be blank"))
            cur.execute('select * from operators where operator_id=?',(int(oid),))
            olist=cur.fetchall()
            if olist==[]:
                raise Exception(messagebox.showerror("operator updation","no such record exist"))
            cur.execute(
                "update operators set name=?,address=?,phone=?,email=? where operator_id=?",
                (n, adr, int(p), e, int(oid)),
            )
            messagebox.showinfo("operator enrty update", "operator record updated successfully")
            con.commit()
            Label(fr2, text="   " + oid + " " + n + " " + adr + " " + p + " " + e + "   ").grid(
                row=5, column=0, columnspan=15
            )
            Opid.delete(0, END)
            Name.delete(0, END)
            Address.delete(0, END)
            Phone.delete(0, END)
            Email.delete(0, END)


        Button(fr2, text="Edit", bg="springgreen2", font="Areil 10 bold", command=edit).grid(
            row=3, column=11
        )
        # cur.execute('drop table operators')
        root.mainloop()

    def New_Bus(self):
        from tkinter import messagebox
        import sqlite3

        con = sqlite3.Connection("bus")
        cur = con.cursor()
        cur.execute(
            "create table if not exists bus_details(busid int,bustype varchar(30),capacity int,fare int,operator_id int,route_id int,CONSTRAINT bus_det_pk PRIMARY KEY(busid),CONSTRAINT bus_det_fk1 foreign key (operator_id) REFERENCES operators (operator_id) ON DELETE CASCADE,CONSTRAINT bus_det_fk2 foreign key (route_id) REFERENCES route_details (route_id) ON DELETE CASCADE)"
        )

        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        fr = Frame(root)
        fr.grid(row=0, column=0)
        fr1 = Frame(root)
        fr2 = Frame(root)
        fr3 = Frame(root)
        fr1.grid(row=1, column=0, pady=20)
        fr2.grid(row=3, column=0, pady=20)
        fr3.grid(row=4, column=0, pady=20)
        img = PhotoImage(file="starbus.png")
        Label(fr, image=img).grid(row=0, column=0, padx=550, pady=20, columnspan=100)
        Label(
            fr1,
            text="Online Bus Booking System",
            font="Ariel 25 bold",
            fg="red",
            bg="light blue",
        ).grid(row=1, column=0, columnspan=20)
        Label(
            fr1,
            text="Add Bus Details",
            fg="green",
            bg="light green",
            relief="ridge",
            font="Areil 15 bold",
        ).grid(row=2, column=0, pady=20, columnspan=20)
        Label(fr2, text="Bus ID").grid(row=3, column=0)
        bid = Entry(fr2)
        bid.grid(row=3, column=1)
        Label(fr2, text="Bus Type").grid(row=3, column=2)
        options = [
            "AC 2X2",
            "AC 3X2",
            "Non AC 2X2",
            "Non AC 3X2",
            "AC Sleeper 2X1",
            "Non AC Sleeper 2X1",
        ]
        btype = StringVar()
        btype.set("Bus Type")
        drop = OptionMenu(fr2, btype, *options)
        drop.grid(row=3, column=3)
        Label(fr2, text="Capacity").grid(row=3, column=4)
        cap = Entry(fr2)
        cap.grid(row=3, column=5)
        Label(fr2, text="Fare Rs").grid(row=3, column=6)
        fare = Entry(fr2)
        fare.grid(row=3, column=7)
        Label(fr2, text="Operator ID").grid(row=3, column=8)
        opid = Entry(fr2)
        opid.grid(row=3, column=9)
        Label(fr2, text="Route id").grid(row=3, column=10)
        rid = Entry(fr2)
        rid.grid(row=3, column=11)
        im = PhotoImage(file="home.png")
        Bid = StringVar()
        Btype = StringVar()
        Cap = StringVar()
        Fare = StringVar()
        Opid = StringVar()
        Rid = StringVar()


        def go_home():
            Label(root, text="go to home page").grid(row=5, column=0)


        def adbus():
            Bid = bid.get()
            Btype = btype.get()
            Cap = cap.get()
            Fare = fare.get()
            Opid = opid.get()
            Rid = rid.get()
            try:
                if Btype == "Bus Type":
                    raise Exception(
                        messagebox.showerror(
                            "BusTypeError", "Bus Type can't be 'Bus Type' select an option"
                        )
                    )
                if Bid == "" or Cap == "" or Fare == "" or Opid == "" or Rid == "":
                    raise Exception(
                        messagebox.showerror("blank_field", "no field can be blank")
                    )
                cur.execute(
                    "insert into bus_details values(?,?,?,?,?,?)",
                    (int(Bid), Btype, int(Cap), int(Fare), int(Opid), int(Rid)),
                )
                messagebox.showinfo("bus entry", "bus record added")
                Label(
                    fr2,
                    text=Bid
                    + " "
                    + Btype
                    + " "
                    + " "
                    + Cap
                    + " "
                    + Fare
                    + " "
                    + Opid
                    + " "
                    + Rid,
                ).grid(row=4, column=2, columnspan=20)
            except sqlite3.IntegrityError:
                messagebox.showerror("insertion error", "record already exists")
            except ValueError:
                messagebox.showerror(
                    "Value Error", "wrong entry please check input and try again"
                )
            bid.delete(0, END)
            btype.set("Bus Type")
            cap.delete(0, END)
            fare.delete(0, END)
            opid.delete(0, END)
            rid.delete(0, END)
            con.commit()


        def edit_bus():
            Bid = bid.get()
            Btype = btype.get()
            Cap = cap.get()
            Fare = fare.get()
            Opid = opid.get()
            Rid = rid.get()
            try:
                if Btype == "Bus Type":
                    raise Exception(
                        messagebox.showerror(
                            "BusTypeError", "Bus Type can't be 'Bus Type' select an option"
                        )
                    )
                if Bid == "" or Cap == "" or Fare == "" or Opid == "" or Rid == "":
                    raise Exception(
                        messagebox.showerror("blank_field", "no field can be blank")
                    )
                cur.execute('select * from bus_details where busid=?',(int(Bid),))
                blist=cur.fetchall()
                if blist==[]:
                    raise Exception("updation error","no such record exist")
                cur.execute(
                    "update bus_details set bustype=?,capacity=?,fare=?,opeartor_id=?,route_id=? where busid=?",
                    (Btype, int(Cap), int(Fare), int(Opid), int(Rid), int(Bid)),
                )
                messagebox.showinfo("bus enrty update", "bus record upadted successfully")
            except ValueError:
                messagebox.showerror(
                    "Value Error", "wrong entry please check input and try again"
                )
            bid.delete(0, END)
            btype.set("Bus Type")
            cap.delete(0, END)
            fare.delete(0, END)
            opid.delete(0, END)
            rid.delete(0, END)
            Label(
                fr2,
                text=Bid + " " + Btype + " " + " " + Cap + " " + Fare + " " + Opid + " " + Rid,
            ).grid(row=4, column=2, columnspan=10)
            con.commit()


        Button(
            fr3, text="Add Bus", bg="springgreen2", font="Areil 10 bold", command=adbus
        ).grid(row=5, column=2, padx=10)
        Button(
            fr3, text="Edit Bus", bg="springgreen2", font="Areil 10 bold", command=edit_bus
        ).grid(row=5, column=3, padx=10)
        Button(fr3, image=im, bg="green", command=go_home).grid(row=5, column=4, padx=10)
        # cur.execute('drop table bus_details')
        root.mainloop()

    def New_Route(self):
        from tkinter import messagebox
        import sqlite3

        con = sqlite3.Connection("bus")
        cur = con.cursor()
        cur.execute(
            "create table if not exists route_details(route_id int,station_name varchar(30),station_id int,mark int,CONSTRAINT route_det_pk PRIMARY KEY(route_id,station_name,station_id))"
        )
        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        fr = Frame(root)
        fr.grid(row=0, column=0)
        fr1 = Frame(root)
        fr2 = Frame(root)
        fr3 = Frame(root)
        fr1.grid(row=1, column=0, pady=20)
        fr2.grid(row=3, column=0, pady=20)
        fr3.grid(row=4, column=0, pady=20)
        img = PhotoImage(file="starbus.png")
        Label(fr, image=img).grid(row=0, column=0, padx=550, pady=20, columnspan=100)
        Label(
            fr1,
            text="Online Bus Booking System",
            font="Ariel 25 bold",
            fg="red",
            bg="light blue",
        ).grid(row=1, column=0, columnspan=20)
        Label(
            fr1,
            text="Add Bus Route Details",
            fg="green",
            bg="light green",
            relief="ridge",
            font="Areil 15 bold",
        ).grid(row=2, column=0, pady=20, columnspan=20)
        Label(fr2, text="Route Id").grid(row=3, column=0)
        rid = Entry(fr2)
        rid.grid(row=3, column=1)
        Label(fr2, text="Station Name").grid(row=3, column=2)
        stname = Entry(fr2)
        stname.grid(row=3, column=3)
        Label(fr2, text="Station Id").grid(row=3, column=4)
        stid = Entry(fr2)
        stid.grid(row=3, column=5, padx=5)
        Rid = StringVar()
        Stname = StringVar()
        Stid = StringVar()


        def add():
            Rid = rid.get()
            Stname = stname.get().upper()
            Stid = stid.get()
            try:
                if Rid == "" or Stname == "" or Stid == "":
                    raise Exception(
                        messagebox.showerror("blank_field", "any field cannot be blank")
                    )
                cur.execute('select station_id from route_details where station_name=? group by station_id',(Stname,))
                slist=cur.fetchall()
                cur.execute('select station_name from route_details where station_id=? group by station_name',(int(Stid),))
                snlist=cur.fetchall()
                if(slist==[] and snlist==[]):
                    cur.execute(
                        "insert into route_details values(?,?,?,?)", (int(Rid), Stname, int(Stid),0)
                    )
                    cur.execute(
                        "insert into route_details values(?,?,?,?)", (int(Rid) + 1, Stname, int(Stid),1)
                    )
                elif slist!=[] and snlist!=[]:
                    slist=slist[0]
                    snlist=snlist[0]
                    print(slist[0],snlist[0])
                    if slist[0]==int(Stid) and snlist[0]==Stname:
                        cur.execute(
                            "insert into route_details values(?,?,?,?)", (int(Rid), Stname, int(Stid),0)
                        )
                        cur.execute(
                            "insert into route_details values(?,?,?,?)", (int(Rid) + 1, Stname, int(Stid),1)
                        )
                    else:
                        raise EXCEPTION(messagebox.showerror("wrong enrty","station id and station name cannot be matched"))
                else:
                    raise EXCEPTION(messagebox.showerror("wrong enrty","station id and station name cannot be matched"))
                con.commit()
                messagebox.showinfo("route enrty", "route added successfully")
                Label(fr2, text=Rid + " " + Stname + " " + Stid).grid(
                    row=4, column=2
                )
                Label(fr2, text=str(int(Rid)+1) + " " + Stname + " " + Stid).grid(
                    row=4, column=3
                )
            except sqlite3.IntegrityError:
                messagebox.showerror("insertion error", "record already exist")
            except ValueError:
                messagebox.showerror("wrong entry", "please check input and try again")
            rid.delete(0, END)
            stname.delete(0, END)
            stid.delete(0, END)


        def de():
            Rid = rid.get()
            Stname = stname.get()
            Stid = stid.get()
            try:
                if Rid == "":
                    raise Exception(
                        messagebox.showerror("blank_field", "route_id field cannot be blank")
                    )
                cur.execute("select * from route_details where route_id=?", (int(Rid),))
                rlist = cur.fetchall()
                if rlist == []:
                    raise EXCEPTION(
                        messagebox.showerror("deletion error", "no such record exist")
                    )
                cur.execute(
                    "DELETE FROM route_details WHERE route_id=?",
                    (int(Rid),),
                )
                rlist=rlist[0]
                if rlist[3]==0:
                    cur.execute(
                        "DELETE FROM route_details WHERE route_id=?",
                        (int(Rid)+1,),
                    )
                else:
                    cur.execute(
                        "DELETE FROM route_details WHERE route_id=?",
                        (int(Rid)-1,),
                    )
                messagebox.showinfo("route deletion", "route deleted successfully")
                con.commit()
            except ValueError:
                messagebox.showerror(
                    "Value Error", "wrong entry please check input and try again"
                )
            rid.delete(0, END)
            stname.delete(0, END)
            stid.delete(0, END)


        Button(fr2, text="Add Route", bg="springgreen2", command=add).grid(
            row=3, column=6, padx=10
        )
        Button(fr2, text="Delete Route", bg="springgreen2", fg="red2", command=de).grid(
            row=3, column=7, padx=10
        )
        im = PhotoImage(file="home.png")


        def hom():
            root.destroy()
            self.page1()


        Button(fr2, image=im, bg="springgreen2", command=hom).grid(row=3, column=8)
        # cur.execute('drop table route_details')
        root.mainloop()

    def New_Run(self):
        from tkcalendar import DateEntry
        from tkinter import messagebox
        from datetime import date
        import sqlite3

        con = sqlite3.Connection("bus")
        cur = con.cursor()
        cur.execute(
            "create table if not exists run_details(bus_id int,running_date date,seat_avl int,CONSTRAINT run_det_pk PRIMARY KEY(bus_id,running_date),CONSTRAINT run_det_fk FOREIGN KEY(bus_id) references bus_details(busid))"
        )
        root = Tk()
        root.title("online bus booking system")
        root.geometry("1500x1000")
        fr = Frame(root)
        fr.grid(row=0, column=0)
        fr1 = Frame(root)
        fr2 = Frame(root)
        fr3 = Frame(root)
        fr1.grid(row=1, column=0, pady=20)
        fr2.grid(row=3, column=0, pady=20)
        fr3.grid(row=4, column=0, pady=20)
        img = PhotoImage(file="starbus.png")
        Label(fr, image=img).grid(row=0, column=0, padx=550, pady=20, columnspan=100)
        Label(
            fr1,
            text="Online Bus Booking System",
            font="Ariel 25 bold",
            fg="red",
            bg="light blue",
        ).grid(row=1, column=0, columnspan=20)
        Label(
            fr1,
            text="Add Bus Running Details",
            fg="green",
            bg="light green",
            relief="ridge",
            font="Areil 15 bold",
        ).grid(row=2, column=0, pady=20, columnspan=20)
        Label(fr2, text="Bus ID").grid(row=3, column=0)
        bid = Entry(fr2)
        bid.grid(row=3, column=1)
        Label(fr2, text="Running Date").grid(row=3, column=2)
        rdate = DateEntry(fr2, date_pattern="dd-mm-yyyy")
        rdate.grid(row=3, column=3)
        Label(fr2, text="Seat Available").grid(row=3, column=4)
        savl = Entry(fr2)
        savl.grid(row=3, column=5)
        Bid = StringVar()
        Rdate = StringVar()
        Savl = StringVar()


        def addrun():
            Bid = bid.get()
            Rdate = rdate.get()
            Savl = savl.get()
            try:
                if Bid == "" or Rdate == "" or Savl == "":
                    messagebox.showerror("blank_field", "any field cannot be blank")
                cur.execute(
                    "insert into run_details values(?,?,?)", (int(Bid), Rdate, int(Savl))
                )
                messagebox.showinfo("run entry", "run added successfully")
                Label(fr2, text=Bid + " " + Rdate + " " + Savl).grid(
                    row=4, column=0, columnspan=20
                )
            except sqlite3.IntegrityError:
                messagebox.showerror("insertion error", "record already exist")
            except ValueError:
                messagebox.showerror("wrong entry", "please check input and try again")
            con.commit()
            bid.delete(0, END)
            rdate.delete(0,END)
            savl.delete(0, END)


        def delrun():
            Bid = bid.get()
            Rdate = rdate.get()
            try:
                if Bid == "" or Rdate == "":
                    messagebox.showerror("blank_field", "Bid")
                cur.execute(
                    "select * from run_details where bus_id=? and running_date=?",
                    (int(Bid), Rdate),
                )
                l = cur.fetchall()
                if l == []:
                    raise EXCEPTION(
                        messagebox.showerror("deletion error", "no such record exist")
                    )
                cur.execute(
                    "delete from run_details where bus_id=? and running_date=?",
                    (int(Bid), Rdate),
                )
                messagebox.showinfo("record deletion", "record deleted successfully")
            except ValueError:
                messagebox.showerror("wrong entry", "please check input and try again")
            con.commit()
            bid.delete(0, END)
            rdate.delete(0,END)
            savl.delete(0, END)
        Button(fr2, text="Add Run", bg="springgreen2", command=addrun).grid(
            row=3, column=6, padx=10
        )
        Button(fr2, text="Delete Run", bg="springgreen2", fg="red2", command=delrun).grid(
            row=3, column=7, padx=10
        )
        def hom():
            root.destroy()
            self.page1()
        im = PhotoImage(file="home.png")
        Button(fr2, image=im, bg="springgreen2").grid(row=3, column=8, padx=10)
        # cur.execute('select * from run_details')
        # Label(fr2,text=cur.fetchall()).grid(row=4,column=1)
        root.mainloop()


b=obp()
b.title()