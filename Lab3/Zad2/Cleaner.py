from abc import ABC, abstractmethod

class Cleaner(ABC):
    def clean(self, text):
        words = text.split()
        words = self._filter_words(words)
        return ' '.join(words)

    @abstractmethod
    def _filter_words(self, words):
        pass

class RemoveShortWords(Cleaner):
    def _filter_words(self, words):
        return [word for word in words if len(word) > 3]

class RemoveWordsStartingWithA(Cleaner):
    def _filter_words(self, words):
        return [word for word in words if not word.startswith('a')]

# Użycie
cleaner = RemoveShortWords()
print(cleaner.clean("ala ma kota i psa"))

cleaner = RemoveWordsStartingWithA()
print(cleaner.clean("ala ma kota i psa"))
