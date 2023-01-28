import matplotlib.pyplot as plt


def show(x, y, n):
    plt.style.use('seaborn-darkgrid')
    plt.figure(facecolor='#3d7a5c')
    plt.title(f'Heating transport equation for n = {n}', color='#fff')

    subplot = plt.subplot()
    subplot.set(xlabel='x')
    subplot.set(ylabel='y')
    subplot.set_facecolor("#a4dec1")
    subplot.plot(x, y, color='red')

    plt.show()
