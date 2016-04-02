from django.shortcuts import render
import string,random
import sys
# Create your views here.
from cd.models import sellerlogindb,request_conf,selldb,adv,feed
from django.views.decorators.csrf import csrf_exempt 
import json
from django.http import HttpResponse
from datetime import datetime
from random import randint
from bs4 import BeautifulSoup
import requests
import os
import time  
#import cv2
def front(request):
	return render(request,'front.html',)
@csrf_exempt
def sellerlogin(request):
	error=[]
	if request.method=='POST':
		slremail=request.POST.get('email','')
		slrpass=request.POST.get('pass','')	
                try:	
			dbobject=sellerlogindb.objects.get(email=slremail)
			k=1
		except:
			error.append("email id not registered")
			k=0
		if k:		
			if slrpass==dbobject.password :
				token=''.join(random.choice(string.lowercase+string.uppercase+string.digits) for i in range(32))
				dbobject.token=token
				dbobject.save()
				dbobject1=request_conf.objects.all()
				k=0
				Cus_link=[]
				Ser_product=[]
				Ser_image=[]
				Cus_expiry=[]
				cus_loc=[]
				Cus_name=[]
				Cus_id=[]
				Ser_price=[]
				time=[]
				aks={}
				const=0
				for i in dbobject1:
					total={}
					if (int(dbobject.category)%int(dbobject1[k].cus_category)==0 and (dbobject1[k].Cus_id not in dbobject.decline)):
						total['Cus_link']=str(dbobject1[k].Cus_link)
						total['Ser_product']=str(dbobject1[k].Ser_product)
						total['Ser_image']=str(dbobject1[k].Ser_image)
						total['Cus_expiry']=str(dbobject1[k].Cus_expiry)
						total['cus_loc']=str(dbobject1[k].cus_loc)
						total['Cus_name']=str(dbobject1[k].Cus_name)
						total['Cus_id']=str(dbobject1[k].Cus_id)
						total['Ser_price']=dbobject1[k].Ser_price
						total['time']=dbobject1[k].time
						try:
							dbobject3=selldb.objects.get(Cus_id=dbobject1[k].Cus_id)
							check=1
						except:
							check=0
						if(check):
							total['quoted']=1
							total['qprice']=dbobject3.Q_price
							total['Sel_comments']=dbobject3.Sel_comments
							total['deltype']=dbobject3.Sel_deltype
							total['type']=dbobject3.Sel_type
							total['cuscon']=dbobject3.Cus2_conf
							total['selcon']=dbobject3.Sel2_conf						
							if dbobject3.bprice!=0:
								total['bargained']=1
								total['bgprice']=dbobject3.bprice
								total['bgexptime']=dbobject3.btime
							else:
								total['bargained']=0
						else:
							total['qprice']="Nil"
							total['quoted']=0
						aks[const]=total
						const=const+1	
					k=k+1
				n={}
				n['result']=1
				n['token']=token
				n['Transactions']=aks
				n['length']=const
				n['cat']=dbobject.category
				n['user']=dbobject.user
				n['password']=dbobject.password
				n['mobile']=dbobject.mobile
				n['shopname']=dbobject.shopname
                		n['shopid']=dbobject.shopid
                		n['office_no']=dbobject.office_no
                		n['city']=dbobject.city
                		n['Address1']=dbobject.Address1
                		n['Address2']=dbobject.Address2
				n['sel_loc']=dbobject.sel_loc
				n['category']=dbobject.category
			#	n['Ser_image']=Ser_image
			#	n['Cus_name']=Cus_name
			#	n['cus_loc']=cus_loc
			#	n['Ser_product']=Ser_product
			#	n['Cus_expiry']=Cus_expiry
				j_d=json.dumps(n)
				return HttpResponse(json.dumps(n), content_type='application/json')
			else:	
				n={}
				n['result']=0
				j_d=json.dumps(n)
				return HttpResponse(json.dumps(n),content_type='application/json')
		elif k==0:
				n={}
				n['result']=-1
				j_d=json.dumps(n)
				return HttpResponse(json.dumps(n),content_type='application/json')
	else:
		return render(request,'front.html',)		
