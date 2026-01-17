# student_record_system.py
# Name: Kevin Pavione
# Student ID: 84012
# Date: January 2026
# Assignment: Student Record Management System

class Student:
    """A class representing a student in the university system."""
    
    def __init__(self, first_name, last_name, student_id, email, major, gpa, credits_completed, enrollment_status):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.email = email
        self.major = major
        self.gpa = float(gpa) if 0.0 <= float(gpa) <= 4.0 else 0.0
        self.credits_completed = max(0, int(credits_completed))
        self.enrollment_status = enrollment_status if enrollment_status in ["Full-Time", "Part-Time"] else "Part-Time"
        
    def get_full_name(self):
        """Return the student's full name."""
        return f"{self.first_name} {self.last_name}"
    
    def update_gpa(self, new_gpa):
        """Update GPA if value is valid (0.0-4.0)."""
        new_gpa = float(new_gpa)
        if 0.0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
        else:
            print(f"Error: GPA must be between 0.0 and 4.0. Current GPA unchanged ({self.gpa}).")
    
    def add_credits(self, credits):
        """Add credits if amount is positive."""
        credits = int(credits)
        if credits > 0:
            self.credits_completed += credits
        else:
            print(f"Error: Cannot add negative or zero credits ({credits}).")
    
    def get_class_standing(self):
        """Determine class standing based on credits completed."""
        if self.credits_completed <= 29:
            return "Freshman"
        elif self.credits_completed <= 59:
            return "Sophomore"
        elif self.credits_completed <= 89:
            return "Junior"
        else:
            return "Senior"
    
    def display_info(self):
        """Print formatted student information."""
        deans = "Yes" if self.is_on_deans_list() else "No"
        print(f"Student: {self.get_full_name()} ({self.student_id})")
        print(f"Email: {self.email}")
        print(f"Major: {self.major}")
        print(f"GPA: {self.gpa:.1f}")
        print(f"Credits: {self.credits_completed}")
        print(f"Status: {self.enrollment_status}")
        print(f"Class Standing: {self.get_class_standing()}")
        print(f"Dean's List: {deans}")
        print()
    
    def is_on_deans_list(self):
        """Return True if student qualifies for Dean's List (GPA >= 3.5)."""
        return self.gpa >= 3.5


class Course:
    """A class representing an academic course offering."""
    
    def __init__(self, course_code, course_name, credits, instructor, max_capacity):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = int(credits)
        self.instructor = instructor
        self.max_capacity = int(max_capacity)
        self.enrolled_students = []
    
    def enroll_student(self, student):
        """Attempt to enroll a student in the course."""
        if self.is_full():
            print(f"Course is full. Cannot enroll {student.get_full_name()} in {self.course_code}")
            return False
        
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"Successfully enrolled {student.get_full_name()} in {self.course_code}")
            return True
        return False
    
    def drop_student(self, student_id):
        """Remove a student from the course by student ID."""
        for i, student in enumerate(self.enrolled_students):
            if student.student_id == student_id:
                removed_name = student.get_full_name()
                self.enrolled_students.pop(i)
                print(f"Successfully dropped {removed_name} from {self.course_code}")
                return True
        print(f"Student ID {student_id} not found in {self.course_code}")
        return False
    
    def get_enrollment_count(self):
        """Return the current number of enrolled students."""
        return len(self.enrolled_students)
    
    def is_full(self):
        """Return True if course has reached maximum capacity."""
        return len(self.enrolled_students) >= self.max_capacity
    
    def get_roster(self):
        """Return list of enrolled students' full names."""
        return [student.get_full_name() for student in self.enrolled_students]
    
    def display_course_info(self):
        """Print formatted course information."""
        print(f"Course: {self.course_code} - {self.course_name}")
        print(f"Instructor: {self.instructor}")
        print(f"Credits: {self.credits}")
        print(f"Enrollment: {self.get_enrollment_count()}/{self.max_capacity}")
        print(f"Status: {'FULL' if self.is_full() else 'OPEN'}")
        print()
        
        if self.enrolled_students:
            print("Enrolled Students:")
            for i, name in enumerate(self.get_roster(), 1):
                print(f"  {i}. {name}")
        print()


def main():
    print("===================================")
    print("STUDENT RECORD MANAGEMENT SYSTEM")
    print("===================================\n")
    
    # --- Creating Students ---
    print("--- Creating Students ---")
    students = [
        Student("John", "Smith", "STU001", "jsmith@ocu.edu", "Computer Science", 3.8, 95, "Full-Time"),
        Student("Sarah", "Johnson", "STU002", "sjohnson@ocu.edu", "Information Technology", 3.6, 75, "Full-Time"),
        Student("Michael", "Davis", "STU003", "mdavis@ocu.edu", "Computer Science", 3.2, 45, "Full-Time"),
        Student("Emily", "Wilson", "STU004", "ewilson@ocu.edu", "Data Science", 3.9, 110, "Full-Time"),
        Student("James", "Brown", "STU005", "jbrown@ocu.edu", "Computer Science", 3.3, 25, "Part-Time")
    ]
    
    for student in students:
        print(f"Student created: {student.get_full_name()} ({student.student_id})")
    print()
    
    # --- Creating Courses ---
    print("--- Creating Courses ---")
    cs125 = Course("CS125", "Programming for Everyone II", 3, "Dr. Miller", 4)
    print(f"Course created: {cs125.course_code} - {cs125.course_name}\n")
    
    # --- Enrolling Students ---
    print("--- Enrolling Students ---")
    cs125.enroll_student(students[0])
    cs125.enroll_student(students[1])
    cs125.enroll_student(students[2])
    cs125.enroll_student(students[3])
    cs125.enroll_student(students[4])  # Should fail - course full
    print()
    
    # --- Student Information ---
    print("--- Student Information ---")
    for student in students:
        student.display_info()
    
    # --- Course Information ---
    print("--- Course Information ---")
    cs125.display_course_info()
    
    # --- Dean's List ---
    print("--- Dean's List Students ---")
    print("Dean's List (GPA >= 3.5):")
    deans_list = [s for s in students if s.is_on_deans_list()]
    if deans_list:
        for student in deans_list:
            print(f"  - {student.get_full_name()} ({student.gpa:.1f} GPA)")
    else:
        print("  No students on Dean's List")
    print()
    
    print("===================================")
    print("END OF REPORT")
    print("===================================")


if __name__ == "__main__":
    main()