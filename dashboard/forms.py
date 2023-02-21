from django import forms 
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from . models import * 


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes 
        widgets = {'title' : forms.TextInput(attrs={'class': 'form-control'}),
                   'description' : forms.TextInput(attrs={'class': 'form-control'})}
        fields = ['title','description']
    
        
class DateInput(forms.DateInput):
    input_type = 'date'

        
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework 
        widgets = {
                   'due' : DateInput(attrs={"class":'form-control'}),
                   'subject':forms.TextInput(attrs={"class":'form-control'}),
                   'title':forms.TextInput(attrs={"class":'form-control'}),
                   'description':forms.Textarea(attrs={"class":'form-control'}),
                   }
        fields = ['subject','title','description','due','is_finished']
   
    
class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label='Enter Your Search : ')
    

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo 
        widgets = {'title' : forms.TextInput(attrs={'class': 'form-control'})}
        fields = ['title','is_finished']
        
    
class ConversionForm(forms.Form):
    CHOICES = [('length',"Length"),('mass','Mass')]
    measurement = forms.ChoiceField(choices= CHOICES, widget=forms.RadioSelect)
    
class ConversionLengthForm(forms.Form):
    CHOICES = [('yard',"Yard"),('foot','Foot')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the Number',"class":'form-control'}
    ))
    measure1 = forms.CharField(
        label = '', widget=forms.Select(choices=CHOICES,attrs={"class":'form-control'})
    )
    
    measure2 = forms.CharField(
        label = '', widget=forms.Select(choices=CHOICES,attrs={"class":'form-control'})
    )
    
class ConversionMassForm(forms.Form):
    CHOICES = [('pound',"Pound"),('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':'Enter the Number',"class":'form-control'}
    ))
    
    measure1 = forms.CharField(
        label = '', widget=forms.Select(choices=CHOICES,attrs={"class":'form-control'})
    )
    
    measure2 = forms.CharField(
        label = '', widget=forms.Select(choices=CHOICES,attrs={"class":'form-control'})
    )    
               
        
        
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User 
        widgets = {
                   'username':forms.TextInput(attrs={"class":'form-control'}),
                   }
        fields =  ['username','password1','password2']   
    

        
 
        