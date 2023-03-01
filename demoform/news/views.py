from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import PostForm, SendEmail
from django.views import View


# Create your views here.


def index(request):
    return HttpResponse("""Hello user, It is the "news" app!!!""")


def add_post(request):
    a = PostForm()
    return render(request, 'news/add_post.html', {'f': a})


def save_post(request):
    # Nếu phương thức của request là POST thì mới xử lý
    if request.method == "POST":
        # Ép kiểu cái gửi lên thành một obj PostForm
        new_post = PostForm(request.POST)
        # Đúng lưu, sai cãi
        if new_post.is_valid():
            new_post.save()
            return HttpResponse("Lưu thành công!!!")
        else:
            return HttpResponse("Dữ liệu không hợp lệ!!!")
    else:
        return HttpResponse("Request ko hợp lệ!!!")


def email_view(request):
    se = SendEmail()
    return render(request, 'news/send_email.html', {'f': se})


def process(request):
    if request.method == "POST":
        e = SendEmail(request.POST)
        if e.is_valid():
            _title = e.cleaned_data['title']
            _email = e.cleaned_data['email']
            _content = e.cleaned_data['content']
            _cc = e.cleaned_data['cc']
            context = {"v_title": _title, "v_email": _email, "v_content": _content, "v_cc": _cc}
            return render(request, 'news/print_email.html', context)
        else:
            return HttpResponse("Form not validate")
    else:
        return HttpResponse("Request is invalid!!!")


class index_class(View):
     def get(self, request):
         return HttpResponse("Class base view test successfully!!")
