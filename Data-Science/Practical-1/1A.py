def print_profile():
    name = "Aditya Rana"
    roll_no = "S105"
    class_name = "S. Y. B. Sc. (Computer Science)"
    semester = "Semester III"
    subject = "Python for Data Science"

    border = "=" * 50
    print(border)
    print(f"|{'STUDENT PROFILE':^48}|")
    print(border)
    print(f"| Name:        {name:<33} |")
    print(f"| Roll No:     {roll_no:<33} |")
    print(f"| Class:       {class_name:<33} |")
    print(f"| Semester:    {semester:<33} |")
    print(f"| Subject:     {subject:<33} |")
    print(border)


print_profile()
