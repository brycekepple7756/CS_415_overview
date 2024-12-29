#
# Bryce Kepple
# Recursion
#


def countdown(n):

    #basecase once 0 is hit it prints blastoff
    if n == 0:
        return print("Blastoff!")

    # prints n and then calls function with one less
    return print(n),countdown(n-1)

countdown(10)


def counting_clovers(n):
    #basecases
    if n == 0:
        return 0
    if n == 1:
        return 4

    #returns one less of the function along with 4, which will be added up at the end
    return counting_clovers(n-1)+4

print(counting_clovers(0))
print(counting_clovers(1))
print(counting_clovers(10))


def count_from_N_to_M(n,m):
    #basecase for when n reaches m
    if n == m:
        return

    # prints out current n then calls function plus one
    return print(n),count_from_N_to_M(n+1,m)

count_from_N_to_M(2,9)


