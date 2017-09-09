import time
def egcd(a, b):
    r = -1
    B = b
    A = a
    eq_set = []
    full_set = []
    mod_set = []

    #euclid's algorithm
    while r!=1 and r!=0:
        r = b%a
        q = b//a
        eq_set = [r, b, a, q*-1]
        b = a
        a = r
        full_set.append(eq_set)

    for i in range(0, 4):
        mod_set.append(full_set[-1][i])

    mod_set.insert(2, 1)
    counter = 0

    #extended euclid's algorithm
    for i in range(1, len(full_set)):
        if counter%2 == 0:
            mod_set[2] = full_set[-1*(i+1)][3]*mod_set[4]+mod_set[2]
            mod_set[3] = full_set[-1*(i+1)][1]

        elif counter%2 != 0:
            mod_set[4] = full_set[-1*(i+1)][3]*mod_set[2]+mod_set[4]
            mod_set[1] = full_set[-1*(i+1)][1]

        counter += 1

    if mod_set[3] == B:
        return mod_set[2]%B
    return mod_set[4]%B
timestamp1 = time.time()
print egcd(1436354634563546363456435635634564572437693486572348678234768374623,123231461346134613746783174587319485798317589721387645783465763174567163457617346578136475863441)
timestamp2 = time.time()
print "This took %.2f seconds" % (timestamp2 - timestamp1)

