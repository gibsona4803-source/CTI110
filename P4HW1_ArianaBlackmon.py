# Ariana Blackmon
# July 1, 2026
# P4HW1_ArianaBlackmon
# A program that collects a user-defined number of scores...

"""
PSEUDOCODE / ALGORITHM:
1. Initialize an empty list named 'score_list' to hold valid scores.
2. Prompt the user to enter the total number of scores they wish to input.
3. Start a FOR loop that iterates 'num_scores' times to collect each score.
4. Inside the loop, prompt the user to input a score.
5. Create a WHILE loop to validate the score:
   - If the score is less than 0 OR greater than 100:
     - Display an error message stating it is an invalid score.
     - Prompt the user to enter a VALID score again.
   - If the score is valid, exit the while loop.
6. Append the valid score to 'score_list'.
7. After the loop finishes, find the lowest score using min() and store it.
8. Create a copy or modify the list by removing the lowest score using .remove().
9. Calculate the average of the modified list: sum(modified_list) / len(modified_list).
10. Use an IF-ELIF-ELSE structure to determine the letter grade based on the average:
    - 90 and above = 'A'
    - 80 to 89.9   = 'B'
    - 70 to 79.9   = 'C'
    - 60 to 69.9   = 'D'
    - Below 60     = 'F'
11. Display the results clearly: Lowest Score, Modified List, Average, and Grade.
"""

# 1. Initialize empty list
score_list = []

# 2. Get total number of scores
num_scores = int(input("How many scores do you want to enter? "))
print() # Prints an empty line for clean spacing

# 3. Loop to collect scores
for i in range(num_scores):
    score = float(input(f"Enter score #{i + 1}: "))
    
    # 5. Validation loop (Ensures score is between 0 and 100)
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100.")
        score = float(input(f"Enter score #{i + 1} again: "))
    
    # 6. Append valid score to our list
    score_list.append(score)

# --- Processing Results ---
print("\n" + "-" * 12 + "Results" + "-" * 12)

# 7. Find lowest score
lowest_score = min(score_list)
print(f"Lowest Score  : {lowest_score}")

# 8. Drop the lowest score
modified_list = score_list.copy()
modified_list.remove(lowest_score)
print(f"Modified List : {modified_list}")

# 9. Calculate the average
average = sum(modified_list) / len(modified_list)
print(f"Scores Average: {average:.2f}")

# 10. Determine the letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# 11. Display grade
print(f"Grade         : {grade}")
print("-" * 31)
