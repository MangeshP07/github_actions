def test_calc_addition():
    output = 2+4
    assert output == 6


def test_calc_substraction():
    # ३. कमेंटच्या मागे बरोबर ४ स्पेस आहेत (E114 फिक्स करण्यासाठी)
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    # ४. कमेंट नीट फॉरमॅट केली आहे
    output = 2 * 4
    assert output == 8


def test_coucou():
    # ५. '=' च्या दोन्ही बाजूला स्पेस दिला आहे (E225 फिक्स करण्यासाठी)
    output = 'hello'
    assert output == 'hello'

