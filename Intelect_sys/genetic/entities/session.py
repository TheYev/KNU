class Session:
    def __init__(self, group, subject, lecturer, classroom, day, period, session_type):
        self.group = group
        self.subject = subject
        self.lecturer = lecturer
        self.classroom = classroom
        self.day = day
        self.period = period
        self.session_type = session_type

    def __repr__(self):
        return (f"Session(Group: {self.group.group_id}, Subject: {self.subject.subject_name}, "
                f"Lecturer: {self.lecturer.lecturer_name}, Classroom: {self.classroom.classroom_id}, "
                f"Day: {self.day}, Period: {self.period}, Type: {self.session_type})")
