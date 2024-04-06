# This fantastic bit of math was discovered by Chinese mathematician Sun Tzu in the 3rd century AD.
# It can be used to calculate the values of large unknown numbers, provided you know the remainders of dividing the unknown number by several smaller, prime numbers.
# I learned about it googling "strategies to solve for unknown numbers using remainders".
# Learn more about the actual theorem at https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html and watch a more basic video on using the process itself at https://www.youtube.com/watch?v=zIFehsBHB8o
# Remember: a lot of computer science and logic can be explained by math and number theory! Always look for mathematical shortcuts in your algorithms; often, you can reduce brute force.

def chinese_remainder_theorem(buses):

    #Create array of remainders
    remainders = []
    for bus in buses:
        remainders.append(bus[1]) #Add remainder to remainders array

    #Create an array of divisor products (the product of every single divisor (bus number) except for the one currently being evaluated)
    divisor_products = []
    for x in range(len(buses)): #Iterate through buses
        product = 1
        for y in range(len(buses)): #For each bus, iterate through all the OTHER buses
            if x != y: #Do not evaluate for the current bus
                product *= buses[y][0]
        divisor_products.append(product) #Add the product to the array of divisor products

    #Create an array of numerical inverses (numbers which when multiplied by the corresponding divisor product and divided by the current term, have a remainder of 1)
    inverses = []
    for x in range(len(divisor_products)): #Iterate through each divisor product and evaluate its inverse
        multiplier = 1
        while ((divisor_products[x]*multiplier)%buses[x][0]) != 1: #While the remainder of 1 condition is not met, continue to increment multiplier
            multiplier += 1
        inverses.append(multiplier) #Once the multiplier is valid, add it to inverses array

    #Store final modulus - the product of all the divisors
    final_modulus = 1
    for bus in buses:
        final_modulus *= bus[0]

    #Store final value - the sum total of the products of each remainder, divisor product and inverse
    final_value = 0
    for x in range(len(buses)):
        final_value += (remainders[x]*divisor_products[x]*inverses[x])

    #Final step - divide the final value by the final modulus
    final_value%=final_modulus

    return final_value
