from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse("Hello, this is Login app!!!")


class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')

    def post(self, request):
        user_name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        my_user = authenticate(username=user_name, password=pwd)
        if my_user is None:
            return HttpResponse('Người dùng không tồn tại!!!')
        else:
            login(request, my_user)
            return HttpResponse("Chào mừng %s" % user_name)


class ViewUser(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return HttpResponse('Nếu view này hiện ra khi bạn chưa đăng nhập thì bạn sai, không thì bạn đúng')


@decorators.login_required(login_url='/login/')
def view_product(View):
    return HttpResponse("Trang này chỉ hiện ra khi bạn đã đăng nhập!!!")


class AddPost(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        f = PostForm()
        context = {'fm': f}
        return render(request, 'Login/add_post.html', context)

    def post(self, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse("Dữ liệu không hợp lệ")
        print(request.user.get_all_permissions())
        # Viết thường tên model
        if request.user.has_perm('Login.add_post'):
            f.save()
            return HttpResponse("Thêm thành công")
        else:
            return HttpResponse("Bạn không có quyền để thực hiện hành động này")