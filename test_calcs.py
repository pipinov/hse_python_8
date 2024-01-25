from calcs import sum

def test_sum():
    assert sum(3, 4) == 7, "Test with integers failed"
    assert sum(2.5, 3.1) == 5.6, "Test with floats failed"
    assert sum(-5, -7) == -12, "Test with negative numbers failed"

if __name__ == "__main__":
    test_sum()
    print("All tests passed successfully!")
