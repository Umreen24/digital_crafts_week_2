import json
import datetime

tables = []
user_input = ""

class PoolTable:
    def __init__(self,number,table_status = "Unoccupied"):
        self.number = number
        self.table_status = table_status
        self.start_time = ""
        self.end_time = ""
        self.total_play_time = ""

def create_a_table():
    number = input("Enter table number: ")
    table_number = PoolTable(number)
    tables.append(table_number)

def status_of_table():
    for index in range(0, len(tables)):
        print(f"Table Number: {tables[index].number} - Status: {tables[index].table_status}")

def menu():
    print("1) Create a table ")
    print("2) View table status ")
    print("3) Open a table ")
    print("4) Return table ")
    print("5) Get the total time played and save play day ")
    
def table_ready_for_play():
    selected_table = int(input("Select the table you wish to play at: "))
    start_time = datetime.datetime.now()
    if selected_table == "Unoccupied":
        selected_table == "Occupied"
    print(f"Table {selected_table} is now occupied. The start time is {start_time} ")

def game_play_done():
    selected_table = int(input("Enter the table you would like to close: "))
    end_time = datetime.datetime.now()
    print(f"Thank you for playing table {selected_table}. The end time was {end_time}")

def total_play_time(table_number):
    total_time = (table_number.end_time.minute) - (table_number.start_time.minute)
    print(total_time)

file_name = "pool_table_management.json"

def save_day():
    with open(file_name, "w") as file_object:
        management_array = []
        for table in tables:
            management_array.append(table.__dict__)
        json.dump(management_array, file_object)

while user_input != "q":
    menu()
    user_input = input("Press 1, 2, 3, 4, or 5 to continue. Press q to quit ")
    
    if user_input == "1":
        create_a_table()
    
    elif user_input == "2":
        status_of_table()
    
    elif user_input == "3":
        table_ready_for_play()
    
    elif user_input == "4":
        game_play_done()
    
    elif user_input == "5":
        total_play_time(tables)
        save_day()


# need to ask about else statement and time