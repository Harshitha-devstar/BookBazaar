from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.utils.text import slugify
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from .forms import SignUpForm, BookForm
from .models import Book, Category
from cart.forms import CartAddBookForm
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm


def test_view(request):
    return HttpResponse('<h1>Hello World!</h1>')

def home_view(request):
    form = AuthenticationForm()
    
    return render(request, 'baseapp/home.html', {'form':form})

def afterlogin_home_view(request):
    return render(request, "baseapp/afterlogin_home.html")

def about_view(request):
    return render(request, 'baseapp/about.html')

def contact_view(request):
    return render(request, 'baseapp/contact.html')

@login_required
def buy_view(request):
    return render(request, 'baseapp/buy.html')


@login_required
def sell_view(request):
    return render(request, 'baseapp/sell.html')

@login_required
def dashboard_view(request):
    username = request.user
    return render(request, 'baseapp/dashboard.html', {'username':username})


class UserView(DetailView):
    template_name = 'baseapp/profile.html'
    def get_object(self):
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional user details to the context
        context['email'] = self.request.user.email
        context['username'] = self.request.user.name
        context['date_joined'] = self.request.user.date_joined
        context['books_bought']=self.request.user.books_bought
        context['books_sold'] = self.request.user.books_sold
        # context['first_name'] = self.request.user.first_name
        # context['last_name'] = self.request.user.last_name
        # Add any custom fields if your user model has them
        # context['phone_number'] = self.request.user.phone_number
        return context
    

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email = user.email, password = raw_password)
            if user is not None:
                login(request, user)
            else:
                print('user is not authenticated')
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})
        

@login_required
def book_add_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)  
            book.seller = request.user
            book.slug = slugify(book.name)
            book.save()  # no param was there before if any issues remove this 
            print('Book Placed on Sale Successfully')
    form = BookForm()
    return render(request, 'baseapp/sell.html', {'form':form}) 

#  book list view
@login_required
def book_list_view(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        books = books.filter(category=category)
    return render(request, 'baseapp/buy.html', {'category':category, 'categories':categories, 'books':books})

# detail view for every product
@login_required
def book_detail(request, id, slug):
    book = get_object_or_404(Book, id = id, slug = slug, available = True)
    cart_book_form = CartAddBookForm()
    return render(request, 'baseapp/book_detail.html', {'book':book, 'cart_book_form':cart_book_form})

@login_required
def sale_list_view(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.filter(available = True, seller_id = request.user)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        books = books.filter(category=category)
    return render(request, 'baseapp/sell_list.html', {'category':category, 'categories':categories, 'books':books})

@login_required
def sale_book_detail(request, id, slug):
    book = get_object_or_404(Book, id = id, slug = slug, available = True)
    # cart_book_form = CartAddBookForm()
    return render(request, 'baseapp/sale_book_detail.html', {'book':book})


@login_required
def sale_update_view(request, id, slug):
    obj = get_object_or_404(Book, id = id, slug = slug)
    form = BookForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/sale/" + str(id)+ "/" + str(slug))
    return render(request, "baseapp/sale_update.html", {'form':form})
    