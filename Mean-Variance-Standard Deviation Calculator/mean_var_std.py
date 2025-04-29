import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
      raise ValueError('List must contain nine numbers.')
    
    calc_list = np.array(input_list)
    calc_list = calc_list.reshape(3,3)
    calculations = {}

    #mean calcs
    mean_0 = np.mean(calc_list, axis=0).tolist()
    mean_1 = np.mean(calc_list, axis=1).tolist()
    mean_flat = float(np.mean(calc_list))
    mean_list = [mean_0, mean_1, mean_flat]
    calculations['mean'] = mean_list
    
#variance calcs
    var_0 = np.var(calc_list, axis=0).tolist()
    var1 = np.var(calc_list, axis=1).tolist()
    var_flat = float(np.var(calc_list))
    var_list = [var_0, var1, var_flat]
    calculations['variance'] = var_list

#'standard deviation' calcs
    std0 = np.std(calc_list, axis=0).tolist()
    std1 = np.std(calc_list, axis=1).tolist()
    std_flat = float(np.std(calc_list))
    std_list = [std0, std1, std_flat]
    calculations['standard deviation'] = std_list

 #'max' calcs
    max0 = np.max(calc_list, axis=0).tolist()
    max1 = np.max(calc_list, axis=1).tolist()
    max_flat = float(np.max(calc_list))
    max_list = [max0, max1, max_flat]
    calculations['max'] = max_list

  #'min' calcs
    min0 = np.min(calc_list, axis=0).tolist()
    min1 = np.min(calc_list, axis=1).tolist()
    min_flat = float(np.min(calc_list))
    min_list = [min0, min1, min_flat]
    calculations['min'] = min_list

  #'sum' calcs
    sum0 = np.sum(calc_list, axis=0).tolist()
    sum1 = np.sum(calc_list, axis=1).tolist()
    sum_flat = float(np.sum(calc_list))
    sum_list = [sum0, sum1, sum_flat]
    calculations['sum'] = sum_list   
    
    return calculations
    
print(calculate([0,1,2,3,4,5,6,7,8]))