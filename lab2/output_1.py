def calculate_score(personal_info, scores):
    name, age, gender, height, weight = personal_info
    total_score = sum(scores)
    is_adult = age >= 18


    results = {
               "Name": name,
               "Age": age,
               "Gender": gender,
               "Height": height,
               "Weight": weight,
               "Total Score": total_score,
               "Adult": is_adult
               }
    return results

# Приклад виклику функції
personal_info = ("John", 25, "Male", 175, 70)
scores = [85, 90, 75, 88, 92]
print(calculate_score(personal_info, scores))
