from django.db.models.expressions import result


def sun_range(start, end):
    result = int(sum(range(start, end +1)))
    return result

result  = sun_range(3, 45)
print(result)

