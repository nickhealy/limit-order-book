from __future__ import annotations
from attrs import define
from typing import Dict

from limit import Limit, Order

# maybe there is a way to have a Limit extend a basic node class, as well


@define
class Book:
    nextId: int = 0
    limits: Dict[int, Limit] = {}
    buyTree: Limit = None

    def addBuy(self, price, qty):
        # get limit, adding if doesn't exist
        if price not in self.limits:
            newLimit = Limit(limitPrice=price)
            if not self.buyTree:
                self.buyTree = newLimit
            else:
                # traverse BT to get where to put this
                currLimit = prevLimit = self.buyTree
                while currLimit:
                    prevLimit = currLimit
                    if price < currLimit.limitPrice:
                        currLimit = currLimit.leftChild
                    else:
                        currLimit = currLimit.rightChild

                if price < prevLimit.limitPrice:
                    prevLimit.leftChild = newLimit
                else:
                    prevLimit.rightChild = newLimit

            # add to dictionary
            self.limits[price] = newLimit

        limit = self.limits[price]

        id = self.nextId
        self.nextId += 1
        order = Order(id, qty)

        limit.addNewOrder(order)




if __name__ == '__main__':
    bk = Book()
    bk.addBuy(10, 100)
    bk.addBuy(10, 50)
    bk.addBuy(5, 5)
    bk.addBuy(5, 500)
    print(bk.buyTree)
