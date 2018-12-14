from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from appdata.models import User, Alu


def login_port(request):
    print(request.GET.get('error'))
    if request.GET.get('error'):
        error='检查用户名与密码'
        print(error)
        return render(request, 'main/Signin.html', {'error':error})

    return render(request, 'main/Signin.html')

# def formimage():
#     from pyecharts import Bar
#     for i in range(100):
#         attr = ["一批", "二批", "艺术", "体育", "专科"]  # 这样X坐标就是星期
#         v1 = [i, 488, 340, 340, 150]
#         v2 = [532, 432, 300, 300, 150]
#         bar = Bar("成绩情况总览", "本图表展示过去一周的ABC情况")  # 这里是主标题和副标题
#         bar.add("文科", attr, v1, mark_line=["average"], mark_point=["max", "min"])  # 每一个值的名称以及要展现平均值和最大最小值
#         bar.add("理科", attr, v2, mark_line=["average"], mark_point=["max", "min"])
#         bar.render('templates/main/1.html')


def login_logic(request):
    # 输入用户名与密码 显示对应数据库的数据
    u = request.POST.get('username')
    p = request.POST.get('password')
    print('logic')
    if User.objects.filter(username=u,password=p):
        print('fresh')
        return render(request,'main/Signin2.html')
    else:
        print('er')
        request.session['error'] = '输入错误请检查用户名与密码'
        return redirect('main:login')
co=0
def show(request):
    global co
    print('in show.....',co)
    co+=1
    re = Alu.objects.all().order_by('-amount').values()
    size1 = []
    amount1 = []
    for i in re:
        print(i['amount'])
        if i['amount'] != '0':
            size1.append(int(i['amount']))
            amount1.append(i['size'])
    print(size1, amount1)
    # bar = Bar('数量总览', 'buffering')
    # bar.add('data', amount1, size1, mark_line=['average'], mark_point=['max', 'min'])
    # bar.render('templates/main/1.html')
    re = [size1,amount1]
    return JsonResponse(re,safe=False)
    # render(request, 'main/1.html')

def show_diagram(request):
    print('show diagram index',co)
    # return render(request, 'main/1.html')

def reset(request):
    #重置数据
    # r=Alu.objects.all().update('amount','0')
    re = Alu.objects.all()

    for i in re:
        i.amount='0'
        i.save()
    print(Alu.objects.all().values('amount'))
    return JsonResponse('reset')
