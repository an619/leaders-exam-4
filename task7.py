from itertools import combinations # გადმოვიტანე ombinations ბიბლიოთეკა, რომლითაც შემეძლება ლისტში ყველა ელემენტის კომბინაციის გაგება
def three_sum(lst):
    result = [] # ცარიელი სია, იმ რიცხვების კომბინაციებისთვის, რომელთა შეკრებითაც მივიღებთ 0-ს
    combs = list(combinations(lst, 3)) # გავიგეთ ყველა შესაძლო 3 ელემენტის კომბინაცია lst სიაში
    for comb in combs: # გადავუარეთ ამ კომბინაციების სიას
        if sum(comb) == 0 and sorted(list(comb)) not in result:# თუ კომბინაციის ჯამი უდრის 0-ს და ასევე მოცემული კომბინაცია არ გვაქ  result სიაში, მაგ შემთხევაში დავამატებთ result სიაში(დასორტირება საჭიროა იმისთვის, რომ შემოწმება მოხდეს არა თანმიმდევრობის, არამედ შიგთავსის მიხედვით)
            result.append(sorted(list(comb)))
    return result # ვაბრუნებთ საბოლოო კომბინაციების სიას
        
print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 0, 0]))
print(three_sum([1, 2, -2, -1]))