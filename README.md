# Анализатор тональности текста

Sentiment analysis (анализ тональности) — это область компьютерной лингвистики, которая занимается изучением мнений и эмоций в текстовых документах.
В зависимости от поставленной задачи нас могут интересовать разные свойства, например:
<ul>
    <li>автор — кому принадлежит это мнение</li>
    <li>тема — о чем говорится во мнении</li>
    <li><b>тональность — позиция автора относительно упомянутой темы</b></li>
</ul>

## Прицип работы программы:
<ol>
    <li><i>Лемматизация документа</i> - приведение всех слов в документе к начальной форме с помощью морфологического анализатора pymorphy2, удаление знаков препинания, служебных частей речи, слов на других языках.</li>
    <li><i>Выделение признаков текста</i> - документу сопоставляется 3 числа, которые являются численной характеристикой его эмоциональной окраски, посчитанной с помощью формулы <i>ΔTF-IDF</i>. Веса считаются для с применением униграмм (слова документа по одному), биграмм (комбинации из двух слов) и триграмм (сочетание 3 слов).</li>
    <li><i>Определение класса документа</i> ("положительный", "нейтральный", "отрицательный") с помощью метода логистической регрессии </li> 
</ol>

## На данном этапе мы осуществили следующее:
<ul>
    <li>Лемматизация документа</li>
    <li>Выделение признаков текста</li>
    <li>Бинарная классификация документов на "положительные" и "отрицательные"</li>
</ul>

## Инструкция по сборке:
Сборка осуществляется с помощью интерпретатора Pytnon 3.x через командную строку или IDE. Необходимо запустить файл "main.py".
<br><b>Входные данные:</b> Полный текст документа.
<br><b>Выходные данные:</b> Тональность документа и вероятность.
<br>Программа имеет возможность голосового ввода.

### Библиотеки, необходимые для сборки:
<ul>
    <li>PyQt5</li>
    <li>sklearn</li>
    <li>pandas</li>
    <li>pymorphy2</li>
    <li>requests</li>
    <li>speech_recognition</li>
    <li>sys</li>
    <li>os</li>
    <li>logging</li>
    <li>datetime</li>
    <li>platform</li>
    <li>math</li>
    <li>sqlite3</li>
    <li>re</li>
    <li>time</li>
    <li>csv</li>
</ul>

### Пример работы:

`cd Text_tone_analyzer`
<br>`python3 master/main.py`


<b>Text:</b> `"Главный итог завершившихся Игр ХХХ Олимпиады в Лондоне – то чувство гордости
за нашу страну, которое испытывали болельщики благодаря выступлениям российских олимпийцев»,
— считает Александр Жуков"`

<b>Output:</b>
<br>`Positive`
<br>`80.598%`

#### Copyright © 2017-2018. All rights reserved.
#### Authors: German Yakimov, Aleksey Sheboltasov
#### License: https://github.com/GermanYakimov/Text_tone_analyzer/blob/master/LICENSE
#### Contacts: german@yakimov.su, alekseysheboltasov@gmail.com
