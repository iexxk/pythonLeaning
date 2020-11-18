import matplotlib.pyplot as plt
import pandas as pd
import pandas_bokeh
import nupy as np

pd.set_option('plotting.backend', 'pandas_bokeh')
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)
# 设置显示的宽度
pd.set_option('display.width', 5000)


def randomData():
    """ 生成随机矩阵7:3数据

    :return: 返回随机数据DataFrame
    """
    array = np.random.rand(7, 3)
    df = pd.DataFrame(array, columns=['first', 'second', 'third'])
    print(df)
    return df

def drowShow():
    """
    plot 画线显示
    :return:
    """
    df = randomData()
    df.plot_bokeh()
    plt.show()


if __name__ == '__main__':
    drowShow()
