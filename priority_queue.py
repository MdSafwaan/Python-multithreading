from queue import PriorityQueue
from threading import Condition, Lock
from dataclasses import dataclass, field
from uuid import uuid4
import time
from threading import Condition, Lock, Thread

@dataclass
class Message:
    content: str
    priority: int
    id: str = field(default_factory=uuid4)

class ProcessThread(Thread):
    def __init__(self):
        super().__init__()
        self.process_delay = 15  # Reduced for demonstration
        self.queue = PriorityQueue(maxsize=5)
        self.condition = Condition()
        self.lock = Lock()  # Add a lock

    def run(self):
        print("-----------------------------\n| Message Processor Started |\n-----------------------------")
        while True:
            with self.condition:
                self.condition.wait(0.5)
            if not self.queue.empty():
                self.process_message()

    def enqueue(self, message):
        with self.lock:
            with self.condition:
                print(f"Message has been added to the queue with id {message.id}")
                self.queue.put((message.priority, message))
                self.condition.notify()

    def process_message(self):
        time.sleep(self.process_delay)
        _, message = self.queue.get()
        print(f"Processed message with id: {message.id}")
        self.condition.notify()

    def peek(self, id):
        print(self.queue.queue)
        with self.lock:
            with self.condition:
                if self.queue.empty():
                    return {"message": "Queue is empty"}
                for pos, msg in enumerate(self.queue.queue):
                    if msg.id == id:
                        return {
                            "id": msg.id,
                            "content": msg.content,
                            "priority": msg.priority,
                            "total_messages_in_queue": self.queue.qsize()
                        }
