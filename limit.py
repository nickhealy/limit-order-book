from __future__ import annotations
from attrs import define, field
from typing import Optional


@define
class Order:
    id: int
    qty: int
    nextOrder: Order = None
    nextOrder: Order = None


@define
class Limit:
    limitPrice: int
    totalVolume: int = 0
    tailOrder: Order = None
    headOrder: Order = None
    leftChild: Limit = None
    rightChild: Limit = None

    def addNewOrder(self, order):
        if self.tailOrder:
            self.tailOrder.nextOrder = order
            self.tailOrder = self.tailOrder.nextOrder
        else:
            self.tailOrder = self.headOrder = order

        self.totalVolume += order.qty 


# doubly linked list for orders
if __name__ == '__main__':
    lim = Limit(0, 0, 0)
    o1 = Order(1, 10)
    o2 = Order(2, 20)
    lim.addNewOrder(o1)
    lim.addNewOrder(o2)
    print(lim)
