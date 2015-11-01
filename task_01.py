#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Combining Two datasets """


def sum_orders(customers, orders):
    """This function combines two datasets from data module.

    Args:
        customers(dict): dictionary of customer id (key) and value information.
        orders(dict): dictionary of order id as key and id and total as values.

    Returns:
        a dictionary of customer id as their key and name, email, orders and
        total as values.

    Examples:
        >>>import data
        >>> sum_orders(customers=data.CUSTOMERS, orders=data.ORDERS)
        {1: {'orders': 3, 'total': 1287, 'name': 'Ekaterin Vorsoisson', 'email':
        'evorsoisson@komarr.net'}, 2: {'orders': 5, 'total': 2778, 'name': 'Cord
        elia Naismith', 'email': 'cordelia@beta.com'}, 3: {'orders': 3, 'total':
        358, 'name': 'Ivan Vorpatril', 'email': 'iv398@barrayar.net'}, 4: {'orde
        rs': 5, 'total': 1207, 'name': 'Aral Vorkosigan', 'email': 'viceroy@serg
        yar.net'}, 5: {'orders': 3, 'total': 451, 'name': 'Eli Quinn', 'email':
        'admiral@dendarii.com'}, 6: {'orders': 3, 'total': 1198, 'name': 'Bel Th
        orne', 'email': 'portmaster@graf.net'}, 7: {'orders': 3, 'total': 1897,
        'name': 'Simon Illyan', 'email': 'impsec@barrayar.net'}, 8: {'orders': 1
        , 'total': 204, 'name': 'Duv Galeni', 'email': 'dg1367@barrayar.net'},9:
        {'orders': 2, 'total': 1704, 'name': 'Gregor Vorbarra', 'email': 'impsec
        @barrayar.net'}}

    """
    final_dict = {}
    for cus_id, cus_info in customers.iteritems():
        order_total = 0
        order_fre = 0
        for order_val in orders.itervalues():
            if cus_id in (order_val['customer_id'],):
                order_total += order_val['total']
                order_fre += 1
                final_dict[cus_id] = {'name': cus_info['name'],
                                      'email': cus_info['email'],
                                      'orders': order_fre,
                                      'total': order_total}
    return final_dict
