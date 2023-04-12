import requests
import time
import threading


def get_html(thread_name, url):
    r = requests.get(url)
    print(f"Поток {thread_name} завершил скачивание страницы со статусом {r.status_code}")
    pass


if __name__ == "__main__":
    start = time.time()
    dic_link = {"link1": "https://mephi.ru/structure/academic_council",
                "link2": "https://mephi.ru/international/relations",
                "link3": "https://scif.mephi.ru/",
                "link4": "https://mephi.ru/content/contacts",
                "link5": "https://mephi.ru/obrdeyat/obrazovatelnye-programmy/dpo"
                }

    thread = list()
    for link_name, link_url in dic_link.items():
        th = threading.Thread(target=get_html, args=("th-"+link_name, link_url, ))
        thread.append(th)
        th.start()

    for th in thread:
        th.join()

    end = time.time() - start
    print(f"Время выполнения паралельного кода, с {end}")

    # последовательный вызов
    start = time.time()

    thread = list()
    for link_name, link_url in dic_link.items():
        th = threading.Thread(target=get_html, args=("th-" + link_name, link_url,))
        thread.append(th)
        th.start()
        th.join()

    end = time.time() - start
    print(f"Время выполнения последовательного кода, с {end}")