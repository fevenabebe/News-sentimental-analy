from src.preprocessing import clean_text


def test_clean_text_basic():
    result = clean_text("Hello!!!")
    assert result == "hello"


def test_clean_text_numbers():
    result = clean_text("AAPL 123 news")
    assert "123" not in result