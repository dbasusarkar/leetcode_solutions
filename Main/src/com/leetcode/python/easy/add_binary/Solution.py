class Solution:
    """
    67. Add Binary
    --------------
    Given two binary strings a and b, return their sum as a binary string.
    
    Example 1:
    Input: a = "11", b = "1"
    Output: "100"
    
    Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"
    
    Constraints:
    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
    """

    def addBinary(self, a, b) -> str:
        """
        All of this docsrting is from https://stackoverflow.com/users/449449/eumiro's answer to 
        https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python

        '{0:08b}'.format(6)
        '00000110'

        Just to explain the parts of the formatting string:
        - {} places a variable into a string
        - 0 takes the variable at argument position 0
        - : adds formatting options for this variable (otherwise it would represent decimal 6)
        - 08 formats the number to eight digits zero-padded on the left
        - b converts the number to its binary representation
        - If you're using a version of Python 3.6 or above, you can also use f-strings:
            f'{6:08b}'
            '00000110'
        """
        
        # Approach #1: NOT ACCEPTABLE (commented out)
#        return "{0:b}".format(int(a, 2) + int(b, 2))

        # Approach #2: BIT MANIPULATION 
            # convert a into an integer variable called x        
            # convert b into an integer variable called y 
            # XOR between x and y to get sum of a and b without considering carry
            # To get the actual carry, do AND between x and y, left shifted by 1
            # At the end of first iteration, x = result, y = carry 
            # Add XOR output and carry output to get actual sum of a and b using while loop

        x = int(a, 2)
        y = int(b, 2)

        while y:
            result = x ^ y
            carry = (x & y) << 1
            
            x = result
            y = carry

#        return bin(x)[2:]
        return "{0:b}".format(x)

