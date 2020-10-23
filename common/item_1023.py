# To define a class, use the class keyword along with the name of a class
#    C#
#    public class Item {...}
# {
#     "id": "123",
#     "name": "Socks (White)",
#     "quantity": 0,
#     "description": ""
# }

class item:
    # STATE VARIABLE (instance variable)
    #    C#
    #    private string id;
    #    IN PYTHON a variable name starting with two underscores "__" is private
    __id = ""
    __name = ""
    __quantity = 0
    __description = ""

    # CONSTRUCTOR
    #    C#
    #    public Item(string Id, string Name) {...}
    # "initializer"
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    # METHODS
    #    C#
    #    public void ShowStatus() {...}
    #    C#
    #      this.quantity = 5
    #      self.quantity = 5
    def showStatus(self):
        print(f"ID: {self.__id}")
        print(f"NAME: {self.__name}")
        print(f"QUANTITY: {self.__quantity}")

    def get_id(self):
        return self.__id

    # QUANTITY GETTERS AND SETTERS
    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, new_value):
        if new_value >= 0:
            self.__quantity = new_value
        else:
            raise ValueError("BAD VALUE")


    # QUANTITY PROPERTY
    #   C#
    #   public int Quantity { get; set; }
    quantity = property(get_quantity, set_quantity)


    # ONTHER METHOD
    def add_quantity(self, how_much):
        self.__quantity += how_much


# k = item("XYZ", "Zipper")
# # k.set_quantity(5)
# k.quantity = 5
# k.showStatus()


# # TO CREATE AN INSTANCE
# #   C#
# #   Item i = new Item()
# i = item("123", "Socks (white)")
# # i.name = "Socks (white)"
# print("i...")
# # print(i.quantity)
# # showStatus(i)
# i.showStatus()
# i.__quantity += 1
# # print(i.quantity)
# i.showStatus()

# j = item("ABC", "Shoes (black)")
# # j.name = "Shoes (black)"
# print("j...")
# # print(j.quantity)
# j.showStatus()
# j.__quantity -= 3
# # print(j.quantity)
# j.showStatus()

# # k = int()
