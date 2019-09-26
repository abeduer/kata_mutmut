from app.demo import Demo


class TestDemo:
    def test_demo(self):
        # Given
        a = 2
        b = 1
        # When
        result = Demo().compute(a, b)
        # Then
        assert result == 3
