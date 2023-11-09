from app import app, db
if __name__ == '__main__': #如果以主程式執行
    # with app.app_context():
    #     db.create_all()
    app.run(host="localhost",port=8000,debug=True)  #立即啟動伺服器
