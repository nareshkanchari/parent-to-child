from django.shortcuts import render
from .models import Courses_Data, Course_Category


# Create your views here.
def home(request):
    if request.method == "POST":
        category = request.POST.get('category', '')
        print(category, end='')
        cname = request.POST.get('cname', '')
        cdiscription = request.POST.get('cdiscription', '')
        cduration = request.POST.get('cduration')
        cprice = request.POST.get('cprice','')
        cid=Courses_Data.objects.all()[:]
        cid=cid.count()
        print(cid)
        if cid:
            cid=cid+1
        else:
            cid=1
        if category == '':
            category = cname
            cdata = Course_Category(c_category=category)
            cdata.save()
            category=Course_Category.objects.get(c_category=cname)
            print(category,"if")
            data = Courses_Data(
                cid=cid,
                course_name=cname,
                course_disctription=cdiscription,
                course_duration=cduration,
                course_price=cprice,
                course_category_id=category.ccid
            )
            print(category, "last")
            data.Course_Category = category.ccid
            print(data)
            data.save()
            return render(request, 'success.html', {'success': "you have successfully entered data"})

        else:
            category = Course_Category.objects.get(c_category=category)
            print(category,"else")

            data = Courses_Data(
                cid=cid,
                course_name=cname,
                course_disctription=cdiscription,
                course_duration=cduration,
                course_price=cprice,
                course_category_id=category.ccid
            )
            print(category,"last")
            data.Course_Category = category.ccid
            print(data)
            data.save()
            return render(request, 'success.html', {'success': "you have successfully entered data"})
    else:
        Ccategory = Course_Category.objects.all()
        return render(request, 'index.html', {'category': Ccategory})
