from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, PropertyForm
from .models import Property, InterestedBuyer

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def post_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.seller = request.user
            property.save()
            return redirect('my_properties')
    else:
        form = PropertyForm()
    return render(request, 'main/post_property.html', {'form': form})

def like_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    property.likes += 1
    property.save()
    return redirect('property_detail', pk=pk)
@login_required
def my_properties(request):
    properties = Property.objects.filter(seller=request.user)
    return render(request, 'main/my_properties.html', {'properties': properties})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'main/property_list.html', {'properties': properties})
def like_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    property.likes += 1
    property.save()
    return redirect('property_detail', pk=pk)
@login_required
def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'POST':
        InterestedBuyer.objects.create(property=property, buyer=request.user)
    return render(request, 'main/property_detail.html', {'property': property})
def home(request):
    return render(request, 'main/home.html')