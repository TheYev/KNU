import re


class Lecturer:
    def __init__(self, lecturer_id, lecturer_name, subject_ids, can_teach_lecture, can_teach_practice):
        self.lecturer_id = lecturer_id
        self.lecturer_name = lecturer_name
        subject_ids = re.sub(r'[\[\]\s]', '', str(subject_ids))
        self.subject_ids = [int(sid) for sid in subject_ids.split(',') if sid.isdigit()]

        self.can_teach_lecture = str(can_teach_lecture).lower() == 'yes'
        self.can_teach_practice = str(can_teach_practice).lower() == 'yes'

    def __repr__(self):
        return (f"Lecturer({self.lecturer_id}, {self.lecturer_name}, {self.subject_ids}, "
                f"{self.can_teach_lecture}, {self.can_teach_practice})")
