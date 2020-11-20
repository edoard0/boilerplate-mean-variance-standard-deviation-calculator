import numpy as np

def calculate(list):
    
    if len(list)<9:
        raise ValueError("List must contain nine numbers.") 
    
    lst_reshaped=np.reshape(list,(3,3))

    means=[np.mean(lst_reshaped,axis=0).tolist(),np.mean(lst_reshaped,axis=1).tolist(),np.mean(np.array(list))]
    variances=[np.var(lst_reshaped,axis=0).tolist(),np.var(lst_reshaped,axis=1).tolist(),np.var(np.array(list))]
    sds=[np.std(lst_reshaped,axis=0).tolist(),np.std(lst_reshaped,axis=1).tolist(),np.std(np.array(list))]
    
    max_=[np.max(lst_reshaped,axis=0).tolist(),np.max(lst_reshaped,axis=1).tolist(),np.max(np.array(list))]
    min_=[np.min(lst_reshaped,axis=0).tolist(),np.min(lst_reshaped,axis=1).tolist(),np.min(np.array(list))]
    sum_=[np.sum(lst_reshaped,axis=0).tolist(),np.sum(lst_reshaped,axis=1).tolist(),np.sum(np.array(list))]
    
    result_dict={"mean":means,
               "variance":variances,
               "standard deviation":sds,
               "max":max_,
               "min":min_,
               "sum":sum_}

    return result_dict
