import queue
import random
import time

application_queue = queue.Queue()


def generate_request():
    request_id = random.randint(1, 1000)
    print(f"Створено заявку: {request_id}")
    application_queue.put(request_id)


def process_request():
    if not application_queue.empty():
        request_id = application_queue.get()
        print(f"Обробка заявки: {request_id}")
    else:
        print("Черга порожня")

try:
    while True:
        generate_request()
        process_request()
        time.sleep(1)

except KeyboardInterrupt:
    print("Вихід з програми.") 
