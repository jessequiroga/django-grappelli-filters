from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from datetime import date
from django.contrib.admin.options import (
    HORIZONTAL, VERTICAL, ModelAdmin, TabularInline,
    get_content_type_for_model,
)
from django.test.utils import isolate_apps
from .models import Band, Song
from grappelli_filters.admin import FiltersMixin
from grappelli_filters.filters import RelatedAutocompleteFilter


class MockRequest:
    pass


class MockSuperUser:
    def has_perm(self, perm):
        return True


class SongAdmin(FiltersMixin, ModelAdmin):
    list_filter = (('band', RelatedAutocompleteFilter),)


request = MockRequest()
request.user = MockSuperUser()


class GrappelliFiltersTests(TestCase):

    def setUp(self):
        self.band = Band.objects.create(name='The Doors')
        self.song = Song.objects.create(band=self.band, name='Light my fire')
        self.site = AdminSite()
        self.ma = SongAdmin(Song, self.site)

    def test_modeladmin_str(self):
        self.assertEqual(str(self.ma), 'grappelli_filters.SongAdmin')

    def test_lookup_allowed(self):
        self.assertIs(self.ma.lookup_allowed('band', self.band), True)

    def test_related_filter(self):        
        field = self.song._meta.get_field('band')
        raf = RelatedAutocompleteFilter.create(
            field=field,
            request=request,
            params={},
            model=Song,
            model_admin=self.ma,
            field_path='grappelli_filters.Song.band'
        )
        self.assertEqual(raf.field, field)
