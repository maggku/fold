from apps.products.models import Category
import pytest

@pytest.mark.django_db
def test_category_fiendly_name():
        trousers = Category.objects.create(name='trousers')
        t = Category.objects.get(name='trousers')

        assert t.get_friendly_name() == None


@pytest.mark.django_db
def test_category_fiendly_name2():
        trousers = Category.objects.create(name='trousers', friendly_name='trousers')
        t = Category.objects.get(name='trousers')

        assert t.get_friendly_name() == 'trousers'





