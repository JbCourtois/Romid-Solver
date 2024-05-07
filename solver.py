from bisect import bisect_left, insort
import json


class Solver:
    def start_game(self):
        """Get word length and init."""
        self.has_mod = False

        while True:
            try:
                self.len = int(input('Word length?\n').strip())
            except ValueError:
                continue
            if not 4 <= self.len <= 10:
                continue
            break

        try:
            with open(f'Mots/{self.len}.json') as file:
                self.wlist = json.load(file)
        except FileNotFoundError:
            with open(f'Mots/{self.len}-full.json') as file:
                self.wlist = json.load(file)
            self.has_mod = True

    def try_word(self, lo=0, hi=None):
        if hi is None:
            hi = len(self.wlist)

        index = (lo + hi) // 2
        word = self.wlist[index]
        res = input(word + '\n')

        if res == 'o':
            return
        if res == 'x':
            self.has_mod = True
            self.wlist.pop(index)
            return self.try_word(lo=lo, hi=hi - 1)
        if res == '+':
            return self.try_word(lo=index, hi=hi)
        if res == '-':
            return self.try_word(lo=lo, hi=index)

    def end_game(self):
        if not self.has_mod:
            return

        with open(f'Mots/{self.len}.json', 'w') as file:
            json.dump(self.wlist, file)

    def run(self):
        self.start_game()
        self.try_word()
        self.end_game()


if __name__ == '__main__':
    solver = Solver()
    solver.run()
