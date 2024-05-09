import threading
counter = 0
counter_lock = threading.Lock()

def increment():
    global counter
    with counter_lock:
        counter += 1

threads = []
for _ in range(10):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Counter: {counter}")