# app.py
# 主app文件，运行文件
from flask import Flask
from flask_migrate import Migrate
from controller import ar
import configs
from exts import db


def create_app():

    app1 = Flask(__name__)

    # 注册蓝图
    app1.register_blueprint(ar, url_prefix='/ar')

    # 加载配置文件
    app1.config.from_object(configs)
    # db绑定app
    db.init_app(app1)

    # 要让Flask-Migrate能够管理app中的数据库，需要使用Migrate(app,db)来绑定app和数据库。假如现在有以下app文件
    # 绑定app和数据库
    migrate = Migrate(app=app1, db=db)
    return app1


app = create_app()
#app.run()
# @app.route('/')
# def hello_world():
#     return 'Hello World!'

#
# @app.route('/ar/add_anchor', methods=["GET", "POST"])
# def add_anchor():
#     json_data = ''
#     if request.method == "GET":
#         json_data = request.args.get("content")
#     if request.method == "POST":
#         if request.content_type.startswith('application/json'):
#             json_data = request.get_json()
#             # application/json 获取的原始参数，接受的是type是'bytes’的对象，如：b{'name':'lucy', 'age':22}
#             # data = request.get_data()
#         elif request.content_type.startswith('multipart/form-data'):
#             json_data = request.form.get('content')
#         else:
#             json_data = request.values.get("content")
#
#     anchors = json_data["collection"]
#     anchor = anchors[0]
#     anchor = json.dumps(anchor)
#     db.session.execute(models.GeoHistory.__table__.insert(), anchors)  # SQLAlchemy Core
#     db.session.commit()
#     # objects = [
#     #     models.ARUser(name="u1"),
#     #     models.ARUser(name="u2"),
#     #     models.ARUser(name="u3")]
#     # db.session.add_all(anchors)
#     # db.session.commit()
#
#     return R.ok(data=None)

#
# @app.route('/ar/nearby')
# def nearby():
#     latitude1 = float(request.args.get('latitude'))
#     longitude = float(request.values.get('longitude'))
#     histories = models.GeoHistory.query.filter(models.GeoHistory.latitude.between(latitude1 - 100, latitude1 + 100)).limit(
#         20).all()
#
#     result = o2d.obj_to_list(histories)
#     return R.ok(result)


if __name__ == '__main__':
    #app = create_app()
    app.run()
