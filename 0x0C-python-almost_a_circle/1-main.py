#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id, r3.width(), r3.height(), r3.x(), r3.y())
    r3.width(20)
    r3.height(21)
    r3.x(22)
    r3.y(23)
    print("After setting new values of r3")
    print(r3.id, r3.width(), r3.height(), r3.x(), r3.y())
