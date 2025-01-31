#!/usr/bin/env python3

import sys
import math

def main():
    if len(sys.argv) != 4:
        print("<div class='error'>Invalid number of arguments.</div>")
        return 1

    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    errors = []
    messages = []

    try:
        a_val = float(a)
    except ValueError:
        errors.append("a is not numeric.")
    try:
        b_val = float(b)
    except ValueError:
        errors.append("b is not numeric.")
    try:
        c_val = float(c)
    except ValueError:
        errors.append("c is not numeric.")

    if errors:
        print(f"<div class='error'>{'<br>'.join(errors)}</div>")
        return 1

    if a_val < 1:
        messages.append("Input a is too small.")
    if b_val == 0:
        messages.append("b is zero and will not affect the result.")
    if c_val < 0:
        errors.append("c cannot be negative.")
    
    if errors:
        print(f"<div class='error'>{'<br>'.join(errors)}</div>")
        return 1

    c_cubed = c_val ** 3
    sqrt_cubed = math.sqrt(c_cubed)

    try:
        if c_cubed > 1000:
            intermediate = sqrt_cubed * 10
        else:
            intermediate = sqrt_cubed / a_val
    except ZeroDivisionError:
        print("<div class='error'>Division by zero because a is zero.</div>")
        return 1

    final = intermediate + b_val

    print("<html><body>")
    if messages:
        print(f"<div class='messages'>{'<br>'.join(messages)}</div>")
    print(f"<p>Result: {final:.2f}</p>")
    print("</body></html>")
    return 0

if __name__ == "__main__":
    main()