class StudentGrader:
    def calculate_grades(self, scores):
        grades = []
        for score in scores:
            # Your grading logic here (you can customize this)
            if score >= 90:
                grades.append('A')
            elif 80 <= score < 90:
                grades.append('B')
            elif 70 <= score < 80:
                grades.append('C')
            elif 60 <= score < 70:
                grades.append('D')
            else:
                grades.append('F')
        return grades

