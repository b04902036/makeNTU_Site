from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
#from resturants.views import menu, resturants_list, comment, comment_delete
#from views import welcome
#from french.views import french_menu, french_note, french_delete, french_note_submit
from raw.views import menu, find_bike, empty_slot, time
from rest_framework import routers, serializers, viewsets
#from sp.views import sp_menu, 
admin.autodiscover()
#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)
#class UserSerializer(serializers.HyperLinkedModelSerializer):
#	class Meta:
#		model = User
#		fields = ('url', 'username', 'email', 'is_staff')

#class UserViewSet(viewsets.ModelViewset):
#	queryset = User.objects.all()
#	serializer_class = UserSerializer

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^menu/$', menu),
    #url(r'^welcome/$', welcome),
    #url(r'^resturants_list/$', resturants_list),
    #url(r'^comment/(\d{1,5})/$', comment),
    #url(r'^comment_delete/$', comment_delete),
    #url(r'^french_menu/$', french_menu),
    #url(r'^french_menu/french_note/(\d{1,5})/$', french_note),
    #url(r'^french_delete/$', french_delete),
    #url(r'^french_menu/french_note/\d{1,5}/french_note_submit/$', french_note_submit),
    #url(r'^sp_menu/$', sp_menu),
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^menu/$', menu),
    url(r'^find_bike/$', find_bike),
    url(r'^empty_slot/$', empty_slot),
    url(r'^time/$', time),
    #url(r'^', include(router.urls)),
    #url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
)
