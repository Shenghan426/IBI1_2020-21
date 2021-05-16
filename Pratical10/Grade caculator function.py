class Grade: #create a class
    def __init__(self, student_name, portfolio, presentation, exam):
        self.name = student_name
        self.portfolio = portfolio
        self.presentation = presentation
        self.exam = exam

    def final_grade(self):
        # use int to make sure is can be calculated
        total_grade = 0.3 * int(self.presentation) + 0.3 * int(self.exam) + 0.4 * int(self.portfolio)
        print('The total grade of ', self.name, 'is', total_grade)
        return
#exaple
student_grade = Grade ('Tony','90','90','80')
student_grade.final_grade()