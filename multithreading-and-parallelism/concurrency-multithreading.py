import threading
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(5)
    print(f"Task {name} completed")

threads = []
for i in range(5):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All tasks completed")