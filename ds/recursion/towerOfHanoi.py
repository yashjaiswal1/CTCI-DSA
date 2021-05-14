# APPROACH:
# (1) Move (n-1) disks to intermediate column
# (2) Move the nth disk from source to destination
# (3) Move the (n-1) disk from intermediate to destination
# BASE CASE: if n = 1, then simply move the disk

# Representation
# 3    |    |
# 2    |    |
# 1    |    |


def tower_of_hanoi(n, source, intermediate, destination):
    if n == 1:
        print("Transfer disk 1 from " + source + " to " + destination)
    else:
        tower_of_hanoi(n-1, source, destination, intermediate)
        print("Transfer disk " + str(n) + " from " +
              source + " to " + destination)
        tower_of_hanoi(n-1, intermediate, source, destination)


tower_of_hanoi(4, 'A', 'B', 'C')
