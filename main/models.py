from django.db import models

class PP1(models.Model):
    podraz = models.CharField('Подразделение 1', max_length=120)

    def __str__(self):
        return self.podraz
    class Meta:
        verbose_name = 'Подразделение 1'
        verbose_name_plural = 'Подразделения 1'


class PP2(models.Model):
    podraz2 = models.CharField('Подразделение 2', max_length=120)
    pp1 = models.ForeignKey(PP1, on_delete=models.CASCADE, related_name='pp2_set', verbose_name='Подразделение 1')

    def __str__(self):
        return self.podraz2
    class Meta:
        verbose_name = 'Подразделение 2'
        verbose_name_plural = 'Подразделения 2'


class PP3(models.Model):
    podraz3 = models.CharField('Подразделение 3', max_length=120)
    pp2 = models.ForeignKey(PP2, on_delete=models.CASCADE, related_name='pp3_set', verbose_name='Подразделение 2')

    def __str__(self):
        return self.podraz3
    class Meta:
        verbose_name = 'Подразделение 3'
        verbose_name_plural = 'Подразделения 3'


class InspDetDOT(models.Model):
    pp1 = models.ForeignKey(PP1, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Подразделение 1')
    pp2 = models.ForeignKey(PP2, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Подразделение 2')
    pp3 = models.ForeignKey(PP3, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Подразделение 3')
    data = models.DateField('Дата проверки')
    act_nubmer = models.CharField('Номер акта', max_length=240)
    fio = models.CharField('ФИО проверяющего', max_length=120)
    dolgnost = models.CharField('Должность проверяющего', max_length=240)
    ab_group = models.CharField('Группа по ЭБ', max_length=240)
    c_level = models.CharField('Уровень контроля', max_length=120)

    def __str__(self):
        return self.fio
    def get_absolute_url(self):
        return f'/about/form'

    class Meta:
        verbose_name = 'Данные проверяющего'
        verbose_name_plural = 'Данные проверяющих'

#----------------------------------------------------------------------------------------------------
class OspDOT(models.Model):
    osp = models.CharField('Основной признак', max_length=120)
    def __str__(self):
        return self.osp
    class Meta:
        verbose_name = 'Основной признак'
        verbose_name_plural = 'Основные признаки'

class DopOstDOT(models.Model):
    dop_osp =models.CharField('Дополнительный признак', max_length=120)
    def __str__(self):
        return self.dop_osp
    class Meta:
        verbose_name = 'Допольнительный признак'
        verbose_name_plural = 'Дополнительные признаки'

class NTDlinkDOT(models.Model):
    ntd_link = models.URLField('Ссылка на НТД')
    def __str__(self):
        return self.ntd_link
    class Meta:
        verbose_name = 'Ссылка на НТД'
        verbose_name_plural = 'Ссылки на НТД'

class VoilByDOT(models.Model):
    np = models.IntegerField('№п/п')
    theme = models.IntegerField('Тема №')
    qust = models.IntegerField('Вопрос №') #qust = models.AutoField('Вопрос №')
    vi_viol = models.TextField('Выявленные нарушения')
    osp = models.ForeignKey(OspDOT, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Основной признак')
    dop_osp = models.ForeignKey(DopOstDOT, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Доп. признак')
    ntd_link = models.ForeignKey(NTDlinkDOT, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Ссылка на НТД')
    photo = models.ImageField(upload_to="uploads/", verbose_name='Фото')

    def __str__(self):
        return self.vi_viol
    class Meta:
        verbose_name = 'Нарушение по тематике ДОТ'
        verbose_name_plural = 'Нарушения по тематике ДОТ'
