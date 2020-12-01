"""
   功能：文件上传处理api

"""
from flask import Blueprint, request,send_from_directory
from common import config
import pandas as pd
import os
import uuid
from common.reponsedata import InvalidUsage


file_api = Blueprint('file', __name__)



@file_api.route('/register')
def upload_file():
    raise InvalidUsage("333333",status_code=500)

@file_api.route('/uploadFile', methods = ['POST'])
def uploadFile():
   formdata=request.form["formdata"]
   print(formdata)
   f = request.files['file']
   unqId=uuid.uuid4()
   filepath= config.uploadfilepath + os.sep + str(unqId) + os.sep + f.filename
   f.save(filepath)
   #通过pandas读取文件
   if f.filename.endswith(".csv"):
      print("csv文件")
      dataframe = pd.read_csv(config.uploadfilepath + os.sep + f.filename)
      return dataframe.to_json(orient="split")
   elif f.filename.endswith(".xlsx") or f.filename.endswith(".xls"):
      print("excel文件")
      dataframe=pd.read_excel(config.uploadfilepath + os.sep + f.filename, header=int(header))
      return dataframe.to_json(orient="split")
   return 'file uploaded successfully'

@file_api.route("/download",methods=["GET",'POST'])
def download():
   return send_from_directory(config.uploadfilepath, filename="用户导入模板.xlsx", as_attachment=True)