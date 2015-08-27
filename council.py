import protector
from extensions.animetwist import AnimeTwistDataProvider

STORAGES = [
    protector.Storage("/animenclave", "animenclave"),
]

DATA_PROVIDERS = [
    AnimeTwistDataProvider(),
]
