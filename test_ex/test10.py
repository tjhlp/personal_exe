import uuid


def fate_uuid():
    return uuid.uuid1().hex


data_1 = {
    'p1': 1,

    'p2': 2
}

rel = 'p1 * p2'

for k, v in data_1.items():
    rel = rel.replace(k, str(v))
    print(rel)

print(rel)
print(eval(rel))

