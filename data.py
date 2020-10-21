import numpy as np
import pandas as pd
import pymongo

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


def mongoData():
    """ mongo test db数据查询

    :return: mongo 测试数据DataFrame
    """
    test = pymongo.MongoClient('mongodb://gt163.cn:14011/')["test"]
    result = test["m_authregister"].find({"auth_type": "faceAuth"},
                                         {"_id": 0, "time": 1, "auth_result": 1}).sort("time", 1)
    df = pd.DataFrame(result)
    print(df)
    return df


if __name__ == '__main__':
    # randomData()
    mongoData()
