import spartan
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
        last_name = input("Please enter the trainee first name")
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


    trainee = Spartan(trainee_id,trainee_first_name, trainee_last_name, trainee_birth_year, trainee_birth_month,
                            trainee_birth_day,trainee_course, trainee_stream, )
    return trainee

def add_trainee():

    trainee = create_trainee()

    trainee_db[trainee.get_id()] = employee
    print("The employee was added to the list")

def print_all_trainee_data():
    for employee_id_key in all_employees_dict:
        print(f"The data of the employee with Employee_ID = {employee_id_key}")
        print(all_employees_dict[employee_id_key])

def save_to_json():
    temp_dict_of_dict = {}
    for employee_id in all_trainee_dict:
        trainee_obj = all_trainee_dict[employee_id]
        trainee_dict = trainee_obj.__dict__
        temp_dict_of_dict[trainee_id] = trainee_dict

    with open("data.json", "w") as data_file:
        json.dump(temp_dict_of_dict, data_file)

def load_from_json():
    global all_employees_dict
    temp_dict_of_dict = {}
    try:
        with open("data.json", "r") as data_file:
            temp_dict_of_dict = json.load(data_file)
    except:
        print("The file data1.json doesn't exist")

    print(temp_dict_of_dict)

    for employee_id_key in temp_dict_of_dict:
        employee_id = temp_dict_of_dict[employee_id_key]['emp_id']
        employee_first_name = temp_dict_of_dict[employee_id_key]['first_name']
        employee_last_name = temp_dict_of_dict[employee_id_key]['last_name']

        employee_obj = Employee(employee_id, employee_first_name, employee_last_name)
        all_employees_dict[employee_id] = employee_obj

def read_options():
    while True:
        options = input("Options: \nadd) Add an Trainee \nremove) Remove an Trainee\nlist) List of Trainees \nupdate) Update Trainee Data \nsave) Save \nexit) Exit\n")
        options = options.strip()
        if options in ["add", "remove", "update", "list ", "save","exit"]:
            return options
        else:
            print("Error, You should select one of the options in the list")

if __name__ == "__name__":

        all_trainee_dict = {}
        json_list = []

        try:
            with open("course.txt", 'w') as log_file:
                log_file.write("New employee added" + "\n")
                log_file.close()
        except FileNotFoundError as file_not_found_error:
            print("create file")
        except Exception as ex:
            print("Error happened")
            print(ex)
        finally:
            print("Finally code")
            print("Unknown option")

        while True:
            option = read_options()

            if option == "add":
                print("The user wants to add an Employee")
                trainee_object = create_trainee()

                # employee_id = read_employee_id()
                trainee_id = trainee_object.get_id()
                all_trainee_dict_dict[trainee_id] = trainee_object
                print(all_employees_dict.get(employee_id))
                log_file.write("Employee Added")




            elif option == "remove":
                print("The user wants to remove an Employee")
                employee_id = read_employee_id()
                del all_employees_dict[employee_id]
                # log_file.write("Employee remove")

            elif option == "list":
                print("The user wants a list of the employees")
                all_employee_data()
                # log_file.write("Employee list")

            elif option == "update":
                print("The user wants to update the data of an employee")
                employee_id = read_employee_id()
                update_employee_data(employee_id)
                # log_file.write("Employee update")

            elif option == "save":
                print("h")

            elif option == "load":
                print("5")
                employees_dict = {}
                with open("data.json", "r") as my_file:
                    all_employees_dict = json.load(my_file)
                print(employees_dict)

            elif option == "7":
                print("You have exited")
                break
            else:
                print("Unknown option")
