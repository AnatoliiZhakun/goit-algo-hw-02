import queue
import threading
import time
import random

# Створюємо чергу заявок
request_queue = queue.Queue()

# Лічильник для красивих номерів заявок
request_id = 100001
lock = threading.Lock()  # щоб уникнути конфлікту доступу до request_id

def generate_request():
    global request_id
    while True:
        # Генеруємо нову заявку
        with lock:
            new_request = f"Request  -  {request_id}"
            request_id += 1
        request_queue.put(new_request)
        print(f"Нова заявка додана: {new_request}")
        
        # Затримка випадкового часу 0.5–1.5 сек
        time.sleep(random.uniform(0.5, 1.5))

def process_request():
    while True:
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Обробляється заявка: {request}")
        else:
            print("Черга пуста, немає заявок для обробки.")
        # Обробляємо заявки кожну секунду
        time.sleep(1)

def main():
    # Створюємо потоки для генерації та обробки заявок
    generator_thread = threading.Thread(target=generate_request, daemon=True)
    processor_thread = threading.Thread(target=process_request, daemon=True)
    
    generator_thread.start()
    processor_thread.start()
    
    try:
        while True:
            time.sleep(0.1)  # головний потік просто чекає
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")

if __name__ == "__main__":
    main()
