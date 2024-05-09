import threading

semaphore = threading.Semaphore(3)

resource = []

def access_resource():
    with semaphore:
        resource.append(threading.current_thread().name)

threads = []
for i in range(10):
    thread = threading.Thread(target=access_resource, name=f"Thread {i + 1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print("Resource:", resource)
