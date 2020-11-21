import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    # return HttpResponse("welcome")
    return render(request, 'home.html', context={'title': '我的测试页面', 'name': '你好，世界'})


def login(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    if username == 'admin' and pwd == '123456':
        return render(request,'home.html',context={'msg':'恭喜登录成功'})
    return render(request, 'home.html', context={'msg': '用户名或密码错误'})
    # '''
    # 请求方法：post
    # 参数类型：json
    # :param request:
    # :return:
    # '''
    #
    # if request.method == 'POST':
    #     try:
    #         data = json.loads(request.body)
    #     except json.decoder.JSONDecodeError:
    #         return HttpResponse('json解析错误')
    #
    #     try:
    #         username = data['username']
    #         pwd = data['pwd']
    #     except KeyError:
    #         return HttpResponse('参数为空')
    #
    #     else:
    #         if username=='admin' and pwd=='123':
    #             return render(request,'home.html',context={'msg':'恭喜登录成功'})
    #         else:
    #             return render(request, 'login.html', context={'msg': '用户名或密码错误'})
    # else:
    #     return HttpResponse('request method error')

