import threading

buffer = []
buffer_size = 5
buffer_lock = threading.Lock()
buffer_not_full = threading.Condition(buffer_lock)
buffer_not_empty = threading.Condition(buffer_lock)

def produce_item(item):
    with buffer_not_full:
        while len(buffer) == buffer_size:
            buffer_not_full.wait()
        buffer.append(item)
        buffer_not_empty.notify()

def consume_item():
    with buffer_not_empty:
        while (len(buffer) == 0):
            buffer_not_empty.wait()
        item = buffer.pop()
        buffer_not_full.notify()
        return item
    
producer = threading.Thread(target=produce_item, args=("Item 1",))
consumer = threading.Thread(target=consume_item)
producer.start()
consumer.start()
producer.join()
consumer.join()