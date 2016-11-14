import rest_framework_filters as filters
from .models import Local, Provision

class ProvisionFilter(filters.FilterSet):

    class Meta:
        model = Provision
        fields = {'local': ['exact', 'in']}
