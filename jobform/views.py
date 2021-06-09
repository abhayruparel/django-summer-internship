from django.shortcuts import render, redirect
from jobform.models import JobApplication


# from django.http import HttpResponse

# from .forms import JobApplicationForm
# Create your views here.


# def jobForm(request):

# 	form = JobApplicationForm()

# 	if request.method == 'POST':
# 		form = JobApplicationForm(request.POST)
# 		if form.is_valid():
# 			form.save()

# 	context = {'form': form}
# 	return render(request, 'mainForm.html', context)


def oldForm(request):
    form = JobApplication()
    if request.method == "POST":
        form = JobApplication(request.POST)
        print(form)
        # if form.is_valid():
        # print(form.cleaned_data)
        # basic details
        print('Received a form submission')
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        designation = request.POST["designation"]
        address = request.POST["address"]
        mail = request.POST["mail"]
        city = request.POST["city"]
        phone = request.POST["phone"]
        gender = request.POST.get("gender", False)
        zip1 = request.POST["zip"]
        relation_status = request.POST["relation_status"]
        dob = request.POST["dob"]

        # education details
        # SSC
        ssc_board_name = request.POST["ssc_board_name"]
        ssc_year = request.POST["ssc_year"]
        ssc_score = request.POST["ssc_score"]

        # HSC / diploman (dip)
        hsc_dip_board_name = request.POST["hsc_dip_board_name"]
        hsc_dip_year = request.POST["hsc_dip_year"]
        hsc_dip_score = request.POST["hsc_dip_score"]

        # bachelor
        bachelor_course_name = request.POST["bachelor_course_name"]
        bachelor_uni_name = request.POST["bachelor_uni_name"]
        bachelor_year = request.POST["bachelor_year"]
        bachelor_score = request.POST["bachelor_score"]

        # masters
        master_course_name = request.POST["master_course_name"]
        master_uni_name = request.POST["master_uni_name"]
        master_year = request.POST["master_year"]
        master_score = request.POST["master_score"]

        # work exp company 1
        workexp_company1_name = request.POST["workexp_company1_name"]
        workexp_company1_designation = request.POST["workexp_company1_designation"]
        workexp_company1_start_date = request.POST["workexp_company1_start_date"]
        workexp_company1_end_date = request.POST["workexp_company1_end_date"]

        # work exp company 2
        workexp_company2_name = request.POST["workexp_company2_name"]
        workexp_company2_designation = request.POST["workexp_company2_designation"]
        workexp_company2_start_date = request.POST["workexp_company2_start_date"]
        workexp_company2_end_date = request.POST["workexp_company2_end_date"]

        # work exp company 3
        workexp_company3_name = request.POST["workexp_company3_name"]
        workexp_company3_designation = request.POST["workexp_company3_designation"]
        workexp_company3_start_date = request.POST["workexp_company3_start_date"]
        workexp_company3_end_date = request.POST["workexp_company3_end_date"]

        # language hindi
        Language1 = request.POST.get("Language1", False)
        Language1_read = request.POST.get("Language1_read", False)
        Language1_write = request.POST.get("Language1_write", False)
        Language1_speak = request.POST.get("Language1_speak", False)

        # language english
        Language2 = request.POST.get("Language2", False)
        Language2_read = request.POST.get("Language2_read", False)
        Language2_write = request.POST.get("Language2_write", False)
        Language2_speak = request.POST.get("Language2_speak", False)

        # language gujarati
        Language3 = request.POST.get("Language3", False)
        Language3_Read = request.POST.get("Language3_Read", False)
        Language3_Write = request.POST.get("Language3_Write", False)
        Language3_Speak = request.POST.get("Language3_Speak", False)

        # technology php
        PHP = request.POST.get("PHP", False)
        beginnerPHP = request.POST.get("beginnerPHP", False)
        MideatorPHP = request.POST.get("MideatorPHP", False)
        ExpertPHP = request.POST.get("ExpertPHP", False)

        # technology mysql
        MYSQL = request.POST.get("MYSQL", False)
        BeginnerMYSQL = request.POST.get("BeginnerMYSQL", False)
        MideatorMYSQL = request.POST.get("MideatorMYSQL", False)
        ExpertMYSQL = request.POST.get("ExpertMYSQL", False)

        # technology laravel
        Laravel = request.POST.get("Laravel", False)
        BeginnerLaravel = request.POST.get("BeginnerLaravel", False)
        MideatorLaravel = request.POST.get("MideatorLaravel", False)
        ExpertLaravel = request.POST.get("ExpertLaravel", False)

        # technology oracle
        Oracle = request.POST.get("Oracle", False)
        BeginnerOracle = request.POST.get("BeginnerOracle", False)
        MideatorOracle = request.POST.get("MideatorOracle", False)
        ExpertOracle = request.POST.get("ExpertOracle", False)

        # reference contact-1
        ref_name1 = request.POST["ref_name1"]
        ref_contact1 = request.POST["ref_contact1"]
        ref_relation1 = request.POST["ref_relation1"]

        # reference contact-2
        ref_name2 = request.POST["ref_name2"]
        ref_contact2 = request.POST["ref_contact2"]
        ref_relation2 = request.POST["ref_relation2"]

        # preferance location
        location1 = request.POST.get("location1", False)
        location2 = request.POST.get("location2", False)
        location3 = request.POST.get("location3", False)

        # notice period
        noticeperiod = request.POST["noticeperiod"]

        # Current and expected ctc
        expectedCTC = request.POST["expectedCTC"]
        currentCTC = request.POST["currentCTC"]

        # department
        Department = request.POST["Department"]
        ins = JobApplication(
            fname=fname,
            lname=lname,
            designation=designation,
            address=address,
            mail=mail,
            city=city,
            phone=phone,
            gender=gender,
            zip=zip1,
            relation_status=relation_status,
            dob=dob,
            ssc_board_name=ssc_board_name,
            ssc_year=ssc_year,
            ssc_score=ssc_score,
            hsc_dip_board_name=hsc_dip_board_name,
            hsc_dip_year=hsc_dip_year,
            hsc_dip_score=hsc_dip_score,
            bachelor_course_name=bachelor_course_name,
            bachelor_uni_name=bachelor_uni_name,
            bachelor_year=bachelor_year,
            bachelor_score=bachelor_score,
            master_course_name=master_course_name,
            master_uni_name=master_uni_name,
            master_year=master_year,
            master_score=master_score,
            workexp_company1_name=workexp_company1_name,
            workexp_company1_designation=workexp_company1_designation,
            workexp_company1_start_date=workexp_company1_start_date,
            workexp_company1_end_date=workexp_company1_end_date,
            workexp_company2_name=workexp_company2_name,
            workexp_company2_designation=workexp_company2_designation,
            workexp_company2_start_date=workexp_company2_start_date,
            workexp_company2_end_date=workexp_company2_end_date,
            workexp_company3_name=workexp_company3_name,
            workexp_company3_designation=workexp_company3_designation,
            workexp_company3_start_date=workexp_company3_start_date,
            workexp_company3_end_date=workexp_company3_end_date,
            Language1=Language1,
            Language1_read=Language1_read,
            Language1_write=Language1_write,
            Language1_speak=Language1_speak,
            Language2=Language2,
            Language2_read=Language2_read,
            Language2_write=Language2_write,
            Language2_speak=Language2_speak,
            Language3=Language3,
            Language3_Read=Language3_Read,
            Language3_Write=Language3_Write,
            Language3_Speak=Language3_Speak,
            PHP=PHP,
            beginnerPHP=beginnerPHP,
            MideatorPHP=MideatorPHP,
            ExpertPHP=ExpertPHP,
            MYSQL=MYSQL,
            BeginnerMYSQL=BeginnerMYSQL,
            MideatorMYSQL=MideatorMYSQL,
            ExpertMYSQL=ExpertMYSQL,
            Laravel=Laravel,
            BeginnerLaravel=BeginnerLaravel,
            MideatorLaravel=MideatorLaravel,
            ExpertLaravel=ExpertLaravel,
            Oracle=Oracle,
            BeginnerOracle=BeginnerOracle,
            MideatorOracle=MideatorOracle,
            ExpertOracle=ExpertOracle,
            ref_name1=ref_name1,
            ref_contact1=ref_contact1,
            ref_relation1=ref_relation1,
            ref_name2=ref_name2,
            ref_contact2=ref_contact2,
            ref_relation2=ref_relation2,
            location1=location1,
            location2=location2,
            location3=location3,
            noticeperiod=noticeperiod,
            expectedCTC=expectedCTC,
            currentCTC=currentCTC,
            Department=Department,
        )
        ins.save()
        print(id, fname, ' ', lname)
        return redirect("/showApplicants")
        # else:
        #     print(form.errors)
    return render(request, "old_mainForm.html")


