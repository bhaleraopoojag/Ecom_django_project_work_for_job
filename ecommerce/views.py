
from django.contrib.auth import authenticate, login,get_user_model
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .forms import ContactForm
from accounts.views import LoginView,RegisterView,logout_req #,register_page,,login_page



def home_page(request):

    # print(request.session.get("first_name","Unknown"))  #getter in session
    # request.session['first_name']
    context={
        "title":"This the basic home page",
        "content":"Welcome to the home page",
    }
    if request.user.is_authenticated:
        context['premium_content']="YEAH"
    return render(request,'home_page.html',context)

def about_page(request):
    context={
        "headline":"This is the heading of about page",
        "content":"Welcome to the about page"
    }
    return render(request,'about_page.html',context=context)

def contact_page(request):

    contact_form=ContactForm(request.POST or None)
    context={
        "heading":"This is last page i.e contact_page",
        "content":"Welcome to the contact page",
        "form":contact_form,
        
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse({"message":"Thank you for your submission"})
        
    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return HttpResponse(errors,status=400,content_type='application/json')
        
    # if request.method=="POST":
    #     print(request.POST)
    #     print(request.POST.get('full_name'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request,'contact/views.html',context=context)




# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     # redirect_path = next_ or next_post or None
#     if form.is_valid():
#         username  = form.cleaned_data.get("username")
#         password  = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/home")
#         else:
#             # Return an 'invalid login' error message.
#             print("Error")
#     return render(request, "auth/login.html", context)


# User=get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         print(form.cleaned_data)
#         username=form.cleaned_data.get("username")
#         email=form.cleaned_data.get("email")
#         password=form.cleaned_data.get("password")
#         new_user=User.objects.create_user(username,email,password)
#         print(new_user)
#     return render(request, "auth/register.html", context)

def home_page_old(request):
    html_="""

        <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
  <div class='text-center'>
    <h1>Hello, world!</h1>
   </div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
  </body>
</html>

"""
    return HttpResponse(html_)
