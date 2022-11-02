"""
Madhava's Method for approximation of Pi

Pi          1     1     1     1     1                 
--  =  1 - --- + --- - --- + --- - --- +  ..........
4           3     5     7     9     11              

"""

def calculate_pi(episodes=125):
    plus = False 
    rhs = 1
    i = 0
    while i < episodes:
        denominator = 3 + (2 * i)
        correction = 1 / denominator
        if plus:
            rhs += correction
        else:
            rhs -= correction 
        pi = rhs * 4
        print(pi)

        i += 1
        plus = not plus

if __name__ == "__main__":
    calculate_pi()