'''	
@csrf_exempt
def simg(request):
	if request.method=='POST':
		token=request.POST.get('token','')
		email=request.POST.get('email','')
		try:
                        dbobject=sellerlogindb.objects.get(token=token)
                        if email==dbobject.email:
                                k=1
                except:

                        k=0
                if k:
			#imgf=cv2.imread(str(request.POST.get('imgf','')))
                        #cv2.imwrite("var/www/image/"+email,imgf)
			#with open(str(request.POST.get('imgf', '')),'rb'):
			#	data=f.read()
			with open("home/ubuntu/image/"+str(email),'wb') as f:
				f.write(request.POST.get('imgf',''))

			imgf=request.POST.get('imgf','')
			#statinfo=os.stat(imgf)
			
							
			dbobject.imgpath="home/ubuntu/image/"+str(email)
			dbobject.save()
               		n={}
                        n['result']=1
                        n['token']=token
			n['size']=sys.getsizeof(imgf)
			
                        j_d=json.dumps(n)
			return HttpResponse(json.dumps(n),content_type='application/json')
		else:
			n={}
                        n['result']=0
                        n['token']=token
                	n['size']=sys.getsizeof(imgf)
			n['img']=imgf     
			j_d=json.dumps(n)
			return HttpResponse(json.dumps(n),content_type='application/json')
		
'''
@csrf_exempt
def sellersignup(request):
	errors=[]
	if request.method=='POST':
			name=request.POST.get('name','')
			pswd=request.POST.get('pass','')
			email=request.POST.get('email','')
			mobile=request.POST.get('mobile','')
			shopname=request.POST.get('shopname','')
			city=request.POST.get('city','')
			Add1=request.POST.get('address1','')
			sid=request.POST.get('sid','')
			office_no=request.POST.get('office','')
			Add2=request.POST.get('address2','')
			sel_loc=request.POST.get('sel_loc','')
			try:
				c=sellerlogindb.objects.get(email=email)
				errors.append('email already used')
				k=0
			except:	
				k=1
			if k:
				p=sellerlogindb(user=name,password=pswd,email=email,mobile=mobile,shopid=sid,shopname=shopname,office_no=office_no,Address1=Add1,Address2=Add2,sel_loc=sel_loc)
				
				p.save()
				#makng token 
				token=''.join(random.choice(string.lowercase+string.uppercase+string.digits) for i in range(32))
				p.token=token
				p.save()


				n={}
				n['result']=1
				n['token']=token
				j_d=json.dumps(n)
	                        
					
				return HttpResponse(json.dumps(n), content_type='application/json' )
			elif k==0:
				n={}
				n['result']=0
				j_d=json.dumps(n)				
				return HttpResponse(json.dumps(n), content_type='application/json' )
				
@csrf_exempt
def decline(request):
                token=request.POST.get('token','')
                email=request.POST.get('email','')
                decid=request.POST.get('decid','')
#check the token and update the decline field, it could change
                try:
                        dbobject=sellerlogindb.objects.get(token=token)
                        if email==dbobject.email:
                                k=1
                except:

                        k=0
                if k:
                        dbobject.decline=str(decid)+dbobject.decline
                        dbobject.save()
                        n={}
                        n['result']=1
                        n['returnid']=dbobject.decline
                        j_d=json.dumps(n)
                        return HttpResponse(json.dumps(n), content_type='application/json' )
                elif k==0:
                        n={}
                        n['result']=0
                        j_d=json.dumps(n)
                        return HttpResponse(json.dumps(n), content_type='application/json' )
@csrf_exempt
def advt(request):
                token=request.POST.get('token','')
                email=request.POST.get('email','')
                advt=request.POST.get('adv','')
		sdate=request.POST.get('sdate','')
		edate=request.POST.get('edate','')		
