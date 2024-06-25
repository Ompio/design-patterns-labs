class Translator:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def translate(self, text):
        return self.strategy.translate(text)

class EnglishTranslator:
    def translate(self, text):
        return "Translation to English: " + text

class GermanTranslator:
    def translate(self, text):
        return "Übersetzung ins Deutsche: " + text

# Użycie
translator = Translator(EnglishTranslator())
print(translator.translate("Ala ma kota"))

translator.set_strategy(GermanTranslator())
print(translator.translate("Ala ma kota"))
