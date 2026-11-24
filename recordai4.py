import csv
students=[
    {"Roll No.":"101","Name":"Anitha","Department":"CSE","Mark":86},
    {"Roll No.":"102","Name":"Bala","Department":"CSE","Mark":91},
    {"Roll No.":"103","Name":"Chitra","Department":"ECE","Mark":78}
]
course=("Python",4)
print("Course Tuple:",course)
with open("student.txt","w") as file:
    for student in students:
        file.write(str(student)+"\n")
with open("students.csv","w",newline="") as file:
    fields=["roll No." , "Name" , "Department" , "Mark"]
    writer=csv.DictWriter(file,fieldnames=fields)
    writer.write()
    writer.writerows(students)

print("\n-----Records from csv-----")
with open("students.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["Roll No"], row["Name"],
              row["Department"], row["Mark"])