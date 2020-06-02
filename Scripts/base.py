def base():
    1 = ["1", "Apple", "США", "1", "11 PRO Max", "256", "6.5", 
         "Apple A13 Bionic", "6", "111"]
    2 = ["1", "Apple", "США", "2", "SE(2020)", "64", "4.7", 
         "Apple A13 Bionic", "2", "56"]
    
    keys = ['code_firm', 'firm', 'memory', 'ram']
    values = [1, 2]
    
    return dict(zip([x[0] for x in values], [dict(zip(keys, x)) 
                    for x in values]))
 
    
if __name__ == '__main__':
    import pickle
    from materials import road_to_data
    data = open(road_to_data, "wb")
    pickle.dump(base(), data)
    data.close()   