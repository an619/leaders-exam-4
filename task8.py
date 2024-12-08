def longest_consecutive(lst):
    result = [] # ცვლადი სადაც ჩავამატებთ თამიმდევრულ რიცხვებს
    for num in range(min(lst), max(lst) + 1): # გადავუვლით თითოეულ რიცხვს, ლისტის მინიმალური რიცხვიდან, მაქსიმალური რიხცვის ჩათვლით.
        if num not in lst: # შევამოწმებთ თანმიმდევორბით, თუ რიცხვი მოცემული დიაპაზონიდან არ იმყოფება lst სიაში(რაც ნიშნავ იმას რომ თამმიმდევლობა დაირღვა) მაშინ ლუპი შეჩერდება.
            break
        else:
            result.append(num) # სხვა შემთხვევაში რიცხვები დაემატებიან result სიაში
    return len(result) # საბოლოოდ დავაბრუნებთ თანმიმდევრული რიცხვების სიგრძეს

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
print(longest_consecutive([0, 0]))
print(longest_consecutive([9, 1, 4, 7, 3, 2, 8, 5, 6]))