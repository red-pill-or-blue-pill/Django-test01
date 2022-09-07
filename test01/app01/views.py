from django.shortcuts import render
from django.http import HttpResponse
# application/write_data.pyをインポートする
from .application import write_data

# Create your views here.
def index(req):
    return render(req, 'index.html')

# ajaxでurl指定したメソッド
def call_write_data(req):
    if req.method == 'GET':
        # write_data.pyのwrite_csv()メソッドを呼び出す。
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        write_data.write_csv(req.GET.get("input_data"))

        # write_data.pyの中に新たに記述したメソッド(return_text())を呼び出す。
        data = write_data.return_text()
        # 受け取ったデータをhtmlに渡す。
        return HttpResponse(data)
