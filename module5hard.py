import time

name_current_film = ''
age_current_user = 0
no_prigl_na_vhod = 0

class User:
    users = []

    def __init__(self,nickname,password,age):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.user_list = []
        self.user_list.append(nickname)
        self.user_list.append(hash(password))
        self.user_list.append(age)
        User.users.append(self.user_list)


class Video:
    videos = []

    def __new__(cls, *args, **kwargs):
        args_list = list(args)
        if len(args_list) == 2:
            args_list.append(0)
        if len(kwargs) == 1:
            args_list.append(kwargs['adult_mode'])
        else:
            args_list.append(False)
        cls.videos.append(args_list)
        return super().__new__(cls)

    def __init__(self,*args,**kwargs):
        pass


class UrTube:
    User.users
    Video.videos
    current_user = []

    def __init__(self):
        pass

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __contains__(self, item):
        return item in self.items

    def __eq__(self, other):
        if not isinstance(other, (int, UrTube)):
            raise TypeError("Операнд справа должен иметь тип int или UrTube")

    def log_in(self,nickname, password):
        cur_name = nickname
        cur_pass = hash(password)
        for i in User.users:
            if i[0] == cur_name and i[1] == cur_pass:
                self.current_user.append(cur_name)
                break

    def log_out(self):
        self.current_user = None

    def add(self,*vid):
        vid_list = list(vid)
        for i in vid_list:
            if isinstance(i,Video) == False:
                tit_new = i[0]
                it_is = 0
                for j in Video.videos:
                    tit_is = j[0]
                    if tit_is == tit_new:
                        it_is = 1
                        break
                        if it_is == 0:
                            Video.videos.append(list(i))

    def get_videos(self,word_poisk):
        same_words = []
        for i in Video.videos:
            i_str = str(i)
            if len(i_str) > len(word_poisk):
                if word_poisk.lower() in i_str.lower():
                    same_words.append(i[0])
            else:
                if word_poisk.lower() in i_str.lower():
                    same_words.append(i[0])
        return  same_words

    def register(self,nickname, password, age):
        global age_current_user
        is_user = 0
        for i in User.users:
            if nickname == str(i[0]):
                is_user = 1
                break
        if is_user == 0:
            list_tmp = []
            list_tmp.append(nickname)
            list_tmp.append(hash(password))
            list_tmp.append(age)
            User.users.append(list_tmp)
            age_current_user = age
            self.log_in(nickname, password)
            self.watch_video(name_current_film)
        else:
            print(f'Пользователь {nickname} уже существует')

    def watch_video(self,name_film):
        global name_current_film
        global no_prigl_na_vhod

        if self.current_user == None:
            self.current_user = []
        if len(self.current_user) == 0:
            name_current_film = name_film
            if no_prigl_na_vhod == 0:
                print('Войдите в аккаунт, чтобы смотреть видео')
            else:
                no_prigl_na_vhod = 0
        else:
            presence_film = 0
            index_of_film = -1
            for i in Video.videos:
                index_of_film += 1
                if str(i[0]) == name_film:
                    presence_film = 1
                    break
            if presence_film == 1:
                ogr_po_vozr = Video.videos[index_of_film][3]
                if ogr_po_vozr == True and age_current_user<18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    no_prigl_na_vhod = 1
                    self.log_out()
                    name_current_film = ''
                else:
                    time_film = Video.videos[index_of_film][1]
                    for i in range(1,time_film + 1):
                        print(str(i)+'  \b',end="")
                        time.sleep(1)
                    print('Конец видео')

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)
ur = UrTube()
ur.add(v1,v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin','lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.watch_video('Лучший язык программирования 2024 года!')