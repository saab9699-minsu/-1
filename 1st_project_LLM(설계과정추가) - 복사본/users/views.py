from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from users.forms import PostForm, LoginForm, SignupForm
from users.models import Post, User

# Create your views here.

# 건의사항 페이지
def feedback(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user_id = request.user
            feedback.save()
    else:
        form = PostForm()

    feedbacks = Post.objects.all()
    context = {
        "feedbacks": feedbacks,
        "form" : form,
    }
    return render(request, "feedback.html", context)

# 건의사항 삭제
def feedback_delete(request, feedback_id):
    Post.objects.filter(id=feedback_id).delete()
    return redirect("users:feedback")

# 건의사항 수정
def feedback_edit(request, feedback_id):
    feedback = get_object_or_404(Post, id = feedback_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=feedback)
        if form.is_valid():
            feedback = form.save(commit = False)
            feedback.save()
            return redirect("users:feedback")
        
    else:
        form = PostForm(instance = feedback) # 수정 대상이 될 데이터를 설정
    return render(request, "feedback_edit.html", {"form" : form})

def login_view(request):
    # 이미 로그인되어 있는 경우
    if request.user.is_authenticated:
        return redirect("cafe:main")
    
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("cafe:main")

            else:
                form.add_error(None, "해당하는 사용자가 없습니다")

        context = {
            "form": form,
        }
        return render(request, "login.html", context)

    else:
        form = LoginForm()

        context = {
            "form": form,
        }
        return render(request, "login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect("users:login")

def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:login")
    
    else:
        form = SignupForm()

    context = {"form" : form}
    return render(request, "signup.html", context)