from .models import *
from django.forms import ModelForm, TextInput, Select, DateInput, FileInput, NumberInput, Textarea

class InspDetDOTForm(ModelForm):
    class Meta:
        model = InspDetDOT
        fields = ['pp1', 'pp2', 'pp3', 'data', 'act_nubmer', 'fio', 'dolgnost', 'ab_group', 'c_level']
        widgets = {
            "pp1": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Подразделение №1'
            }),
            "pp2": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Подразделение №2'
            }),
            "pp3": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Подразделение №3'
            }),
            "data": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'ДД.ММ.ГГГГ'
            }),
            "act_nubmer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер акта в формате №СВТК-ДЗО-СП-№пп/ГГ'
            }),
            "fio": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО проверяющего'
            }),
            "dolgnost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность проверяющего'
            }),
            "ab_group": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Группа ЭБ'
            }),
            "c_level": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Уровень контроля'
            }),

        }

class VoilByDOTForm(ModelForm):
    class Meta:
        model = VoilByDOT
        fields = ['np', 'theme', 'qust', 'vi_viol', 'osp', 'dop_osp', 'ntd_link', 'photo']
        widgets = {
            "np": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '№п/п'
            }),
            "theme": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема №'
            }),
            "qust": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вопрос №'
            }),
            "vi_viol": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Выявленное нарушение'
            }),
            "osp": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Основной признак'
            }),
            "dop_osp": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительный признак'
            }),
            "ntd_link": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на НТД'
            }),
            "photo": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фото'
            }),

        }
