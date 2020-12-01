"""
   功能:运行主程序
"""
from app.appregister import webapp

if __name__ == "__main__":
    print(webapp.url_map)
    webapp.run()