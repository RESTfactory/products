import rest_framework_filters as filters
from .models import Local, Provision

class ProvisionFilter(filters.FilterSet):
    # local = filters.RelatedFilter(queryset=Local.objects.all())
    class Meta:
        model = Provision
        fields = {'id': ['exact']}
