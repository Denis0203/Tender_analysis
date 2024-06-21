from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Tender, Addres, Category,Inn, Status,Test1, Region
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.forms import UserCreationForm, User 
from django.views.generic.edit import CreateView
from django.core.exceptions import PermissionDenied
import datetime
import random
import pytz
from sklearn.cluster import AgglomerativeClustering, DBSCAN, OPTICS
import copy
from datetime import datetime, timedelta
from django.utils import timezone
import os
import pandas as pd
import numpy as np
import seaborn as sn
from io import BytesIO
import base64

from collections import Counter

import csv


 
@login_required #Проверка вошёл ли пользователь в свою учетную запись
def index(request):
    """
    Функция отображения для страницы просмотра тендеров.
    """

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context


    #tender_list = Test1.objects.all()
    cat_list=[]
    t_id =[]
    #region_list = Region.objects.all()
    rn=1
    rid=1
    # Генерация "количеств" некоторых главных объектов

    podcat=[
    		['Полное строительство и реконструкция зданий и сооружений',
    		'Строительно-монтажные работы, Монтаж конструкций и ограждений',
    		'Ремонт зданий и сооружений',
    		'Фасадные работы, Кровельные работы, Высотные работы',
    		'Установка окон и дверей, Производство окон и дверей',
    		'Подготовка площадей под строительство, Расчистка просек, Сооружение насыпей',
    		'Сантехнические работы, Внутренние сети водо-, тепло-, газо-снабжения и канализации',
    		'Электротехнические работы в зданиях', 'Строительство и обслуживание объектов энергетики и электрических сетей',
    		'Строительство и обслуживание сетей связи и сооружений связи',
    		'Строительство, ремонт и обслуживание дорог, мостов, тоннелей и ЖД путей',
    		'Строительство и ремонт трубопроводов и прочих инженерных коммуникаций',
    		'Проектирование, монтаж и обслуживание систем вентиляции', 
    		'Строительство и обслуживание гидротехнических сооружений', 
    		'Огнезащитные и антикоррозийные работы', 'Благоустройство и озеленение'],
    		['Охранные услуги, Инкассация'],
    		['Технологическое оборудование, монтаж и обслуживание'],
    		['Организация спортивных мероприятий, билеты на спортивные мероприятия',
    		'Организация концертов, праздников,билеты на концерты, показы фильмов и праздники'],
    		['Крупы, Макароны, Хлебобулочные изделия, Крупяная и макаронная продукция, Зерно, Злаки'],
    		['Услуги по реабилитации, Санаторно-курортное лечение'],
    		['Телекоммуникационное оборудование и материалы, Оборудование связи'],
    		['Услуги Интернет, передачи данных, местной телефонной связи'],
    		['Проектные работы в области строительства и ремонта зданий, внутридомовых сетей'],
    		['Медицинские и лабораторные исследования','Прочие медицинские услуги']
    		]



    #list1= Test1.objects.all()
    #for i in list1:
    #    if i.data2 < timezone.now():
    #        i.status = Status.objects.get(idstatus=4)
    #        i.save()
    #    else:
    #        i.status = Status.objects.get(idstatus=1)
    #        i.save()
    #for j in tender_list:
    #    if j.idten not in t_id:
    #        t_id.append(j.idten)
    #with open('D:\Downloads\dost7.csv', newline='', encoding="utf-8") as f:
    #	reader = csv.reader(f)
    #	for row in reader:
    #		r_list=[]
    #		#print(row)
    #		if row[1]=='Номер тендера' or row[1]=='' or row[1] in t_id or row[5]=='' or ((datetime.strptime((row[9]+":00"),"%d.%m.%Y %H:%M:%S")-datetime.strptime((row[8]+" 00:00:01"),"%d.%m.%Y %H:%M:%S"))<timedelta(days=0)):
    #			continue
    #		if row[10]=='':
    #			row[10]='0'
    #		if row[12]=='':
    #			row[12]='0%'
    #		if row[11]=='':
    #			row[11]='0%'
    #		elif row[11][-1]!='%' and row[10]!='0':
    #			x = int(row[11].replace(',', ''))
    #			y = int(row[10].replace(',', ''))
    #			row[11]= str(round(x/y*100,1))+'%'
    #
    #		for i in Region.objects.all():
    #			r_list.append(i.regname)
    #		r_id=len(r_list)
    #		if row[2].split(' ')[0] not in r_list:
    #			b=Region(idregion=r_id+1,regname=row[2].split(' ')[0])
    #			b.save()
    #		for i in Region.objects.all():
    #			if i.regname == row[2].split(' ')[0]:
    #				cr = i



    #		inn_list=[]
    #		ind=0
    #		for i in Inn.objects.all():
    #			if i.inn == row[5].split(', ')[0]:
    #				ind = 1
    #				rg=Inn.objects.get(inn=row[5].split(', ')[0])
    #		inn_id=len(Inn.objects.all())
    #		if ind==0:
    #			c=Inn(idi=inn_id+1,inn=row[5].split(', ')[0],name=row[4])
    #			c.save()
    #			rg=Inn.objects.get(idi=inn_id+1)



    #		if row[14] in podcat[0]:
    #			j=Category.objects.get(idcategory=1)
    #		elif row[14] in podcat[1]:
    #			j=Category.objects.get(idcategory=2)
    #		elif row[14] in podcat[2] or podcat[2][0] in row[14]:
    #			j=Category.objects.get(idcategory=3)
    #		elif row[14] in podcat[3] or podcat[3][0] in row[14] or podcat[3][1] in row[14]:
    #			j=Category.objects.get(idcategory=4) 
    #		elif row[14] in podcat[4] or podcat[4][0] in row[14]:
    #			j=Category.objects.get(idcategory=5)  
    #		elif row[14] in podcat[5]:
    #			j=Category.objects.get(idcategory=6)
    #		elif row[14] in podcat[6] or podcat[6][0] in row[14] :
    #			j=Category.objects.get(idcategory=7) 
    #		elif row[14] in podcat[7] or podcat[7][0] in row[14] :
    #			j=Category.objects.get(idcategory=8) 
    #		elif row[14] in podcat[8]:
    #			j=Category.objects.get(idcategory=9)
    #		elif row[14] in podcat[9] or podcat[9][0] in row[14] or podcat[9][1] in row[14]:
    #			j=Category.objects.get(idcategory=10)  
    #		a = Test1(idten = row[1],
    # 				name = row[0],
    # 				data1 =datetime.strptime((row[8]+" 00:00:01"),"%d.%m.%Y %H:%M:%S"), 
    #				data2 =datetime.strptime((row[9]+":00"),"%d.%m.%Y %H:%M:%S"),
    #				inn = rg,
    #				sum0 = int(row[10].replace(',', '')), 
    #				prepayment = row[12],
    #				provision = row[11],
    #				region = cr,
    #				source = row[13],
    #				category = j)
    #		a.save()

    #list1= Test1.objects.all()
    #for i in Test1.objects.all():
    #	if i.data2 < timezone.now():
    #		i.status = Status.objects.get(idstatus=4)
    #		i.save()
    #	else:
    #		i.status = Status.objects.get(idstatus=1)
    #		i.save()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context



    #num_tenders=Tender.objects.all().count()
    #print(Test1.objects.all().count())
    #tender_list = Test1.objects.all()
    #category_list = Category.objects.all()
    #n_tenders = [0]*((len(category_list))+1)
    #for i in category_list:
    	#prices = Tender.summ.get(Tender.category.categorycol=i.categorycol)
    #	for j in tender_list:
            #x1=datetime.now()
    #        if j.category.categorycol == i.categorycol:
    #            n_tenders[i.idcategory]+=1
            #print(datetime.now() - x1)
    #n_tenders.pop(0)


    
    
    #for i in range (Category.objects.all().count()):
    #	cat_list.append([0]*6)
    	#print('1')
    #for i in range (Category.objects.all().count()):
    #	min=1000000000000
    #	max=0
    #	act = 0
    #	end = 0
    #	cat_list[i][0]= (Category.objects.all())[i]
    #	cat_list[i][1]= n_tenders[i]
    #	for j in tender_list:
    #		x1=datetime.now()
    #		if j.category.categorycol==cat_list[i][0].categorycol:
    #			if j.sum0 > max:
    #				max = j.sum0
    #			if j.sum0 < min:
    #				min = j.sum0
    #			if j.status.statusname == "Активный":
    #				act+=1
    #			else:
    #				end+=1
    		#print(datetime.now() - x1)
    #	cat_list[i][2]= min
    #	cat_list[i][3]= max
    #	cat_list[i][4]= act
    #	cat_list[i][5]= end
    cat_list=Category.objects.all()

    obl=['Амурская','Архангельская','Астраханская',
    'Белгородская','Брянская','Владимирская','Волгоградская',
    'Вологодская','Воронежская','Ивановская','Иркутская',
    'Калининградская','Калужская','Кемеровская','Кировская',
    'Костромская','Курганская','Курская','Ленинградская',
    'Липецкая','Магаданская','Московская','Мурманская',
    'Нижегородская','Новгородская','Новосибирская','Омская',
    'Оренбургская','Орловская','Пензенская','Псковская',
    'Ростовская','Рязанская','Самарская','Саратовская',
    'Сахалинская','Свердловская','Смоленская','Тамбовская',
    'Тверская','Томская','Тульская','Тюменская',
    'Ульяновская','Челябинская','Ярославская']

    kr=['Алтайский','Забайкальский','Камчатский','Краснодарский','Красноярский',
    'Пермский','Приморский','Ставропольский','Хабаровский'
    ]

    resp=['Адыгея','Алтай','Башкортостан','Бурятия',
    'Дагестан','Ингушетия','Калмыкия','Карелия',
    'Коми','Крым','Марий Эл','Мордовия',
    'Саха (Якутия)','Северная Осетия – Алания','Татарстан','Тыва',
    'Хакасия','']


    for i in Region.objects.all():
        if i.regname in obl:
            i.regname=i.regname+' область'
        elif i.regname in kr:
            i.regname=i.regname+' край'
        elif i.regname in resp:
            i.regname=i.regname+' республика'
        i.save()

    MyList = [] 
    for i in Test1.objects.all().values('prepayment'):
        if i['prepayment'][:-1]!='' and i['prepayment'][:-1]!='0':
            MyList.append(int(i['prepayment'][:-1]))
    MyFile = open ('D:\Downloads\output.txt', 'w')
    for element in MyList:
        MyFile.write(str(element)+',')
    MyFile.close()


    return render(
        request,
        'watcher/list.html',
        context={'cat_list':cat_list},
    )

