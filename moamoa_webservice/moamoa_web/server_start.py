from control.user_crud import User
from flask import Flask,jsonify,request,render_template,make_response
from flask_login import LoginManager,current_user, login_manager,login_required,login_user,logout_user
from flask_cors import CORS
import os
from view import notice
from control.user_crud import User

os.environ['QAUTHLIB_INSECURE_TRANSPORT']='1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key='moa_server'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
app.register_blueprint(notice.moa_notice,url_prefix='/moa')

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.unauthorized_handler #login이 안된 사용자가 login이 된 사용자만 접근할 수 있는 api들을 리퀘스트 했을 경우 에러를 내면서 호출
def umauthorized():
    return make_response(jsonify(success=False),401)

if __name__ =='__main__':
    app.run()

