import sys
import pandas as pd
from catboost import CatBoostClassifier

# prof dict
target_dict = {'Прочее': 0, 'Экономика и управление': 1, 'Техника и технологи': 2, 'Образование и педагогика': 3,
               'Здравоохранение': 4,
               'Культура и искусство': 5, 'Гуманитарные и социальные науки': 6, 'Юридические науки': 7,
               'Естественные науки и метематика': 8, 'Сельское и рыбное хозяйство': 9}

# get id
id = int(sys.argv[1])

# get id data
data = pd.read_csv("results/model_user_info.csv", encoding='cp1251', sep=';')

# predict
cb = CatBoostClassifier()
cb = cb.load_model("results/cb_model")
prediction = cb.predict(data[data.uid == id].drop('uid', 1))[0][0]
prediction_prof = list(target_dict.keys())[list(target_dict.values()).index(prediction)]

# return result
print(prediction_prof)
