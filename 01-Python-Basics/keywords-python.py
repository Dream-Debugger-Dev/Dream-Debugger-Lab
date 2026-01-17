# Keywords in Python
# Keywords are reserved words in Python that have special meaning and cannot be used as identifiers (variable names, function names, etc.)
# Here are some examples of Python keywords:
import keyword
print("List of Python keywords:")
print(keyword.kwlist)
# Example usage of some keywords
def example_function():
    global x
    x = 10  # 'global' keyword
    if x > 5:  # 'if' keyword
        return True  # 'return' keyword
    else:  # 'else' keyword
        return False