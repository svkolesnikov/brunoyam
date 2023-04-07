import json


class Model:
    count = 0

    def __init__(self):
        self.title = ''
        self.text = ''
        self.author = ''

    def save(self, fname="model"):
        Model.count += 1
        ls = list(filter(lambda x: not x.startswith('_'), dir(self)))
        ls_atr = {}
        for val in ls:
            if val == 'save':
                continue
            else:
                ls_atr[val] = getattr(self, val)

        with open(fname + '.json', 'w') as f:
            json.dump(ls_atr, f)


if __name__ == '__main__':
    C1 = Model()
    C1.text = "Умный текст"
    C1.title = "Умная книга"
    C1.author = "Какой то автор"
    C1.sub_title = "Подзаголовок"

    C2 = Model()
    C2.text = "Умный текст2"
    C2.title = "Умная книга2"
    C2.author = "Какой то автор2"
    C2.sub_title = "Подзаголовок2"

    C1.save('c1')
    C2.save('c2')
