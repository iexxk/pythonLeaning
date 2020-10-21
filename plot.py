import matplotlib.pyplot as plt
import data


def drowShow():
    """
    plot 画线显示
    :return:
    """
    df = data.randomData()
    df.plot()
    df.plot.line(subplots=True)
    plt.show()


if __name__ == '__main__':
    drowShow()
