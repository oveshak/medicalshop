from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from homehero.models import About, Counter, Service, Slider,Testimonial
from doctor.models import Doctors
from appointment.models import Appointments,Contacts
from blog.models import AllBlog, Blogss
from department.models import Department
from globals.models import Global
from protfolio.models import Protfolio_Category,Protfolios
# Create your views here.



class CommonMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Protfolio_Category.objects.all()
        context['protfolio'] = Protfolios.objects.all()
        context['doctor'] = Doctors.objects.all()
        context['counter'] = Counter.objects.first()
        context['blog'] = AllBlog.objects.first()
        context['ter']=Testimonial.objects.all()
        context['glo']=Global.objects.first()

        return context
        



class Index(CommonMixin ,TemplateView):
    template_name = "temp/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.first()  # Retrieve the 'sliders' data
        context['about'] = About.objects.first()
        context['service'] = Service.objects.first()
        # context['testimonials'] = Testimonial.objects.all()
        return context
    def post(self,request,*args, **kwargs):
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        data=request.POST.get('date')
       
        message=request.POST.get('message')

        #update_date=datetime.strptime(data,'%Y-%m-%d').strftime('%d-%m-%Y')

        Appointments.objects.create(
            lname=lname,
            fname=fname,
            phone=phone,
            subject=subject,
            data=data,
            email=email,
            message=message,
        )

        return redirect('contact')


class Doctor_Team(CommonMixin,TemplateView):
    template_name = "temp/team-col-4.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
    #     context['doctor'] = Doctors.objects.all()
    #     return context

class Doctor_Details( TemplateView):

    template_name = "temp/team-details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug=self.kwargs.get('slug')
        context['doctor']=Doctors.objects.get(slug=slug)
        # context['doctor'] = .objects.first()
        context['allBlog'] = AllBlog.objects.first()
        return context

class Protfolio(CommonMixin,TemplateView):
    template_name = "temp/portfolio-col-3.html"

class Blog(CommonMixin,TemplateView):
    template_name = "temp/blog-grid.html"
class BlogDetails(CommonMixin,TemplateView):
    template_name = "temp/blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['blog'] = Blogss.objects.get(slug=slug)
        context['allBlog'] = AllBlog.objects.first()
        
        return context



class Contact(CommonMixin,TemplateView):
    template_name = "temp/contact-style-1.html"
    def post(self,request,*args, **kwargs):
        name=request.POST.get('name')
       
        email=request.POST.get('email')
        
        subject=request.POST.get('subject')
        
       
        message=request.POST.get('message')

        #update_date=datetime.strptime(data,'%Y-%m-%d').strftime('%d-%m-%Y')

        Contacts.objects.create(
            name=name,
            subject=subject,
            email=email,
            message=message,
        )

        return redirect('index')



class Cardiologists_Department(CommonMixin, TemplateView):
    template_name = "temp/depertment-1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept'] = Department.objects.filter(dept_name="Cardiologists").first()  # Get the Cardiologists department
        context['dept_doctor'] = Doctors.objects.filter(profession_name__regex=r'(?i)cardiologists')  # Get all doctors in Cardiologists
        print(f"doctor {context}")
        return context
    

class Orthopaedics_Department(CommonMixin,TemplateView):
    template_name = "temp/depertment-1.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept'] = Department.objects.filter(dept_name="Orthopaedics").first()  # Get the Cardiologists department
        context['dept_doctor'] = Doctors.objects.filter(profession_name__regex=r'(?i)orthopaedics')  # Get all doctors in Cardiologists
        print(f"doctor {context}")
        return context

class Gastroenterology_Department(CommonMixin,TemplateView):
    template_name = "temp/depertment-1.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept'] = Department.objects.filter(dept_name="Gastroenterology").first()  # Get the Cardiologists department
        context['dept_doctor'] = Doctors.objects.filter(profession_name__regex=r'(?i)gastroenterology')  # Get all doctors in Cardiologists
        print(f"doctor {context}")
        return context

class Neuroscience_Department(CommonMixin,TemplateView):
    template_name = "temp/depertment-1.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept'] = Department.objects.filter(dept_name="Neurosciences").first()  # Get the Cardiologists department
        context['dept_doctor'] = Doctors.objects.filter(profession_name__regex=r'(?i)neuroscience')  # Get all doctors in Cardiologists
        print(f"doctor {context}")
        return context

class Spine_Department(CommonMixin,TemplateView):
    template_name = "temp/depertment-1.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept'] = Department.objects.filter(dept_name="Spine").first()  # Get the Cardiologists department
        context['dept_doctor'] = Doctors.objects.filter(profession_name__regex=r'(?i)spine')  # Get all doctors in Cardiologists
        print(f"doctor {context}")
        return context

class Cancer_Department(CommonMixin,TemplateView):
    template_name = "temp/depertment-1.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept'] = Department.objects.filter(dept_name="Cancer").first()  # Get the Cardiologists department
        context['dept_doctor'] = Doctors.objects.filter(profession_name__regex=r'(?i)cancer')  # Get all doctors in Cardiologists
        print(f"doctor {context}")
        return context

class Colorectal_Department(CommonMixin,TemplateView):
    template_name = "temp/depertment-1.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept'] = Department.objects.filter(dept_name="Colorectal").first()  # Get the Cardiologists department
        context['dept_doctor'] = Doctors.objects.filter(profession_name__regex=r'(?i)colorectal')  # Get all doctors in Cardiologists
        print(f"doctor {context}")
        return context

class Bariatric_Department(CommonMixin, TemplateView):
    template_name = "temp/depertment-1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dept'] = Department.objects.filter(dept_name="Bariatric").first()  # Get the Bariatric department
        context['dept_doctor'] = Doctors.objects.filter(profession_name__regex=r'(?i)bariatric')  # Filter doctors with regex
       
        return context
    
class Shop_Details(CommonMixin,TemplateView):
    template_name = "temp/shop-single.html"

class Shop_List(CommonMixin,TemplateView):
    template_name = "temp/shop-list.html"

# class Bariatric_Department(TemplateView):
#     template_name = "temp/depertment-8.html"