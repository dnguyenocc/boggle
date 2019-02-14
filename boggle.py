import random
from trie import Trie, Node
class Boggle:
    trie = Trie('words_alpha.txt')
    def __init__(self, n, board=None):
        self.size = n
        if board:
            self.board = board
        else:
            self.board = []

    def addWord(self, word):
        if len(word) == self.size and len(self.board) < self.size:
            self.board.append(word)

    def search(self, trie, found, row, col, path=None, node=None, word=None):
        letter = self.board[row][col]
        if node is None or path is None or word is None:
            node = trie.getRoot().getChild(letter)
            path = [(row, col)]
            word = letter
        else:
            node = node.getChild(letter)
            path.append((row, col))
            word = word + letter
        if node is None:
            return
        elif node.isEndOfWord() and len(word) >= 3:
            found.add(word)

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (r >= 0 and r < self.size
                        and c >= 0 and c < self.size
                        and not (r == row and c == col)
                        and (r, c) not in path):
                    self.search(trie, found, r, c, path[:], node, word[:])

    def play(self, found):
        for r in range(0, self.size):
            for c in range(0, self.size):
                self.search(self.trie, found, r, c)

    def __repr__(self):
        return "Boggle(size={0}, board={1})".format(self.size, self.board)

def main():
    boggle = Boggle(3, ['cje', 'eao', 'ite'])
    found = set()
    print(boggle.trie.getNode('cat').end)
    boggle.play(found)
    print(found)
    for word in sorted(found):
        print(word)
    print(boggle)

if __name__ == '__main__':
    main()
