from function_to_be_tested import function_to_be_tested

test_cases = [
    {
        "input1": 1,
        "input2": 2,
        "expected1": 3,
        "expected2": 2
    },
    {
        "input1": 5,
        "input2": 3,
        "expected1": 8,
        "expected2": 15
    },
    {
        "input1": 8,
        "input2": 4,
        "expected1": 10,
        "expected2": 20
    }
]


def test_function_to_be_tested():
    for test_case in test_cases:
        print(f"Testing with {test_case}")
        actual1, actual2 = function_to_be_tested(test_case["input1"], test_case["input2"])
        assert actual1 == test_case["expected1"]
        assert actual2 == test_case["expected2"]


test_function_to_be_tested()