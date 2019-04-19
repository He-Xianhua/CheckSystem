# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CRecord(models.Model):
    number = models.AutoField(primary_key=True)
    c_id = models.CharField(db_column='C_id', max_length=20, blank=True, null=True, verbose_name=u"课程号")  # Field name made lowercase.
    c_name = models.CharField(db_column='C_name', max_length=255, blank=True, null=True, verbose_name=u"课程名")  # Field name made lowercase.
    notcome = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"未到情况")
    date = models.CharField(db_column='Date', max_length=255, blank=True, null=True, verbose_name=u"日期")  # Field name made lowercase.
    totalnum = models.IntegerField(blank=True, null=True, verbose_name=u"总人数")
    realnum = models.IntegerField(blank=True, null=True, verbose_name=u"实到人数")

    class Meta:
        managed = False
        db_table = 'c_record'
        verbose_name = "考勤记录"
        verbose_name_plural = verbose_name


class Course(models.Model):
    c_id = models.CharField(db_column='C_id', primary_key=True, max_length=20, verbose_name=u"课程号")  # Field name made lowercase.
    c_name = models.CharField(db_column='C_name', max_length=255, blank=True, null=True, verbose_name=u"课程名")  # Field name made lowercase.
    t_id = models.CharField(db_column='T_id', max_length=255, blank=True, null=True, verbose_name=u"老师ID")  # Field name made lowercase.
    week = models.CharField(db_column='Week', max_length=255, blank=True, null=True, verbose_name=u"课程安排")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'
        verbose_name = "课程"
        verbose_name_plural = verbose_name


class Learn(models.Model):
    number = models.AutoField(primary_key=True)
    s_id = models.CharField(db_column='S_id', max_length=20, verbose_name=u"学号")  # Field name made lowercase.
    c_name = models.CharField(db_column='C_name', max_length=20, null=True, verbose_name=u"课程名")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'learn'

        verbose_name = "学生选课情况"
        verbose_name_plural = verbose_name


class SRecord(models.Model):
    number = models.AutoField(primary_key=True)
    s_id = models.CharField(db_column='S_id', max_length=20, verbose_name=u"学号")  # Field name made lowercase.
    c_id = models.CharField(db_column='C_id', max_length=20, verbose_name=u"课程号")  # Field name made lowercase.
    c_name = models.CharField(db_column='C_name', max_length=20, verbose_name=u"课程名")  # Field name made lowercase.
    num = models.IntegerField(blank=True, null=True, verbose_name=u"缺勤次数")

    class Meta:
        managed = False
        db_table = 's_record'
        verbose_name = "学生考勤记录"
        verbose_name_plural = verbose_name



class Student(models.Model):
    s_id = models.CharField(db_column='S_id', primary_key=True, max_length=20, verbose_name=u"学号")  # Field name made lowercase.
    s_name = models.CharField(db_column='S_name', max_length=20, blank=True, null=True, verbose_name=u"姓名")  # Field name made lowercase.
    s_password = models.CharField(db_column='S_password', max_length=20, blank=True, null=True, verbose_name=u"密码")  # Field name made lowercase.
    # s_image = models.TextField(db_column='S_image', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'
        verbose_name = "学生"
        verbose_name_plural = verbose_name



class Teacher(models.Model):
    t_id = models.CharField(db_column='T_id', primary_key=True, max_length=20, verbose_name=u"教师编号")  # Field name made lowercase.
    t_name = models.CharField(db_column='T_name', max_length=20, blank=True, null=True, verbose_name=u"姓名")  # Field name made lowercase.
    t_password = models.CharField(db_column='T_password', max_length=20, blank=True, null=True, verbose_name=u"密码")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacher'
        verbose_name = "老师"
        verbose_name_plural = verbose_name

