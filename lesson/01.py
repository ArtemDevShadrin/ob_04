###################################################################
# Принцип единственной ответственности
###################################################################
#####
# не правильно
# class UserManager():
#     def __init__(self, user):
#         self.user = user
#
#     def change_user_name(self, user_name):
#         self.user = user_name
#
#     def save_user(self):
#         file = open("users.txt", "a")
#         file.write(self.user)
#         file.close()
#####

#####
# должно выглядеть!
class User():
    def __init__(self, user):
        self.user = user


class UserNameChanger():
    def __init__(self, user):
        self.user = user

    def change_name(self, new_name):
        self.user = new_name


class SaveUser():
    def __init__(self, user):
        self.user = user

    def save(self):
        file = open("users.txt", "a")
        file.write(self.user)
        file.close()


#####

###################################################################
# Принцип открытости/закрытости (OCP, Open/Closed Principle)
###################################################################
#####
# не правильно
# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f"сформирован отчет - {self.title} - {self.content}")
#####

#####
# должно выглядеть!
from abc import ABC, abstractmethod


class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass


class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)


class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")


class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)


report = Report("Заголовок отчета", "Текст отчета", TextFormatted())

report.docPrinter()


#####

###################################################################
# Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)
###################################################################
#####
# не правильно
# class Bird():
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def fly(self):
# #         print('птица летает')
#
# class Ping(Bird):
#     pass
#
# p = Ping("Bob")
#
# p.fly()
#####

#####
# должно выглядеть!
class Bird():
    def fly(self):
        print('птица летает')


class Ping(Bird):
    def fly(self):
        print('птица не - летает')


def fly_in_the_sky(animal):
    animal.fly()


b = Bird()
p = Ping()

fly_in_the_sky(b)
fly_in_the_sky(p)


#####

###################################################################
# Принцип разделения интерфейсов (ISP, Interface Segregation Principle)
###################################################################
#####
# не правильно
# class SmartHouse():
#     def turn_on_light(self):
#         pass
#
#     def heat_food(self):
#         pass
#
#     def turn_on_music(self):
#         pass
#####

#####
# должно выглядеть!
class Light():
    def light(self):
        print("Light")


class Food():
    def food(self):
        print("Food")


class Music():
    def music(self):
        print("Music")


#####

###################################################################
# Принцип инверсии зависимости (DIP, Dependency Inversion Principle)
###################################################################
#####
# не правильно
# class Book():
#     def read(self):
#         print("read")
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read()
#####

#####
# должно выглядеть!
class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass


class Book(StorySource):
    def get_story(self):
        print("read")


class AudioBook(StorySource):
    def get_story(self):
        print("audio")


class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()


book = Book()
audiobook = AudioBook()

readerBook = StoryReader(book)
audioreaderBook = StoryReader(audiobook)

readerBook.tell_story()
audioreaderBook.tell_story()
