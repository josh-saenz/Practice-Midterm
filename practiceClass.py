'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''
        
class Play: 
    def __init__(self, id, name, number_of_seats, date, status):
        self.__id =id
        self.__name = name
        self.__number_of_seats=number_of_seats
        self.__date = date
        self.__status = True

    def get_name(self):
        return self.__name
    
    def get_number_of_seats(self):
        return self.__number_of_seats

    def get_status(self):
        return self.__status
    
    def get_id(self):
        return self.__id
    
    def seats_left(self):
        self.__number_of_seats = self.__number_of_seats - 1

    def set_status(self):
        self.__status = False 

class Booking: 
    def __init__(self, customername, seatnumber):
        self.__customername = customername
        self.__seatnumber = seatnumber

    def get_customername(self):
        return self.__customername

    def get_seatnumber(self):
        return self.__seatnumber