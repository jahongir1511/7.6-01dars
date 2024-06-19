def sentence(dicts):

    sorted_dicts = sorted(dicts, key=lambda d: int(list(d.keys())[0]))

    result = ' '.join(list(d.values())[0] for d in sorted_dicts)

    return result

List = [
    {'4': 'dog'}, {'2': 'took'}, {'3': 'his'},

    {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}

]

output = sentence(List)

print(output)


