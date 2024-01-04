import classes
import os
import json
from datetime import date

user_inp = int(input("Press 1 to enter problem, press 2 to see problems to review "))

if user_inp == 1:
    lc_num = input("LC problem number: ")
    difficulty = input("Rate the difficulty of the problem (1-5): ")
    date_completed = input("Date of completion (DD/MM/YYYY): ")
    review = int(input("Press 1 to review ASAP, press 2 to review in 1 day, press 3 to review in 2 days: "))

    date_completed = date_completed.split('/')

    prob = classes.Problem(lc_num, difficulty, date(int(date_completed[2]), int(date_completed[1]), int(date_completed[0])), review)

    review_date = str(prob.review_calc())

    if os.path.exists("./tracker.json"):
        with open("tracker.json", 'r') as file:
            cur_data = json.load(file)
        
        # Dates are not JSON serializable
        new_data = {
                "number":prob.number, "difficulty":prob.difficulty, "date_completed":date_completed, "review":prob.review, "review_date":review_date
                }
        
        cur_data["problems"].append(new_data)

        with open("tracker.json", "w") as file:
            json.dump(cur_data, file)
    else:
        data = {
            "problems" : [
                {
                "number":prob.number, "difficulty":prob.difficulty, "date_completed":date_completed, "review":prob.review, "review_date":review_date
                }
            ]
        }
        with open("tracker.json", "w") as file:
            #file.write(f"{prob.number}: {prob.difficulty}, {prob.date}, {prob.review}")
            json.dump(data, file)
    

elif user_inp == 2:
    # return every prob and when the review will spawn
    with open("tracker.json", "r") as file:
        contents = json.load(file)
        for i in range(len(contents["problems"])):
            date_input = contents['problems'][i]['review_date'].split('-')
            if date(int(date_input[0]), int(date_input[1]), int(date_input[2])) == date.today():
                print(f"Problem number {contents['problems'][i]['number']} is due today")
            else:
                print(f"Problem number {contents['problems'][i]['number']} is due on {contents['problems'][i]['review_date']}")
