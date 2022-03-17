class spartan:

    def __init__ (self,s_id ,f_name,l_name,b_year, b_month,b_day,s_course,s_stream):
    
        self.sparta_id = s_id
        self.first_name = f_name
        self.last_name = l_name
        self.birth_year = b_year
        self.birth_month = b_month
        self.birth_day = b_day
        self.sparta_course = s_course
        self.sparta_stream = s_stream

    def __str__(self):
        return f"ID: {self.sparta_id}, first_name : {self.first_name}, last_name :{self.last_name}, birth_year: {self.birth_year}, birth_month: {self.birth_month}, birth_day: {self.birth_day}, sparta_course: {self.sparta_course}, sparta_stream: {self.sparta_stream}"

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

    def set_sparta_id(self,sparta_id):
        self.sparta_id = sparta_id
    def set_first_name(self,first_name):
        self.first_name = first_name
    def set_last_name(self,last_name):
        self.last_name = last_name
    def set_birth_year(self,birth_year):
        self.birth_year = birth_year
    def set_birth_mont(self,birth_month):
        self.birth_month = birth_month
    def set_birth_day(self,birth_day):
        self.birth_day = birth_day
    def set_sparta_course(self,sparta_course):
        self.sparta_course= sparta_course
    def set_sparta_stream(self,sparta_stream):
        self.sparta_stream = sparta_stream

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
