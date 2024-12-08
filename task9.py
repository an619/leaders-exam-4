def non_prime_numbers(start, end):
    # ფუნქცია იმის გასაგებად, არის თუ არა რიცხვი მარტივი(თუ მარტივია გვიბრუნდება true, სხვა შემთხევაში false)
    def is_prime(num):
            gamyofebi = [] # აქ შეინახება რიცხვის გამყოფები
            for i in range(1, num + 1): # გადავუვლით თითოეულ რიცხვს 1-დან num-ის ჩათვლით და შევამოწმებთ იყოფა თუ არა num რიცხვი ამ თითოეულ რიცხვზე 
                if num % i == 0:
                    gamyofebi.append(num) # თუ იყოფა ვამატებთ სიაში
            return len(gamyofebi) == 2  # საბოლოოდ ვამოწმებთ არის თუ არა გამყოფების რაოდენობა ზუსტად 2-ის ტოლი. 
    result = [] # სია სადაც დავამატებთ ყველა არამარტვი რიცხვს
    for num in range(start, end + 1): # გადავუვლით თითოეულ რიცხვს start-იდან end-ის ჩათვლით
        if not is_prime(num): # გადავამოწმებთ არიან თუ არა მოცემული რიხვები არამარტივები
            result.append(num) # თუ შეგვხდება არამარტივი რიცხვი, ის დაემატება result სიაში
    return result # საბოლოოდ დავაბრუნებთ სიას, რომელიც შედგება არამარტივი რიხვებისგან

print(non_prime_numbers(10, 20))
print(non_prime_numbers(1, 10))
print(non_prime_numbers(20, 30))
print(non_prime_numbers(24, 25))
print(non_prime_numbers(1, 1))