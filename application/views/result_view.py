
import pickle
from flask import Blueprint, render_template, request

result_bp = Blueprint('result', __name__)

@result_bp.route('/result', methods=['POST'])
def post():
    if request.method == 'POST':
        temp = float(request.form['temp'])
        hum = float(request.form['hum'])
        wind_speed = float(request.form['wind_speed'])

        model = None
        with open('model.pkl','rb') as pickle_file:
            model = pickle.load(pickle_file)
        
        X_test = [[temp, hum, wind_speed]] 
        y_pred = model.predict(X_test)
        if y_pred <= 0 :
            link = 'https://mblogthumb-phinf.pstatic.net/MjAxNzA2MThfMTQ2/MDAxNDk3NzE2MDMwNzM0.IZClJepa3sExQZD8jwzWf1huXWSD_pyPwWtAWnPmZ7Qg.4ngGE3NCZsbjp3W5-mYgRwndXxj6AxL-W88yfZjON3kg.PNG.koowq/%EB%A7%91%EC%9D%8C_%EC%BB%AC%EB%9F%AC_%EC%95%84%EC%9D%B4%EC%BD%98-01.png?type=w800'
        elif y_pred <= 10 :
            link = 'https://mblogthumb-phinf.pstatic.net/MjAxNzA1MjNfMTc0/MDAxNDk1NTQ1MjM0MTUw.MZIUHLC1n4EoywXX9EXmAucKrlDG4uWhR6m1pbZ6eqUg.lsPo4rQwSjW1_gOFw05NyZWUJ9cCQgvfiSvuH2Huuicg.PNG.koowq/%EA%B5%AC%EB%A6%84%EC%A1%B0%EA%B8%88_%EC%BB%AC%EB%9F%AC_%EC%95%84%EC%9D%B4%EC%BD%98-01.png?type=w800'
        elif y_pred <= 50 : 
            link = 'https://mblogthumb-phinf.pstatic.net/MjAxNzA2MDNfMTgz/MDAxNDk2NDgxNjk5Njg0.qh1W_AYRIltQZkP6KrI2MmyaAZBpqtfO35HQasqvJJUg.133ikjo2KzwYeJH98qqXovvZq2kD1lhifw9Ccl7xKR8g.PNG.koowq/%EA%B5%AC%EB%A6%84_%EC%BB%AC%EB%9F%AC_%EC%95%84%EC%9D%B4%EC%BD%98-01.png?type=w800'
        else :
            link = 'https://mblogthumb-phinf.pstatic.net/MjAxNzA2MjlfMTgy/MDAxNDk4NjYzODE2NTU5.xAdrH2mM1pZXLvX_6O7sfQUY-ICurTYvx-DYtYJ6fiMg.S-ZhPx3r9DfiUbM-vUKrUSaN8vpuqKMKnS7YC5CNbdMg.PNG.koowq/%EB%B9%84%EA%B5%AC%EB%A6%84_%EC%BB%AC%EB%9F%AC_%EC%95%84%EC%9D%B4%EC%BD%98-01.png?type=w800'

    return render_template('result.html', predict = y_pred.round(1), link = link), 200