class BoardItem:
    def __init__(self, desc, top_left, top_right, bottom_right, bottom_left):
        self.desc = desc
        self.coords = [top_left, top_right, bottom_right, bottom_left]


R0H0 = {'R1': BoardItem('Regulates power', (10, 10), (15, 10), (15, 5), (10, 5)),
        'R2': BoardItem('Regulates power', (100, 100), (150, 100), (150, 50), (100, 50))}
