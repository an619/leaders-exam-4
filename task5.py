def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower()) # აიღებს ორივე სიტყვას, დაუპატარავებს ასოებს(რომ არ იყოს ქეის სენსიტიური) და დაალაგებს ერთი და იგივე თამნიმდევრობით, და თუ ეს ორი სიტყვა დალაგებული ერთმანეთის ტოლი იქნება, ანუ ანაგრაამაა და დავბრინებს true, სხვა შემთხევაში false)

print(are_anagrams("listen", "silent"))

print(are_anagrams("hello", "world"))

print(are_anagrams("triangle", "integral"))