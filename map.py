from locations import Location


class Map:
    CASTLE = Location("hrad", "Jsi na hradě.", False)
    FOREST = Location("les", "Jsi v lese.", False)
    LAKE = Location("rybník", "Jsi u rybníka.", False)
    HOME = Location("domov", "Jsi doma.", True)

    map = [[CASTLE],
           [FOREST, FOREST],
           [FOREST, FOREST, FOREST, LAKE],
           [FOREST, HOME],
           [LAKE]]
