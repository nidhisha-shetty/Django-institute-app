from django.shortcuts import  render, redirect, get_object_or_404  		#render for "return render(request, "home.html", context)"
														#messages for "messages.info(request, "Password already taken")" 
														#redirect for "return redirect('http://127.0.0.1:8000/')"  
														# get_object_or_404 for "get_object_or_404(Student, id=pass_id)"


from django.contrib import messages
from django.http import HttpResponse              #for (home_view)return HttpResponse("<h1> Welcome to Python classes </h1>")
from .models import Student                       #for (student_details_view)s_object=Student.objects.get(id=3
from .forms import StudentForm					  #for (student_create_view)form = StudentForm(request.POST or None)

from django.contrib.auth.models import User, auth  #for (register_view) user=User.objects.create_user(username=u_n, password=pwd, email=email_id, first_name=f_n, last_name=l_n)

# Create your views here.

# def home_view( request):
# 	#print(args, kwargs)
# 	#print(request.user)
# 	return HttpResponse("<h1> Welcome to Python classes </h1>")
	


def home_view(request):
	context={}
	return render(request, "home.html", context)

def admin_home_view(request):
	return render(request, 'admin_home.html')

def student_details_view(request):
	s_object=Student.objects.all()
	context={'object':s_object}
	return render(request, "student_details.html", context)

def student_create_view(request):
	
	form = StudentForm(request.POST or None)
	
	
	if form.is_valid():
		form.save()
		form = StudentForm()
	

	
	context={
		'form':form
	}
	
	
	return render(request, "student_create.html", context)

def register_view(request):


	if request.method == 'POST':
		f_n=request.POST['first_name']
		l_n=request.POST['last_name']
		u_n=request.POST['username']
		email_id=request.POST['email']
		pwd=request.POST['password']
		cnf_pwd=request.POST['confirm password']

		if pwd==cnf_pwd:
			if User.objects.filter(username=u_n).exists():
				messages.info(request, "User name already taken")
				return redirect('register')
			elif User.objects.filter(email=email_id).exists():
				messages.info(request, "Email already taken")
				return redirect('register')
			else:
				user=User.objects.create_user(username=u_n, password=pwd, email=email_id, first_name=f_n, last_name=l_n)
				user.save()
				messages.info(request, "User sucessfully created") #for printing on UI
				print("user created")  #for printing on cmd prompt
				return redirect("register")

				
		else:
			print("Confirm password do not match password")
			messages.info(request, "Confirm password do not match password")
			return redirect('register')
		return redirect('/')
	else:
		return render(request, "register.html")
		messages.info(request, "Invalid credentials")


def login_view(request):
	if request.method == "POST":
		u_n=request.POST["username_l"]
		pwd=request.POST["password_l"]

		user = auth.authenticate(username=u_n, password=pwd)

		if user is not None:
			auth.login(request, user)
			return redirect("home")
		else:
			messages.info(request, "Invalid credentials")
			return redirect("login")
	else:
		return render(request, "login_view.html")



def logout_view(request):
	auth.logout(request)
	return redirect('/')



def loggedin_home(request):
	return render(request, "logged-in_home.html")



def student_detail_display_view(request, my_id):
	obj=Student.objects.get(id=my_id)
	obj=get_object_or_404(Student, id=my_id)

	context={
		'RollNo': obj.Student_Rollno,
		'Name': obj.Student_Name,
		'Class': obj.Student_Class,

	}	
	return render(request, "student_detail.html", context)


def render_initial_data(request, my_id):
	obj=Student.objects.get(id=my_id)

	form=StudentForm(request.POST or None, instance=obj)  #instance is used to dispaly data of each field from DB
	if form.is_valid():
		form.save()
		return redirect("/")
	context={
		"my_form": form,
		"object": obj
	}
	return render(request, "student_edit.html", context)

def student_delete_view(request, my_id):
	obj=get_object_or_404(Student, id=my_id)
	if request.method == "POST":
		obj.delete()
		return redirect("/")
	context={
		'object':obj
	}

	return render(request, "studnet_delete.html", context)

def student_details_delete_view(request):
	obj=Student.objects.all()
	context={
		'object':obj
	}
	return render(request, "student_list_delete.html", context)

def student_details_edit_view(request):
	obj=Student.objects.all()
	context={
		'object':obj
	}
	return render(request, "student_list_edit.html", context)

def student_view_details(request):
	obj=Student.objects.all()
	context={
		'object':obj
	}
	return render(request, "student_view_details.html", context)