class VendingMachine:
    def __init__(self):
        self.status = "ON"
        self.balance = 0.00
        self.snack_price = 1.50
        self.snack_stock = 5
        self.total_sales = 0.00

    # Method 1: Turn on the machine
    def turn_on(self):
        self.status = "ON"
        print("Vending machine is now ON.")

    # Method 2: Turn off the machine
    def turn_off(self):
        self.status = "OFF"
        print("Vending machine is now OFF.")

    # Method 3: Insert money
    def insert_money(self, amount):
        if self.status == "ON" and amount > 0:
            self.balance += amount
            print(f"Inserted ${amount:.2f}")
        else:
            print("Unable to insert money.")

    # Method 4: Buy a snack
    def buy_snack(self):
        if self.status == "OFF":
            print("Machine is turned off.")
        elif self.snack_stock == 0:
            print("Sorry, snacks are sold out.")
        elif self.balance < self.snack_price:
            print("Not enough money.")
        else:
            self.balance -= self.snack_price
            self.snack_stock -= 1
            self.total_sales += self.snack_price
            print("Snack purchased successfully!")

    # Method 5: Restock snacks
    def restock(self, amount):
        if amount > 0:
            self.snack_stock += amount
            print(f"Restocked {amount} snacks.")
        else:
            print("Restock amount must be positive.")

    # Method 6: Display machine status
    def display_status(self):
        print("\n--- Vending Machine Status ---")
        print("Status:", self.status)
        print(f"Balance: ${self.balance:.2f}")
        print(f"Snack Price: ${self.snack_price:.2f}")
        print("Snacks Available:", self.snack_stock)
        print(f"Total Sales: ${self.total_sales:.2f}")
        print("------------------------------")


# Create the vending machine object
machine = VendingMachine()

# Demonstrate the methods
machine.display_status()

machine.turn_off()
machine.turn_on()

machine.insert_money(5.00)
machine.buy_snack()
machine.buy_snack()

machine.restock(3)

machine.display_status()