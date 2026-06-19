def student_marks_tracker():
    student_records = {
        "Rahul": 85,
        "Aditya": 92,
        "Sneha": 78,
        "Priya": 95,
        "Amit": 64
    }
    
    print("\n--- Student Records ---")
    for name, marks in student_records.items():
        print(f"Student: {name:<10} | Marks: {marks}")
    
    all_marks = student_records.values()
    class_average = sum(all_marks) / len(all_marks)
    
    top_student = max(student_records, key=student_records.get)
    highest_marks = student_records[top_student]
    
    print("\n" + "=" * 40)
    print(f"Class Average: {class_average:.2f}")
    print(f"Top Performer: {top_student} ({highest_marks} Marks)")
    print("=" * 40)

student_marks_tracker()
