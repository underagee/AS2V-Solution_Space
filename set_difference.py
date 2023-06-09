# Enter your code here. Read input from STDIN. Print output to STDOUT
english_num = int(input())
english_roll = input().split()

french = int(input())
french_roll = input().split()

total_student = set(english_roll).difference(french_roll)
print(len(total_student))
