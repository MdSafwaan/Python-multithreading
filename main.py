from priority_queue import ProcessThread
from thread_pool import UserInputThread
from concurrent.futures import ThreadPoolExecutor

def main():
    process_thread = ProcessThread()
    user_thread = UserInputThread(process_thread)

    # Create a ThreadPoolExecutor to run both threads
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(process_thread.run)
        executor.submit(user_thread.run)

if __name__ == "__main__":
    main()
