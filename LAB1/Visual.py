import matplotlib.pyplot as plt


def showGraph(data_a, ):
    plt.hist(data_a, bins=20 )
    plt.xlabel("Film")
    plt.ylabel("«Частота / частота»")
    plt.show()

