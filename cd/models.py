from __future__ import unicode_literals

from django.db import models

# Create your models here.
class request_conf(models.Model):
	Cus_link=models.URLField()
	Ser_product=models.CharField(max_length=50)
	Ser_image=models.URLField()
	cus_category=models.CharField(max_length=50,default=1)
	Cus_email=models.CharField(max_length=50,null=True)
	Ser_price=models.CharField(max_length=50)
	Cus_expiry=models.IntegerField(null=True)
	Cus_id=models.CharField(max_length=30,primary_key=True)
	cus_loc=models.CharField(max_length=100,null=True)
	Cus_name=models.CharField(max_length=100,null=True)
	time=models.BigIntegerField(default=100)


class sellerlogindb(models.Model):
	user=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	email=models.EmailField(primary_key=True)
	mobile=models.BigIntegerField()
	shopname=models.CharField(max_length=80)
	shopid=models.CharField(max_length=80)
	office_no=models.IntegerField(null=True)
	city=models.CharField(max_length=200)
	Address1=models.CharField(max_length=200)
	Address2=models.CharField(max_length=200)
	sel_loc=models.CharField(max_length=100,null=True)
	category=models.BigIntegerField(default=1)
	gcmid=models.CharField(max_length=1000)
	token=models.CharField(max_length=100)
	gps=models.CharField(max_length=100)
    imagepath=models.CharField(max_length=200,null=True)
	decline=models.CharField(max_length=60000,default="123")

class selldb(models.Model):
	Cus_id=models.CharField(max_length=30) 
	Q_price=models.CharField(max_length=50)
	Sel_type=models.IntegerField(default=False)
	Sel_comments=models.CharField(max_length=500)
 	Sel_deltype=models.IntegerField(default=False)
	Cus2_conf=models.IntegerField(default=False)
	Sel2_conf=models.IntegerField(default=False)
	img_path=models.CharField(max_length=100,null=True)
	Sel_id=models.CharField(max_length=30,primary_key=True)
	Sel_email=models.EmailField(null=True)
	bprice=models.CharField(max_length=200,null=True)
	btime=models.BigIntegerField(null=True)
class adv(models.Model):
	adv=models.CharField(max_length=2000,null=True)
	edate=models.CharField(max_length=100)
	sdate=models.CharField(max_length=100)
	email=models.CharField(max_length=100,null=True)


class feed(models.Model):
	feed=models.CharField(max_length=2000,null=True)
	email=models.CharField(max_length=100,null=True)

	
	
