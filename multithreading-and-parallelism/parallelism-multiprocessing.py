import multiprocessing
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(5)
    print(f"Task {name} completed")

processes = []
for i in range(5):
    process = multiprocessing.Process(target=task, args=(i,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

print("All tasks completed")