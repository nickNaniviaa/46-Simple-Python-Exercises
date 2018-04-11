# Exercise 11:
# ======================
# Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n
# characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the
# string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate
# to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)


def generate_n_chars(n, c):
    output_string = ''
    for i in range(n):
        output_string+=c
    
    return output_string


if __name__ == '__main__':
    print(generate_n_chars(5,'x'))  #xxxxx - type: string