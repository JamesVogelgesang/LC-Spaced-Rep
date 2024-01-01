class Problem:
    """A simple class"""
    def __init__(self, number, difficulty, date, review):
        self.data = {"number":number, "difficulty":difficulty, "date_completed":date, "review":review}
        self.number = number
        self.difficulty = difficulty
        self.date = date
        self.review = review


def date_parse(date):
    date_specifics = date.split('/')
    month = date_specifics[0]
    day = date_specifics[1]
    year = date_specifics[2]
    return month, day, year


# prob = problem(12, 3, "1/1/2024", "ASAP")

# print(date_parse(prob.date))