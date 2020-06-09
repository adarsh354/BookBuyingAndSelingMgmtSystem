from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import connection

def home_view(request, sem=0):
	if request.session.get('username') is None :
		request.session['username'] = 'NULL'
		context = {'user':request.session.get('username'), 'set':Books.objects.all(), 'sem':sem }
	elif request.session.get('username') == 'NULL':
		request.session['username'] = 'NULL'
		context = {'user':request.session.get('username'), 'set':Books.objects.all(), 'sem':sem }
	else:
		obj=Customer.objects.get(username=request.session.get('username'))
		context = {'user':request.session.get('username'), 'set':Books.objects.all(), 'sem':sem, 'objec':obj } 

	return render(request,"home.html",context)

def login_view(request):

	request.session['username'] = 'NULL'
	context = {'user':request.session.get('username') }
	if request.method == "POST":
		userid = request.POST.get('userid')
		request.session['username'] = userid
		print(userid)
		pwd = request.POST.get('pwd')
		print(pwd)
		queryset = Customer.objects.all()
		flag = 0
		for obj in queryset:
			if obj.username == userid :
				if obj.password == pwd :
					flag=1
					break
		if flag == 1:
			print("login successfull")
			
		else:
			print("login unsuccessfull")
			request.session['username'] = "fail"
		context = {'user':request.session.get('username') }	
	return render(request,"login.html",context)	

def signup_view(request):
	context = {'user':request.session.get('username')}
	if request.method == "POST":
		queryset = Customer.objects.all()
		name = request.POST.get('name')
		email = request.POST.get('email')
		phno = request.POST.get('phno')
		address = request.POST.get('address')
		dob = request.POST.get('dob')
		userid = request.POST.get('userid')
		password = request.POST.get('password')
		repeat_password = request.POST.get('repeat_password')
		profilepic = request.POST.get('profilepic')
		queryset = Customer.objects.all()
		print(name)
		print(email)
		print(phno)
		print(address)
		print(dob)
		print(userid)
		print(password)
		print(repeat_password)
		print(profilepic)
		request.session['username'] = userid
		count=1;
		for obj in queryset:
			count = count+1
		customer_id=count+1;
		C = Customer(customer_id=count, customer_name=name, email=email, phno=phno, Address=address, dob=dob, books_bought=0, books_on_sale=0, books_sold=0,image='images/'+profilepic , username=userid, password=password)
		C.save()
		seller = Customer.objects.get(customer_id=count)
		S = Sellers(seller_id=seller, payment_method_1=1, payment_method_2=0)
		S.save()
		context = {'user':request.session.get('username')}
	return render(request,"signup.html",context)

def register_view(request):
	context = {'user':request.session.get('username')}
	if request.method == "POST":
		queryset = Books.objects.all()
		book_name = request.POST.get('book_name')
		author = request.POST.get('author')
		subject = request.POST.get('subject')
		semester = request.POST.get('semester')
		price = request.POST.get('price')
		description = request.POST.get('description')
		image =request.POST.get('pic')
		print(book_name)
		print(author)
		print(subject)
		print(semester)
		print(price)
		print(description)
		print(image)
		count=1
		sellerid=0

		for obj in queryset:
			count = count+1
		print(count)
		obj1 = Customer.objects.get(username=request.session.get('username'))
		seller = Sellers.objects.get(seller_id=obj1.customer_id)  
		book_id=count+1;
		
		B = Books(book_id=count, book_name=book_name, author=author, subject=subject, semester=semester, seller_id=seller, price=price, image='images/'+image, description=description)
		B.save()
		context = {'user':request.session.get('username') }
	context = {'user':request.session.get('username') }
	return render(request,"register.html",context)	

def profile_view(request):
	context = {'user':request.session.get('username')}
	if request.session.get('username') == "NULL":
		print("in null condition")
		context = {'user':request.session.get('username') }
	else:
		obj1 = Customer.objects.get(username=request.session.get('username'))
		print(obj1.customer_name)
		queryset = Books.objects.all()
		queryset1 = Customer.objects.all()
		queryset2 = Sellers.objects.all()
		context = {'user':request.session.get('username'), 'obj':obj1 , 'set':queryset , 'set1':queryset1 ,'set2':queryset2 ,'id':obj1.customer_id }	
	return render(request,"profile.html",context)	


def logout_view(request):
	request.session['username'] = "NULL"
	context = {'user':request.session.get('username')}
	cursor = connection.cursor()
	cursor.execute('''call logout''')
	response = redirect('/')
	return response

def buying_view(request,book):
	context = {'user':request.session.get('username')}
	request.session['book_bought'] = 'false'
	if request.session.get('username') == "NULL":
		print("in null condition")
		context = {'user':request.session.get('username') }
	else:
		obj1 = Customer.objects.get(username=request.session.get('username'))
		print(obj1.customer_name)
		book = Books.objects.get(book_id=book)
		context = {'user':request.session.get('username'), 'obj':obj1, 'book':book, 'status':request.session.get('book_bought')}
	print(book)
	print(context)
	if request.method == "POST":
		book_name = request.POST.get('bookid')
		print("in post")
		obj2 = Books.objects.get(book_id=book_name)
		obj3 = Sellers.objects.get(seller_id=obj2.seller_id)#Customer.objects.get(customer_id=obj2.seller_id))
		S = Books_buying(book_id=obj2, status="pre-booked" , paymentmethod_selected=1 , seller_id=obj3 ,buyer_id=obj1)
		S.save()
		request.session['book_bought'] = 'true'
		context = {'user':request.session.get('username'), 'obj':obj1, 'book':book, 'status':request.session.get('book_bought')}
	print(context)
	return render(request,"empty.html",context)