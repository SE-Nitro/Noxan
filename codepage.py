FUNCTIONS = []
FUNCTIONS += ["+", "-", "×", "÷", "ⁱ", "g", "¶", "Đ"]
FUNCTIONS += ["Ŋ", "Ƣ", "!", "¡", "□", "i", "s", "t", "n"]
FUNCTIONS += ["h", "½"]

INDICATORS = ["↹", "{", "}"]

codepage = FUNCTIONS + INDICATORS

assert len(codepage) <= 256
