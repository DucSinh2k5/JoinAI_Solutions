import math

def sigmoid_derivative(xs):
    derivatives = []
    
    for x in xs:
        # Bước 1: Tính giá trị sigmoid (s)
        s = 1 / (1 + math.exp(-x))
        
        # Bước 2: Tính đạo hàm bằng s * (1 - s)
        derivatives.append(s * (1 - s))
        
    return derivatives
