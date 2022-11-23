from django.shortcuts import render,redirect
from .models import Admin
from core_app.models import *



# Create your views here.
def getfilename(img):
    temp=str(img).split('/')
    # print('temp')
    return temp[len(temp)-1]

def is_email_exist(email):
    try:
        status=Admin.objects.filter(email__iexact=email).exists()  #if not exsists RETURNS FALSE'
        return status #means email already exists
    except:
        return None



# Create your views here.
def login(request):
    return render(request,'admn_login.html')

def register(request):
    if request.method=='POST':
        user_data=request.POST.dict()
        email_varification_status=is_email_exist(user_data['email'])
        data={'redirect_url':'/admin','message':None}
        
        if email_varification_status:
            data['message']=f'{user_data["email"]} already exists!'
            return render(request,'alert.html',data)
        elif email_varification_status is None:
            data['message']='Unable to verify your email!, try later'
            return render(request,'alert.html',data)
        try:
            user_object=Admin(
                    email=user_data['email'],
                    fullname=user_data['fullname'],
                    password=user_data['password'] )
            user_object.save()
            request.session['ssk_logged_user_id'] = user_object.id  #session created
            return redirect('/dashboard')
        except Exception as e:
            data['message']=f'Unable to complete the request, Error: {str(e)}'
            return render(request,'alert.html',data)

    else:
        # return redirect('    else:
        return render(request,'admn_register.html')

    #     try:
    #         user_obj=Users(email=)

    # pass

def dashboard(request):
    return render(request,'admn_dashboard.html')

def products(request):

    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        product_obj=ProductCard(
                heighliter=request.POST['heighliter'],
                title=request.POST['title'],
                img=request.FILES['img'],
        )
        product_obj.save()
        product_obj.filename=getfilename(product_obj.img)
        product_obj.save()
        return redirect('/admin/products')
    if request.method=='GET':
        products=ProductCard.objects.all().order_by('-updated_at')
        context={'products':products}
        return render(request,'admn_product_update.html',context)
def product_update(request,pid):
    if request.method=='POST':
        product_obj=ProductCard.objects.filter(id=pid).get()
        product_obj.heighliter=request.POST['heighliter']
        product_obj.title=request.POST['title']
        product_obj.img=request.FILES.get('img')
        product_obj.save()
        product_obj.filename=getfilename(product_obj.img)
        product_obj.save()
    return redirect('/admin/products')

def site_update(request):
    return render(request,'admn_site_update.html')

def socialmedia_contact_update(request):
    return render(request,'admn_socialmedia_contact.html')

def logout(request):
    return render(request,'admn_base.html')