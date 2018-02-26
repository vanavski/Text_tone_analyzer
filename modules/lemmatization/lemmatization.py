# Copyright © 2017-2018. All rights reserved.
# Authors: German Yakimov, Aleksey Sheboltasov
# License: https://github.com/GermanYakimov/Text_tone_analyzer/blob/master/LICENSE
# Contacts: german@yakimov.su, alekseysheboltasov@gmail.com


import pymorphy2
from string import ascii_letters


def latin_letter(word):
    return all(map(lambda c: c in ascii_letters, word))


def lemmatization(string):
    morph = pymorphy2.MorphAnalyzer()
    new_string = ''
    for word in string.split():
        if word.isalpha() and not latin_letter(word):
            new_string += word + ' '

    string = new_string.strip()

    punctuations_list = ['.', ',', '?', '!', ':', ';', '/', '&', '*', '%', '@', '#', '+', '=', '>', '<', '{', '}', '[',
                         ']', '"', "'", '`',
                         '$', '№', '^', '(', ')', '—', '«', '»']

    interjections_list = [' а ', ' а как же ', ' алло ', ' алле ', ' аминь ', ' ах ', ' ах ах ах ',
                          ' боже ', ' бах ', ' бац ', ' все ', ' го ', ' господи ', ' да ', ' е ', ' ё ',
                          ' е мае ', ' ё мае ',
                          ' ей богу ', ' елки палки ', ' елы палы ',
                          ' ёлки палки ', ' ёлы палки ', ' епт ', ' ёпт ', ' епть', ' ёпть ', ' естественно ',
                          ' здравствуйте ', ' здравствуй ', ' здрасьте ',
                          ' извините ', ' кыш ', 'ко ко ко', ' м ', ' ну ка ', ' ну ', ' ну ну ', ' о ',
                          ' окей ', ' ой ', ' опа ', ' опаньки ',
                          ' ох ', ' поди ', ' подожди ', ' привет ', ' простите ', ' прощайте ', ' пока ', ' стоп ',
                          ' то то ', ' тик так ', ' тсс ', ' ух ',
                          ' фух ', ' фуух ', ' фууух ', ' ха ', ' хлобысь ', ' эй ']

    prepositions_list = [' а ля ', ' без ', ' без ведома ', ' безо ', ' благодаря ', ' близ ', ' близко от ', ' в ',
                         ' в виде ', ' в зависимости от ',
                         ' в интересах ', ' в качестве ', ' в лице ', ' в отличие от ', ' в отношении ', ' в пользу ',
                         ' в преддверии ', ' в продолжение ',
                         ' в результате ', ' в роли ', ' в связи с ', ' в силу ', ' в случае ', ' в соответствии с ',
                         ' в течение ', ' в целях ',
                         ' вблизи ', ' ввиду ', ' вглубь ', ' вдогон ', ' вдоль ', ' взамен ', ' включая ', ' вокруг ',
                         ' вместо ', ' вне ', ' внизу ',
                         ' внутри ', ' внутрь ', ' во ', ' во имя ', ' вовнутрь ', ' возле ', ' вопреки ', ' впереди ',
                         ' вплоть до ', ' впредь до ',
                         ' вразрез ', ' вроде ', ' вслед ', ' вследствие ', ' для ', ' до ', ' за ', ' за вычетом ',
                         ' за исключением ', ' за счет ',
                         ' из ', ' из за ', ' из под ', ' изнутри ', ' изо ', ' исключая ', ' исходя из ', ' к ',
                         ' касаемо ', ' касательно ', ' ко ',
                         ' кроме ', ' кругом ', ' лицом к лицу с ', ' на ', ' на благо ', ' на виду у ',
                         ' на глазах у ', ' на предмет ', ' наверху ',
                         ' наверху ', ' навстречу ', ' над ', ' надо ', ' назад ', ' накануне ', ' наместо ',
                         ' наперекор ', ' наперерез ', ' наперехват ',
                         ' наподобие ', ' напротив ', ' наряду с ', ' насчет ', ' начиная с ', ' насчёт ', ' не без ',
                         ' не считая ', ' невзирая на ',
                         ' недалеко от ', ' независимо от ', ' несмотря на ', ' ниже ', ' о ', ' об ', ' обо ',
                         ' около ', ' окромя ', ' от ',
                         ' от имени ', ' от лица ', ' относительно ', ' ото ', ' перед ', ' передо ', ' по ',
                         ' по линии ', ' по мере ',
                         ' по направлению к ', ' по поводу ', ' по причине ', ' по случаю ', ' по сравнению с ',
                         ' поблизости от ', ' поверх ', ' под ',
                         ' под видом ', ' под эгидой ', ' подле ', ' подо ', ' подобно ', ' позади ', ' позднее ',
                         ' помимо ', ' поперек ', ' поперёк ',
                         ' порядка ', ' посередине ', ' посерёдке ', ' посередке ', ' посередь ', ' после ',
                         ' посреди ', ' посредине ', ' посредством ',
                         ' пред ', ' предо ', ' прежде ', ' при ', ' при помощи ', ' применительно к ', ' про ',
                         ' промеж ', ' против ', ' противно ',
                         ' путем ', ' путём ', ' ради ', ' рядом с ', ' с ', ' с ведома ', ' с помощью ',
                         ' с прицелом на ', ' с точки зрения ',
                         ' с целью ', ' сверх ', ' сверху ', ' свыше ', ' сзади ', ' следом за ', ' смотря по ',
                         ' снизу ', ' со ', ' согласно ',
                         ' спустя ', ' среди ', ' сродни ', ' судя по ', ' у ', ' через ']

    particles_list = [' а вот ', ' авось ', ' ага ', ' бишь ', ' будто ', ' буквально ', ' бы ', ' ведь ', ' вероятно ',
                      ' вон ', ' вот ', ' вот вот ',
                      ' вроде ', ' вряд ли ', ' все ', ' таки ', ' всего ', ' да ', ' да уж ', ' ка ', ' давай ',
                      ' даже ', ' дескать ', ' едва ли ',
                      ' едва ли не ', ' если ', ' еще ', 'ещё ', ' же ', ' ка ', ' как ', ' ладно ', ' навряд ли ',
                      ' наоборот ', ' неа ', ' неужто ',
                      ' ну ', ' ну ну ', ' ну с ', ' откуда ', ' очевидно ', ' по видимому ', ' поди ', ' пожалуй ',
                      ' пожалуйста ', ' походу ', ' прямо ',
                      ' пусть ', ' разве ', ' ровно ', ' с ', ' словно ', ' собственно ', ' спасибо ', ' так ',
                      ' таки ', ' типа ', ' то то ', ' тоже ',
                      ' уж ', ' уже ', ' хотя ', ' хоть ', ' якобы ']

    numbers_list = [' восемнадцать ', ' восемь ', ' восемьдесят ', ' восьмеро ', ' два ', ' двадцать ', ' двенадцать ',
                    ' две ', ' двое ', ' девять ',
                    ' девяносто ', ' девятеро ', ' девятнадцать ', ' десять ', ' десятеро ', ' дофига ', ' много ',
                    ' немного ', ' немножно ',
                    ' несколько ', ' оба ', ' один ', ' одиннадцать ', ' полтора ', ' пятеро ', ' пятнадцать ',
                    ' пять ', ' пятьдесят ', ' раз ',
                    ' семь ', ' семеро ', ' семнадцать ', ' семьдесят ', ' сорок ', ' сто ', ' двести ', ' триста ',
                    ' четыреста ', ' пятьсот ',
                    ' шестьсот ', ' семьсот ', ' восемьсот ', ' девятьсот ', ' тысяча ', ' три ', ' тридцать ',
                    ' трое ', ' четыре ', ' четверо ',
                    ' четырнадцать ', ' шесть ', ' шестеро ', ' шестнадцать ', ' шестьдесят ']

    conjuctions_list = [' а ', ' и ', ' а ведь ', ' а именно ', ' а не то ', ' а то ', ' аки ', ' благодаря тому что ',
                        ' благодаря чему ', ' будто ',
                        ' в результате чего ', ' ведь ', ' впрочем ', ' вследствие чего ', ' где ', ' где то ',
                        ' дабы ', ' даже ', ' до тех пор пока ',
                        ' до тех пор пока не ', ' до того как ', ' докуда ', ' едва ', ' если ', ' ежели ', ' же ',
                        ' зато ', ' зачем ', ' и ', ' или ',
                        ' ибо ', ' из за того что ', ' из за этого ', ' иль ', ' именно ', ' иначе ', ' итак ',
                        ' кабы ', ' как ', ' как бы не ',
                        ' как то ', ' каков ', ' какой ', ' когда ', ' коли ', ' который ', ' куда ', ' либо ',
                        ' лишь ', ' лишь только ', ' настолько ',
                        ' нежели ', ' но ', ' однако ', ' однако же ', ' окуда ', ' оттого ', ' отчего ',
                        ' перед тем как ', ' по мере того как ',
                        ' пока не ', ' поскольку ', ' потому как ', ' потому что ', ' притом ', ' причем ', ' причём ',
                        ' просто ', ' пусть ', ' равно ',
                        ' разве ', ' с тем чтобы ', ' сколько ', ' следовательно ', ' словно ', ' столько ',
                        ' так как ', ' также ', ' то ', ' то есть  ',
                        ' то ли ', ' тоже ', ' только ', ' хоть ', ' хотя ', ' чем ', ' что ', ' чтоб ', ' чтобы ',
                        ' чуть ']

    pronouns_list = [' все все ', ' какой либо ', ' кое кто ', ' кое что ', ' кто ', ' кто либо ', ' многий ',
                     ' сий ', ' такой то ', ' тот то ', ' чей либо ', ' чей нибудь ', ' чей то ', ' мы ',
                     ' вы ', ' он ', ' она ', ' оно ', ' они ', ' ты ', ' некто ', ' нечто ', ' каждый ',
                     ' любой ', ' ваш ', ' их ', ' мой ', ' мое ', ' мое ', ' моя ', ' наш ', ' свой ', ' твой ',
                     ' чей ', ' тот ', ' этот ', ' эта', ' эти ', ' это ', ' друг друга ', ' друг с другом ',
                     ' между собой ', ' его ', ' ее ', ' её ', ' их ', ' вас ', ' нас ', ' они ']

    link_parts_list = ['http', 'https', 'ftp', 'com', 'ru', 'de', 'kz', 'aero', 'asia', 'biz', 'edu', 'coop', 'gov', 'info',
                  'int', 'net', 'org', 'onion', 'pro', 'es', 'eu', 'fr', 'ga', 'gb', 'gp', 'tv', 'me', 'su', 'ua', 'uk', 'us', ]

    part_of_speech_dictionary = {'interjection': interjections_list, 'preposition': prepositions_list,
    'particles': particles_list, 'number': numbers_list, 'conjuction': conjuctions_list, 'pronouns': pronouns_list}

    string = string.lower()

    string = ' ' + string + ' '

    for word in punctuations_list:
        string = string.replace(word, '')

    for part_of_speech in part_of_speech_dictionary:
        for word in part_of_speech_dictionary[part_of_speech]:
            string = string.replace(word, ' ')

    string = string.strip().split()
    new_string = list()
    flag = False

    for word in string:
        for link_part in link_parts_list:
            if link_part in word:
                flag = True
                break
        if not flag:
            new_string.append(word)
        flag = False

    string = new_string

    for num, word in enumerate(string):
        string[num] = morph.parse(word)[0].normal_form

    string = [word + ' ' for word in string]

    return ''.join(string).strip().lower()

