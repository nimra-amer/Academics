import threading

# Define a class to hold thread information
class ThreadStruct:
    def __init__(self, t_msg, tid):
        self.t_msg = t_msg
        self.tid = tid

# Define the function that the thread will run
def thread_struct_manipulation(t_mani):
    t_mani.t_msg += ". Hi I am manipulated Thread"
    t_mani.tid += 1
    return t_mani

def main():
    # Create a structure instance and populate it with initial data
    t_str = ThreadStruct("Hi I am Thread", 2)
    print(f"Before: {t_str.t_msg} {t_str.tid}")

    # Define a list to store the result
    result = []

    # Define a wrapper function to capture return data from thread
    def wrapper(result):
        manipulated_data = thread_struct_manipulation(t_str)
        result.append(manipulated_data)

    # Create and start the thread
    thread = threading.Thread(target=wrapper, args=(result,))
    thread.start()
    thread.join()  # Wait for the thread to complete

    # Access the modified data
    t_mani = result[0]
    print(f"After: {t_mani.t_msg} {t_mani.tid}")

if __name__ == "__main__":
    main()
