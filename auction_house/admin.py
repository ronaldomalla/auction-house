from django.contrib import admin

from . models import contact,drawing_product,painting_product,carving_product,photographic_product,sculpture_product,bid
admin.site.register(contact)
admin.site.register(drawing_product)
admin.site.register(painting_product)
admin.site.register(carving_product)
admin.site.register(sculpture_product)
admin.site.register(photographic_product)
admin.site.register(bid)

