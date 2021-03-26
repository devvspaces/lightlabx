from fractions import Fraction
from random import sample
import string


def simplify(n):
	num = Fraction(n).limit_denominator()
	return str(num)


def random_text(p=5):
	return ''.join(sample(string.ascii_letters+string.digits,p))

def get_usable_slug(instance, slug=None):
	if slug is None:
		slug=random_text(16)

	# Check if this slug has been used before
	exists = instance.__class__.objects.filter(slugid=slug).exists()
	if exists:
		return get_usable_slug(instance, random_text())

	return slug