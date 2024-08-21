from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Service, Project, Blog, BlogHero, Details, Testimonial, Teamwork ,About,TopService,HeroHeader

# from .models import ContactFormSubmission
# views.py

from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country_code = request.POST.get('countryCode')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        email = request.POST.get('email')

        message = f'Name: {name}\nCountry Code: {country_code}\nPhone: {phone}\nMessage: {subject}\nEmail: {email}'

        try:
            send_mail(
                'Contact Form Submission',  # Subject
                message,  # Message
                email,  # From Email (User's Email)
                ['ayanguradi2@gmail.com'],  # To Email (Your Email)
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except BadHeaderError:
            return JsonResponse({'success': False, 'message': 'Invalid header found.'})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})

def service_page(request):
    services = Service.objects.all()
    return render(request, 'service_page.html',{'services': services,})

def blog_list(request):
    blogs = Blog.objects.all()
    hero = BlogHero.objects.first()
    services = Service.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs, 'hero': hero,'services': services,})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    services = Service.objects.all()
    return render(request, 'blog_detail.html', {'blog': blog,'services': services,})


def home(request):
    top_services = TopService.objects.all()
    services = Service.objects.all()
    hero_header = HeroHeader.objects.first()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    teamwork = Teamwork.objects.first()  
    return render(request, 'index.html', {
        'top_services': top_services,
        'services': services,
        'hero_header': hero_header,
        'projects': projects,
        'testimonials': testimonials,
        'teamwork': teamwork
    })

def details_context_processor(request):
    details = Details.objects.first()  # Assuming you have only one set of details
    return {'details': details}

def about(request):
    services = Service.objects.all()
    return render(request, 'about.html',{'services': services,})

# def services(request):
#     services = Service.objects.all()
#     return render(request, 'services.html', {'services': services})

def service_detail(request, pk):
    services = Service.objects.all()
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service,'services': services,})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})


def contact(request):
    if request.method == 'POST':
        # Handle contact form submission
        pass
    return render(request, 'main/contact.html')


# def projects_view(request):
#     categories = Project.CATEGORY_CHOICES
#     projects = {category[0]: Project.objects.filter(category=category[0]) for category in categories}
#     return render(request, 'projects.html', {'projects': projects, 'categories': categories})

# def service_detail(request, pk):
#     service = get_object_or_404(Service, pk=pk)
#     return render(request, 'service_detail.html', {'service': service})

