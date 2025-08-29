
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Title line
        title = f"{self.name:*^30}\n"

        # Items
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"

        # Total line
        total = f"Total: {self.get_balance():.2f}"

        return title + items + total


def create_spend_chart(categories):
    # Calculate spending for each category
    spends = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spends.append(spent)

    total_spent = sum(spends)
    percentages = [int((s / total_spent) * 100) // 10 * 10 for s in spends]

    # Title
    chart = "Percentage spent by category\n"

    # Chart body
    for i in range(100, -1, -10):
        line = f"{i:>3}|"
        for p in percentages:
            if p >= i:
                line += " o "
            else:
                line += "   "
        chart += line + " \n"

    # Divider line
    chart += "    -" + "---" * len(categories) + "\n"

    # Category names vertically
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "     "
        for cat in categories:
            if i < len(cat.name):
                line += cat.name[i] + "  "
            else:
                line += "   "
        if i < max_len - 1:
            chart += line + "\n"
        else:
            chart += line

    return chart
