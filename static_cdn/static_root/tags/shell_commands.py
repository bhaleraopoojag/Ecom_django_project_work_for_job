# from tags.models import TagModel

# qs=TagModel.objects.all()

# print(qs)
# <QuerySet [<TagModel: T shirt>, <TagModel: TShirt>, <TagModel: T-shirt>, <TagModel: Red>, <TagModel: Black>]>

# black=TagModel.objects.last()

# black.title
# 'Black'

# black.slug
# 'black'

# black.products

# black.products.all()
# ProductQuerySet[<ProductModel: T-shirt>, <ProductModel: Hat>, <ProductModel: Npkin>, <ProductModel: hat>, <ProductModel: t-shirt>]>

# black.products.all().first()
# <ProductModel: T-shirt>

# exit()
# # PS D:\Ecomm> python manage.py shell

# from products.models import ProductModel

# qs = ProductModel.objects.all()

# print(qs)
# <ProductQuerySet [<ProductModel: T-shirt>, <ProductModel: Hat>, <ProductModel: Npkin>, <ProductModel: super computer>, <ProductModel: hat>, <ProductModel: t-shirt>, <ProductModel: ipsum text>]>

# tshirt = qs.first()

# tshirt.title
# 'T-shirt'

# tshirt.description
# 'This is awesome shirt.'

# tshirt.tag
# <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0x210bb5e7310>

# tshirt.tag.all()
# <QuerySet [<TagModel: T shirt>, <TagModel: TShirt>, <TagModel: T-shirt>, <TagModel: Red>, <TagModel: Black>]>

# tshirt.tag.filter(title__icontains='black')
# <QuerySet [<TagModel: Black>]>


