import threading

# Global variable to keep track of thread IDs
tid = 1
tid_lock = threading.Lock()  # Lock for synchronized access to tid

def print_thread_id():
    global tid
    with tid_lock:
        print(f"This is Thread {tid}")
        tid += 1

def main():
    # Creating two threads
    thread1 = threading.Thread(target=print_thread_id)
    thread2 = threading.Thread(target=print_thread_id)

    # Starting the threads
    thread1.start()
    thread2.start()

    # Waiting for both threads to complete
    thread1.join()
    thread2.join()

# Calling the main function
if __name__ == "__main__":
    main()
