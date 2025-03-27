student_scores = {
    'Alex': 88,
    'Ben': 75,
    'Cyrus': 93,
    'Denver': 85
}
sorted_by_values = dict(sorted(student_scores.items(), key=lambda item: item[1]))