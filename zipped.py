# Enter your code here. Read input from STDIN. Print output to STDOUT
num_students, num_subjects = map(int, input().split())
scores_list = []

for _ in range(num_subjects):
    scores = list(map(float, input().split()))
    scores_list.append(scores)

zipped_scores = zip(*scores_list)

for subject_scores in zipped_scores:
    average_score = sum(subject_scores) / len(subject_scores)
    print(average_score)

