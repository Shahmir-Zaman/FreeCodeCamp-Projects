class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        """Add a deposit to the ledger"""
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        """Withdraw money if sufficient funds available"""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        """Calculate current balance from ledger entries"""
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, category):
        """Transfer money to another category"""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        """Check if sufficient funds are available"""
        return amount <= self.get_balance()
    
    def __str__(self):
        """String representation of the category"""
        title = self.name.center(30, "*")
        
        # Create ledger lines
        lines = [title]
        for item in self.ledger:
            # First 23 characters of description
            desc = item["description"][:23]
            # Amount formatted to 2 decimal places
            amount = f"{item['amount']:.2f}"
            # Create line with proper spacing (total 30 chars)
            line = f"{desc:<23}{amount:>7}"
            lines.append(line)
        
        # Add total line
        total = f"Total: {self.get_balance():.2f}"
        lines.append(total)
        
        return "\n".join(lines)


def create_spend_chart(categories):
    """Create a bar chart showing percentage spent by category"""
    
    # Calculate total spent for each category (only withdrawals)
    category_spending = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spending.append(spent)
    
    # Calculate total spending across all categories
    total_spent = sum(category_spending)
    
    # Calculate percentages and round down to nearest 10
    percentages = []
    for spent in category_spending:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int((spent / total_spent) * 100 // 10) * 10
        percentages.append(percentage)
    
    # Build the chart
    lines = ["Percentage spent by category"]
    
    # Create bars from 100 down to 0
    for i in range(100, -1, -10):
        line = f"{i:>3}| "
        for j, percentage in enumerate(percentages):
            if percentage >= i:
                line += "o"
            else:
                line += " "
            if j < len(percentages) - 1:
                line += "  "
        line += "  " 
        lines.append(line)
    
    # Create horizontal line
    horizontal_line = "    " + "-" * (len(categories) * 3 + 1)
    lines.append(horizontal_line)
    
    # Create vertical category names
    max_name_length = max(len(category.name) for category in categories)
    
    for i in range(max_name_length):
        line = "     "  
        for j, category in enumerate(categories):
            if i < len(category.name):
                line += category.name[i]
            else:
                line += " "
            if j < len(categories) - 1:
                line += "  "
        line += "  "  
        lines.append(line)
    
    return "\n".join(lines)


# Example usage:
if __name__ == "__main__":
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)
    print()
    
    auto = Category('Auto')
    auto.deposit(1000, 'initial deposit')
    auto.withdraw(15)
    
    print(create_spend_chart([food, clothing, auto]))
