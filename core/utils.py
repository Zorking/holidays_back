from holidays_back.settings import DATE_PRICE, DATE_ALERT


class RegistrationMessage:
    def __init__(self, giver, is_female):
        self.is_female = is_female
        self.giver = giver

    def __str__(self):
        return (f"{self.giver}, ты успешно зарегистрировался в игру. {DATE_PRICE} будет день вручения подарков."
                f" {DATE_ALERT} мы вышлем тебе на почту имя одариваемого человека"
                f"{' и категорию подарка.' if self.is_female else ', категорию подарка и твоих напарников.'}")


class AnnouncementMessage(RegistrationMessage):
    def __init__(self, recipient, theme, teammates=None,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.teammates = teammates
        self.theme = theme
        self.recipient = recipient

    def __str__(self):
        return (f"Привет, {self.giver}.\nНапоминаем, что {DATE_PRICE}, в рамках нашей игры, "
                f"Вам нужно вручить приятный подарок представителю нашего славного коллектива.\n"
                f"Тема подарка: {self.theme}\n"
                f"Тво{'и' if self.is_female else 'й'} счастливчик{'и' if self.is_female else ''}: {self.recipient}.\n"
                f"{f'Твои напарники: {self.teammates}.' if not self.is_female else ''}")


def chunk_it(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out
