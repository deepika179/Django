from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    age=forms.IntegerField()
    place=forms.CharField()
    email=forms.EmailField()
    
    def clean_name(self):
        n= self.cleaned_data['name']
        if len(n)<=3:
            raise forms.ValidationError("min no of characters must be greater than 3")
        return n