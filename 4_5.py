class Deck_Card:
    def __init__(self):
        self.num = 0
        self.suits = ['Червей', 'Пик', 'Бубен', 'Треф']
        self.card = ['2-ка', '3-ка', '4-ка', '5-ка', '6-ка', '7-ка', '8-ка', '9-ка', '10-ка', 'Валет', 'Дама', 'Король', 'Туз']

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= 52:
            raise StopIteration
        suit = self.suits[self.num // len(self.card)]
        card = self.card[self.num % len(self.card)]
        self.num += 1
        return f"{card} {suit}"


deck = Deck_Card()

try:
    while True:
        print(next(deck))
except StopIteration:
    pass