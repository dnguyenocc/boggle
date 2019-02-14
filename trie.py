class Node:
    def __init__(self, char=None):
        self.label = char
        self.children = []
        self.end = False

    def hasChild(self, chr):
      """Returns True if the node has a child matching character chr"""
      for child in self.children:
          if child.label == chr:
              return True
      return False

    def getChild(self, chr):
      """Returns a Node if the node has a child matching chr, returns None otherwise"""
      for child in self.children:
            if child.label == chr:
                return child
      return None

    def addChild(self, chr):
      """Creates a new Node as a child of this and sets its lookup to character chr"""
      self.children.append(Node(chr))

    def setEndOfWord(self):
      """Marks this node as representing the end of a word"""
      self.end = True

    def isEndOfWord(self):
      """Returns True if this node represents the end of a word, False otherwise"""
      return self.end


class Trie:
    def __init__(self, file_name=None):
        """
        >>> t = Trie('words_alpha.txt')
        >>> t.isPrefix('a')
        True
        >>> t.isPrefix('nlaskndla')
        False
        """
        self.root = Node()
        if file_name:
            file = open(file_name, "r")
            for line in file:
                self.addWord(line.rstrip())



    def getRoot(self):
        """Returns the root Node of this Trie"""
        return self.root

    def addWord(self, word):
        """Adds word to the Trie."""
        curr_node = self.getRoot()
        for chr in word:
            if not curr_node.hasChild(chr):
                curr_node.addChild(chr)
            curr_node = curr_node.getChild(chr)
        curr_node.setEndOfWord()

    def getNode(self, str):
        curr_node = self.getRoot()
        for chr in str:
            curr_node = curr_node.getChild(chr)
            if not curr_node:
                return None
        return curr_node


    def isPrefix(self, str):
        return bool(self.getNode(str))

    def isWord(self, word):
        node = self.getNode(word)
        if not node:
            return False
        return node.isEndOfWord()
