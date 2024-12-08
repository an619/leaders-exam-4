def find_missing_number(nums):  
    # გადავუვლით თითოეულ რიცხვს 2-დან nums-ის უდიდესი რიცხვის ჩათვლით და თუ რიცხვი არ არის nums სიაში, ეს რიცხვი დაბრუნდება. თუ არც ერთი რიცხვი არ აკლია სიას, მაგ შემთხევაში დაბრუნდება ცარიელი ლისტი
    for num in range(2, max(nums) + 1):
            if num not in nums:
                  return num
    return []

print(find_missing_number([1, 2, 4, 5]))
print(find_missing_number([3, 5, 6, 1, 2]))
print(find_missing_number([2]))