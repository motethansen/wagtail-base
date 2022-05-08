from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, RichTextField
#from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class HomePage(Page):
    """Home page model"""
    templates = "home/home_page.html"
    header =''
    banner_title = models.CharField(max_length=100,blank=False,null=True)
    #header = models.CharField("Header", max_length=200)
    body = RichTextField(blank=True)
    #image = models.ForeignKey('wagtailimages.Image', related_name='+', on_delete=models.CASCADE)
    content_panels = Page.content_panels + [ 
    #     FieldPanel('header'),
    #     ImageChooserPanel('image'),
         FieldPanel("banner_title"),
         FieldPanel('body', classname="full"),
    #     FieldPanel("banner_title")
    ]

    class Meta:
        verbose_name = "home page"
