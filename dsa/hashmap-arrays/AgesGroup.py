ages = [12, 13, 45, 32, 34, 23, 45, 12, 34, 56, 23, 12, 11, 18, 19]
minors = 0
adults = 0

ages_group = {}

for age in ages:
    if age < 18:
        minors = minors + 1
    else:
        adults = minors + 1

    if age in ages_group:
        actual_count = ages_group.get(age) + 1
        ages_group.update({age: actual_count})
    else:
        ages_group.update({age: 1})

ages_group_list = []
for age_item in ages_group.keys():
    ages_group_list.append({age_item: ages_group.get(age_item)})

result = {
    'ages_group': list(ages_group_list),
    'minors': minors,
    'adults': adults
}
print(result)
