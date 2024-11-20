class Group:
    def __init__(self, group_id, students, subgroups):
        self.group_id = group_id
        self.students = students
        self.subgroups = subgroups

    def __repr__(self):
        return f"Group({self.group_id}, {self.students}, {self.subgroups})"
