def base():
    11_PRO_Max = ["1", "Apple", "США", "1", "11 PRO Max", "256", "6.5", 
         "Apple A13 Bionic", "6", "111"]
    SE = ["1", "Apple", "США", "2", "SE(2020)", "64", "4.7", 
         "Apple A13 Bionic", "2", "56"]
    Galaxy_Z_Flip = ['2', 'Samsung', 'Южная Корея', '3', 'Galaxy Z Flip', 
                     '256', '6.7', 'Qualcomm Snapdragon 855 Plus', '8', '256']
    Galaxy_S20_ULTRA = ['2', 'Samsung', 'Южная Корея', '4', 'Galaxy S20 ULTRA', '128', '6.9', 
         'Samsung Exynos 990', '12', '15']
    View_30_PRO = ['3', 'Honor', 'Китай', '5', 'View 30 PRO', '256', '6.57', 
         'HiSilicon Kirin 990 5G', '8', '25']
    P40PRO = ['4', 'Huawei', 'Китай', '6', 'P40PRO', '256', '6.58', 
         'HiSilicon Kirin 990 5G', '8', '33']
    NEX3 = ['5', 'VIVO', 'Китай', '7', 'NEX3', '128', '6.89', 
         'Qualcomm Snapdragon 855 Plus', '8', '3']
    #['', '', '', '', '', '', '', '', '', '']
    
    #'Код производителя', 'Производитель', 'Страна', 'Код товара', 'Модель', 'Внутренняя память', 'Диагональ экрана', 'Процессор', 'Оперативная память', 'Кол-во смартфонов'

    keys = ['number', 'RAM', 'CPU', 'diagonal', 'storage', 'os', 'model', 'code_smart', 'country', 'firm', 'code']
    values = [11_PRO_Max, SE, Galaxy_Z_Flip, Galaxy_S20_ULTRA, View_30_PRO, P40PRO, NEX3]
    
    return dict(zip([x[0] for x in values], [dict(zip(keys, x)) 
                    for x in values]))
 
    
if __name__ == '__main__':
    import pickle
    from materials import road_to_data
    data = open(road_to_data, "wb")
    pickle.dump(base(), data)
    data.close()
    