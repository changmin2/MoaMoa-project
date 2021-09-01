
from tensorflow.keras.models import load_model
import joblib
from control.user_crud import User

User.truncate()

cabbage_model = load_model('moamoa_web/model/price_model/cabbage.h5')
daikon_model = load_model('moamoa_web/model/price_model/daikon.h5')
leaf_model = load_model('moamoa_web/model/price_model/leaf.h5')
lettuce_model = load_model('moamoa_web/model/price_model/lettce.h5')
onion_model = load_model('moamoa_web/model/price_model/onion.h5')

lettuce_strain = joblib.load('moamoa_web/model/scaler_model/lettuce_strain.pkl')
daikon_strain = joblib.load('moamoa_web/model/scaler_model/daikon_strain.pkl')
leaf_strain = joblib.load('moamoa_web/model/scaler_model/leaf_strain.pkl')
onion_strain = joblib.load('moamoa_web/model/scaler_model/onion_strain.pkl')

#오늘기온
mean_temp=28
min_temp=24
max_temp=31
rain=0
mean_wind=1
max_wind=2.5

#내일기온
mean_temp2=27
min_temp2=24
max_temp2=29
rain2=2
mean_wind2=1
max_wind2=2

#모레기온
mean_temp3=28
min_temp3=23
max_temp3=31
rain3=0
mean_wind3=1
max_wind3=5

#다음주기온
mean_temp4=25
min_temp4=21
max_temp4=29
rain4=0
mean_wind4=1
max_wind4=3

# 배추
#오늘
cabbage_total=272
cabbage_last_total=408.4
cabbage_last_price=11258
cabbage_income = 7
#내일
cabbage_last_total2=552.4
cabbage_last_price2=11843
#모레
cabbage_last_total3=272
cabbage_last_price3=15398

# 상추
#오늘
lettuce_total=30.3
lettuce_last_total=57.5
lettuce_last_price=35542
lettuce_income = 50
#내일
lettuce_last_total2=82.8
lettuce_last_price2=31042
#모레
lettuce_last_total3=30.3
lettuce_last_price3=27043

# 양파
#오늘
onion_total=561
onion_last_total=774.8
onion_last_price=10925
onion_income = 1500
#내일
onion_last_total2=604.6
onion_last_price2=10861
#모레
onion_last_total3=561
onion_last_price3=10005

# 무
#오늘
daikon_total=452.4
daikon_last_total=355.6
daikon_last_price=11368
daikon_income = 136
#내일
daikon_last_total2=393
daikon_last_price2=13641
#모레
daikon_last_total3=764.4
daikon_last_price3=14984

# 깻잎
#오늘
leaf_total=36.1
leaf_last_total=54.1
leaf_last_price=32668
leaf_income = 0
#내일
leaf_last_total2=54.1
leaf_last_price2=11478
#모레
leaf_last_total3=36.1
leaf_last_price3=11478

cabbage_trade = joblib.load('moamoa_web/model/trade_model/trade_cabbage.pkl')
daikon_trade = joblib.load('moamoa_web/model/trade_model/trade_daikon.pkl')
leaf_trade = joblib.load('moamoa_web/model/trade_model/trade_leaf.pkl')
lettuce_trade = joblib.load('moamoa_web/model/trade_model/trade_lettuce.pkl')
onion_trade = joblib.load('moamoa_web/model/trade_model/trade_onion.pkl')

# 오늘가격예측
#배추
price_cabbage=cabbage_model.predict([[[mean_temp],[min_temp],[max_temp],[rain],[mean_wind],[cabbage_total],[cabbage_last_price]]])
#무
daikon=daikon_strain.transform([[mean_temp,min_temp,max_temp,rain,mean_wind,daikon_total,daikon_last_total,daikon_last_price]])
daikon = daikon.reshape(daikon.shape[0],8,1)
price_daikon=daikon_model.predict(daikon)
#깻잎
leaf=leaf_strain.transform([[mean_temp,min_temp,max_temp,rain,mean_wind,leaf_total,leaf_last_price]])
leaf = leaf.reshape(leaf.shape[0],7,1)
price_leaf = leaf_model.predict(leaf)
#상추
lettuce=lettuce_strain.transform([[mean_temp,min_temp,max_temp,mean_wind,rain,lettuce_total,lettuce_last_total,lettuce_last_price]])
lettuce=lettuce.reshape(lettuce.shape[0],8,1)
price_lettuce = lettuce_model.predict(lettuce)
#양파
onion=onion_strain.transform([[mean_temp,min_temp,max_temp,mean_wind,rain,onion_total,onion_last_total,onion_last_price]])
onion=onion.reshape(onion.shape[0],8,1)
price_onion = onion_model.predict(onion)

