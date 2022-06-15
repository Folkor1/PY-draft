class Matrix:
    """
    Matrix superclass.
    """
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
    
    def calc_2x2(self):
        return self.num1 * self.num4 - self.num2 * self.num3

class Matrix_2x2(Matrix):
    """
    2x2 matrix class,
    returns 2x2 matrix determinant.
    """
    def __init__(self, num1, num2, num3, num4):
        super().__init__(num1, num2, num3, num4)
    
    def determinant_2x2(self):
        return f'{super().calc_2x2()}'

class Matrix_3x3(Matrix):
    """
    3x3 matrix class,
    calculates 3x3 matrix determinant.
    """
    def __init__(self, num1, num2, num3, num4, num5, num6, num7, 
    num8, num9):
        Matrix.__init__(self, num1, num2, num3, num4)
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
        self.num8 = num8
        self.num9 = num9
    
    def determinant_3x3(self):
        a = self.num1 * self.num5 * self.num9
        b = self.num2 * self.num6 * self.num7
        c = self.num3 * self.num4 * self.num8
        d = self.num3 * self.num5 * self.num7
        e = self.num2 * self.num4 * self.num9
        f = self.num1 * self.num6 * self.num8
        
        return a + b + c - d - e - f

class Matrix_4x4(Matrix):
    """
    4x4 matrix class,
    calculates 4x4 matrix determinant.
    """
    def __init__(self, num1, num2, num3, num4, num5, num6, num7,
     num8, num9, num10, num11, num12, num13, num14, num15, num16):
        Matrix.__init__(self, num1, num2, num3, num4)
        self.num5 = num5
        self.num6 = num6
        self.num7 = num7
        self.num8 = num8
        self.num9 = num9
        self.num10 = num10
        self.num11 = num11
        self.num12 = num12
        self.num13 = num13
        self.num14 = num14
        self.num15 = num15
        self.num16 = num16
    
    def determinant_4x4(self):
        a1 = self.num6 * self.num11 * self.num16
        b1 = self.num7 * self.num12 * self.num14
        c1 = self.num8 * self.num10 * self.num15
        d1 = self.num8 * self.num11 * self.num14
        e1 = self.num7 * self.num10 * self.num16
        f1 = self.num6 * self.num12 * self.num15

        a2 = self.num5 * self.num11 * self.num16
        b2 = self.num7 * self.num12 * self.num13
        c2 = self.num8 * self.num9 * self.num15
        d2 = self.num8 * self.num11 * self.num13
        e2 = self.num7 * self.num9 * self.num16
        f2 = self.num5 * self.num12 * self.num15

        a3 = self.num5 * self.num10 * self.num16
        b3 = self.num6 * self.num12 * self.num13
        c3 = self.num8 * self.num9 * self.num14
        d3 = self.num8 * self.num10 * self.num13
        e3 = self.num6 * self.num9 * self.num16
        f3 = self.num5 * self.num12 * self.num14

        a4 = self.num5 * self.num10 * self.num15
        b4 = self.num6 * self.num11 * self.num13
        c4 = self.num7 * self.num9 * self.num14
        d4 = self.num7 * self.num10 * self.num13
        e4 = self.num6 * self.num9 * self.num15
        f4 = self.num5 * self.num11 * self.num14
        
        m1 = self.num1 * (a1 + b1 + c1 - d1 - e1 - f1)
        m2 = self.num2 * (a2 + b2 + c2 - d2 - e2 - f2)
        m3 = self.num3 * (a3 + b3 + c3 - d3 - e3 - f3)
        m4 = self.num4 * (a4 + b4 + c4 - d4 - e4 - f4)

        return m1 - m2 + m3 - m4