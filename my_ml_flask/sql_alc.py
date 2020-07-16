

import pandas as pd
from sqlalchemy import create_engine
from sklearn.externals import joblib

filename = '/Users/Vera/Downloads/final_logreg_model.sav'

loaded_model = joblib.load(filename)


engine = create_engine('sqlite:////appdata.sqlite')



def data_for_gender_prediction(id):
    ex = engine.execute('''SELECT * FROM session_views 
                   WHERE session_id == ( ? )''',(id,)).fetchall()
    if ex is not None:
       ex1=list()
       j=0
       for it in ex:
          ex1.append(list())
          for i in range(2,6):
              ex1[j].append(int(it[i].lstrip('ABCD')))
          j=j+1
       return ex1
    else: return None
    
          

def predict_function(ex_data): 
   if ex_data is not None :
      pred_ex=loaded_model.predict(ex_data)
      count_1=0
      count_0=0
      for b in pred_ex:
          if b==0:
              count_0=count_0+1
          else:
              count_1=count_1+1

      if count_0>count_1:
            gender_ex='male'
      else:
            gender_ex='female'
      return gender_ex
   else : return None
   
   
def find_data(id, par):
    ex = list(engine.execute('''SELECT * FROM categories 
                   WHERE session_id == ( ? )''',(id,)).fetchall()[0])
    if ex is None : 
        return -1
    else : 
        if int(par)==1 :
          return ex
        elif int(par)==2 :
          tot = ex[1]+ex[2]+ex[3]+ex[4]
          for i in range(1,5):
             ex[i]=ex[i]/tot
          return ex
        else: return None
 
           


