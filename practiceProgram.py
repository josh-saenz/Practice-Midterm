import practiceClass as p
import csv


shows = {
    "play1":{
        'id':3245,
        'name':'Phantom of the Opera',
        'capacity':65,
        'event_date':'03/01/2023'
    },
    "play2":{
        'id':1548,
        'name':'The Music Man',
        'capacity':45,
        'event_date':'05/15/2023'
    },
    "play3":{
        'id':9587,
        'name':'Hamilton',
        'capacity':124,
        'event_date':'07/21/2023'
    },
    "play4":{
        'id':6254,
        'name':'The Lion King',
        'capacity':89,
        'event_date':'09/29/2023'
    },

}

'''using the above dictionary iterate through it and create an instance of the 
play class that has id 9587
NOTE: Do not hard code the values to create the instance but use
keys and values from the dictionary '''



'''using the bookings.csv file process only those 
reservations for the same play (9587). Create an 
instance of the Booking class for each customer
that is going to play 9587 - Hamilton. 
if the play reaches capacity print out a 
error message as shown in output.JPG'''


#open the csv file in read mode
infile = open('bookings.csv', 'r')



#create a csv object from the file object from the step above
reader = csv.reader(infile, delimiter= ',')

next(reader)


# use a for loop to iterate through each record in the bookings file

for key in shows:
    if shows[key]['id'] == 9587:
        play = p.Play(shows['play3']['id'],shows['play3']['name'], shows['play3']['capacity'], shows['play3']['event_date'], True)


for i in reader:
    if int(i[0]) == play.get_id():
        play.seats_left()
        p.Booking(i[1],i[2])
        if play.get_number_of_seats()<0:
            print('*************ERROR****************')
            print(f'Guest Name: {i[1]}')
            print(f'Sorry, show: ' + play.get_name()+ ' is sold out')
            print('**********************************')
