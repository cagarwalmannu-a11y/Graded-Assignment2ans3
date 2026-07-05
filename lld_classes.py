class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def get_student_id(self):
        return self.student_id

class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id

    def get_enrollment_id(self):
        return self.enrollment_id

class EnrollmentRepository:
    def get_enrollment(self, enrollment_id):
        pass

    def create_enrollment(self, enrollment):
        pass
