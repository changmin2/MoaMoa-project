from flask_login import login_user,current_user,logout_user
from flask import Flask, Blueprint,request,redirect,url_for
from flask.templating import render_template
from control.user_crud import User
import datetime
from control.crawling import crawling
from control.weather import weather
from control.policy import policy
from control.naver import kakao_crawling

moa_notice = Blueprint('moa',__name__)
# 모아모아

@moa_notice.route('/get_find')
def get_find():
    temp = request.args.get('vegetable')
    url = 'https://www.yna.co.kr/search/index?query='+temp
    return redirect(url)

@moa_notice.route('/subcribe')
def subcribe():
    return render_template('contact.html')

@moa_notice.route('/register',methods=['POST'])
def register():
    
    user = User.create(request.form['user_name'],request.form['user_email'],request.form['user_location'],request.form['user_product'])
    login_user(user,remember=True,duration=datetime.timedelta(days=365))
    return redirect('/moa/no_subcribe')

@moa_notice.route('/history')
def history():
    return render_template('history.html')

@moa_notice.route('/howmuch')
def howmuch():
    cabbage=User.predict('배추')
    onion=User.predict('양파')
    daikon=User.predict('무')
    lettuce=User.predict('상추')
    leaf=User.predict('깻잎')
    return render_template('howmuch.html',cabbage_today=cabbage[0][1],cabbage_tomorrow=cabbage[0][3],cabbage_toto=cabbage[0][5] ,cabbage_next=cabbage[0][7],
    onion_today=onion[0][1],onion_tomorrow=onion[0][3],onion_toto=onion[0][5] ,onion_next=onion[0][7],
    daikon_today=daikon[0][1],daikon_tomorrow=daikon[0][3],daikon_toto=daikon[0][5] ,daikon_next=daikon[0][7],
     lettuce_today=lettuce[0][1],lettuce_tomorrow=lettuce[0][3],lettuce_toto=lettuce[0][5] ,lettuce_next=lettuce[0][7],
     leaf_today=leaf[0][1], leaf_tomorrow=leaf[0][3], leaf_toto=leaf[0][5] , leaf_next=leaf[0][7])

@moa_notice.route('/where')
def where():
    return render_template('where.html')


@moa_notice.route('/what')
def what():
    cabbage=User.predict('배추')
    onion=User.predict('양파')
    daikon=User.predict('무')
    lettuce=User.predict('상추')
    leaf=User.predict('깻잎')
    return render_template('what.html',cabbage_today=cabbage[0][2],cabbage_tomorrow=cabbage[0][4],cabbage_toto=cabbage[0][6] ,cabbage_next=cabbage[0][8],
    onion_today=onion[0][2],onion_tomorrow=onion[0][4],onion_toto=onion[0][6] ,onion_next=onion[0][8],
    daikon_today=daikon[0][2],daikon_tomorrow=daikon[0][4],daikon_toto=daikon[0][6] ,daikon_next=daikon[0][8],
     lettuce_today=lettuce[0][2],lettuce_tomorrow=lettuce[0][4],lettuce_toto=lettuce[0][6] ,lettuce_next=lettuce[0][8],
     leaf_today=leaf[0][2], leaf_tomorrow=leaf[0][4], leaf_toto=leaf[0][6] , leaf_next=leaf[0][8])

@moa_notice.route('/farmer')
def farmer():
    return render_template('farmer.html')

@moa_notice.route('/no_where',methods=['POST'])
def no_where():
    cabbage=User.predict('배추')
    oil = 1644
    product = request.form['product']
    cost = request.form['cost']
    total = request.form['total']
    start = request.form['start']
    end = request.form['end']
    predict=User.predict(product)
    distance = kakao_crawling(start,end)
    result = (int(total) * float(predict[0][1])+ int(distance)*oil+int(cost))/int(total)
    return render_template('where_no.html',result = round(result,2),cabbage_today=cabbage[0][1],cabbage_tomorrow=cabbage[0][3],cabbage_toto=cabbage[0][5] ,cabbage_next=cabbage[0][7])

