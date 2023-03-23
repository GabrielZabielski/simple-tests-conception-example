def function_to_be_tested(input1, input2):
    print("inside the function")
    return input1 + input2, input1 * input2


print("outside the function and __name__ == __main__")

if __name__ == "__main__":
    print("inside __name__ == __main__")
    function_to_be_tested(1, 2)