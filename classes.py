import datetime

class Problem:
    def __init__(self, number, difficulty, date, review):
        self.number = number
        self.difficulty = difficulty
        self.date = date
        self.review = review

    def review_calc(self):
        return self.date + datetime.timedelta(days=(self.review)-1)