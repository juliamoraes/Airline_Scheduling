#libs 
import numpy as np 

#check if desired seats are valid
def check_desired_seats(passenger_desired_seats, num_flights, num_seats):
    for desired_seat in passenger_desired_seats:
        flight_num = desired_seat // num_seats
        seat_num = desired_seat % num_seats
        if flight_num >= num_flights or seat_num >= num_seats:
            return False  #Return False if the desired seat is invalid
    return True  #All desired seats are valid

#assign seats to passengers based on desired seats
def solve_airline_scheduling(flight_data, passenger_data):
    num_flights = len(flight_data)
    num_seats = flight_data[0]['num_seats']  #Number of seats in a flight

    if not all(check_desired_seats(passenger['desired_seats'], num_flights, num_seats) for passenger in passenger_data):
        return None, "Invalid desired seat numbers"  
    
    #Creating a matrix to represent seat availability
    seat_matrix = np.zeros((num_flights, num_seats), dtype=int)  

    #Assigning available seats in each flight
    for flight in flight_data:
        flight_num = flight['flight_number']
        flight_seats = flight['num_seats']
        seat_matrix[flight_num-1, :flight_seats] = 1  

    seat_assignments = []
    #Assigning seats to passengers based on their desired seats
    for passenger in passenger_data:
        passenger_assignments = []
        for desired_seat in passenger['desired_seats']:
            flight_num = desired_seat // num_seats
            seat_num = desired_seat % num_seats
            if seat_matrix[flight_num-1, seat_num] == 1:
                #Assigning valid seat to passenger
                passenger_assignments.append((flight_num, seat_num)) 
                #Seat occupied in the matrix 
                seat_matrix[flight_num-1, seat_num] = 2  
        seat_assignments.append(passenger_assignments)
        
    #Return seat assignments
    return seat_assignments, "Seats assigned successfully"  

#Flight data, number, seat number 
flight_data = [
    {"flight_number": 1, "num_seats": 30},  
    {"flight_number": 2, "num_seats": 15}, 
    {"flight_number": 3, "num_seats": 15},  
]

#Passenger data
passenger_data = [
    {"name": "Alice", "phone": "123-456-7890", "address": "123 Main St", "credit_card": "1234567890123456", "desired_seats": [5, 10]},
    {"name": "Bob", "phone": "234-567-8901", "address": "456 Broadway", "credit_card": "2345678901234567", "desired_seats": [30, 35]},
    {"name": "Charlie", "phone": "345-678-9012", "address": "789 Elm St", "credit_card": "3456789012345678", "desired_seats": [15, 20]},
]

#seats to passengers
seat_assignments, status = solve_airline_scheduling(flight_data, passenger_data)
print(status)  #Printing the status of seat


#Printing statement seat assignments for each passenger
for passenger_assignments in seat_assignments:
    passenger_name = passenger_data[seat_assignments.index(passenger_assignments)]['name']
    assigned_seats = ', '.join(str(seat_num) for flight_num, seat_num in passenger_assignments)
    print(f" Passenger {passenger_name} -> Seats {assigned_seats}")  # Displaying assigned seats per passenger


#Flight data
flight_data = [
    {"flight_number": 1, "num_seats": 30},
    {"flight_number": 2, "num_seats": 15},
    {"flight_number": 3, "num_seats": 15},
]

#Passenger data
passenger_data = [
    {"name": "Alice", "phone": "123-456-7890", "address": "123 Main St", "credit_card": "1234567890123456", "desired_seats": [5, 10]},
    {"name": "Bob", "phone": "234-567-8901", "address": "456 Broadway", "credit_card": "2345678901234567", "desired_seats": [30, 35]},
    {"name": "Charlie", "phone": "", "address": "789 Elm St", "credit_card": "3456789012345678", "desired_seats": [15, 20]},
]

seat_assignments, status = solve_airline_scheduling(flight_data, passenger_data)
print(status)
for passenger_assignments in seat_assignments:
    print(f" Passenger {passenger_data[seat_assignments.index(passenger_assignments)]['name']} -> Seats {', '.join(str(seat_num) for flight_num, seat_num in passenger_assignments)}")
