from django.db import models
from django.utils.timezone import now

class Customer(models.Model):
	customer_id = models.AutoField(primary_key=True)
	customer_name = models.CharField(max_length=30)
	email = models.EmailField()
	phno = models.BigIntegerField(unique=True)
	Address = models.CharField(max_length=200)
	dob = models.DateField()
	books_bought = models.SmallIntegerField() 
	books_on_sale = models.SmallIntegerField()
	books_sold = models.SmallIntegerField()
	image = models.ImageField(upload_to='images/' ,blank=True, null=True)
	username = models.CharField(max_length=15 , unique=True)
	password = models.CharField(max_length=15 , unique=True)




class Sellers(models.Model):
	seller_id = models.ForeignKey(Customer ,primary_key=True , on_delete=models.CASCADE)
	payment_method_1 = models.CharField(max_length=1)
	payment_method_2 = models.CharField(max_length=1)



class Books(models.Model):  
	book_id=models.AutoField(primary_key=True)
	book_name=models.CharField(max_length=30)
	author=models.CharField(max_length=30) 
	subject=models.CharField(max_length=10)
	semester=models.CharField(max_length=1)
	seller_id=models.ForeignKey(Sellers,on_delete=models.CASCADE)
	price=models.SmallIntegerField()
	image=models.ImageField(upload_to='images/' ,blank=True, null=True)
	description=models.CharField(max_length=200)




class Administrator(models.Model):
	administrator_id = models.AutoField(primary_key=True)
	administrator_name = models.CharField(max_length=30)
	email = models.EmailField()
	phno = models.BigIntegerField(unique=True)
	Address	= models.CharField(max_length=200)
	dob = models.DateField()
	no_booksverified = models.SmallIntegerField()




class Books_buying(models.Model):
	book_id		 			= models.ForeignKey(Books , on_delete=models.CASCADE)
	status		 			= models.CharField(max_length=20)
	paymentmethod_selected	= models.CharField(max_length=1)
	seller_id				= models.ForeignKey(Sellers , on_delete=models.CASCADE)
	buyer_id				= models.ForeignKey(Customer , on_delete=models.CASCADE)




class websitelogs(models.Model):
	user_id			= models.SmallIntegerField(default=1)
	user_log	= models.CharField(max_length=30 ,default='log')
	log = models.CharField(max_length=30 ,default='log')








