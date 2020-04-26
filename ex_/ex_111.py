import csv


def write_csv(results):
    # 创建文件写入对象
    f = open('ticket_test.csv', 'w', encoding='utf-8')
    # 通过文件对象创建 csv 写入对象
    csv_writer = csv.writer(f)
    # 把数据写入到 csv 文件中
    # 写入标题
    csv_writer.writerow(results[0])
    results.pop(0)
    for result in results:
        csv_writer.writerow(result.values())
    f.close()


data = [['periods', 'ticket_date', 'red_ball', 'blue_ball'],
        {'periods': '2020023', 'ticket_date': '2020-04-12(日)', 'ticket_red_ball': '040520213033',
         'ticket_blue_ball': '08'},
        {'periods': '2020022', 'ticket_date': '2020-04-09(四)', 'ticket_red_ball': '021020222530',
         'ticket_blue_ball': '02'},
        {'periods': '2020021', 'ticket_date': '2020-04-07(二)', 'ticket_red_ball': '020614162731',
         'ticket_blue_ball': '07'},
        {'periods': '2020020', 'ticket_date': '2020-04-05(日)', 'ticket_red_ball': '010609131522',
         'ticket_blue_ball': '14'},
        {'periods': '2020019', 'ticket_date': '2020-04-02(四)', 'ticket_red_ball': '151927283033',
         'ticket_blue_ball': '03'},
        {'periods': '2020018', 'ticket_date': '2020-03-31(二)', 'ticket_red_ball': '050708111722',
         'ticket_blue_ball': '13'},
        {'periods': '2020017', 'ticket_date': '2020-03-29(日)', 'ticket_red_ball': '020407152027',
         'ticket_blue_ball': '04'},
        {'periods': '2020016', 'ticket_date': '2020-03-26(四)', 'ticket_red_ball': '050608172427',
         'ticket_blue_ball': '07'},
        {'periods': '2020015', 'ticket_date': '2020-03-24(二)', 'ticket_red_ball': '080922243033',
         'ticket_blue_ball': '01'},
        {'periods': '2020014', 'ticket_date': '2020-03-22(日)', 'ticket_red_ball': '020708101216',
         'ticket_blue_ball': '07'},
        {'periods': '2020013', 'ticket_date': '2020-03-19(四)', 'ticket_red_ball': '020810202130',
         'ticket_blue_ball': '14'},
        {'periods': '2020012', 'ticket_date': '2020-03-17(二)', 'ticket_red_ball': '041314232631',
         'ticket_blue_ball': '09'},
        {'periods': '2020011', 'ticket_date': '2020-03-15(日)', 'ticket_red_ball': '040507171829',
         'ticket_blue_ball': '01'},
        {'periods': '2020010', 'ticket_date': '2020-03-12(四)', 'ticket_red_ball': '111422273132',
         'ticket_blue_ball': '09'},
        {'periods': '2020009', 'ticket_date': '2020-01-21(二)', 'ticket_red_ball': '030608141926',
         'ticket_blue_ball': '12'},
        {'periods': '2020008', 'ticket_date': '2020-01-19(日)', 'ticket_red_ball': '010406101128',
         'ticket_blue_ball': '16'},
        {'periods': '2020007', 'ticket_date': '2020-01-16(四)', 'ticket_red_ball': '051217202531',
         'ticket_blue_ball': '10'},
        {'periods': '2020006', 'ticket_date': '2020-01-14(二)', 'ticket_red_ball': '030405101632',
         'ticket_blue_ball': '09'},
        {'periods': '2020005', 'ticket_date': '2020-01-12(日)', 'ticket_red_ball': '111617222632',
         'ticket_blue_ball': '04'},
        {'periods': '2020004', 'ticket_date': '2020-01-09(四)', 'ticket_red_ball': '021517273233',
         'ticket_blue_ball': '03'},
        {'periods': '2020003', 'ticket_date': '2020-01-07(二)', 'ticket_red_ball': '091726293032',
         'ticket_blue_ball': '03'},
        {'periods': '2020002', 'ticket_date': '2020-01-05(日)', 'ticket_red_ball': '040914151629',
         'ticket_blue_ball': '11'},
        {'periods': '2020001', 'ticket_date': '2020-01-02(四)', 'ticket_red_ball': '021523262930',
         'ticket_blue_ball': '02'},
        {'periods': '2019151', 'ticket_date': '2019-12-31(二)', 'ticket_red_ball': '020609182426',
         'ticket_blue_ball': '14'},
        {'periods': '2019150', 'ticket_date': '2019-12-29(日)', 'ticket_red_ball': '020914222729',
         'ticket_blue_ball': '02'},
        {'periods': '2019149', 'ticket_date': '2019-12-26(四)', 'ticket_red_ball': '010627283133',
         'ticket_blue_ball': '07'},
        {'periods': '2019148', 'ticket_date': '2019-12-24(二)', 'ticket_red_ball': '091013202627',
         'ticket_blue_ball': '08'},
        {'periods': '2019147', 'ticket_date': '2019-12-22(日)', 'ticket_red_ball': '010912142327',
         'ticket_blue_ball': '12'},
        {'periods': '2019146', 'ticket_date': '2019-12-19(四)', 'ticket_red_ball': '010410123032',
         'ticket_blue_ball': '14'},
        {'periods': '2019145', 'ticket_date': '2019-12-17(二)', 'ticket_red_ball': '010813171819',
         'ticket_blue_ball': '16'}]

write_csv(results=data)
