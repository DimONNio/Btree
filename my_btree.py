class MyBTree(object):
    class Item(object):
        def __init__(self, data: int):
            self.left = None
            self.right = None
            self.data = data

    def __init__(self):
        self.root = None
        self.deep = 0
        self.height = 0
        self.deepX = 0
        self.heightX = 0
        print("root = None")

    '''def is_empty(self):
        print("return self.root is None")
        return self.root is None'''

    def insert(self, data):
        item = MyBTree.Item(data)
        print("item = MyBTree.Item(data)", data)
        if not self.root:
            self.root = item
            self.deep = 1
            self.height = 1
            print("self.root = item", data, self.deep, self.height)
        else:
            current_item = self.root
            # self.deep = 1
            print("current_item = self.root", data, self.deep, self.height)
            while True:
                if current_item.data <= item.data:
                    if current_item.right is None:
                        current_item.right = item
                        self.deep += 1
                        self.height = max(self.height, self.deep)
                        print("current_item.right = item", data, self.deep, self.height)
                        return
                    else:
                        current_item = current_item.right
                        self.deep += 1
                        self.height = max(self.height, self.deep)
                        print("current_item = current_item.right", data, self.deep, self.height)
                else:
                    if current_item.left is None:
                        current_item.left = item
                        self.deep += 1
                        self.height = max(self.height, self.deep)
                        print("current_item.left = item", data, self.deep, self.height)
                        return
                    else:
                        current_item = current_item.left
                        self.deep += 1
                        self.height = max(self.height, self.deep)
                        print("current_item = current_item.left", data, self.deep, self.height)

    def _print_subtree(self, sub_item: Item):
        """ Comment """
        # dive-calculator
        self.deepX += 1
        # 1. Check self.left
        if sub_item.left:
            self._print_subtree(sub_item.left)
        # 2. Print self.data
        print('Елемент: ', sub_item.data, 'Глибина елементу: ', self.deepX)
        # 3. Check self.right
        if sub_item.right:
            self._print_subtree(sub_item.right)
        self.heightX = max(self.heightX, self.deepX)
        self.deepX -= 1


    def print(self):
        self._print_subtree(self.root)
        print('Висота дерева = ', self.heightX)
