# Decorator
def decorate_report(func):
    def wrapper(*args):
        print("________________________________")
        func(*args)
        print("________________________________")
    return wrapper


class Report:

    template = "Default Template"

    # Constructor
    def __init__(self, name, class_name, roll_no, college, project):
        self.name = name
        self.class_name = class_name
        self.roll_no = roll_no
        self.college = college
        self.project = project

    # Class Method
    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    # Magic Method
    def __str__(self):
        return (
            f"Template : {self.template}\n"
            f"Name     : {self.name}\n"
            f"Class    : {self.class_name}\n"
            f"Roll No. : {self.roll_no}\n"
            f"College  : {self.college}\n"
            f"Project  : {self.project}"
        )

    # Decorated Method
    @decorate_report
    def show_report(self):
        print(self)


# Main Program
Report.change_template("Student Report")

r1 = Report(
    "Atharva Parande",
    "SY11",
    12,
    "MIT ADT University",
    "Dynamic Report Generator using OOP"
)

r1.show_report()