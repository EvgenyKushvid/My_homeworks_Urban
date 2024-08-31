...
import time
class User:
    def __init__(self, nickname, password,age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__ (self):
        return self.nickname

    def __contains__(self, item):
        for obj in ur.users:
            if item.nickname == obj.nickname:
                return True
        #return any(item.nickname == obj.nickname for obj in ur.users)

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    # def __new__(cls, *args, **kwargs):
    #     cls.videos.append(args)
    #     return object.__new__(cls)
    def video_title(self):
        return self.title

    def __str__(self):
        return self.title

class UrTube : # доделать проверку на повторы

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    # def __new__(cls, *args, **kwargs):
    #     cls.videos.append(args)
    #     return object.__new__(cls)
    def add (sefl, *args):
          for arg in args:
            if arg.title not in sefl.videos:
                sefl.videos.append(arg)

            # print(arg)


            # if arg.title not in UrTube.videos.__str__() :
            #     print(UrTube.videos)
            #     # print(f'Добавлено видео : {arg}')
            #     UrTube.videos.append(arg)

    def get_videos(self, string):
        search_video = []
        for video in self.videos:
            # print(video.title.lower(), string.lower())
            if string.lower() in video.title.lower():
                search_video.append(video)
                print(video)
        return search_video
    def watch_video (self, video_title):
        # if self.current_user != None and int(self.current_user.age) >=18:
            for video in self.videos:
                if video_title == video.title:
                    for second in range(video.time_now, video.duration):
                        # print (second)
                        # time.sleep(1)
                        print("End of video")



    def log_in(self, nickname, password, age):
        user = User(nickname,password,age)
        if user in self.users:
            self.current_user = user
            print(f'Вход пользавателя {user}')
        else:
            print('Такого нет в списке пользователей! ')

    def log_out (self):
        self.current_user = None




    def register(self, nickname, password, age): # нужнв проверка на пользователя в базе
        new_user = User(nickname, password, age)
        if new_user not in self.users:

            self.users.append(new_user)
            self.current_user = new_user
            print ("new user  - ", new_user )
        else:
            print(f'NO!!!{nickname}')
            self.log_out()








if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')