#check the token and update the decline field, it could change
                try:
                        dbobject=sellerlogindb.objects.get(token=token)
                        if email==dbobject.email:
                                k=1
                except:
                        k=0
                if k:
                        q=adv(advt=advt,sdate=sdate,edate=edate,email=email)
			q.save()
                        n={}
                        n['result']=1
                        j_d=json.dumps(n)
                        return HttpResponse(json.dumps(n), content_type='application/json' )
                elif k==0:
                        n={}
                        n['result']=0
                        j_d=json.dumps(n)
                        return HttpResponse(json.dumps(n), content_type='application/json' )

@csrf_exempt
def bargain(request):

                	#token=request.POST.get('token','')
                	#email=request.POST.get('email','')
                	sel_id=request.POST.get('selid','')
			bprice=request.POST.get('bprice','')
			btime=request.POST.get('btime','')
#check the token and update the decline field, it could change
               # try:
                #        dbobject=sellerlogindb.objects.get(token=token)
               #         if email==dbobject.email:
               #                 k=1
               # except:

               #         k=0
               # if k:
                        dbobject2=selldb.objects.get(Sel_id=sel_id)
			dbobject2.bprice=bprice
			dbobject2.btime=btime
                        dbobject2.save()
			Sel_email=dbobject2.Sel_email
			dbobject=sellerlogindb.objects.get(email=Sel_email)
			dbobject1=request_conf.objects.get(Cus_id=dbobject2.Cus_id)
                        pson={'delay_while_idle': True, 'collapse_key': 'score_update', 'time_to_live': 108, 'data': {'quoted':"1",'bargained':1,'selcon':0,'cuscon':0,'bgprice':bprice,'bgexptime':btime,'id':dbobject2.Cus_id,'price': dbobject1.Ser_price,'loc':dbobject1.cus_loc, 'name': dbobject1.Ser_product,'buyer_name':dbobject1.Cus_name,'imgurl':dbobject1.Ser_image,'time':dbobject1.Cus_expiry,'timenow':dbobject1.time,'qprice':dbobject2.Q_price,'deltype':dbobject2.Sel_deltype,'type':dbobject2.Sel_type,'comment':dbobject2.Sel_comments},'registration_ids':[dbobject.gcmid]}
                        h={'Content-Type': 'application/json', 'Authorization': 'key=AIzaSyBxEodHSh3moPoMwYkipLEXAhYUn3rptTg'}
                        kson=json.dumps(pson)
                        r=requests.post("https://android.googleapis.com/gcm/send",data=kson,headers=h)

                        n={}
                        n['result']=1
			n['gcmid']=dbobject.gcmid
			n['r']=r.text
                        j_d=json.dumps(n)
                        return HttpResponse(json.dumps(n), content_type='application/json' )
             #   elif k==0:
               #         n={}
                #        n['result']=0
                 #       j_d=json.dumps(n)
                  #      return HttpResponse(json.dumps(n), content_type='application/json' )


@csrf_exempt
def feed(request):
               
                token=request.POST.get('token','')
                email=request.POST.get('email','')
		feed=request.POST.get('feed','')
#check the token and update the decline field, it could change
                try:
                        dbobject=sellerlogindb.objects.get(token=token)
                        if email==dbobject.email:
                                k=1
                except:

                        k=0
                if k:
                        dbobject=feed(feedb=feed,email=email)
                        dbobject.save()
			n={}
                        n['result']=1
                        j_d=json.dumps(n)
                        return HttpResponse(json.dumps(n), content_type='application/json' )
                elif k==0:
                        n={}
                        n['result']=0
                        j_d=json.dumps(n)
                        return HttpResponse(json.dumps(n), content_type='application/json' )
