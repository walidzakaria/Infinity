from rest_framework import routers
from .viewsets import CountryViewSet, RegionViewSet, CityViewSet, SeasonViewSet, SupplierViewSet, HotelChainViewSet, TeamViewSet, HotelViewSet

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'region', RegionViewSet)
router.register(r'city', CityViewSet)
router.register(r'season', SeasonViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'hotel_chain', HotelChainViewSet)
router.register(r'team', TeamViewSet)
router.register(r'hotel', HotelViewSet)


