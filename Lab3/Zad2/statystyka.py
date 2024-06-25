class TextStatistics:
    def __init__(self, text):
        self.text = text

    def calculate(self):
        pass

class BaseDecorator(TextStatistics):
    def __init__(self, wrapped):
        self._wrapped = wrapped
        super().__init__(wrapped.text)

    def calculate(self):
        self._wrapped.calculate()

class CountLetterA(BaseDecorator):
    def calculate(self):
        super().calculate()
        count = self.text.count('a')
        print(f"Liczba liter 'a': {count}")

class ContainsAla(BaseDecorator):
    def calculate(self):
        super().calculate()
        contains_ala = 'ala' in self.text
        print(f"Czy zawiera słowo 'ala': {contains_ala}")

class CountWords(BaseDecorator):
    def calculate(self):
        super().calculate()
        word_count = len(self.text.split())
        print(f"Liczba słów: {word_count}")

# Użycie
text2 = TextStatistics("ala ma kota i psa")
statistics = CountLetterA(ContainsAla(CountWords(text2)))
statistics.calculate()