@moa_notice.route('/write')
def write():
    return render_template('write.html')

@moa_notice.route('/minicalc_ok',methods=['POST'])
def miniclac_ok():
    oil = 1644
    vegetable = request.form['vegetable']
    cost = request.form['cost']
    total = request.form['total']
    start = request.form['start']
    end = request.form['end']
    predict=User.predict(vegetable)
    distance = kakao_crawling(start,end)
    result = (int(total) * float(predict[0][1])+ int(distance)*oil+int(cost))/int(total)
    return render_template('miniCalc_ok.html',result=result)


@moa_notice.route('/minicalc')
def minicalc():
    return render_template('miniCalc.html')

@moa_notice.route('/get_email')
def get_email():
    get = User.all_email()
    print(get[0])
    return render_template('test.html',get=get)

@moa_notice.route('/logout')
def user_logout():
    User.delete(current_user.id)
    logout_user()
    return redirect('/moa/no_subcribe')

@moa_notice.route('/no_subcribe')
def no_subcribe():
    cabbage=User.predict('배추')
    onion=User.predict('양파')
    daikon=User.predict('무')
    lettuce=User.predict('상추')
    leaf=User.predict('깻잎')
    temp,last,temp_min,temp_max,chegam,mise = weather('서울')
    weather_ = last.split(',')
    mood1=weather_[0].lstrip()
    policy_list,href_policy=policy()
    news_list,href_list=crawling()
    if current_user.is_authenticated:
        location = current_user.user_location
        temp,last,temp_min,temp_max,chegam,mise = weather(location)
        weather2_=last.split(',')
        mood2 = weather2_[0].lstrip()
        return render_template('main_page.html',temperature = temp, last=last,temp_min=temp_min,temp_max=temp_max,chegam=chegam,mise=mise
        ,policy_list=policy_list,href_policy=href_policy,news_list=news_list,href_list=href_list,user_location=current_user.user_location,mood=mood2,
        cabbage_today=cabbage[0][1],cabbage_tomorrow=cabbage[0][3],cabbage_toto=cabbage[0][5] ,cabbage_next=cabbage[0][7],
    onion_today=onion[0][1],onion_tomorrow=onion[0][3],onion_toto=onion[0][5] ,onion_next=onion[0][7],
    daikon_today=daikon[0][1],daikon_tomorrow=daikon[0][3],daikon_toto=daikon[0][5] ,daikon_next=daikon[0][7],
     lettuce_today=lettuce[0][1],lettuce_tomorrow=lettuce[0][3],lettuce_toto=lettuce[0][5] ,lettuce_next=lettuce[0][7],
     leaf_today=leaf[0][1], leaf_tomorrow=leaf[0][3], leaf_toto=leaf[0][5] , leaf_next=leaf[0][7])
    else:
        return render_template('no_main_page.html',temperature = temp, last=last,temp_min=temp_min,temp_max=temp_max,chegam=chegam,mise=mise
        ,policy_list=policy_list,href_policy=href_policy,news_list=news_list,href_list=href_list,mood=mood1,
        cabbage_today=cabbage[0][1],cabbage_tomorrow=cabbage[0][3],cabbage_toto=cabbage[0][5] ,cabbage_next=cabbage[0][7],
    onion_today=onion[0][1],onion_tomorrow=onion[0][3],onion_toto=onion[0][5] ,onion_next=onion[0][7],
    daikon_today=daikon[0][1],daikon_tomorrow=daikon[0][3],daikon_toto=daikon[0][5] ,daikon_next=daikon[0][7],
     lettuce_today=lettuce[0][1],lettuce_tomorrow=lettuce[0][3],lettuce_toto=lettuce[0][5] ,lettuce_next=lettuce[0][7],
     leaf_today=leaf[0][1], leaf_tomorrow=leaf[0][3], leaf_toto=leaf[0][5] , leaf_next=leaf[0][7])