def add():
	tender_list = Test1.objects.all()
	cat_list=[]
	t_id =[]
	region_list = Region.objects.all()
	rn=1
	rid=1
	# Генерация "количеств" некоторых главных объектов

	podcat=[
    		['Полное строительство и реконструкция зданий и сооружений',
    		'Строительно-монтажные работы, Монтаж конструкций и ограждений',
    		'Ремонт зданий и сооружений',
    		'Фасадные работы, Кровельные работы, Высотные работы',
    		'Установка окон и дверей, Производство окон и дверей',
    		'Подготовка площадей под строительство, Расчистка просек, Сооружение насыпей',
    		'Сантехнические работы, Внутренние сети водо-, тепло-, газо-снабжения и канализации',
    		'Электротехнические работы в зданиях', 'Строительство и обслуживание объектов энергетики и электрических сетей',
    		'Строительство и обслуживание сетей связи и сооружений связи',
    		'Строительство, ремонт и обслуживание дорог, мостов, тоннелей и ЖД путей',
    		'Строительство и ремонт трубопроводов и прочих инженерных коммуникаций',
    		'Проектирование, монтаж и обслуживание систем вентиляции', 
    		'Строительство и обслуживание гидротехнических сооружений', 
    		'Огнезащитные и антикоррозийные работы', 'Благоустройство и озеленение'],
    		['Охранные услуги, Инкассация'],
    		['Технологическое оборудование, монтаж и обслуживание'],
    		['Организация спортивных мероприятий, билеты на спортивные мероприятия',
    		'Организация концертов, праздников,билеты на концерты, показы фильмов и праздники',
    		'Организация выставок, конференций, семинаров'],
    		['Крупы, Макароны, Хлебобулочные изделия, Крупяная и макаронная продукция, Зерно, Злаки'],
    		['Услуги по реабилитации, Санаторно-курортное лечение'],
    		[],
    		[],
    		['Проектные работы в области строительства и ремонта зданий, внутридомовых сетей'],
    		['Медицинские и лабораторные исследования','Прочие медицинские услуги']
    		]
	for j in tender_list:
		if j.idten not in t_id:
			t_id.append(j.idten)
	with open('D:\Downloads\dost4_1.csv', newline='', encoding="utf-8") as f:
		reader = csv.reader(f)
		for row in reader:
			r_list=[]
    		#print(row)
			if row[1]=='Номер тендера' or row[1]=='' or row[1] in t_id or row[5]=='' or ((datetime.strptime((row[9]+":00"),"%d.%m.%Y %H:%M:%S")-datetime.strptime((row[8]+" 00:00:01"),"%d.%m.%Y %H:%M:%S"))<timedelta(days=0)):
				continue
			if row[10]=='':
				row[10]='0'
			if row[12]=='':
				row[12]='0%'
			if row[11]=='':
				row[11]='0%'
			elif row[11][-1]!='%' and row[10]!='0':
				x = int(row[11].replace(',', ''))
				y = int(row[10].replace(',', ''))
				row[11]= str(round(x/y*100,1))+'%'

			for i in Region.objects.all():
				r_list.append(i.regname)
			r_id=len(r_list)
			if row[2].split(' ')[0] not in r_list:
				b=Region(idregion=r_id+1,regname=row[2].split(' ')[0])
				b.save()
			for i in Region.objects.all():
				if i.regname == row[2].split(' ')[0]:
					cr = i



			inn_list=[]
			ind=0
			for i in Inn.objects.all():
				if i.inn == row[5].split(', ')[0]:
					ind = 1
					rg=Inn.objects.get(inn=row[5].split(', ')[0])
			inn_id=len(Inn.objects.all())
			if ind==0:
				c=Inn(idi=inn_id+1,inn=row[5].split(', ')[0],name=row[4])
				c.save()
				rg=Inn.objects.get(idi=inn_id+1)



			if row[14] in podcat[0]:
				j=Category.objects.get(idcategory=1)
			elif row[14] in podcat[1]:
				j=Category.objects.get(idcategory=2)
			elif row[14] in podcat[2] or podcat[2][0] in row[14]:
				j=Category.objects.get(idcategory=3)
			elif row[14] in podcat[3] or podcat[3][0] in row[14] or podcat[3][1] in row[14] or podcat[3][2] in row[14] :
				j=Category.objects.get(idcategory=4) 
			elif row[14] in podcat[4] or podcat[4][0] in row[14]:
				j=Category.objects.get(idcategory=5)  
			elif row[14] in podcat[5]:
				j=Category.objects.get(idcategory=6) 
			elif row[14] in podcat[8]:
				j=Category.objects.get(idcategory=9)
			elif row[14] in podcat[9] or podcat[9][0] in row[14] or podcat[9][1] in row[14]:
				j=Category.objects.get(idcategory=10) 
			a = Test1(idten = row[1],
    				name = row[0],
    				data1 =datetime.strptime((row[8]+" 00:00:01"),"%d.%m.%Y %H:%M:%S"), 
    				data2 =datetime.strptime((row[9]+":00"),"%d.%m.%Y %H:%M:%S"),
    				inn = rg,
    				sum0 = int(row[10].replace(',', '')), 
    				prepayment = row[12],
    				provision = row[11],
    				region = cr,
    				source = row[13],
    				category = j)
			a.save()

	list1= Test1.objects.all()
	for i in list1:
		if i.data2 < timezone.now():
			i.status = Status.objects.get(idstatus=4)
			i.save()
		else:
			i.status = Status.objects.get(idstatus=1)
			i.save()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context



