import threading
import time


def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)
    pass


if __name__ == "__main__":

    start = time.time()

    thread = list()
    for i in range(5):
        th = threading.Thread(target=get_thread, args=("th-" + str(i),))
        thread.append(th)
        th.start()

    for th in thread:
        th.join()

    end = time.time() - start

    print(f"Время выполнения, с {end}")
