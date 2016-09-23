from django.shortcuts import render , redirect
from django.http import HttpResponse
from lists.models import Item
# Create your views here.

def home_page(request):
	if request.method == 'POST':
		text = request.POST.get('item_text','')
		item = Item()
		item.text = text
		item.save()
		string = {'new_item_text' : text,}
		return redirect('/')
	items = Item.objects.all()
	return render(request,'home.html',{'items':items})
