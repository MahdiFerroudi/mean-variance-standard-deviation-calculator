import numpy as np


def calculate(list):
  try :
    shaped_list = np.array(list).reshape(3,3)
    List_transposed=np.matrix.transpose(shaped_list)
      
    ls_mean=[]
    lt_mean=[]
    ls_var=[]
    lt_var=[]
    ls_std=[]
    lt_std=[]
    ls_max=[]
    lt_max=[]
    ls_min=[]
    lt_min=[]
    ls_sum=[]
    lt_sum=[]
    for i in range(0,3) : 
                
      #mean
      ls_mean.append(shaped_list[i].mean())
      lt_mean.append(List_transposed[i].mean())
                             
      #variance
      ls_var.append(shaped_list[i].var()) 
      lt_var.append(List_transposed[i].var())
                        
               
      #standard deviation
      ls_std.append(shaped_list[i].std())
      lt_std.append(List_transposed[i].std())
                        
      
      #max
      ls_max.append(shaped_list[i].max())
      lt_max.append(List_transposed[i].max())
                        
      #min
      ls_min.append(shaped_list[i].min())
      lt_min.append(List_transposed[i].min())
                        
      #sum
      ls_sum.append(shaped_list[i].sum())
      lt_sum.append(List_transposed[i].sum())
  
    mean=[ls_mean]+[lt_mean]+[shaped_list[i].mean()]
    var=[ls_var]+[lt_var]+[shaped_list[i].var()]
    std=[ls_std]+[lt_std]+[shaped_list[i].std()]
    max=[ls_max]+[lt_max]+[shaped_list[i].max()]
    min=[ls_min]+[lt_min]+[shaped_list[i].min()]
    sum=[ls_sum]+[lt_sum]+[shaped_list[i].sum()]
  
    calculations={ 
           'mean' : mean ,
           'variance': var,
           'standard deviation': std,
           'max': max,
           'min': min,
           'sum': sum
    }
    
  
    return calculations
  except ValueError as err:
    print(err.args)
        