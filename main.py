import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    temp = sandwich_maker_instance
    while temp.size.lower() != 'off':
        size = temp.size.lower()
        if size.lower() == 'report':
            for x in resources:
                print(x + ": {0} slice(s).".format(temp.machine_resources[x]))
        else:
            ingredients = recipes[size]['ingredients']
            if not temp.check_resources(ingredients):
                print("Please come again!")
            else:
                print("Your total is ${0}".format(recipes[size]['cost']))
                payment = cashier_instance.process_coins()
                if not cashier_instance.transaction_result(payment, recipes[size]['cost']):
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    temp.make_sandwich(size, recipes[size]['ingredients'])
        temp = SandwichMaker(temp.machine_resources)

if __name__=="__main__":
    main()
