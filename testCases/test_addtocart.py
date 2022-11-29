import pytest
from pageObjects.addToCard import AddToCard


class Test001AddToCart:
    @pytest.mark.usefixtures("base_fix")
    @pytest.mark.regression
    def test_add_to_card(self, setup):
        AddToCard(setup).check_cart_jm()
