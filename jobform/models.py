from django.db import models

# Create your models here.


class JobApplication(models.Model):
    # basic details
    fname = models.CharField(max_length=200, blank=True)
    lname = models.CharField(max_length=200, blank=True)
    designation = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    mail = models.EmailField(max_length=254)
    city = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=200, blank=True)
    zip = models.CharField(max_length=200, blank=True)
    relation_status = models.CharField(max_length=200, blank=True)
    dob = models.CharField(max_length=200, null=True)

    # education details
    # SSC
    ssc_board_name = models.CharField(max_length=200, blank=True)
    ssc_year = models.CharField(max_length=200, blank=True)
    ssc_score = models.CharField(max_length=200, blank=True)

    # HSC / diploma (dip)
    hsc_dip_board_name = models.CharField(max_length=200, blank=True)
    hsc_dip_year = models.CharField(max_length=200, blank=True)
    hsc_dip_score = models.CharField(max_length=200, blank=True)

    # bachelor
    bachelor_course_name = models.CharField(max_length=200, blank=True)
    bachelor_uni_name = models.CharField(max_length=200, blank=True)
    bachelor_year = models.CharField(max_length=200, blank=True)
    bachelor_score = models.CharField(max_length=200, blank=True)

    # masters
    master_course_name = models.CharField(max_length=200, blank=True)
    master_uni_name = models.CharField(max_length=200, blank=True)
    master_year = models.CharField(max_length=200, blank=True)
    master_score = models.CharField(max_length=200, blank=True)

    # work exp company 1
    workexp_company1_name = models.CharField(max_length=200, blank=True)
    workexp_company1_designation = models.CharField(max_length=200, blank=True)
    workexp_company1_start_date = models.CharField(max_length=200, blank=True)
    workexp_company1_end_date = models.CharField(max_length=200, blank=True)

    # work exp company 2
    workexp_company2_name = models.CharField(max_length=200, blank=True)
    workexp_company2_designation = models.CharField(max_length=200, blank=True)
    workexp_company2_start_date = models.CharField(max_length=200, blank=True)
    workexp_company2_end_date = models.CharField(max_length=200, blank=True)

    # work exp company 3
    workexp_company3_name = models.CharField(max_length=200, blank=True)
    workexp_company3_designation = models.CharField(max_length=200, blank=True)
    workexp_company3_start_date = models.CharField(max_length=200, blank=True)
    workexp_company3_end_date = models.CharField(max_length=200, blank=True)

    # language hindi
    Language1 = models.CharField(max_length=200, blank=True)
    Language1_read = models.CharField(max_length=200, blank=True)
    Language1_write = models.CharField(max_length=200, blank=True)
    Language1_speak = models.CharField(max_length=200, blank=True)

    # language english
    Language2 = models.CharField(max_length=200, blank=True)
    Language2_read = models.CharField(max_length=200, blank=True)
    Language2_write = models.CharField(max_length=200, blank=True)
    Language2_speak = models.CharField(max_length=200, blank=True)

    # language gujarati
    Language3 = models.CharField(max_length=200, blank=True)
    Language3_Read = models.CharField(max_length=200, blank=True)
    Language3_Write = models.CharField(max_length=200, blank=True)
    Language3_Speak = models.CharField(max_length=200, blank=True)

    # technology php
    PHP = models.CharField(max_length=200, blank=True)
    beginnerPHP = models.CharField(max_length=200, blank=True)
    MideatorPHP = models.CharField(max_length=200, blank=True)
    ExpertPHP = models.CharField(max_length=200, blank=True)

    # technology mysql
    MYSQL = models.CharField(max_length=200, blank=True)
    BeginnerMYSQL = models.CharField(max_length=200, blank=True)
    MideatorMYSQL = models.CharField(max_length=200, blank=True)
    ExpertMYSQL = models.CharField(max_length=200, blank=True)

    # technology laravel
    Laravel = models.CharField(max_length=200, blank=True)
    BeginnerLaravel = models.CharField(max_length=200, blank=True)
    MideatorLaravel = models.CharField(max_length=200, blank=True)
    ExpertLaravel = models.CharField(max_length=200, blank=True)

    # technology oracle
    Oracle = models.CharField(max_length=200, blank=True)
    BeginnerOracle = models.CharField(max_length=200, blank=True)
    MideatorOracle = models.CharField(max_length=200, blank=True)
    ExpertOracle = models.CharField(max_length=200, blank=True)

    # refrence contact-1
    ref_name1 = models.CharField(max_length=200, blank=True)
    ref_contact1 = models.CharField(max_length=200, blank=True)
    ref_relation1 = models.CharField(max_length=200, blank=True)

    # refrence contact-2
    ref_name2 = models.CharField(max_length=200, blank=True)
    ref_contact2 = models.CharField(max_length=200, blank=True)
    ref_relation2 = models.CharField(max_length=200, blank=True)

    # preferance location
    location1 = models.CharField(max_length=200, blank=True)
    location2 = models.CharField(max_length=200, blank=True)
    location3 = models.CharField(max_length=200, blank=True)

    # notice period
    noticeperiod = models.CharField(max_length=200, blank=True)

    # Current and expected ctc
    expectedCTC = models.CharField(max_length=200, blank=True)
    currentCTC = models.CharField(max_length=200, blank=True)

    # department
    Department = models.CharField(max_length=200, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Applications_master"


class language(models.Model):
    jobapplicationDetails = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    language_choice = [('hindi', 'Hindi'), ('HindiSpeak', 'speak'), ]
    data = models.JSONField()

    class Meta:
        db_table = "languages"
