class TestApp:

    def test_addition(self):
        assert 2 + 3 == 5

    def test_subtraction(self):
        assert 5 - 2 == 3

test = TestApp()
test.test_addition()
test.test_subtraction()

print("All tests passed successfully!")