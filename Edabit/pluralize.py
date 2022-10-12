def pluralize(elems):
    pluralized = []
    extra = []
    for elem in elems:
        if elem in extra and elem + "s" not in pluralized:
            pluralized.remove(elem)
            pluralized.append(elem + "s")
        elif elem not in extra:
            pluralized.append(elem)
            extra.append(elem)
    return pluralized

print(pluralize(["cow", "pig", "cow", "cow", 'horse', 'horse', 'cat']))

# or elem + "s" not in pluralized