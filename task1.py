def sum_of_positives(lst):
    # გადავუარეთ თითოეულ რიცხვს სიაში და თუ რიცხვი არის ნულზე მეტი, დაემატება ახალ სიაში. საბოლოოდ ახალი სიის ჯამს გამოვითვლით sum() ფუნქციით და დავაბრუნებთ
    return sum([num for num in lst if num > 0])

print(sum_of_positives([-1, -2, -3, -4]))
print(sum_of_positives([1, -4, 7, 12]))
print(sum_of_positives([]))
