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
from datetime import datetime
from django.utils import timezone

import csv


 
@login_required #Проверка вошёл ли пользователь в свою учетную запись
def index(request):
    """
    Функция отображения для страницы просмотра тендеров.
    """	
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
    		[]
    		]
    for j in tender_list:
    	if j.idten not in t_id:
    		t_id.append(j.idten)
    with open('D:\Downloads\dost4.csv', newline='', encoding="utf-8") as f:
    	reader = csv.reader(f)
    	
    	for row in reader:
    		r_list=[]
    		#print(row)
    		if row[1]=='Номер тендера' or row[1]=='' or row[1] in t_id or row[5]=='':
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



    num_tenders=Tender.objects.all().count()
    tender_list = Test1.objects.all()
    category_list = Category.objects.all()
    n_tenders = [0]*((len(category_list))+1)
    for i in category_list:
    	#prices = Tender.summ.get(Tender.category.categorycol=i.categorycol)
    	for j in tender_list:
    		if j.category.categorycol == i.categorycol:
    			n_tenders[i.idcategory]+=1
    n_tenders.pop(0)


    
    
    for i in range (Category.objects.all().count()):
    	cat_list.append([0]*6)
    for i in range (Category.objects.all().count()):
    	min=1000000000000
    	max=0
    	act = 0
    	end = 0
    	cat_list[i][0]= (Category.objects.all())[i]
    	cat_list[i][1]= n_tenders[i]
    	for j in tender_list:
    		if j.category.categorycol==cat_list[i][0].categorycol:
    			if j.sum0 > max:
    				max = j.sum0
    			if j.sum0 < min:
    				min = j.sum0
    			if j.status.statusname == "Активный":
    				act+=1
    			else:
    				end+=1
    	cat_list[i][2]= min
    	cat_list[i][3]= max
    	cat_list[i][4]= act
    	cat_list[i][5]= end


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
    		[]
    		]
	for j in tender_list:
		if j.idten not in t_id:
			t_id.append(j.idten)
	with open('D:\Downloads\dost4.csv', newline='', encoding="utf-8") as f:
		reader = csv.reader(f)
		for row in reader:
			r_list=[]
    		#print(row)
			if row[1]=='Номер тендера' or row[1]=='' or row[1] in t_id or row[5]=='':
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
    tender_list = Tender.objects.all()
    num_tenders=Tender.objects.all().count()
    category_list = Category.objects.all()
    status_list = Status.objects.all()
    num_category = Category.objects.all().count()
    num_status = Status.objects.all().count()
    d=[]
    for i in range (num_category):
        d.append([0]*(num_status+2))
        d[i][0]=category_list[i].categorycol
        for j in  tender_list:
            if d[i][0] == j.category.categorycol and j.status.statusname == 'Активный':
                d[i][1]+=1
            elif d[i][0] == j.category.categorycol and j.status.statusname == 'Завершенный':
                d[i][2]+=1
            elif d[i][0] == j.category.categorycol and j.status.statusname == 'Несостоявшийся':
                d[i][3]+=1
        d[i][4]=d[i][1]+d[i][2]+d[i][3]
        if d[i][4]!=0:
            d[i][1]=d[i][1]/d[i][4]*100
            d[i][2]=d[i][2]/d[i][4]*100
            d[i][3]=d[i][3]/d[i][4]*100

    s=[]
    for i in range (num_category):
        s.append([0]*3)
        s[i][0]=category_list[i].categorycol
        for j in  tender_list:
            if s[i][0] == j.category.categorycol:
                s[i][1]+=j.summ
                s[i][2]+=1
        if s[i][2] != 0:
            s[i][1] = s[i][1]/s[i][2]
    print(d)        
    return render(
        request,
        'watcher/stats.html',
        context={'category_list': category_list,'num_tenders': num_tenders,'status_list': status_list,'dict_cat':d,'dict_summ':s},
    )

def main_page(request):
	    return render(
        request,
        'watcher/main.html',
    )


def tender_page(request,tender_id):
    #Функция для отображения страницы тендера
	try:
		a=Tender.objects.get(idtender=tender_id)
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
		category_name = Category.objects.get(idcategory=category_id)
		tender_list = []
		for i in Test1.objects.all():
			#print(i.data2)
			#print(timezone.now())
			#if i.data2 <= timezone.now():
			#	i.status = Status.objects.get(idstatus = 4)
			#	i.save() 
			if i.category == category_name:
				tender_list.append(i)
	except:
		raise Http404("Страница не найдена")
	
	return render(
		request,
		'watcher/category_page.html',
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