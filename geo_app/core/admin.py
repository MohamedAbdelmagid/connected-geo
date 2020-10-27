from django.contrib import admin
from .models import (
    BaeaNests, BaeaSurveys, BuowlHabitat, BuowlSurveys, GbhRookeries,
    LinearProjects, RaptorNests, RaptorSurveys
)
from leaflet.admin import LeafletGeoAdmin


admin.site.register(BaeaNests, LeafletGeoAdmin)
admin.site.register(BaeaSurveys, LeafletGeoAdmin)
# admin.site.register(BuowlSurveys)
admin.site.register(BuowlHabitat, LeafletGeoAdmin)
admin.site.register(GbhRookeries, LeafletGeoAdmin)
admin.site.register(LinearProjects, LeafletGeoAdmin)
admin.site.register(RaptorNests, LeafletGeoAdmin)
admin.site.register(RaptorSurveys, LeafletGeoAdmin)

# from django.apps import apps
# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