@csrf_exempt
def userdata(request):
	 
         email=""
         token=""
         token=request.POST.get('token','')
         email=request.POST.get('email','')
         try:
                dbobject=sellerlogindb.objects.get(token=token)
                if email==dbobject.email:
                        k=1
         except:
                k=0
         if k:
		data={}
		data['user']=dbobject.user
		data['password']=dbobject.password
		data['mobile']=dbobject.mobile
		data['shopname']=dbobject.shopname
                data['shopid']=dbobject.shopid
                data['office_no']=dbobject.office_no
                data['city']=dbobject.city
                data['Address1']=dbobject.Address1
                data['Address2']=dbobject.Address2
		data['sel_loc']=dbobject.sel_loc
		data['category']=dbobject.category
                n={}
                n['result']=1
                n['token']=token
                n['data']=data
                        #       n['Ser_image']=Ser_image
                        #       n['Cus_name']=Cus_name
                        #       n['cus_loc']=cus_loc
                        #       n['Ser_product']=Ser_product
                        #       n['Cus_expiry']=Cus_expiry
                j_d=json.dumps(n)
                return HttpResponse(json.dumps(n), content_type='application/json')
         elif k==0:
                n={}
                n['result']=0
                j_d=json.dumps(n)
                return HttpResponse(json.dumps(n), content_type='application/json' )



@csrf_exempt
def updateuser(request):
	
	 email=""
         token=""
         token=request.POST.get('token','')
         email=request.POST.get('email','')
	 try:
 	 	dbobject=sellerlogindb.objects.get(token=token)
                if email==dbobject.email:
      		        k=1
	 except:
		k=0
	 if k:
		name=request.POST.get('name','')
                pswd=request.POST.get('pass','')
                mobile=request.POST.get('mobile','')
                shopname=request.POST.get('shopname','')
                city=request.POST.get('city','')
                Add1=request.POST.get('address1','')
                sid=request.POST.get('sid','')
                office_no=request.POST.get('office','')
                Add2=request.POST.get('address2','')
                sel_loc=request.POST.get('sel_loc','')
	        #p=sellerlogindb(user=name,password=pswd,mobile=mobile,shopid=sid,shopname=shopname,office_no=office_no,Address1=Add1,Address2=Add2,sel_loc=sel_loc)
	        dbobject.user=name
		dbobject.password=pswd
		dbobject.mobile=mobile
                dbobject.shopid=sid
                dbobject.shopname=shopname
                dbobject.office_no=office_no
                dbobject.Address1=Add1
                dbobject.Address2=Add2
                dbobject.sel_loc=sel_loc
		dbobject.save()
		n={}
                n['result']=1
	
                j_d=json.dumps(n)
                return HttpResponse(json.dumps(n), content_type='application/json' )
         elif k==0:
                n={}
                n['result']=0	
                j_d=json.dumps(n)
                return HttpResponse(json.dumps(n), content_type='application/json' )


 
 



@csrf_exempt
def sellergcm(request):
	if request.method=='POST':
#Header authorisation
#Gcm request to google
		email=""
		gcmid=""
		token=""
		gcmid=request.POST.get('gcmid','')
		token=request.POST.get('token','')	
		email=request.POST.get('email','')
#check the token and update the gcmid, it could change
		try:
			dbobject=sellerlogindb.objects.get(token=token)
			if email==dbobject.email:
				k=1
		except:
			
			k=0
		if k:
			dbobject.gcmid=str(gcmid);
			dbobject.save()
			n={}
			n['result']=1
			n['returnid']=dbobject.gcmid
			j_d=json.dumps(n)				
			return HttpResponse(json.dumps(n), content_type='application/json' )
				
		elif k==0:
			n={}
			n['result']=0
			
			n['gcmid']=gcmid
			j_d=json.dumps(n)				
			return HttpResponse(json.dumps(n), content_type='application/json' )
				

@csrf_exempt
def sellercategory(request):
	# accept the prime no category 
	# check for the token b4
	if request.method=='POST':
		token=request.POST.get('token','')
		email=request.POST.get('email','')
		category=request.POST.get('category','')
		
		try:
			dbobject=sellerlogindb.objects.get(token=token)
			if email==dbobject.email:				
				k=1
		except:
			k=0
			#return render(request,'front.html',)
		if k:
			dbobject.category=category
			dbobject.save()
			n={}
			n['result']=1
			n['category']=category
			j_d=json.dumps(n)				
			return HttpResponse(json.dumps(n), content_type='application/json' )
		

		elif k==0:
			n={}
			n['result']=0
			j_d=json.dumps(n)				
			return HttpResponse(json.dumps(n), content_type='application/json' )
