from tortoise import Model, fields


class User(Model):
    """
    Модель базы данных юзеров
    Важная вещь для работы бота и преподов
    основной параметр vk_id
    id = юзер вк айди (по нему мы определяем кто)
    rank = ранг юзера (-1 игнор, 0, гость (студент) 1 (препод) а выше нету потому что нету норм системы админов так что пофик
    time_work = Время работы препода
    tel = Телефон препода (Чисто по приколу созраним строку)
    mail = почта
    predmet = предмет который ведет препод
    kab = Кабинет препода (должно быть интовое значение но кабинетов может быть несколько так что похуй)
    opis = Описание (немного о себе хз зачем нужно просто хочу)
    """
    id = fields.IntField(pk=True)  # вк айди
    rank = fields.IntField(default=0)
    time_work = fields.CharField(max_length=256, null=True)
    tel = fields.CharField(max_length=256, null=True)
    mail = fields.CharField(max_length=256, null=True)
    predmet = fields.CharField(max_length=256, null=True)
    kab = fields.CharField(max_length=256, null=True)
    opis = fields.CharField(max_length=256, null=True)


    @classmethod
    async def get_or_new(cls, **kwargs) -> "User":
        user, _ = await cls.get_or_create(**kwargs)
        return user



class Prepods(Model):
    """
    Модель базы данных
    """
    id = fields.IntField(pk=True, generated=True)  #Автозаполняюзийся id при создании
    last_name = fields.CharField(max_length=256, null=True) #фамилия
    first_name = fields.CharField(max_length=256, null=True) # имя
    patronymic = fields.CharField(max_length=256, null=True) # отчество


    @classmethod
    async def get_or_new_prepod(cls, **kwargs) -> "Prepods":
        user, _ = await cls.get_or_create(**kwargs)
        return user

class Kabinet(Model):
    """
    Модель базы данных кабинетов
    id = ид записи как не странно
    id_prepods = id препода который следит за кабинетом

    """
    id = fields.IntField(pk=True, generated=True)  #Автозаполняюзийся id при создании
    namber = fields.CharField(max_length=256, null=True)
    id_prepods = fields.ForeignKeyField('models.Prepods', related_name='codes_admin_')
    id_predmet = fields.ForeignKeyField('models.Predmets', related_name='codes_admin__')



    @classmethod
    async def get_or_new_kab(cls, **kwargs) -> "Kabinet":
        user, _ = await cls.get_or_create(**kwargs)
        return user

class Predmets(Model):
    """
    Модель базы данных предметов
    id = ид записи как не странно
    namder = номер кабинета в текстовом формате
    id_prepods = id проподователей которые его ведут
    """
    id = fields.IntField(pk=True, generated=True)  #Автозаполняюзийся id при создании
    id_prepods = fields.ForeignKeyField('models.Prepods', related_name='codes_admin')
    name = fields.CharField(max_length=256, null=True)

    @classmethod
    async def get_or_new_predmets(cls, **kwargs) -> "Predmets":
        user, _ = await cls.get_or_create(**kwargs)
        return user