def showApplications(request):
    applications = JobApplication.objects.all()
    return render(request, "showApplication.html", {'application': applications})


def editApplication(request, id):
    applications = JobApplication.objects.get(id=id)
    return render(request, 'editApplication.html', {'application': applications})


def updateApplication(request, id):
    # form = JobApplication(request.POST, instance=applications)
    # if form.is_valid():
    #     form.save()
    if request.method == "POST":
        # applications = JobApplication.objects.get(id=id)
        # basic details
        print('update request found')
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        designation = request.POST["designation"]
        address = request.POST["address"]
        mail = request.POST["mail"]
        city = request.POST["city"]
        phone = request.POST["phone"]
        gender = request.POST.get("gender", False)
        zip1 = request.POST["zip"]
        relation_status = request.POST["relation_status"]
        dob = request.POST["dob"]

        # education details
        # SSC
        ssc_board_name = request.POST["ssc_board_name"]
        ssc_year = request.POST["ssc_year"]
        ssc_score = request.POST["ssc_score"]

        # HSC / diploman (dip)
        hsc_dip_board_name = request.POST["hsc_dip_board_name"]
        hsc_dip_year = request.POST["hsc_dip_year"]
        hsc_dip_score = request.POST["hsc_dip_score"]

        # bachelor
        bachelor_course_name = request.POST["bachelor_course_name"]
        bachelor_uni_name = request.POST["bachelor_uni_name"]
        bachelor_year = request.POST["bachelor_year"]
        bachelor_score = request.POST["bachelor_score"]

        # masters
        master_course_name = request.POST["master_course_name"]
        master_uni_name = request.POST["master_uni_name"]
        master_year = request.POST["master_year"]
        master_score = request.POST["master_score"]

        # work exp company 1
        workexp_company1_name = request.POST["workexp_company1_name"]
        workexp_company1_designation = request.POST["workexp_company1_designation"]
        workexp_company1_start_date = request.POST["workexp_company1_start_date"]
        workexp_company1_end_date = request.POST["workexp_company1_end_date"]

        # work exp company 2
        workexp_company2_name = request.POST["workexp_company2_name"]
        workexp_company2_designation = request.POST["workexp_company2_designation"]
        workexp_company2_start_date = request.POST["workexp_company2_start_date"]
        workexp_company2_end_date = request.POST["workexp_company2_end_date"]

        # work exp company 3
        workexp_company3_name = request.POST["workexp_company3_name"]
        workexp_company3_designation = request.POST["workexp_company3_designation"]
        workexp_company3_start_date = request.POST["workexp_company3_start_date"]
        workexp_company3_end_date = request.POST["workexp_company3_end_date"]

        # language hindi
        Language1 = request.POST.get("Language1", False)
        Language1_read = request.POST.get("Language1_read", False)
        Language1_write = request.POST.get("Language1_write", False)
        Language1_speak = request.POST.get("Language1_speak", False)

        # language english
        Language2 = request.POST.get("Language2", False)
        Language2_read = request.POST.get("Language2_read", False)
        Language2_write = request.POST.get("Language2_write", False)
        Language2_speak = request.POST.get("Language2_speak", False)

        # language gujarati
        Language3 = request.POST.get("Language3", False)
        Language3_Read = request.POST.get("Language3_Read", False)
        Language3_Write = request.POST.get("Language3_Write", False)
        Language3_Speak = request.POST.get("Language3_Speak", False)

        # technology php
        PHP = request.POST.get("PHP", False)
        beginnerPHP = request.POST.get("beginnerPHP", False)
        MideatorPHP = request.POST.get("MideatorPHP", False)
        ExpertPHP = request.POST.get("ExpertPHP", False)

        # technology mysql
        MYSQL = request.POST.get("MYSQL", False)
        BeginnerMYSQL = request.POST.get("BeginnerMYSQL", False)
        MideatorMYSQL = request.POST.get("MideatorMYSQL", False)
        ExpertMYSQL = request.POST.get("ExpertMYSQL", False)

        # technology laravel
        Laravel = request.POST.get("Laravel", False)
        BeginnerLaravel = request.POST.get("BeginnerLaravel", False)
        MideatorLaravel = request.POST.get("MideatorLaravel", False)
        ExpertLaravel = request.POST.get("ExpertLaravel", False)

        # technology oracle
        Oracle = request.POST.get("Oracle", False)
        BeginnerOracle = request.POST.get("BeginnerOracle", False)
        MideatorOracle = request.POST.get("MideatorOracle", False)
        ExpertOracle = request.POST.get("ExpertOracle", False)

        # reference contact-1
        ref_name1 = request.POST["ref_name1"]
        ref_contact1 = request.POST["ref_contact1"]
        ref_relation1 = request.POST["ref_relation1"]

        # reference contact-2
        ref_name2 = request.POST["ref_name2"]
        ref_contact2 = request.POST["ref_contact2"]
        ref_relation2 = request.POST["ref_relation2"]

        # preferance location
        location1 = request.POST.get("location1", False)
        location2 = request.POST.get("location2", False)
        location3 = request.POST.get("location3", False)

        # notice period
        noticeperiod = request.POST["noticeperiod"]

        # Current and expected ctc
        expectedCTC = request.POST["expectedCTC"]
        currentCTC = request.POST["currentCTC"]

        # department
        Department = request.POST["Department"]
        applications = JobApplication.objects.filter(id=id).update(
            fname=fname,
            lname=lname,
            designation=designation,
            address=address,
            mail=mail,
            city=city,
            phone=phone,
            gender=gender,
            zip=zip1,
            relation_status=relation_status,
            dob=dob,
            ssc_board_name=ssc_board_name,
            ssc_year=ssc_year,
            ssc_score=ssc_score,
            hsc_dip_board_name=hsc_dip_board_name,
            hsc_dip_year=hsc_dip_year,
            hsc_dip_score=hsc_dip_score,
            bachelor_course_name=bachelor_course_name,
            bachelor_uni_name=bachelor_uni_name,
            bachelor_year=bachelor_year,
            bachelor_score=bachelor_score,
            master_course_name=master_course_name,
            master_uni_name=master_uni_name,
            master_year=master_year,
            master_score=master_score,
            workexp_company1_name=workexp_company1_name,
            workexp_company1_designation=workexp_company1_designation,
            workexp_company1_start_date=workexp_company1_start_date,
            workexp_company1_end_date=workexp_company1_end_date,
            workexp_company2_name=workexp_company2_name,
            workexp_company2_designation=workexp_company2_designation,
            workexp_company2_start_date=workexp_company2_start_date,
            workexp_company2_end_date=workexp_company2_end_date,
            workexp_company3_name=workexp_company3_name,
            workexp_company3_designation=workexp_company3_designation,
            workexp_company3_start_date=workexp_company3_start_date,
            workexp_company3_end_date=workexp_company3_end_date,
            Language1=Language1,
            Language1_read=Language1_read,
            Language1_write=Language1_write,
            Language1_speak=Language1_speak,
            Language2=Language2,
            Language2_read=Language2_read,
            Language2_write=Language2_write,
            Language2_speak=Language2_speak,
            Language3=Language3,
            Language3_Read=Language3_Read,
            Language3_Write=Language3_Write,
            Language3_Speak=Language3_Speak,
            PHP=PHP,
            beginnerPHP=beginnerPHP,
            MideatorPHP=MideatorPHP,
            ExpertPHP=ExpertPHP,
            MYSQL=MYSQL,
            BeginnerMYSQL=BeginnerMYSQL,
            MideatorMYSQL=MideatorMYSQL,
            ExpertMYSQL=ExpertMYSQL,
            Laravel=Laravel,
            BeginnerLaravel=BeginnerLaravel,
            MideatorLaravel=MideatorLaravel,
            ExpertLaravel=ExpertLaravel,
            Oracle=Oracle,
            BeginnerOracle=BeginnerOracle,
            MideatorOracle=MideatorOracle,
            ExpertOracle=ExpertOracle,
            ref_name1=ref_name1,
            ref_contact1=ref_contact1,
            ref_relation1=ref_relation1,
            ref_name2=ref_name2,
            ref_contact2=ref_contact2,
            ref_relation2=ref_relation2,
            location1=location1,
            location2=location2,
            location3=location3,
            noticeperiod=noticeperiod,
            expectedCTC=expectedCTC,
            currentCTC=currentCTC,
            Department=Department,
        )
        print(f"ID:- {id} update application done")
        return redirect("/showApplicants")
    print('im here')
    return render(request, 'editApplication.html', {'application': applications})


def deleteApplication(request, id):
    applications = JobApplication.objects.get(id=id)
    print(f"Deleting {applications.fname}, {applications.id}")
    applications.delete()
    return redirect("/showApplicants")


def test(request):
    hindi = request.POST["Hindi"]
    obj = JobApplication(Language1=hindi,)
    obj.save()
