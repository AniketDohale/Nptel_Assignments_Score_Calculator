def sort_Score_List():
    for i in range(len(score_List)):
        for j in range(i+1, len(score_List)):
            if score_List[i] <= score_List[j]:
                score_List[i], score_List[j] = score_List[j], score_List[i]


best_Assignments = int(input("Enter Number of Best Assignments -> "))

score, sum = 0, 0

file = open('score.txt', 'r')

list = ['Week', 'Assignment', ':']

score_List = []

for line in file:
    for word in line.split():
        if word not in list and len(word) > 3:
            score_List.append(float(word))

sort_Score_List()

for i in range(best_Assignments):
    sum = sum + score_List[i]

score = (sum/best_Assignments)*25/100

print("Score ->", score)
