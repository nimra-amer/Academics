import threading

def print_thread_id(message):
    print(message)

def main():
    # Messages to pass to threads
    message1 = "Thread 1"
    message2 = "Thread 2"

    # Creating and starting threads
    thread1 = threading.Thread(target=print_thread_id, args=(message1,))
    thread1.start()
    thread1.join()  # Wait for thread1 to finish before starting thread2

    thread2 = threading.Thread(target=print_thread_id, args=(message2,))
    thread2.start()
    thread2.join()  # Wait for thread2 to finish before ending the main thread

if __name__ == "__main__":
    main()
