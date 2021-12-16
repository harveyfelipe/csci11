import user_ops as user
import order_ops as order_ops   
from decimal import Decimal

if __name__ == '__main__':
    
    # print(user.query_user_profile("tgrimes1"))
    
    orders = order_ops.query_pending_orders("PENDING")

    for order in orders:
        print(order['sk'])
    
    # try:
    #     orders = order_ops.query_user_order_by_status_date('tgrimes1', 'PENDING', '11-13-2021')
    # except Exception as err:
    #     print('No entries found')
    
    # for order in orders:
    #     print(order)
    
    # orders1 = order_ops.query_user_order_by_status_date('tgrimes1', 'PENDING', '11-13-2021')
    # print('Orders by Status (Pending) and Date (11-13-2021)')
    # for order in orders1:
    #     order_id = order['sk'][33:]
    #     print('Order#{0}'.format(order_id))
    
    # orders2 = order_ops.query_pending_orders('PENDING')
    # print('\nPending Orders')
    # for order in orders2:
    #     order_id = order['sk'][33:]
    #     print('Order#{0}'.format(order_id))