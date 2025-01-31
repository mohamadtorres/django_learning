from django.shortcuts import render
from . import models
from django.http import HttpResponse as httpresponse, Http404
from django.core.paginator import Paginator
# Create your views here.
#function base view ke ba def shoroo mishe

def post_list(request):
    #posts =  models.Post.objects.filter(status='published') #inja migim bebin hame
    posts = models.Post.objects.all()  #inja migim bebin hame
    paginator = Paginator(posts, 3) # Show 2 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    print(posts)
    return render(request, 'post_list.html',context=context)

# def post_detail(request,year,month, day, slug):
#     try:
#         post = models.Post.objects.get(
#             created_data__year=year,
#             created_data__month=month,
#             created_data__day=day,
#             slug=slug,
#             status = 'published',
#         )
#     except models.Post.DoesNotExist:
#         raise Http404("In post be ga rafte")

#     context = {
#         'post': post
#     }
#     return httpresponse(f"{post.title}")


#ye rah asoon tari hast bara inke age safheyi nabod chi biad bala Error 404 bede

from django.shortcuts import get_object_or_404,render
def post_detail(request,year,month, day, slug):

    post = get_object_or_404(models.Post,
        created_data__year=year,
        created_data__month=month,
        created_data__day=day,
        slug=slug,
        status = 'published',
    )

    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context=context)



def contact_us(request):
    # return httpresponse("Contact Us")
    return render(request, 'contact_us.html')



# def home_view(request):
#     return render(request, 'home.html', {'name': 'Mamadkhavari'}) #render ham post request, template name, dictionary ham post mishe

# def about_view(request):
#     return render(request, 'about.html')