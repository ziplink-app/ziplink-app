import datetime
import hashlib
import random

HASH_LENGTH = 6
def generate_hash():
    salt = str(random.randint(0, 1000000))
    sha256_hash = hashlib.sha256(salt.encode()).hexdigest()
    short_hash = sha256_hash[:HASH_LENGTH]

    # is_existing_hash = ShortUrl.objects.filter(hash=short_hash).exists()
    # if is_existing_hash:
    #     short_hash = self.generate_as_short_sha256()
    return short_hash

def get_url_expiry() -> float:
    return int((datetime.datetime.now() + datetime.timedelta(hours=1)).timestamp())