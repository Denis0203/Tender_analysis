# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addres(models.Model):
    idaddress = models.IntegerField(primary_key=True)
    addresscol = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.addresscol

    class Meta:
        managed = False
        db_table = 'address'
        verbose_name='Адрес'
        verbose_name_plural = 'Адреса'


class Application(models.Model):
    idapplication = models.IntegerField(primary_key=True)
    tender = models.ForeignKey('Tender', models.DO_NOTHING, db_column='tender', blank=True, null=True)
    client = models.ForeignKey('Client', models.DO_NOTHING, db_column='client', blank=True, null=True)
    partner = models.ForeignKey('Partner', models.DO_NOTHING, db_column='partner', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    vender = models.ForeignKey('Vender', models.DO_NOTHING, db_column='vender', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'application'
        verbose_name='Адрес'
        verbose_name_plural = 'Адресы'



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    idcategory = models.IntegerField(primary_key=True)

    categorycol = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.categorycol

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name='Категория'
        verbose_name_plural = 'Категории'


class Client(models.Model):
    idclient = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    inn = models.IntegerField(db_column='INN', blank=True, null=True)  # Field name made lowercase.
    address = models.ForeignKey(Addres, models.DO_NOTHING, db_column='address', blank=True, null=True)
    e_mail = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'client'
        verbose_name='Клиент'
        verbose_name_plural = 'Клиенты'



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Partner(models.Model):
    idpartner = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    inn = models.IntegerField(db_column='INN', blank=True, null=True)  # Field name made lowercase.
    address = models.ForeignKey(Addres, models.DO_NOTHING, db_column='address', blank=True, null=True)
    e_mail = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'partner'
        verbose_name='Партнер'
        verbose_name_plural = 'Партнеры'



class Region(models.Model):
    idregion = models.IntegerField(primary_key=True)

    regname = models.TextField( blank=True, null=True)

    def __str__(self):
        return self.regname


    class Meta:
        managed = False
        db_table = 'region'
        verbose_name='Регион'
        verbose_name_plural = 'Регионы'


class Status(models.Model):
    idstatus = models.IntegerField(primary_key=True)
    statusname = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.statusname

    class Meta:
        managed = False
        db_table = 'status'
        verbose_name='Статус'
        verbose_name_plural = 'Статусы'


class Tender(models.Model):
    idtender = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    status = models.ForeignKey('Status', models.DO_NOTHING, db_column='status', blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)
    data2 = models.DateTimeField(blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='unit', blank=True, null=True)
    summ = models.FloatField(blank=True, null=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='region', blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tender'
        verbose_name='Тендер'
        verbose_name_plural = 'Тендеры'


class Unit(models.Model):
    idunit = models.IntegerField(primary_key=True)

    unitname = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.unitname

    class Meta:
        managed = False
        db_table = 'unit'


class Vender(models.Model):
    idvender = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    inn = models.IntegerField(db_column='INN', blank=True, null=True)  # Field name made lowercase.
    address = models.ForeignKey(Addres, models.DO_NOTHING, db_column='address', blank=True, null=True)
    e_mail = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name
        
    class Meta:
        managed = False
        db_table = 'vender'

class Inn(models.Model):
    idi = models.IntegerField(primary_key=True)
    inn = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Test1(models.Model):
    idten = models.IntegerField(primary_key=True)
    name = models.TextField()
    data1 = models.DateTimeField()
    data2 = models.DateTimeField()
    inn = models.ForeignKey(Inn, models.DO_NOTHING, db_column='watcher_inn', blank=True, null=True)
    sum0 = models.BigIntegerField(blank=True, null=True)
    prepayment = models.TextField(blank=True, null=True)
    provision = models.TextField(blank=True, null=True)
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='region', blank=True, null=True)
    source = models.TextField()
    category =  models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    status = models.ForeignKey(Status, models.DO_NOTHING, db_column='status', blank=True, null=True)
    totalprice = models.IntegerField(default=0,blank=True, null=True)
    participants = models.IntegerField(default=0,blank=True, null=True)
    
    def __str__(self):
        return self.name
        
