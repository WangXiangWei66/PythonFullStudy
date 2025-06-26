from flask import Flask #Flask 应用的核心类，用于创建 Web 应用实例。
from flask_sqlalchemy import SQLAlchemy #Flask-SQLAlchemy 提供的数据库 ORM（对象关系映射）工具，简化数据库操作

# 创建Flask应用和数据库实例
app = Flask(__name__) #创建Flask应用实例，（__name__）是python模块名，用于定位资源
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # 使用SQLite数据库
db = SQLAlchemy(app)  #对数据库类型进行初始化

# 定义User模型  所有的SQLAlchey模型必须继承字db.Model
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True) #自动递增的整数类型
    user_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    introduction = db.Column(db.String(200))

# 创建数据库表（如果不存在）
with app.app_context():
    db.create_all()

# 添加测试数据（仅首次运行时需要）
with app.app_context():
    if not User.query.first():
        user = User(user_name='python', age=28, introduction='')
        db.session.add(user)
        db.session.commit()
        print("测试数据已添加")

# 查询用户并打印结果
with app.app_context():
    user = User.query.filter_by(user_id=1).first()
    if user:
        print(f"用户ID: {user.user_id}")
        print(f"用户名: {user.user_name}")
        print(f"年龄: {user.age}")
        print(f"简介: {user.introduction}")
    else:
        print("未找到用户")