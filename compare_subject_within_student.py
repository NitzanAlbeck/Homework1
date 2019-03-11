# I will first create two dicts of students and their two grades as a mock data
subj1_all_students = {'Lily' :[67, 87],'Marshall':[ 75, 93], 'Ted':[95, 99],'Robin':[65, 86],'Barney':[90, 96]}
subj2_all_students = {'Lily':[77, 97],'Marshall':[56, 91], 'Ted':[80, 74],'Tracy':[90, 61],'Barney':[98, 95]}

def compare_subjects_within_student(subj1_all_students,subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
        
    def high_score (students_grades_1):
        """
        determines the highest score for each student in this subject.
        the parameter entered is dictonary with 2 grades, and the output is a dictonary with the
            highest grade.
        """
        highest_score = dict()
        keys = students_grades_1.keys()
        
        for key in keys:
            grades = students_grades_1.get(key)
            highest_score[key] = max(grades)
        return highest_score

        
    subj1_grades = high_score (subj1_all_students)
    subj2_grades = high_score (subj2_all_students)

    #creating a list with only students that appear in both dicts, ussing union operator:
    students = set(subj1_grades.keys()) & set(subj2_grades.keys())    

    best_subject = dict()
    sub1_name = 'Hitory'
    sub2_name = 'Math'

    for student in students:
        grade1 = subj1_grades[student]
        grade2 = subj2_grades[student]
        if grade1>grade2:
            best_subject [student] = sub1_name
        else:
            best_subject[student] = sub2_name
    return best_subject

print(compare_subjects_within_student(subj1_all_students,subj2_all_students))
