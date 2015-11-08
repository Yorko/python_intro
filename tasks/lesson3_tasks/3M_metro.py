n = int(input())

C1, C2, C3 = 15, 125, 440
N1, N2, N3 = 1, 10, 60

def cost(n1, n2, n3):
    return C1 * n1 + C2 * n2 + C3 * n3

def num_rides(n1, n2, n3):
    return N1 * n1 + N2 * n2 + N3 * n3

# first we buy as many 60-tickets as possible
initial_n3 = n // N3

# the remaining number of tickets to by
n = n % N3

# init for optimal numbers of tickets
opt_n = (0, 0, initial_n3)
# initialize min_cost to some large number
min_cost = pow(10, 20)

for n1 in range(N3) :
    for n2 in range(int(N3 / N2) + 1) :
        for n3 in range(int(N3 / N3) + 1) :
            if ((num_rides(n1, n2, n3) >= n) & (cost(n1, n2, n3) < min_cost)) :
                min_cost = cost(n1, n2, n3)
                opt_n = (n1, n2, n3 + initial_n3)

print(opt_n[0], opt_n[1], opt_n[2], sep=' ')