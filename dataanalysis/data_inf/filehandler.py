"""
   功能：文件上传处理api

"""
from flask import Blueprint,render_template,request,send_from_directory
from dataanalysis import config
import pandas as pd
import os

file_api = Blueprint('file', __name__)




@file_api.route('/upload')
def upload_file():
   return render_template('uploadtest.html')

@file_api.route('/uploader', methods = ['POST'])
def uploader():
   header=request.form["header"]
   f = request.files['file']
   f.save(config.uploadfilepath+os.sep+f.filename)
   #通过pandas读取文件
   if f.filename.endswith(".csv"):
      print("csv文件")
      dataframe = pd.read_csv(config.uploadfilepath+os.sep+f.filename)
      return dataframe.to_json(orient="split")
   elif f.filename.endswith(".xlsx") or f.filename.endswith(".xls"):
      print("excel文件")
      dataframe=pd.read_excel(config.uploadfilepath + os.sep + f.filename,header=int(header))
      return dataframe.to_json(orient="split")
   return 'file uploaded successfully'

@file_api.route("/download",methods=["GET",'POST'])
def download():
   return send_from_directory(config.uploadfilepath, filename="用户导入模板.xlsx", as_attachment=True)