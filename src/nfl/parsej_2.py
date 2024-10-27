data = (
    {
        'inquiry_date': '2021-01-14',
        'address': {
            'city': 'Warsaw',
            'zip_code': '20-200',
            'country': 'Poland',
            'house_no': '22',
            'street': 'Some-Street'
        },
        'insert_date': '2020-12-20',
        'is_active': False
    },
    {
        "accounting": [
            {"firstName": "John", "lastName": "Doe", "age": 23,
             "x": {1: 2, 2: 3}},
            {"firstName": "Mary", "lastName": "Smith", "age": 32}
        ],
        "sales": [
            {"firstName": "Sally", "lastName": "Green", "age": 27},
            {"firstName": "Jim", "lastName": "Galley", "age": 41}
        ]
    }
)


def extract(payload, header=''):
    if isinstance(payload, dict):
        for k, v in payload.items():
            new_header = f"{header} {k}".strip()
            extract(v, new_header)
    elif isinstance(payload, list):
        for number, item in enumerate(payload):
            extract(item, str(number) + "," + header)
    else:
        print(f'{header.replace(" ", ":")},{payload}')


if __name__ == "__main__":
    for count in range(len(data)):
        extract(data[count])