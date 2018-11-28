scores = [
            {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
            {'school_class': '4b', 'scores': [3, 5, 5, 5, 3]},
            {'school_class': '5b', 'scores': [4, 5, 4, 5, 3]},
            {'school_class': '6b', 'scores': [5, 5, 4, 5, 4]}
        ]

sum_score = 0
for sc in scores:
    aver_score_class = sum(sc['scores'])/len(sc['scores'])
    print(f"Класс {sc['school_class']}: средний бал: {aver_score_class}")
    sum_score += aver_score_class

print(f"Средний бал по всей школе: {sum_score/len(scores)}")
