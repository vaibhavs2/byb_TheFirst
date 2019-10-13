from django import forms
from sell.models import sell_order
from theFirst.models import branch
from sell.models import stock
from django.core.exceptions import ObjectDoesNotExist

class sellform(forms.ModelForm):
    number = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    pinCode = forms.CharField(widget=forms.TextInput(attrs={'type':'number'}))
    class Meta:
        model=sell_order
        fields = ['branch', 'semester', 'book_name','year_of_book', 'number','address','landmark','city','pinCode' ]

    def __init__(self, *args, **kwargs):
        super(sellform, self).__init__(*args, **kwargs)
        self.fields['branch'].empty_label = '--choose please--'
        
    def clean(self):

        cbranch = self.cleaned_data['branch']
        csem = self.cleaned_data['semester']
        try:
            br = branch.objects.get(branches=cbranch)
            cr = stock.objects.get(branch=br, semester=csem)
            if cr.stock_need:
                pass
            else:
                raise forms.ValidationError(f"Hey sorry! we have much stock for the branch {cbranch} sem-{csem}. Try later")
                
        except ObjectDoesNotExist:
                br=cr=None
                raise forms.ValidationError("Something went wrong! wait we are working to fix it out. you can try for other branch or semester")
        return self.cleaned_data
        