@csrf_exempt
def  customer2seller(request):
	gcmida=[]
	if request.method=='POST':
		price=request.POST.get('price','')
		pname=request.POST.get('pname','')
		img=request.POST.get('img','')
		cat=request.POST.get('cat','')
		exptime=request.POST.get('time','')
		cus_loc=request.POST.get('cus_loc','')
		name=request.POST.get('name','')
		tim=int(round(time.time() * 1000))
		dbobject2=request_conf(time=tim,Ser_product=pname,Ser_price=price,Ser_image=img,cus_category=cat,Cus_expiry=exptime,cus_loc=cus_loc,Cus_name=name)
		cus_id=''.join(random.choice(string.lowercase+string.uppercase+string.digits) for i in range(30))
		dbobject2.Cus_id=cus_id
		dbobject2.save()
		
		dbobject=sellerlogindb.objects.all()
		k=0
		l=1
		for i in dbobject:

			if int(dbobject[k].category)%int(cat)==0:
				l=l+1
				gcmida.append(dbobject[k].gcmid)
			k=k+1
		k=0
		q=[]
		for i in gcmida:
			
			pson={'delay_while_idle': True, 'collapse_key': 'score_update', 'time_to_live': 108, 'data': {'quoted':"0",'price': price,'cus_loc':cus_loc, 'name': pname,'buyer_name':name,'imgurl': img,'time':exptime,'id':cus_id,'timenow':tim}, 'registration_ids': [gcmida[k]]}
			
			h={'Content-Type': 'application/json', 'Authorization': 'key=AIzaSyBxEodHSh3moPoMwYkipLEXAhYUn3rptTg'}
			kson=json.dumps(pson)
			r=requests.post("https://android.googleapis.com/gcm/send",data=kson,headers=h)
			k=k+1
			q.append(r.text)
		n={}
		n['result']=gcmida
		n['re']=q
		j_d=json.dumps(n)
		return HttpResponse(json.dumps(n),content_type='application/json')
			
@csrf_exempt
def s2c(request):
		if request.method=='POST':
				prtype=request.POST.get('type','')
				deltype=request.POST.get('deltype','')
				comment=request.POST.get('comment','')
				qprice=request.POST.get('qprice','')
				#imfile=request.POST.get('image','')
				token=request.POST.get('token','')
				cid=request.POST.get('id','')
				email=request.POST.get('email','')
				try:
					dbobject1=sellerlogindb.objects.get(token=token)
					if email==dbobject1.email:				
						k=1
				except:
					k=0

				if k:
					Sel_id=''.join(random.choice(string.lowercase+string.uppercase+string.digits) for i in range(32))

					dbobject2=selldb(Cus_id=cid,Q_price=qprice,Sel_type=prtype,Sel_comments=comment,Sel_email=email,Sel_id=Sel_id,Sel_deltype=deltype)
					dbobject2.save()
					n={}
					n['result']=1
					j_d=json.dumps(n)				
					return HttpResponse(json.dumps(n), content_type='application/json' )
		  

				elif k==0:
					n={}
					n['result']=0
					j_d=json.dumps(n)				
					return HttpResponse(json.dumps(n), content_type='application/json' )

