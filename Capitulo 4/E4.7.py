from operator import add, sub, mul, truediv  # Import necessary operators

class PostfixTranslator:
    def __init__(self):
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "=": 0  # Assignment has lowest precedence
        }

    def infix_to_postfix(self, expression):
        stack = []
        output = []
        for token in expression.split():
            if token.isalnum():  # Variable or number
                output.append(token)
            elif token == "(":
                stack.append(token)
            elif token == ")":
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()  # Remove the "("
            else:  # Operator
                while stack and stack[-1] != "(" and self.precedence[stack[-1]] >= self.precedence[token]:
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return " ".join(output)

# Example usage
translator = PostfixTranslator()
expression = "(A = 3 + 4 * 5) + (B = 7 * 6) + B/A"
postfix_expression = translator.infix_to_postfix(expression)
print("The postfix representation is:", postfix_expression)





from ordered_record_array import OrderedRecordArray

class PostfixEvaluator:
    def __init__(self):
        self.variables = OrderedRecordArray()  # Store variables and their values

    def evaluate_postfix(self, expression):
        stack = []
        for token in expression.split():
            if token.isalnum():
                if token in self.variables:  # Check if it's a variable
                    value = self.variables.find(token).value
                else:
                    try:
                        value = float(token)  # Convert number to float
                    except ValueError:
                        raise ValueError(f"Invalid variable name: {token}")
                stack.append(value)
            elif token == "=":  # Assignment operator
                right_value = stack.pop()
                self.variables.insert((stack.pop(), right_value))  # Update variable
            else:  # Operator
                right_value = stack.pop()
                left_value = stack.pop()
                result = {
                    "+": add(left_value, right_value),
                    "-": sub(left_value, right_value),
                    "*": mul(left_value, right_value),
                    "/": truediv(left_value, right_value),
                }[token]
                stack.append(result)
            print("After processing", token, "stack holds:", stack)
        if len(stack) != 1:
            raise ValueError("Invalid expression")
        return stack.pop()

# Example usage
evaluator = PostfixEvaluator()
expression = "(A = 3 + 4 * 5) + (B = 7 * 6) + B/A"
postfix_expression = evaluator.evaluate_postfix(expression)
print("Final result =", postfix_expression)




