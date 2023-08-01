# forms.py
from django import forms
from .models import Persons
class SearchForm(forms.Form):
    search_query = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder ':'Find individuals using available information'}))



# forms.py
from django import forms

class FormEntryForm(forms.Form):
    username = forms.CharField(max_length=100, label='نام کاربری یا شماره دستگاه')

# views.py
from django.shortcuts import render, redirect
from .models import FormEntry
from .forms import FormEntryForm

def form_entry_view(request):
    if request.method == 'POST':
        form = FormEntryForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if not FormEntry.objects.filter(username=username).exists():
                # اطلاعات ورودی را در دیتابیس ذخیره کنید
                FormEntry.objects.create(username=username, has_filled_form=True)
                return redirect('success')
            else:
                # شخص قبلاً اطلاعات وارد کرده است
                return redirect('already_filled')
    else:
        form = FormEntryForm()

    return render(request, 'form_entry.html', {'form': form})

class PersonForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = ['name', 'family','email','phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'family': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