@csrf_exempt
def cus_conf(request):
	if request.method=='POST':
			Sel_id=request.POST.get('Sel_id','')
			try:
				dbobject2=selldb.objects.get(Sel_id=Sel_id)
				k=1
			except:
				k=0
			if k:
				dbobject2.Cus2_conf=1
				dbobject2.save()
				dbobject=sellerlogindb.objects.get(email=dbobject2.Sel_email)
				dbobject1=request_conf.objects.get(Cus_id=dbobject2.Cus_id)
				pson={'delay_while_idle': True, 'collapse_key': 'score_update', 'time_to_live': 108, 'data': {'quoted':"1",'bargained':1,'selcon':1,'cuscon':1,'bgprice':dbobject2.bprice,'bgexptime':dbobject2.btime,'id':dbobject2.Cus_id,'price': dbobject1.Ser_price,'loc':dbobject1.cus_loc, 'name': dbobject1.Ser_product,'buyer_name':dbobject1.Cus_name,'imgurl':dbobject1.Ser_image,'time':dbobject1.Cus_expiry,'timenow':dbobject1.time,'qprice':dbobject2.Q_price,'deltype':dbobject2.Sel_deltype,'type':dbobject2.Sel_type,'comment':dbobject2.Sel_comments},'registration_ids':[dbobject.gcmid]}
				h={'Content-Type': 'application/json', 'Authorization': 'key=AIzaSyBxEodHSh3moPoMwYkipLEXAhYUn3rptTg'}
	                        kson=json.dumps(pson)
	                        r=requests.post("https://android.googleapis.com/gcm/send",data=kson,headers=h)				
				n={}
				n['result']=1
				j_d=json.dumps(n)				
				return HttpResponse(json.dumps(n), content_type='application/json' )
			else:
				n={}
				n['result']=0
				j_d=json.dumps(n)				
				return HttpResponse(json.dumps(n), content_type='application/json' )
@csrf_exempt
def sel_conf(request):
	 token=request.POST.get('token','')
         email=request.POST.get('email','')
	 Cus_id=request.POST.get('Cus_id','')
	 try:
 	 	dbobject=sellerlogindb.objects.get(token=token)
                if email==dbobject.email:
      		        k=1
	 except:
		k=0
	 if k:
		dbobject2=selldb.objects.get(Sel_email=email,Cus_id=Cus_id)
			
		dbobject2.Sel2_conf=1
		dbobject2.save()
		n={}
		n['result']=1
		j_d=json.dumps(n)				
		return HttpResponse(json.dumps(n), content_type='application/json' )
	 else:
		n={}
		n['result']=0
		j_d=json.dumps(n)				
		return HttpResponse(json.dumps(n), content_type='application/json' )
		
		
	

@csrf_exempt
def item(request):
	#
	if 'item' in request.POST:
		s=""
		p=""
		c=""
		sc=""
		k=""
		
		ki=""
		
		img=""
		if "amazon" in str(request.POST):
 			p="dasd"
			s=""
			b="http"
			
			link=request.POST.get('item','')
			rlinklen=link.find(b)	
			rlink=link[rlinklen:]
			r=requests.get(rlink)
		
			soup=BeautifulSoup(r.content,"lxml")
			#return render(request,'item.html',{'item':link})
			data=soup.find_all("span",{"id":"productTitle"})
			for i in data:

				s=i.text
			price=soup.find_all("span",{"class":"a-size-medium a-color-price"})
			for i in price:
				k=i.text
			cat=soup.find_all("a",{'class':'a-link-normal a-color-tertiary'})
			
			
			r=soup.find_all("div",{"id":"imgTagWrapperId"})	
			q=str(r)
			b="data-a-dynamic-image"
			i=q.find(b)+len(b)+4
			try:			
				while q[i]!='"':
					img=img+q[i]
					i=i+1
			except:
				
				img=""
			c=str(cat[0].text)
			sc=str(cat[1].text)
			
			#return render(request,'item.html',{'item':s,'price':k,'kk':c,'sc'=sc})	
		elif "snapdeal" in str(request.POST):
			p="dasd"
			s=""
			link=request.POST.get['item']
		
		
			r=requests.get(link)
		
			soup=BeautifulSoup(r.content,"lxml")
			#return render(request,'item.html',{'item':link})
			data=soup.find_all("h1",{"itemprop":"name"})
			for i in data:

				s=i.text
			price=soup.find_all("span",{"itemprop":"price"})
			for i in price:
				k=i.text
		
	
			#return render(request,'item.html',{'item':s,'nn':k,'kk':'Thats all'})	
 		
		if 'computer' in c.lower() :
			cat=7
		elif 'watches' in c.lower():
			cat=19
		elif 'sports' in c.lower():
			cat=17
		elif 'mobiles' in c.lower():
			cat=13
		elif 'camera' in c.lower() or 'camera' in sc.lower():
			cat=2
		elif 'books' in c.lower():
			cat=5
		elif 'musical instuments' in c.lower():
			cat=3
		elif 'electronics' in c.lower() and 'accessories' in sc.lower():
			cat=23
		elif 'video games' in c.lower():
			cat=11


		n={}
		n['result']=s
		n['price']=k
		n['img']=img
		cl=len(c)
		n['category']=c[17:cl-13]
		scl=len(sc)
		n['sub-cat']=sc[17:scl-13]

		n['cat']=cat
		j_d=json.dumps(n)
		
		return HttpResponse(json.dumps(n),content_type='application/json')
		
		


