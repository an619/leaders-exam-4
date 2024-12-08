def find_intersection(lst1, lst2):
    # გადავუარეთ lst1 სიის თითოეულ რიცხვს და თუ რიცხვი არ არის მეორე ლისტში ან არ არის  diff = [] სიაში(ეს მეორე შემოწმება საჭიროა იმისთვის, რომ არ გვქონდეს დუბლიკატები სიაში), მაგ შემთხვევაში დაემატება  diff = [] სიას. საბოლოოდ კი ვაბრუნებთ ამ განხვავებული რიცხვების სიას.
    diff = []
    for num in lst1:
        if num in lst2 and num not in diff:
            diff.append(num)
    return diff


print(find_intersection([1, 2, 3], [2, 3, 4]))
print(find_intersection([1, 1, 2], [1, 3]))
print(find_intersection([], [1, 2]))