class DataBurger:
    BLACK_BUN = ("black bun", 100)
    WHITE_BUN = ("white bun", 200) 
    RED_BUN = ("red bun", 300)

    # Соусы
    HOT_SAUCE = ("SAUCE", "hot sauce", 100)
    SOUR_CREAM = ('SAUCE', "sour cream", 200)
    CHILI_SAUCE = ('SAUCE', "chili sauce", 300)

    # Начинки
    CUTLET = ('FILLING', "cutlet", 100)
    DINOSAUR = ('FILLING', "dinosaur", 200)
    SAUSAGE = ('FILLING', "sausage", 300)   

    expected_receipt = """(==== red bun ====)
= sauce hot sauce =
(==== red bun ====)

Price: 700"""