# class Greeter:
#     def __init__(self, boss):
#         self.boss = boss
#
#     def enters(self, visitor):
#         if isinstance(visitor, list):
#             self.name = visitor[-1]
#         elif isinstance(visitor, str):
#             self.name = visitor
#         else:
#             self.name = None
#         if self.name is None:
#             self.word = None
#         elif self.name == self.boss:
#             self.word = "Hello"
#         else:
#             self.word = "Welcome"
#
#     def greet(self):
#         if self.word is None:
#             return None
#         return self.word + "," + self.name


