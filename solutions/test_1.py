def solution(cacheSize, cities):
    answer = 0
    reference = []
    for city in cities:
        reference.append(city.casefold())
    cache = []

    if cacheSize == 0:
        return 5 * len(cities)

    for ref in reference:
        if not ref in cache:
            if len(cache) < cacheSize:
                cache.append(ref)
            else:
                cache.pop(0)
                cache.append(ref)
        else:
            cache.pop(cache.index(ref))
            cache.append(ref)

    for city in reference:
        if city in cache:
            answer += 1
        else:
            answer += 5
    return answer