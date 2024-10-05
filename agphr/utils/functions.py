from django.utils.text import slugify

def generate_unique_slug(instance, source_field='name', slug_field='slug'):
    source_value = getattr(instance, source_field, None)

    if not source_value:
        raise ValueError(f"{source_field} cannot be empty")

    slug = slugify(source_value)
    unique_slug = slug
    num = 1

    # Check for existing slugs
    while instance.__class__.objects.filter(**{slug_field: unique_slug}).exists():
        unique_slug = f"{slug}-{num}"
        num += 1

    return unique_slug
