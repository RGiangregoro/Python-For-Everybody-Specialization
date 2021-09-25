text = "X-DSPAM-Confidence:    0.8475";

numberString = text[text.find('0'):]


print(float(numberString));