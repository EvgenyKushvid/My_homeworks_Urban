...
import time
class User:
    def __init__(self, nickname, password,age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __eq__(self, other):
        return other.nickname == self.nickname
    def __str__ (self):
        return self.nickname

    # def __hash__(self):
    #     return hash(self.password)
    def get_info (self):
        return self.nickname,hash(self.password)


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return other.title == self.title
    def video_title(self):
        return self.title

    def __str__(self):
        return self.title

class UrTube :

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    def info_users (self):
        info_us = []
        for i in self.users:
            info_us.append(i.nickname)
        return info_us
    def add (sefl, *args):
          for arg in args:
            if arg.title not in sefl.videos:
                sefl.videos.append(arg)

    def get_videos(self, string):
        search_video = []
        for video in self.videos:
            if string.lower() in video.title.lower():
                search_video.append(video.title)
                #print(video)
        return search_video
    def watch_video (self, video_title):
        if self.current_user :
            if self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
            else:
                for video in self.videos:
                    if video_title == video.title:
                        for second in range(video.time_now +1, video.duration+1):
                            print(f'\r{second:3}', end='')
                            time.sleep(1)
                        print(" End of video")
        else:
            print("Войдете в акаунт для того что бы смотреть видео")


    def log_in(self, nickname, password):
        for user in self.users:
           if (nickname, hash(password)) == user.get_info():
                self.current_user = user
                print(f'Вход пользователя: {self.current_user}')
                return user


    def log_out (self):
        self.current_user = None




    def register(self, nickname, password, age): # нужнв проверка на пользователя в базе
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')


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
    # --------------------------
    ur.log_out()
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
