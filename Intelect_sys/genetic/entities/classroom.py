class Classroom:
    def __init__(self, classroom_id, capacity):
        self.classroom_id = classroom_id
        self.capacity = capacity

    def __repr__(self):
        return f"Classroom({self.classroom_id}, {self.capacity})"

