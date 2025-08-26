from collections import deque

def is_palindrome(s):
    # Приводимо рядок до нижнього регістру і видаляємо пробіли та неалфавітні символи
    clean_s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Додаємо всі символи до двосторонньої черги
    char_deque = deque(clean_s)
    
    # Порівнюємо символи з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def main():
    print("Перевірка паліндрому. Введіть рядок (або 'exit' для виходу):")
    while True:
        user_input = input(">>> ")
        if user_input.lower() == "exit":
            print("Програма завершена.")
            break
        if is_palindrome(user_input):
            print("Це паліндром")
        else:
            print("Це не паліндром")

if __name__ == "__main__":
    main()