def contacts(request):
    #Функция отображения страницы контактов
	return render(
        request,
        'watcher/contacts.html',
    )



@login_required
def stats(request):
    #Функция отображения страницы статистики
    x1=datetime.now()

    tender_list = Test1.objects.all().values('category','status','sum0')
    #tender_list = Test1.objects.filter(category=category_id).values('idten','data1','name','sum0','region','status')
    category_list = Category.objects.all()
    num_category = Category.objects.all().count()
    num_status = Status.objects.all().count()
    pie=[[],[],[],[],[],[],[],[],[],[]]
    d=[]
    for i in range (num_category):
        d.append([0]*(num_status+2))
        d[i][0]=category_list[i].idcategory
        pie[i]=round(Test1.objects.filter(category= category_list[i]).count()/Test1.objects.all().count()*100)
        for j in  tender_list:
            if d[i][0] == j['category'] and j['status'] == 1:
                d[i][1]+=1
            elif d[i][0] == j['category'] and j['status'] == 4:
                d[i][2]+=1
            elif d[i][0] == j['category'] and j['status'] == 3:
                d[i][3]+=1
        d[i][4]=d[i][1]+d[i][2]+d[i][3]
        if d[i][4]!=0:
            d[i][1]=round(d[i][1]/d[i][4]*100,1)
            d[i][2]=round(d[i][2]/d[i][4]*100,1)
            d[i][3]=round(d[i][3]/d[i][4]*100,1)

    s=[]
    for i in range (num_category):
        s.append([0]*3)
        s[i][0]=category_list[i].idcategory
        for j in  tender_list:
            if s[i][0] == j['category']:
                s[i][1]+=j['sum0']
                s[i][2]+=1
        if s[i][2] != 0:
            s[i][1] = round(s[i][1]/s[i][2],2)
    #print(d)
    x=12

    #Кластер к средних

    #n=Test1.objects.all().count()
    k=6
    dim=2  
    max_cluster_value=1177123951
    
    def data_distribution(array, cluster):
        cluster_content = [[] for i in range(k)]
        for i in range(n):
            min_distance = float('inf')
            situable_cluster = -1
            for j in range(k):
            	distance = 0
            	for q in range(dim):
            		distance += (array[i][q]-cluster[j][q])**2
            				
            	distance = distance**(1/2)
            	if distance < min_distance:
            		min_distance = distance
            		situable_cluster = j

            cluster_content[situable_cluster].append(array[i])
		
        return cluster_content

    def cluster_update(cluster, cluster_content, dim):
        k = len(cluster)
        for i in range(k): #по i кластерам
            for q in range(dim): #по q параметрам
            	updated_parameter = 0
            	for j in range(len(cluster_content[i])): 
            		updated_parameter += cluster_content[i][j][q]
            	if len(cluster_content[i]) != 0:
            		updated_parameter = updated_parameter / len(cluster_content[i])
            	cluster[i][q] = round(updated_parameter,1)
        return cluster

    #array = [[0] * dim for i in range(n)]
    #ai=0
    #for i in Test1.objects.all():
    #	if i.data2-i.data1>timedelta(days=0) and i.sum0 >0:
    #		array[ai][1]=round((i.data2-i.data1)/timedelta(days=1),1)*74284942
    #		array[ai][0]=i.sum0
    #		ai=ai+1
    #print(array)
    #cluster = [[0 for i in range(dim)] for q in range(k)] 
    #cluster_content = [[] for i in range(k)] 

    #for i in range(dim):
    #    for q in range(k):
    #        cluster[q][i] = random.randint(0, max_cluster_value) 

    #cluster_content = data_distribution(array, cluster)

    #privious_cluster = copy.deepcopy(cluster)
    #while 1:
    #    cluster = cluster_update(cluster, cluster_content, dim)
    #    cluster_content = data_distribution(array, cluster)
    #    if cluster == privious_cluster:
    #        break
    #    privious_cluster = copy.deepcopy(cluster)

    #print(cluster)
    #print('___________________________________________________________________________')
    #print(cluster_content)

    #Кластер агломеративныЙ
    #k1=6
    #agg_clustering = AgglomerativeClustering(n_clusters = k1, affinity = 'manhattan', linkage = 'average')
    #labels = agg_clustering.fit_predict(array)

    #zipped_list = zip(labels, array)
	# Returns zip object 

    #sorted_list = sorted(zipped_list)
	# Returns [(3, 'Falafel'), (4, 'Icaco'), (5, 'Nori'), (8, 'Xacuti'), (10, 'Tabbouleh'), (12, 'Escargot'), (18, 'Rouladen')]

    #array = [value[1] for value in sorted_list]
    #labels.sort()
    #xi=0
    #xarray=[]
   # new_list=[[],[],[],[],[],[]]
   # for i in range(len(array)):
   # 	for j in range(k1):
   # 		if labels[i]==j:
   # 			new_list[j].append(array[i])


    #Кластер DBSCAN

    #DBSCAN_clustering =DBSCAN()
    #labels =  DBSCAN_clustering.fit_predict(array)
    #zipped_list = zip(labels, array)
	# Returns zip object 

    #sorted_list = sorted(zipped_list)
	# Returns [(3, 'Falafel'), (4, 'Icaco'), (5, 'Nori'), (8, 'Xacuti'), (10, 'Tabbouleh'), (12, 'Escargot'), (18, 'Rouladen')]

    #array = [value[1] for value in sorted_list]
    #labels.sort()
    #xi=0
    #xarray=[]
    #new_list=[[],[],[],[],[],[]]
    #for i in range(len(array)):
    #	for j in range(k1):
    #		if labels[i]==j:
    #			new_list[j].append(array[i])

    #Кластер OPTICS

    #DBSCAN_clustering =OPTICS()
    #labels =  DBSCAN_clustering.fit_predict(array)
    #for i in labels:
    #	print(i)
    #zipped_list = zip(labels, array)
	# Returns zip object 

    #sorted_list = sorted(zipped_list)
	# Returns [(3, 'Falafel'), (4, 'Icaco'), (5, 'Nori'), (8, 'Xacuti'), (10, 'Tabbouleh'), (12, 'Escargot'), (18, 'Rouladen')]

    #array = [value[1] for value in sorted_list]
    #labels.sort()
    #xi=0
    #xarray=[]
    
    #new_list=[[],[],[],[],[],[]]
    #for i in range(len(array)):
    #	for j in range(k1):
    #		if labels[i]==j:
    #			new_list[j].append(array[i])

    #lst1 = Counter(labels).keys() 
    #print("output list : ",lst1)
    #print("No of unique elements in the list are:", len(lst1))
    #xqew=0
    #for i in labels:
    #	if i==-1:
    #		xqew=xqew+1
    #print(xqew)



    #list1=Test1.objects.exclude(participants=0)
    #myFile = open('D:\example3.csv', 'w')
    #with myFile:
    ##    writer = csv.writer(myFile)
    #    writer.writerow(['апрг','Cena',
    #           'avans','obespech','uchast','Economy'])
    #    
    #    for i in list1:
    #        writer.writerow([(i.data2-i.data1)/timedelta(days=1),i.sum0,int(i.prepayment[:-1]),float(i.provision[:-1]),i.participants,(i.sum0-i.totalprice)/i.sum0])
    #BIKE=pd.read_csv('D:\example3.csv')
    #pd.read_csv('D:\example3.csv')
    #numeric_col = ['Dlitelnost','Cena',
     #          'avans','obespech','uchast','Economy']
    #corr_matrix = BIKE.loc[:,numeric_col].corr()
    #print(corr_matrix)

    #Using heatmap to visualize the correlation matrix
    #plot=sn.heatmap(corr_matrix, annot=True)
    #plot_file = BytesIO() 
    #plot.figure.savefig(plot_file, format='png')
    #encoded_file = base64.b64encode(plot_file.getValue())




    print((datetime.now()-x1)/timedelta(seconds=1))
    return render(
        request,
        'watcher/stats.html',
        context={'category_list': category_list,
        'dict_cat':d,
        'dict_summ':s,
        'pies':pie}

        #'matrix':encoded_file
        #'cluster_content':cluster_content,
        #'cluster':cluster,
        #'new_list':new_list}
    )

