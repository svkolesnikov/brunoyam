import requests
import datetime
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        """
        Инициализация объекта.
        page - объект BeautifulSoup для хранения полученного контента
        dates - список для хранения пропарсенных дат
        value - список для хнанения пропарсенных значений
        """
        self.page = None
        self.dates = []
        self.values = []

    def get_page(self, url):
        """
        Функция скачивает страницу, если скачать страницу не удается в page хранится статус
        :param url: адрес страницы которую надо скачаmь
        :return:
        """
        try:
            self.page = requests.get(url)
        except:
            print(f'Не удалось скачать страницу')

    def parse(self):
        """
        Если в response есть объект и статус его 200, то осуществляется парсинг странцы и заполняется
        |словарь (дата : значение)
        :return:
        """
        try:
            if (self.page is not None) & (self.page.status_code == 200):
                # парсим страницу
                soup = BeautifulSoup(self.page.text, "html.parser")
                page = soup.findAll('table', class_='mfd-currency-table')
                tag_dates = page[0].select("tr > td:nth-child(1)")
                tag_values = page[0].select("tr > td:nth-child(2)")

                self.dates.clear()
                for value in tag_dates:
                    self.dates.append(datetime.datetime.strptime(value.text, 'с %d.%m.%Y'))

                self.values.clear()
                for value in tag_values:
                    self.values.append(float(value.text))

            else:
                print(f'Запрос пустой или вернулся с ошибкой')
        except:
            print(f'Критическая ошибка при парсинге')

    def plot(self):
        """
        Строится график заполненому словарю, если данных нет, то выводится сообщение что данных
        для построения графика нет
        :return:
        """
        if (len(self.dates) == len(self.values)) & (len(self.values) > 0):
            plt.figure(figsize=[10, 5])
            plt.plot(self.dates, self.values)
            plt.title('График курса а валют')
            plt.xlabel('Дата')
            plt.ylabel('Курс валюты')
            plt.grid(True)
            plt.show()
        else:
            print("Не могу построить график, данных нет или неверно спарсились")


if __name__ == "__main__":
    parser = Parser()
    parser.get_page("https://mfd.ru/currency/?currency=USD")
    parser.parse()
    parser.plot()
