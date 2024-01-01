import classes
import os
import json

user_inp = int(input("Press 1 to enter problem, press 2 to see problems to review"))

if user_inp == 1:
    lc_num = input("LC problem number: ")
    difficulty = input("Rate the difficulty of the problem (1-5): ")
    date = input("Date of completion (MM/DD/YYYY): ")
    review = input("Press 1 to review ASAP, press 2 to review in 1 day, press 3 to review in 2 days: ")

    prob = classes.Problem(lc_num, difficulty, date, review)
    # print(prob.data)

    # print(problem1.number, problem1.difficulty, problem1.date)

    if os.path.exists("./tracker.json"):
        # read, modify, write data --- not just append
        with open("tracker.json", 'r') as file:
            cur_data = json.load(file)
        
        new_data = {
                "number":lc_num, "difficulty":difficulty, "date_completed":date, "review":review
                }
        
        cur_data["problems"].append(new_data)

        with open("tracker.json", "w") as file:

            #file.write(f"\n{prob.number}: {prob.difficulty}, {prob.date}, {prob.review}")
            json.dump(cur_data, file)
    else:
        data = {
            "problems" : [
                {
                "number":lc_num, "difficulty":difficulty, "date_completed":date, "review":review
                }
            ]
        }
        with open("tracker.json", "w") as file:
            #file.write(f"{prob.number}: {prob.difficulty}, {prob.date}, {prob.review}")
            json.dump(data, file)
    

elif user_inp == 2:
    # return every prob and when the review will spawn
    with open("tracker.txt", "r") as file:
        contents = file.read()
        print(contents[7])