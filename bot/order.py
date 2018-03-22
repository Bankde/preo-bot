# @Description : Structures for keeping orders from users.

import pandas as pd
import numpy as np


class OrderPool:
    "Order pool maps order bags with group id."

    def __init__(self):
        self.order_bag_dict = {}

    def new_bag(self, bag_id):
        self.order_bag_dict[bag_id] = OrderBag(bag_id)


class OrderBag:
    """
    Order bag for each chat room.
    Implemented by DataFrame.
    """

    DATA_HEADER = ['user_id', 'item_name', 'amount']
    DTYPE= {
        'user_id' : 'object',
        'item_name': 'object',
        'amount' : 'int8'
    }
    @classmethod
    def __init_data_frame(cls):
        df = pd.DataFrame(columns=cls.DATA_HEADER).astype(dtype=cls.DTYPE)
        return df

    def __init__(self, bag_id):
        self.id = bag_id
        self.df = self.__init_data_frame()

    def set_order(self, user_id, item_name, amount):
        df = self.df
        prev_order = df.loc[(df['user_id'] == user_id) & (df['item_name'] == item_name)]
        if len(prev_order) == 0:
            # new order
            order = [user_id, item_name, amount]
            # TODO(M) : Add order to df
        else:
            # old order exists. Then, old order should be updated.
            prev_order['amount'] = amount

    def del_order(self, user_id, item_name):
        # TODO:
        # 1. remove order if any
        pass

    def list_order(self):
        print(self.df)
