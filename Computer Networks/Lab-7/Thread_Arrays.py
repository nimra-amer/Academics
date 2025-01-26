import threading

# Define a class to hold thread information
class ThreadStruct:
    def __init__(self, t_msg, tid):
        self.t_msg = t_msg
        self.tid = tid

# Define the function that each thread will run
def print_thread_info(thread_struct):
    print(thread_struct.t_msg, end="")
    print(thread_struct.tid)

def main():
    threads = []
    thread_data = []

    # Populating the thread data with messages and IDs
    for i in range(10):
        thread_data.append(ThreadStruct("Hi I am thread ", i + 1))

    # Creating and starting threads
    for i in range(10):
        thread = threading.Thread(target=print_thread_info, args=(thread_data[i],))
        threads.append(thread)
        thread.start()
        thread.join()  # Wait for each thread to finish before creating the next one

if __name__ == "__main__":
    main()
