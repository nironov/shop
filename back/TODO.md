# TODO Shop

## Apps
- [ ] core
    - Models
        - [X] Settings
            - title
            - description
            - favicon (FileField)
            - favicon (ImageField)
            - telegram
            - email
    - [ ] Context processor for Settings

- [ ] products
    - Models
        - [ ] Product
            - active
            - name
            - description
            - sku
            - price
            - discount
            - created_at
            - updated_at
            - category (M2M)
            - brand (FK)
            - user (FK)
            - main_image (?)

        - [ ] Image
        - [ ] Category
        - [ ] Brand

- [ ] orders
    - Models
        - status
        - amount
        - shipment_method
        - user
        - date
        - products

- [ ] shipment
    - API

- [ ] cart
- [ ] payment

- [ ] pages
    - main
    - about
    - contacts
    - catalog
    - cart
    - user

- [ ] custom_user
    - Model
        - login
        - password
        - name
        - last_name
        - email
        - telegram
        - phone
        - last_seen
        - created_at
        - orders
        - payment_methods

- [ ] email distribution


## Business Logic

## Front
