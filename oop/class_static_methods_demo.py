class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to return the sum of two numbers.
        Does not depend on class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to return the product of two numbers.
        Accesses class-level data using the cls parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()
