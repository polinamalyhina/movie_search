from django.contrib.admin.views.decorators import staff_member_required
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Backend for movie-search tool",
        default_version='v1',
        description="Test assignment for Workbounce",
        contact=openapi.Contact(email="polja.malygina@gmail.com"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

staff_protected_schema_view = staff_member_required(schema_view.with_ui('swagger', cache_timeout=0))