# 오늘거래량예측
trade_cabbage=cabbage_trade.predict([[cabbage_income,max_temp,min_temp,rain,mean_wind,max_wind]])
trade_daikon=daikon_trade.predict([[daikon_income,max_temp,min_temp,rain,mean_wind,max_wind]])
trade_leaf=leaf_trade.predict([[max_temp,min_temp,rain,mean_wind,max_wind]])
trade_lettuce=lettuce_trade.predict([[lettuce_income,max_temp,min_temp,rain,mean_wind,max_wind]])
trade_onion=onion_trade.predict([[max_temp,min_temp,rain,mean_wind,max_wind]])

# 내일가격예측
#배추
price_cabbage2=cabbage_model.predict([[[mean_temp2],[min_temp2],[max_temp2],[rain2],[mean_wind2],[cabbage_total],[cabbage_last_price2]]])
#무
daikon=daikon_strain.transform([[mean_temp2,min_temp2,max_temp2,rain2,mean_wind2,daikon_total,daikon_last_total2,daikon_last_price2]])
daikon = daikon.reshape(daikon.shape[0],8,1)
price_daikon2=daikon_model.predict(daikon)
#깻잎
leaf=leaf_strain.transform([[mean_temp2,min_temp2,max_temp2,rain2,mean_wind2,leaf_total,leaf_last_price2]])
leaf = leaf.reshape(leaf.shape[0],7,1)
price_leaf2 = leaf_model.predict(leaf)
#상추
lettuce=lettuce_strain.transform([[mean_temp2,min_temp2,max_temp2,mean_wind2,rain2,lettuce_total,lettuce_last_total2,lettuce_last_price2]])
lettuce=lettuce.reshape(lettuce.shape[0],8,1)
price_lettuce2 = lettuce_model.predict(lettuce)
#양파
onion=onion_strain.transform([[mean_temp2,min_temp2,max_temp2,mean_wind2,rain2,onion_total,onion_last_total2,onion_last_price2]])
onion=onion.reshape(onion.shape[0],8,1)
price_onion2 = onion_model.predict(onion)
# 내일거래량예측
trade_cabbage2=cabbage_trade.predict([[cabbage_income,max_temp2,min_temp2,rain2,mean_wind2,max_wind2]])
trade_daikon2=daikon_trade.predict([[daikon_income,max_temp2,min_temp2,rain2,mean_wind2,max_wind2]])
trade_leaf2=leaf_trade.predict([[max_temp2,min_temp2,rain2,mean_wind2,max_wind2]])
trade_lettuce2=lettuce_trade.predict([[lettuce_income,max_temp2,min_temp2,rain2,mean_wind2,max_wind2]])
trade_onion2=onion_trade.predict([[max_temp2,min_temp2,rain2,mean_wind2,max_wind2]])

# 모레가격예측
#배추
price_cabbage3=cabbage_model.predict([[[mean_temp3],[min_temp3],[max_temp3],[rain3],[mean_wind3],[cabbage_total],[cabbage_last_price3]]])
#무
daikon=daikon_strain.transform([[mean_temp3,min_temp3,max_temp3,rain3,mean_wind3,daikon_total,daikon_last_total3,daikon_last_price3]])
daikon = daikon.reshape(daikon.shape[0],8,1)
price_daikon3=daikon_model.predict(daikon)
#깻잎
leaf=leaf_strain.transform([[mean_temp3,min_temp3,max_temp3,rain3,mean_wind3,leaf_total,leaf_last_price3]])
leaf = leaf.reshape(leaf.shape[0],7,1)
price_leaf3 = leaf_model.predict(leaf)
#상추
lettuce=lettuce_strain.transform([[mean_temp3,min_temp3,max_temp3,mean_wind3,rain3,lettuce_total,lettuce_last_total3,lettuce_last_price3]])
lettuce=lettuce.reshape(lettuce.shape[0],8,1)
price_lettuce3 = lettuce_model.predict(lettuce)
#양파
onion=onion_strain.transform([[mean_temp3,min_temp3,max_temp3,mean_wind3,rain3,onion_total,onion_last_total3,onion_last_price3]])
onion=onion.reshape(onion.shape[0],8,1)
price_onion3 = onion_model.predict(onion)
# 모레거래량예측
trade_cabbage3=cabbage_trade.predict([[cabbage_income,max_temp3,min_temp3,rain3,mean_wind3,max_wind3]])
trade_daikon3=daikon_trade.predict([[daikon_income,max_temp3,min_temp3,rain3,mean_wind3,max_wind3]])
trade_leaf3=leaf_trade.predict([[max_temp3,min_temp3,rain3,mean_wind3,max_wind3]])
trade_lettuce3=lettuce_trade.predict([[lettuce_income,max_temp3,min_temp3,rain3,mean_wind3,max_wind3]])
trade_onion3=onion_trade.predict([[max_temp3,min_temp3,rain3,mean_wind3,max_wind3]])

