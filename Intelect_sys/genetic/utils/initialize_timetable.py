from constants import PERIODS, DAYS
from entities.session import Session
import random

def find_suitable_lecturer(lecturers, subject, session_type):
    suitable_lecturers = [l for l in lecturers if subject.subject_id in l.subject_ids]
    if session_type == 'lecture':
        suitable_lecturers = [l for l in suitable_lecturers if l.can_teach_lecture]
    else:
        suitable_lecturers = [l for l in suitable_lecturers if l.can_teach_practice]

    return random.choice(suitable_lecturers) if suitable_lecturers else None


def find_suitable_classroom(classrooms, capacity):
    suitable_classrooms = [c for c in classrooms if c.capacity >= capacity]
    if not suitable_classrooms:
        print(f"Warning: No suitable classroom found for capacity {capacity}")
    return random.choice(suitable_classrooms) if suitable_classrooms else None


def find_balanced_slot(timetable, lecturer, classroom, group):
    day_counts = {day: sum(len(timetable[day][period]) for period in timetable[day]) for day in DAYS}
    sorted_days = sorted(day_counts, key=day_counts.get) 

    for day in sorted_days:
        for period in range(1, PERIODS + 1):
            if all(session.lecturer != lecturer for session in timetable[day][period]) and \
               all(session.classroom != classroom for session in timetable[day][period]) and \
               all(session.group != group for session in timetable[day][period]):
                return day, period
    return None, None



def initialize_balanced_timetable(groups, subjects, lecturers, classrooms):
    timetable = {day: {period: [] for period in range(1, PERIODS + 1)} for day in DAYS}

    random.shuffle(groups) 

    for group in groups:
        group_subjects = [s for s in subjects if s.group_id == group.group_id]
        random.shuffle(group_subjects)  

        for subject in group_subjects:
            lecturer = find_suitable_lecturer(lecturers, subject, session_type='lecture')
            if lecturer:
                classroom = find_suitable_classroom(classrooms, group.students)
                if classroom:
                    day, period = find_balanced_slot(timetable, lecturer, classroom, group)
                    if day is not None and period is not None:
                        session = Session(group, subject, lecturer, classroom, day, period, 'lecture')
                        timetable[day][period].append(session)

            lecturer = find_suitable_lecturer(lecturers, subject, session_type='practice')
            if lecturer:
                capacity = group.students // group.subgroups if group.subgroups > 1 else group.students
                classroom = find_suitable_classroom(classrooms, capacity)
                if classroom:
                    day, period = find_balanced_slot(timetable, lecturer, classroom, group)
                    if day is not None and period is not None:
                        session = Session(group, subject, lecturer, classroom, day, period, 'practice')
                        timetable[day][period].append(session)

    return timetable
