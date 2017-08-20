def item_order(order):
    salad = 0
    hamburger = 0
    water = 0
    item=order.split()
    for check in item:
        if check == 'salad' :
            salad+=1
        elif check == 'water' :
            water+=1
        elif check == 'hamburger':
            hamburger+=1
    return ('salad:'+str(salad)+' hamburger:'+str(hamburger)+' water:'+str(water))
