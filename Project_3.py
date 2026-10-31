
subjects = ('Python','Maths','DBMS')
n_students=int(input("How many students to be added?"))
student_ids =[]
student_records={}
averages=[]
Class_total = 0
highest_average= -1
highest_student=""
lowest_average= 101
lowest_student=""
passed_subjects=set()
while n_students!=0: 
    student_id=(input("\nEnter Student ID:"))
           
    student_name=input("Enter Student Name:")
        
    python_mark=int(input("Enter Python Marks:"))
    
    if 0<=python_mark<=100:
        pass
    else:
        print("Python marks must be in between 0 and 100.")
        continue
       
    maths_mark=int(input("Enter Maths Marks:"))
    
    if  0<=maths_mark<=100 :
        pass
    else:
        print("Maths marks must be in between 0 and 100.")
        continue 
        
    dbms_mark=int(input("Enter DBMS Marks:"))
    
    if  0<=dbms_mark<=100:
        pass
    else:
        print("Maths marks must be in between 0 and 100.")
        continue
      
    marks = [python_mark,maths_mark,dbms_mark] 
    
    student_records[student_id]={'Name':student_name,'Marks':marks}
    
    if student_id not in student_records :
    
        print("This student ID is already exist!. Try Again")
        continue
    
    student_ids.append(student_id)           
    n_students-=1
print("\n"+"="*50)
print("\n       STUDENT REPORT\n")
print("="*50)
for student in student_ids:
    
    name=student_records[student]["Name"]
    
    mark_list=student_records[student]['Marks']
    
    total_marks=0
    for i in range(len(mark_list)):
        
        total_marks = total_marks+mark_list[i]
        
        if mark_list[i]>=40:
            passed_subjects.add(subjects[i])

    Average=total_marks/(len(subjects))
    
    Class_total=Class_total+Average
    
    averages.append(Average)
    if Average>=75:
        result = 'Distinction'
    elif Average>=40:
        result = 'Pass'
    else:
        result = 'Fail'
    if Average > highest_average:  
        highest_average=Average
        highest_student=student_id     
    if Average < lowest_average:
        lowest_average=Average
        lowest_student=student_id
    print(f"\n{student} | {student_records[student]['Name']}") 
    
    for i in range(len(subjects)):
        print(f"{subjects[i]}:{mark_list[i]}, ",end=' ')
        
    print(f"\nTotal: {total_marks} | Average: {Average} | Result:{result}")

print("\nFirst Two Students ID are: ", student_ids[:2])
print("\n"+"="*50)

search_id = input("Enter Student ID to search:")

if search_id in student_records:
    
    print("Student Record Found!")
    print(f"Student Name: {student_records[search_id]["Name"]}")
    print(f"Student Marks: {student_records[search_id]['Marks']}")
    
else:
    print("Student Record Not Found!")
    
'''Update Marks'''
print("="*50)

update_id = input("Enter Student ID to update:")

if update_id in student_records:
    
    for i in range(len(subjects)):
        print(f"{i+1}.{subjects[i]}")
        
    pos = int(input("choose position of subject(1-3): "))
    
    if 1<=pos<=3:
        
        new_mark=int(input(f"Enter updated marks for {subjects[pos-1]}: "))
        
        if 0<=new_mark<=100:
            
            student_records[update_id]["Marks"][pos-1] = new_mark
            print("Marks Updated Successfully!!")
            
        else:
            print("Marks must be in between 0 and 100")      
    else:
        print("Invalid Subject position!")      
else:
    print("Student ID not found.")
    
''' Recalculate Updated Results for Class Summary '''
subjects_passed_by_anyone= set()

#passed student Dictionary
student_pass_sets = {}
class_total = 0
highest_average = -1
lowest_average = 101
highest_student = ""
lowest_student = ""
for student_id in student_ids:
    marks = student_records[student_id]["Marks"]
    total = 0
    passed_subjects = set()
    for j in range(len(marks)):
        total = total + marks[j]
        if marks[j] >= 40:
            passed_subjects.add(subjects[j])
            subjects_passed_by_anyone.add(subjects[j])
    student_pass_sets[student_id] = passed_subjects
    average = total / len(subjects)
    class_total = class_total + average
    if average > highest_average:
        highest_average = average
        highest_student = student_id
    if average < lowest_average:
        lowest_average = average
        lowest_student = student_id
print('\n'+'='*50)
if len(student_ids)>=2:
    id_1 = input("Enter first student ID for set Analysis: ")
    id_2 = input("Enter second student ID for set Analysis: ")
    if (id_1 in student_records and id_2 in student_records and id_1!=id_2):   
        first_set = student_pass_sets[id_1]
        second_set = student_pass_sets[id_2]
        print("First student's passed subjects:", sorted(first_set))
        print("Second student's passed subjects:", sorted(second_set))
        print("Union:", sorted(first_set | second_set))
        print("Intersection:", sorted(first_set & second_set))
        print("Difference:", sorted(first_set - second_set))
        print("Symmetric difference:", sorted(first_set ^ second_set))
    else:
        print("Enter two different valid student IDs.")
else:
    print("At least two students are needed for set comparison.")
print("\n" + "=" * 55)
print("                  CLASS SUMMARY")
print("=" * 55)
print("Students Recorded: ", len(student_ids))   
if len(student_ids)>0:
    class_average = class_total/(len(student_ids))
    print(f"Class Average: {class_average}")  
    print(f"Highest Average: {highest_average} | Highest Scoring Student: {highest_student}")  
    print(f"Lowest Average: {lowest_average} | Lowest Scoring Student: {lowest_student}") 
    print("Unique subjects:", sorted(set(subjects)))
    print("Subjects passed by at least one student:", sorted(subjects_passed_by_anyone))