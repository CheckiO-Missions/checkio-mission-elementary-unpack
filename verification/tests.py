"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [(1, 2, 3, 4, 5, 6, 7, 9)],
            "answer": (1, 3, 7),
        },
        {
            "input": [(1, 1, 1, 1)],
            "answer": (1, 1, 1),
        },
        {
            "input": [(6, 3, 7)],
            "answer": (6, 7, 3),
        },
    ],
    "Extra": [
        {
            "input": [(30, 40, 100)],
            "answer": (30, 100, 40),
        },
        {
            "input": [(5, 5, 5, 5, 5, 5)],
            "answer": (5, 5, 5),
        },
    ]
}
