class Subject:
    def __init__(self, group_id, subject_id, subject_name, lecture_hours, practice_hours, requires_subgroups):
        self.group_id = group_id
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.lecture_hours = lecture_hours
        self.practice_hours = practice_hours
        self.requires_subgroups = str(requires_subgroups).lower() == 'yes'

    def __repr__(self):
        return (f"Subject({self.group_id}, {self.subject_id}, {self.subject_name}, "
                f"{self.lecture_hours}, {self.practice_hours}, {self.requires_subgroups})")
