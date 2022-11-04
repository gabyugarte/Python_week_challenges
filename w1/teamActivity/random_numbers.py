import random
def main():
    
    numbers = [16.2, 75.1, 52.3]
    print(f'numbers{numbers}')
    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")
    words = ['Hello', 'World', 'laugh', 'smile', 'love']
    append_random_words(words)
    print(f"words {words}")
    append_random_words(words, 4)
    print(f"words {words}")
    
    
def append_random_numbers(numbers_list, quantity = 1):
    for _ in range(quantity):
        random_number = random.uniform(0,100)
        rounded = round(random_number,1)
        numbers_list.append(rounded)
def append_random_words(words_list, quantity = 1):
    mood = ['Happy', 'Beautiful', 'friendship', 'brothers', 'sisters']
    for _ in range(quantity):
        random_word = random.choice(mood)
        words_list.append(random_word)
            
if __name__ == "__main__":
    main()