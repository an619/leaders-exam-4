import math
def sum_of_positives(lst):
    # გადავუვლით თითოეულ რიცხვს სიაში და თუ რიცხვი არის ნულზე მეტი, ის დაემატება ახალ სიაში დაბლითა რიცხვისკენ დამრგვალებული. საბოლოოდ ჯამს გამოვითვლით sum ფუნქციით და დავაბრუნებთ.
    return sum([math.floor(num) for num in lst if num > 0])

print(sum_of_positives([1, -4, 7, 12]))
print(sum_of_positives([-1.5, 2.7, -3.3, 4.8]))
print(sum_of_positives([]))
print(sum_of_positives(([-1, -2, -3])))