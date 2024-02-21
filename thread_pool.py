from threading import Thread
import time
from priority_queue import Message

class UserInputThread(Thread):
    def __init__(self, process_thread):
        super().__init__()
        self.process_thread = process_thread
        self.running = True  # Flag to control the loop

    def run(self):
        while self.running:
            choice = input("1. Add Message\n2. Peek\n3. Stop\nEnter a choice number: ")
            if choice == "1":
                priority = input("Enter priority (0 for high/1 for low): ")
                if priority not in ["0", "1"]:
                    print("Please enter either 0 or 1 to mention priority.")
                    continue
                content = input("Enter message content: ")
                if not content:
                    print("Message cannot be empty.")
                    continue
                message = Message(content=content, priority=int(priority))
                self.process_thread.enqueue(message)
                time.sleep(0.1)  # Adjust delay as needed
            elif choice == "2":
                msg_id = input("Enter the message id:")
                message_details = self.process_thread.peek(msg_id)
                if message_details.get("message") != "Queue is empty":
                    print(f"Message details:")
                    print(f"- ID: {message_details['id']}")
                    print(f"- Content: {message_details['content']}")
                    print(f"- Priority: {message_details['priority']}")
                    print(f"- Total messages: {message_details['total_messages']}")
                else:
                    print("Queue is empty")
            elif choice == "3":
                self.running = False  # Set flag to stop the loop
                print("Exiting...")
            else:
                print("Invalid choice!!!")
