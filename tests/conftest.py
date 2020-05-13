import pytest


mcmurdo = (-77.8419, 166.6863)
washington_monument = (38.8895, -77.0353)
giza_pyramid = (29.9792, 31.1342)


class Loc:
    def __init__(self, latlon, maiden):
        self.latlon = latlon
        self.maiden = maiden


@pytest.fixture(
    params=[(mcmurdo, "RB32id27"), (washington_monument, "FM18lv53"), (giza_pyramid, "KL59nx65")]
)
def location(request):
    return Loc(*request.param)