def main_page(request):


    #list1=Test1.objects.exclude(participants=0)
    #myFile = open('D:\example3.csv', 'w')
    #with myFile:
    #    writer = csv.writer(myFile)
    #    writer.writerow(['Time' ,'Price',
    #           'Prepaid','Garant','N members','Economy'])
    #    
    #    for i in list1:
    #        writer.writerow([(i.data2-i.data1)/timedelta(days=1),i.sum0,int(i.prepayment[:-1]),float(i.provision[:-1]),i.participants,(i.sum0-i.totalprice)/i.sum0])
        return render(
        request,
        'watcher/main.html',
    )


def tender_page(request,tender_id):
    #Функция для отображения страницы тендера
	try:
		a=Test1.objects.get(idten=tender_id)
	except:
		raise Http404("Страница не найдена")
	
	return render(
		request,
		'watcher/tender_page.html',
		{'tender':a}
		)

def category_page(request,category_id):
    #Функция для отображения страницы тендера

    try:
        #a=Tender.objects.get(category=category_id)
        print('category')
        #category_name = Category.objects.get(idcategory=category_id)
        utc=pytz.UTC
        tender_list = Test1.objects.filter(category=category_id).iterator()
        n=[0,0,0,0,0]
        for i in tender_list:
            if i.data1.replace(tzinfo=utc)<datetime(2022,1,31,23,59).replace(tzinfo=utc):
                    n[0]+=1
            elif i.data1.replace(tzinfo=utc)<datetime(2022,2,28,23,59).replace(tzinfo=utc):
                n[1]+=1
            elif i.data1.replace(tzinfo=utc)<datetime(2022,3,31,23,59).replace(tzinfo=utc):
                n[2]+=1
            elif i.data1.replace(tzinfo=utc)<datetime(2022,4,30,23,59).replace(tzinfo=utc):
                n[3]+=1
            elif i.data1.replace(tzinfo=utc)<datetime(2022,5,31,23,59).replace(tzinfo=utc):
                n[4]+=1
        #for i in Test1.objects.all():
            #print(i.data2)
            #print(timezone.now())
            #if i.data2 <= timezone.now():
            #   i.status = Status.objects.get(idstatus = 4)
            #   i.save() 
            #if i.category == category_name:
                #tender_list.append(i)
        tender_list = Test1.objects.filter(category=category_id).values('idten','data1','name','sum0','region','status')
        for i in tender_list:
            i['region']=Region.objects.get(idregion=i['region']).regname
            i['status']=Status.objects.get(idstatus=i['status']).statusname
    except:
        raise Http404("Страница не найдена")
    
    return render(
        request,
        'watcher/category_page.html',
        {'tender_list':tender_list,
        'n':n
        }
        )

def analysis_page(request,category_id):
    #Функция для отображения страницы тендера
	try:
		#a=Tender.objects.get(category=category_id)
		category_name = Category.objects.get(idcategory=category_id)
		tender_list = Test1.objects.filter(category=category_id)
		#for i in Test1.objects.all():
			#print(i.data2)
			#print(timezone.now())
			#if i.data2 <= timezone.now():
			#	i.status = Status.objects.get(idstatus = 4)
			#	i.save() 
			#if i.category == category_name:
				#tender_list.append(i)
	except:
		raise Http404("Страница не найдена")
	
	return render(
		request,
		'watcher/analysis_page.html',
		{'tender_list':tender_list}
		)


#Класс регистрации нового пользователя
class Registr(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/registr.html"


class UserForm(UserCreationForm):
	first_name = forms.CharField(label="Имя")
	last_name = forms.CharField(label="Фамилия")
	email = forms.EmailField(label="Эл.почта")

	class Meta:
		model = User 
		fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2')

def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserForm()

	return render(request, 'registration/registr.html',{'form':form})