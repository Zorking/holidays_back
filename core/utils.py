from holidays_back.settings import DATE_PRICE, DATE_ALERT


class RegistrationMessage:
    def __init__(self, giver):
        self.giver = giver

    def __str__(self):
        return (f"{self.giver}, ты успешно зарегистрировался в игру. {DATE_PRICE} будет день вручения подарков."
                f" {DATE_ALERT} мы вышлем тебе на почту имя одариваемого человека")


class AnnouncementMessage(RegistrationMessage):
    def __init__(self, recipient, theme,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme = theme
        self.recipient = recipient

    def __str__(self):
        return (f"Привет, {self.giver}.\nНапоминаем, что {DATE_PRICE}, в рамках нашей игры, "
                f"Вам нужно вручить приятный подарок представителю нашего славного коллектива.\n"
                f"Тема подарка: {self.theme}\n"
                f"Твой счастливчик: {self.recipient}.\n")