'''def sellercustomer1(request):
	# sends price,details of pro everything check for token
	if request.method=='POST':
		token=request.POST.get('token','')
		try:
			dbobject=sellerlogin.objects.get(token=token)
			if email=dbobject.email:
				k=1
		except:
			k=0
		if k:
			

		
def customer1(request):
	#sends  the url
#scrape and get image and send to phone cust
	if request.method=='POST':
		#p=request.POST.get('link','')
		s=""
		p=""
		c=""
		sc=""
		k=""
		scat=""
		cat=""
		if "amazon" in str(request.GET):
 			
			s=""
			link=request.POST.get('item','')
			img=""
		
			r=requests.get(link)
		
			soup=BeautifulSoup(r.content,"lxml")
			#return render(request,'item.html',{'item':link})
			data=soup.find_all("span",{"id":"productTitle"})
			for i in data:

				s=i.text
			price=soup.find_all("span",{"id":"priceblock_saleprice"})
			for i in price:
				k=i.text
			r=s.find_all("div",{"id":"imgTagWrapperId"})
			
			k=str(r)
			b="data-a-dynamic-image"
			i=k.find(b)+len(b)+4
			while k[i]!='"':
				img=img+k[i]
				i=i+1
			





			cat=soup.find_all("a",{'class':'a-link-normal a-color-tertiary'})
			c=str(cat[0].text)
			sc=str(cat[1].text)
			
			#return render(request,'item.html',{'item':s,'price':k,'kk':c,'sc'=sc})	
		elif "snapdeal" in str(request.GET):
			p="dasd"
			s=""
			link=request.GET['item']
			r=requests.get(link)
			soup=BeautifulSoup(r.content,"lxml")
			#return render(request,'item.html',{'item':link})
			data=soup.find_all("h1",{"itemprop":"name"})
			for i in data:
				s=i.text
			price=soup.find_all("span",{"itemprop":"price"})
			for i in price:
				k=i.text

				#return render(request,'item.html',{'item':s,'nn':k,'kk':'Thats all'})	

		#return price and name in json


		if 'computer' in c.lower() :
			cat="Computers"
			if "laptop" in sc.lower():
				scat="Laptops"
			elif "desktop" in sc.lower() or "printer" in sc.lower() or "monitor" in sc.lower() :
				scat="Desktops,printers and monitors"
		return render(request,'item.html',{'item':s,'price':k,'c':c,'sc':sc,"cios":cat,"scios":scat})	
	#else:
	#	return render(request,'item.html',)
def customer2seller(request):
	#url,expiry etcc...... and send it to phones through gcm
	if request.method=='POST':
		
		expiry=request.POST.get('expiry','')
		product=request.POST.get('product','')
		price=request.POST.get('price','')
		dbobject=request_conf(Cus_link=url,Ser_product=product,Ser_price=price,Cus_expiry=expiry)
		db.save()


	
def custcnf(request):
	#confirms the 



def sellerconf(request):
	#conf and check for the token '''

'''
Amazon 
Flipkart
Paytm
Snapdeal
shopclues
'''





			
		
		
