import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
# Include paths for module search
sys.path.insert(0, os.path.join(parentdir, 'bot'))
from order import (
    OrderPool, OrderBag
)

###########################
# OrderPool test cases
###########################


def test_order_pool_init():
    order_pool = OrderPool()
    assert order_pool != None
    assert isinstance(order_pool, OrderPool)

###########################
# OrderBag test cases
###########################


def test_order_bag_init():
    bag_id = 'mock_id'
    order_bag = OrderBag(bag_id)
    assert order_bag != None
    assert isinstance(order_bag, OrderBag)
    assert order_bag.id == bag_id
    assert len(order_bag.df) == 0
