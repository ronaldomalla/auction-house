from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . models import contact,drawing_product,painting_product,sculpture_product,photographic_product,carving_product,bid
from .forms import login_form,register_form
from django.contrib.auth import login,authenticate,get_user_model
from django.views.generic import ListView


# Create your views here.
def index(request):
    drawpost=drawing_product.objects.all()
    paintpost = painting_product.objects.all()
    carvpost = carving_product.objects.all()
    sculppost = sculpture_product.objects.all()
    photopost = photographic_product.objects.all()
    context={
        'drawing_product': drawpost,
        'painting_product':paintpost,
        'carving_product': carvpost,
        'sculpture_product': sculppost,
        'photographic_product': photopost
    }


    if request.method == 'POST':
        fullname_f = request.POST.get('fullname')
        email_e = request.POST.get('email')
        number_n= request.POST.get('number')
        message_m = request.POST.get('message')

        c = contact(full_name=fullname_f, email=email_e,number=number_n, message=message_m)
        c.save()

        return HttpResponse("thank you for message..")
    else:

      return render(request,'auction_house/index.html',context)




def login_page(request):

    form=login_form(request.POST or None)
    context={
        "form":form
             }
    # print("you are logged in")
    # print(request.user.is_authenticated())

    if form.is_valid():
        # print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        login(request,user)
        print(user)
        if User is not None:

            return redirect("/allproduct")
        else:
            print("error")
    return render(request,'auction_house/login.html',context)
User=get_user_model()
def register_page(request):
    form = register_form(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")


        new_user=User.objects.create_user(username,password,email)
        print(new_user)
    return render(request,'auction_house/register.html',context)

def allproducts(request):
    drawpost=drawing_product.objects.all()
    paintpost = painting_product.objects.all()
    carvpost = carving_product.objects.all()
    sculppost = sculpture_product.objects.all()
    photopost = photographic_product.objects.all()
    context={
        'drawing_product': drawpost,
        'painting_product':paintpost,
        'carving_product': carvpost,
        'sculpture_product': sculppost,
        'photographic_product': photopost
    }
    return  render(request,'auction_house/allproducts.html',context)

def drawing_details(request,drawing_product_id):
    draw_details = get_object_or_404(drawing_product, pk=drawing_product_id)
    return render(request, 'auction_house/drawing_details.html', {'drawingdetails':draw_details})


def painting_details(request,painting_product_id):
    paint_details = get_object_or_404(painting_product, pk=painting_product_id)
    return render(request, 'auction_house/painting_details.html', {'paintingdetails':paint_details})

def carving_details(request,carving_product_id):
    carv_details = get_object_or_404(carving_product, pk=carving_product_id)
    return render(request, 'auction_house/carving_details.html', {'carvingdetails':carv_details})


def sculpture_details(request,sculpture_product_id):
    sculp_details = get_object_or_404(sculpture_product, pk=sculpture_product_id)
    return render(request, 'auction_house/sculpture_details.html', {'sculpturedetails':sculp_details})


def photographic_details(request,photographic_product_id):
    photo_details = get_object_or_404(photographic_product, pk=photographic_product_id)
    return render(request, 'auction_house/photographic_details.html', {'photographicdetails':photo_details})


def about_us(request):
    return render(request,'auction_house/about.html')

def Bid(request):
    if request.method == 'POST':
        fullname_f = request.POST.get('fullname')
        email_e = request.POST.get('email')
        number_n= request.POST.get('phone')
        file_f=request.POST.get('file')
        amount_a= request.POST.get('amount')

        c = bid(fullname=fullname_f, email=email_e,contact_number=number_n, amount=amount_a,idproof=file_f)
        c.save()

        return render(request,'auction_house/bidsuccess.html')
    else:

      return render(request,'auction_house/bid.html')





class searchview(ListView):
    paginate_by = 20
    count=0
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data( )
        context['count']= self.count or 0
        context['query']= self.request.GET.get('q')
        return context
    def get_queryset(self):
        request=self.request
        query= request.GET.get('q', None)
        if query is not None:
            return carving_product.objects.search(query=query)
        return carving_product.objects.none()