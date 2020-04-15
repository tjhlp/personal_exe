import matplotlib.pyplot as plt


def plot_data(plot_data, filenames):
    """
    将信息可视化
    :param plot_data: 以键值对信息传入
    :param filenames: 保存文件的位置
    :return: None
    """
    ball_list = []
    x_core = []
    y_core = []
    for key, value in plot_data.items():
        x_core.append(key)
        ball_list.append(key)
        y_core.append(value)
    # plt.rcParams['figure.figsize'] = (20, 8.0)  # 显示大小
    plt.bar(x_core, y_core, facecolor='orange')
    # 添加数字标号
    # for score, pos in zip(y_core, x_core):
    #     plt.text(score + 2, pos, '%d' % score)
    plt.savefig(filenames)
    plt.xticks(x_core)
    plt.yticks(y_core)
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    test_data = {1: 2, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 4, 8: 2, 9: 3, 10: 1, 11: 1, 12: 2, 13: 1, 14: 4, 15: 0, 16: 2}
    plot_data(test_data, 'jpg/ticket_info.jpg')
