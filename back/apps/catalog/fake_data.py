from apps.core.postgresql_connection import cur

cur.execute(
    "INSERT INTO Products (id, name, price, description, brand, category) VALUES \
    (\
    '1', 'product name 1' 1299, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'rowenta', 1\
    ),\
    (\
    '1', 'product name 2' 1199, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'rowenta', 1\
    )\
    (\
    '1', 'product name 3' 799, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'rowenta', 1\
    ),\
    (\
    '1', 'product name 4' 999, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'rowenta', 1\
    ),\
    (\
    '1', 'product name 5' 599, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'rowenta', 1\
    ),\
    (\
    '1', 'product name 6' 1999, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'dyson', 2\
    ),\
    (\
    '1', 'product name 7' 1699, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'dyson', 2\
    ),\
    (\
    '1', 'product name 8' 399, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'bosch', 3\
    ),\
    (\
    '1', 'product name 9' 499, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'bosch', 3\
    ),\
    (\
    '1', 'product name 10' 399, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae accusantium vero', 'bosch', 3\
    ),\
    "
)