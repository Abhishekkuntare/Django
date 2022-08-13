from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name =models.CharField(max_length=50)
    category  = models.CharField(max_length=50,default="")
    subcategory  = models.CharField(max_length=50,default="")
    desc =models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    pub_date  = models.DateField()
    image = models.ImageField(upload_to ="shop/images",default="")

    # getting the new product name 
    def __str__(self):          
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name =models.CharField(max_length=50)
    email  = models.CharField(max_length=50,default="")
    phone  = models.CharField(max_length=10,default="")
    desc =models.CharField(max_length=300,default="")

    # getting the new Msg data 
    def __str__(self):          
        return self.name    