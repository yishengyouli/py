from flask import Flask,Blueprint   

app = Flask(__name__)

from user.views import user_bp
from item.views import item_bp
# 注册蓝图
app.register_blueprint(user_bp,url_prefix='/user')
app.register_blueprint(item_bp)

if __name__ == '__main__':
    app.run(debug=True)