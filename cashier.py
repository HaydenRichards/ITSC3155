class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollar = float(input("How many dollars?: "))
        half_dollar = float(input("How many half dollars?: "))
        quarter = float(input("How many quarters?: "))
        nickel = float(input("How many nickels?: "))
        return dollar + (half_dollar * .5) + (quarter * .25) + (nickel * .05)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            diff = coins - cost
            print("Here is your change ${0}.".format(diff))
            return True
        return False
