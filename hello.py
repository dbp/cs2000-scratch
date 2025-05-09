import numpy as np

# Define a literal table: each row is a student, columns are scores in Math, Physics, Chemistry
scores = np.array([
    [85, 92, 78],
    [90, 88, 91],
    [76, 95, 85],
    [88, 82, 89]
])

# 1. Sum of scores for each student (sum across columns → axis=1)
student_totals = scores.sum(axis=1)
# 2. Average score in each subject (mean down rows → axis=0)
subject_means = scores.mean(axis=0)
# 3. Overall class average
class_average = scores.mean()

print("Scores table:\n", scores)
print("\nTotal per student:", student_totals)
print("Average per subject:", subject_means)
print("Overall class average:", class_average)