from rest_framework import routers
from .viewsets import CountryViewSet

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)


