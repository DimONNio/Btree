import random

from my_btree import MyBTree as BTree


def fill_tree(btree: BTree):
    for i in range(7):
        data = random.randint(1, 101)
        print(data)
        btree.insert(data)
        print(data)


def main():
    the_tree = BTree()
    print('Fill tree')
    fill_tree(the_tree)
    print('Tree height')
    the_tree.print()


if __name__ == '__main__':
    main()
