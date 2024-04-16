import django_filters
from polling_units.models import AnnouncedPuResults


class ResultFilter(django_filters.FilterSet):
    party_score = django_filters.RangeFilter()
    class Meta:
        model = AnnouncedPuResults
        fields = {
                'polling_unit_uniqueid': ['exact'],
                'party_abbreviation': ['exact'],
            
                'entered_by_user': ['icontains'],
                'date_entered' : ['icontains']
        }
    
    