
    # bikes models, costs and inventory
bikes = {
        'Orbita Classic': [100, 10],
        'Orbita Luxury': [1500, 15],
        'Orbita City:': [1900, 19],
        'Orbita Kid': [90, 9],
        'Orbita Trail': [300, 3],
        'Orbita Pink:': [490, 4]
        }

class Bicycle(object):

    def __init__(self, name, weight, cost):
        # has a name
        self.name = name
        # has a weight
        self.weight = weight
        # has a cost to produce
        self.cost = cost


class BikeShop(Bicycle):

    def __init__(self, name, inventory, margin):
        #  has a name
        self.name = name
        # has an inventory of different bicycle
        self.inventory = inventory
        # sell bicyles with a margin over cost
        self.margin = margin
        # can see how much profit has been made from selling BikeShops
        self.profit = 0

    def bike_price(self):
        # set prices for bikes and pass them to a new list
        price = {}
        for k, v in self.inventory.items():
            # add to new dict
            price[k] = v[0]*(1+self.margin) # DO I NEED TO CALL v[0]? Is there a more efficient way?
        return(price)
        #HOW CAN WE UPDATE THE bikes dict instead?

    def bike_check(self, budget):
        #return bikes that are within customer budget
        bikes_available = self.bike_price()
        for k, v in bikes_available.items():
            if v >= budget:
                del bikes_available[k]
        return(bikes_available)


    def bike_sell(self, bike, customer):
        pass
        # sell a bike to a customer and update inventory
        #customer_bike = bike
        #customer_budget -= bike_price
        #self.profit += bike_price
        #del self.inventory[bike_key???]


class Customer(BikeShop):

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def bikes_within_budget(self):
        # can buy and own a new bicycle
        pass



def main():

    # print the initial inventory of bikes
    print('\nInventory of {}:'.format(shop.name))
    for k,v in shop.inventory.items():
        print('{}: {} bikes'.format(k,v))

    # print the name of each customer and the bikes available to buy
    #print("{}: {}".format(customer1.name, 'BIKES_IN_BUDGET')) # BIKES_IN_BUDGET: need to price the bikes
    #print("{}: {}".format(customer2.name, 'BIKES_IN_BUDGET'))
    #print("{}: {}".format(customer3.name, 'BIKES_IN_BUDGET'))

    # each customer purchases a bike
    # print the name of bike
    # print the cost
    # print how much money the customer have left

    # print the shop remaining inventory
    # print how much profit was made selling the three bikes


if __name__ == "__main__":
    print("Starting...")

    # set a new shop
    shop = BikeShop(name="SnakeBikes", inventory=bikes, margin=0.20)

    # set 3 customers
    customer1 = Customer(name = "Cloe", budget = 200)
    customer2 = Customer(name = "Sofia", budget = 500)
    customer3 = Customer(name = "Dario", budget = 1000)


    print('bike prices:')
    print(shop.bike_price())

    print('bike availability:')
    print(shop.bike_check(1000))



# THEN GO TO THE EXTENSION CHALLENGE!
