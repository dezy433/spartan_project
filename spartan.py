import spartan
import json
class Spartan:

    def __init__(self, s_id, f_name, l_name, b_year, b_month, b_day, s_course, s_stream):
        self.sparta_id = s_id
        self.first_name = f_name
        self.last_name = l_name
        self.birth_year = b_year
        self.birth_month = b_month
        self.birth_day = b_day
        self.sparta_course = s_course
        self.sparta_stream = s_stream

    def __str__(self):
        return f"ID: {self.sparta_id} \n first_name : {self.first_name} \n last_name :{self.last_name} \n birth_year: {self.birth_year}\n birth_month: {self.birth_month}\n birth_day: {self.birth_day}\n sparta_course: {self.sparta_course}\n sparta_stream: {self.sparta_stream}\n"

    def get_sparta_id(self):
        return self.sparta_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_year(self):
        return self.birth_year

    def get_birth_month(self):
        return self.birth_month

    def get_birth_day(self):
        return self.birth_day

    def get_sparta_course(self):
        return self.sparta_course

    def get_sparta_stream(self):
        return self.sparta_stream

    def set_sparta_id(self, sparta_id):
        self.sparta_id = sparta_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_birth_year(self, birth_year):
        self.birth_year = birth_year

    def set_birth_mont(self, birth_month):
        self.birth_month = birth_month

    def set_birth_day(self, birth_day):
        self.birth_day = birth_day

    def set_sparta_course(self, sparta_course):
        self.sparta_course = sparta_course

    def set_sparta_stream(self, sparta_stream):
        self.sparta_stream = sparta_stream


def read_trainee_id():
    while True:
        id_str = input("Please enter the Trainee ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            id = int(id_str)
            if id > 0:
                return id
            else:
                print("Error, The Employee ID should be positive number")
        else:
            print("Error, The Employee ID should be a number")



def read_first_name():
    while True:
        first_name = input("Please enter the trainee first name")
        first_name = first_name.strip()
        if len(first_name) >= 2:
            return first_name
        else:
            print("Error, Trainee name has to be at least 2 characters")

def read_last_name():
    while True:
        last_name = input("Please enter the trainee last name")
        last_name = last_name.strip()
        if len(last_name) >= 2:
            return last_name
        else:
            print("Error,Trainee last name has to be at least 2 characters")

def read_year():
    while True:
        year_str = input("Please enter the Trainee Birth Year:")
        year_str = year_str.strip()

        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, The Trainee Birth Year should be between 1900 and 2004")



def read_month():
    while True:
        month_str = input("Please Enter the Trainee Birth Month:")
        month_str = month_str.strip()

        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, The Trainee Birth Month should be between 1 and 12")
        else:
            print("Error, The Trainee Birth Month should be a number")


def read_day():
    while True:
        day_str = input("Please Enter the Trainee Birth Day:")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The Trainee Birth Day should be between 1 and 31")
        else:
            print("Error, The Trainee Birth Day should be a number")

def read_course():
    while True:
        course = input("Please Enter The Trainee Course:")
        course = course.strip()

        if len(course) >= 1:
            return course
        else:
            print("Error, The Trainee Course should be at least 1 Characters")

def read_stream():
    while True:
        stream = input("Please Enter The Trainee Stream:")
        stream = stream.strip()

        if len(stream) >= 1:
            return stream
        else:
            print("Error, The Trainee stream should be at least 1 Characters")

def create_trainee():
    trainee_id = read_trainee_id()
    trainee_first_name = read_first_name()
    trainee_last_name = read_last_name()
    trainee_birth_year = read_year()
    trainee_birth_month = read_month()
    trainee_birth_day = read_day()
    trainee_course = read_course()
    trainee_stream = read_stream()

    trainee = Spartan(trainee_id,trainee_first_name, trainee_last_name, trainee_birth_year, trainee_birth_month, trainee_birth_day,trainee_course, trainee_stream, )
    return trainee

def add_trainee():

    trainee = create_trainee()

    trainee_db[trainee.get_id()] = trainee
    print("The employee was added to the list")
def print_trainee_db():
    global trainee_db
    for entry in trainee_db:
        print(trainee_db[entry])

def print_all_trainee_data():
    for trainee_id_key in all_trainee_dict:
        print(f"The data of the Trainers with Trainee_ID = {trainee_id_key}")
        print(all_trainee_dict[trainee_id_key])

def save_to_json():
    global trainee_id
    temp_dict_of_dict = {}
    for trainee_id in all_trainee_dict:
        trainee_obj = all_trainee_dict[trainee_id]
        trainee_dict = trainee_obj.__dict__
        temp_dict_of_dict[trainee_id] = trainee_dict

    with open("data.json", "w") as data_file:
        json.dump(temp_dict_of_dict, data_file)


def load_from_json():
    temp_dict_of_dict = {}
    global all_trainee_dict

    for trainee_id_key in temp_dict_of_dict:
        trainee_id = temp_dict_of_dict[trainee_id_key]['s_id']
        trainee_first_name = temp_dict_of_dict[trainee_id_key]['first_name']
        trainee_last_name = temp_dict_of_dict[trainee_id_key]['last_name']

        with open("data.json", "r") as data_file:
            temp_dict_of_dict = json.load(data_file)
    trainee_obj = Spartan(trainee_id, trainee_first_name, trainee_last_name, trainee_birth_year, trainee_birth_month,
                          trainee_birth_day, trainee_course, trainee_stream)
    all_trainee_dict[trainee_id] = trainee_obj

def read_options():
    while True:
        options = input("Options: \nadd) Add an Trainee \nremove) Remove an Trainee\nlist) List of Trainees \nupdate) Update Trainee Data \nsave) Save \nload)Load\nexit) Exit\n")
        options = options.strip()
        if options in ["add", "remove", "update", "list", "save","load","exit"]:
            return options
        else:
            print("Error, You should select one of the options in the list")

if __name__ == "__main__":
    all_trainee_dict = {}
    json_list = []

    while True:
        option = read_options()

        if option == "add":
            print("The user wants to add an Employee")
            trainee_object = create_trainee()

            # employee_id = read_employee_id()
            trainee_id = trainee_object.get_sparta_id()
            all_trainee_dict[trainee_id] = trainee_object
            print(all_trainee_dict.get(trainee_id))
            #log_file.write("Trainee Added")
            save_to_json()
        elif option == "remove":
            print("The user wants to remove an trainee")
            trainee_id = read_trainee_id()
            del all_trainee_dict[trainee_id]
            # log_file.write("Employee remove")

        elif option == "list":
            print("The user wants a list of the employees")
            print_all_trainee_data()
            # log_file.write("Employee list")

        elif option == "save":
            save_to_json()

        elif option == "load":
            print("5")
            employees_dict = {}
            with open("data.json", "r") as my_file:
                all_employees_dict = json.load(my_file)
                print(employees_dict)

        elif option == "exit":
            print("You have exited")
            break
        else:
            print("Unknown option")
