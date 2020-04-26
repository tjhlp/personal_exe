import matplotlib.pyplot as plt


def plot_bar_pic(plot_data, filenames, index=1, count=1, p_type=1):
    """
    将信息可视化
    :param plot_data: 以键值对信息传入
    :param filenames: 保存文件的位置
    :return: None
    """
    # 标注
    label_dict = {
        # '标注': ['职位数量', '语言数量', '职位数量'],
        '标题': ['红球数目分布图', '蓝球数目分布图', '第%s个位置红球的出现次数' % count]
    }
    ball_list = []
    x_core = []
    y_core = []
    for key, value in plot_data.items():
        x_core.append(key)
        ball_list.append(key)
        y_core.append(value)
    plt.rcParams['figure.figsize'] = (20, 8.0)  # 显示大小
    x_core.sort()
    if p_type == 1:
        plt.bar(x_core, y_core, facecolor='orange')
    else:
        plt.plot(x_core, y_core)
    # 添加数字标号
    for score, pos in zip(x_core, y_core):
        plt.text(score, pos, '%d' % pos)
    plt.xticks(x_core)
    plt.legend(loc='best')
    plt.xlabel(label_dict['标题'][index])
    plt.savefig(filenames)
    # plt.show()



if __name__ == '__main__':
    test_data = {1: 2, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 4, 8: 2, 9: 3, 10: 1, 11: 1, 12: 2, 13: 1, 14: 4, 15: 0, 16: 2}
    plot_bar_pic(test_data, 'jpg/ticket_info.jpg')
