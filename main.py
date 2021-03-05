import matplotlib.pyplot as plt
import pec


def plot(Y, w):
    plt.subplot(2, 1, 1)
    plt.plot(Y)

    pe_list = [0] * w
    #print(pe_list)

    for i in range(len(Y)-w):
        S = Y[i:i+w]
        #pe = pec.pec(S, 5, 1)
        pe = pec.permutation_entropy(S, 5, 1)
        pe_list.append(pe)

    plt.subplot(2, 1, 2)
    plt.plot(pe_list)
    plt.show()


if __name__ == "__main__":
    time = []
    voltage = []
    with open("vfdb-418.txt") as f:
        for line in f.readlines():
            line.rstrip('\n')
            x, y = line.split()
            #time.append(eval(x))
            voltage.append(float(y))

    f.close()
    plot(voltage, 135)
