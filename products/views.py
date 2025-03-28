from django.http import Http404
from django.shortcuts import render,get_list_or_404
from django.views.generic import ListView,DetailView
from .models import ProductModel
from carts.models import CartModel
from analytics.mixins import ObjectViewedMixin



# Create your views here.
class ProductFeaturedListView(ListView):
    template_name="products/list.html"


    def get_queryset(self,*args,**kwargs):
        request=self.request
        return ProductModel.objects.all().featured()
    
class ProductFeaturedDetailView(ObjectViewedMixin,DetailView):
    queryset=ProductModel.objects.all().featured()
    template_name="products/featured-detail.html"

    # def get_queryset(self,*args,**kwargs):
    #     request=self.request
    #     return ProductModel.objects.featured()



class ProductListView(ListView):
   
    template_name="products/list.html"

    # def get_context_data(self,*args, **kwargs):
    #     context=super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context 
    def get_context_data(self, *args,**kwargs):
        context=super(ProductListView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj=CartModel.objects.new_or_get(self.request)
        context['cart']=cart_obj
        return context

    def get_queryset(self,*args,**kwargs):
        request=self.request
        return ProductModel.objects.all()

def product_list_view(request):
    queryset=ProductModel.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,"products/list.html",context)




class ProductDetailslugView(ObjectViewedMixin,DetailView):
    queryset=ProductModel.objects.all()
    template_name="products/detail.html"

    def get_context_data(self, *args,**kwargs):
        context=super(ProductDetailslugView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj=CartModel.objects.new_or_get(self.request)
        context['cart']=cart_obj
        return context


    def get_object(self,*args,**kwargs):
        request=self.request
        slug=self.kwargs.get('slug')
        
        # instance= get_list_or_404(ProductModel,slug=slug,active=True)
        try:
            instance=ProductModel.objects.get(slug=slug,active=True)
        except ProductModel.DoesNotExist:
            raise Http404("Not Found..")
        except ProductModel.MultipleObjectsReturned :
            qs=ProductModel.objects.filter(slug=slug,active=True)
            instance= qs.first()
        except:
            raise Http404("Uhhm")
        return instance
    


class ProductDetailView(ObjectViewedMixin,DetailView):
    # queryset=ProductModel.objects.all()
    template_name="products/detail.html"

    def get_context_data(self,*args, **kwargs):
        context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        return context 
    

    def get_object(self,*args,**kwargs):
        request=self.request
        pk=self.kwargs.get('pk')
        instance=ProductModel.objects.get_by_id(pk) # type: ignore
        if instance is None:
            raise Http404("Product Doesn't exist")
        return instance
    
    # def get_queryset(self,*args,**kwargs):
    #     request=self.request
    #     pk=self.kwargs.get('pk')
    #     return ProductModel.objects.filter(pk)
        


def product_detail_view(request,pk=None,*args,**kwargs):
    # instance=ProductModel.objects.get(pk=pk,featured=True)
    # instance=get_list_or_404(ProductModel,pk=pk)
    # try:
    #     instance=ProductModel.objects.get(id=pk)
    # except ProductModel.DoesNotExist:
    #     print('No Product Here')
    #     raise Http404("Product Doesn't exist")
    # except:
    #     print('Huh?')
    #     raise Http404("Product Doesn't exist")

    instance=ProductModel.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product Doesn't exist")


    # print(instance)
    # qs=ProductModel.objects.filter(id=pk)
    # if qs.exists() and qs.count()==1:
    #     instance=qs.first()
    # else:
    #     raise Http404("Product Doesn't exist")

    context={
        'object':instance
    }
    return render(request,"products/detail.html",context)