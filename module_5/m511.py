class StringVar:
    # Тут храним строку
    val = ""
    def __init__(self, s=""):
        self.val = s

    # Установить значение
    def set(self, s):
        self.val = s

    # Получить значение
    def get(self):
        return self.val


myString = StringVar("123")
print(myString.get())

myString.set("321")
print(myString.get())