# 다음주가격예측
#배추
price_cabbage4=cabbage_model.predict([[[mean_temp4],[min_temp4],[max_temp4],[rain4],[mean_wind4],[cabbage_total],[price_cabbage[0][0]]]])
#무
daikon=daikon_strain.transform([[mean_temp4,min_temp4,max_temp4,rain4,mean_wind4,daikon_total,trade_daikon[0],price_daikon[0][0]]])
daikon = daikon.reshape(daikon.shape[0],8,1)
price_daikon4=daikon_model.predict(daikon)
#깻잎
leaf=leaf_strain.transform([[mean_temp4,min_temp4,max_temp4,rain4,mean_wind4,leaf_total,price_leaf[0][0]]])
leaf = leaf.reshape(leaf.shape[0],7,1)
price_leaf4 = leaf_model.predict(leaf)
#상추
lettuce=lettuce_strain.transform([[mean_temp4,min_temp4,max_temp4,mean_wind4,rain4,lettuce_total,trade_lettuce[0],price_lettuce[0][0]]])
lettuce=lettuce.reshape(lettuce.shape[0],8,1)
price_lettuce4 = lettuce_model.predict(lettuce)
#양파
onion=onion_strain.transform([[mean_temp4,min_temp4,max_temp4,mean_wind4,rain4,onion_total,trade_onion[0],price_onion[0][0]]])
onion=onion.reshape(onion.shape[0],8,1)
price_onion4 = onion_model.predict(onion)
# 다음주거래량예측
trade_cabbage4=cabbage_trade.predict([[cabbage_income,max_temp4,min_temp4,rain4,mean_wind4,max_wind4]])
trade_daikon4=daikon_trade.predict([[daikon_income,max_temp4,min_temp4,rain4,mean_wind4,max_wind4]])
trade_leaf4=leaf_trade.predict([[max_temp4,min_temp4,rain4,mean_wind4,max_wind4]])
trade_lettuce4=lettuce_trade.predict([[lettuce_income,max_temp4,min_temp4,rain4,mean_wind4,max_wind4]])
trade_onion4=onion_trade.predict([[max_temp4,min_temp4,rain4,mean_wind4,max_wind4]])

User.product('배추',price_cabbage[0][0],round(trade_cabbage[0],2),price_cabbage2[0][0],round(trade_cabbage2[0],2),price_cabbage3[0][0],round(trade_cabbage3[0],2),price_cabbage4[0][0],round(trade_cabbage4[0],2))
User.product('무',price_daikon[0][0],round(trade_daikon[0],2),price_daikon2[0][0],round(trade_daikon2[0],2),price_daikon3[0][0],round(trade_daikon3[0],2),price_daikon4[0][0],round(trade_daikon4[0],2))
User.product('양파',price_onion[0][0],round(trade_onion[0],2),price_onion2[0][0],round(trade_onion2[0],2),price_onion3[0][0],round(trade_onion3[0],2),price_onion4[0][0],round(trade_onion4[0],2))
User.product('깻잎',price_leaf[0][0],round(trade_leaf[0],2),price_leaf2[0][0],round(trade_leaf2[0],2),price_leaf3[0][0],round(trade_leaf3[0],2),price_leaf4[0][0],round(trade_leaf4[0],2))
User.product('상추',price_lettuce[0][0],round(trade_lettuce[0],2),price_lettuce2[0][0],round(trade_lettuce2[0],2),price_lettuce3[0][0],round(trade_lettuce3[0],2),price_lettuce4[0][0],round(trade_lettuce4[0],2))


