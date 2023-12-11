# excell_functions
> На данный момент библиотека находится в процессе разработки. Текущее состояние можно посмотреть [здесь](https://github.com/A1eksMa/excell_functions/blob/main/PROGRESS.md)


## О проекте

**excell_functions** - библиотека, которая позволяет использовать привычный синтаксис функций MS Excell в работе с объектами DataFrame / Serias библиотеки pandas

===

<details>
<summary>** Бэкграунд **</summary>

Идея создания этой библиотеки родилась как шутка, из сравнения библиотеки pandas с *Excell*-ем (как средства работы с таблицами).

Я ❤️ Excell - и не стесняюсь в этом признаться.

Не так давно меня занесло на курс по анализу данных, где в качестве основного инструмента для изучения и работы с данными использовалась библиотека *pandas*, а также другие библиотеки и средства визуализации данных на *python*.

Когда я только начинал изучать pandas, мне всегда не хватало привычного функционала MS Excell. Безусловно, аналог практически всего функционала Excell (и даже больше) есть в pandas, и может быть реализован с помощью собственных методов этой библиотеки, либо средствами базового python. Но поначалу синтаксис pandas был для меня не очень привычен, да и навыков базового программирования на python мне изрядно не хватало. Честно говоря, я до сих пор продолжаю практически каждый день открывать в этой области все новые и новые грани.

Временами доходило до того, что вместо обработки данных с помощью pandas мне проще было выгрузить датафрейм в xls-файл и сделать некоторую предобработку, используя привычный функционал MS Excell.

Поразмыслив, я пришел к выводу что в утверждении "Пандас - это Ексель питона" есть зерно истины.
Я решил, что создание библиотеки, которая позволяет использовать привычный синтаксис функций MS Excell в работе с объектами DataFrame / Serias библиотеки pandas, имеет некоторый смысл.

Есть несколько причин, по которым я написал эту библиотеку:
- во-первых: я хотел немного прокачать навыки базового python на не слишком сложной, с точки зрения кода и требований к программированию, основе;
- во-вторых: я подумал, что совсем не лишним будет освежить в памяти или открыть для себя новые, редко используемые функции MS Excell;
- в-третьих:  я только-только открыл для себя git и мне хотелось получить некоторый практический навык работы с ним, а также немного освоиться на github;
- в-четвертых: я намеревался немного потренироваться с размещением кодовой базы в центральном репозитории python, чтобы иметь возможность свободно размещать и скачивать ее посредством pip.

К тому же (в-пятых?), я как раз осваивал новый для меня текстовый редактор с весьма необычной логикой набора текста [vim], а также прокачивал навыки слепой печати в английской раскладке, и мне хотелось немного попрактиковаться в наборе кода на python.
</details>

===

Я надеюсь, что создание этой библиотеки будет полезно кому-нибудь, кто также как и я делает свои первые шаги в области машинного обучения или анализа данных, и не имея значительного опыта в программировании сможет опереться на язык аналогий между pandas и MS Excell, которые я попытался провести.

Не судите слишком строго - это мой первый репозиторий и первый опыт работы с открытым кодом на github.
Я буду признателен за любые комментарии, правки или замечания, которые позволят сделать мой код чище и лучше.

**Проект всегда открыт для Ваших pull requests!**
 
## Установка

### Первый способ - ручная установка из репозитория на github
Чтобы установить библиотеку с помощью git, перейдите в директорию, из которой Ваш python сможет подключить ее в качестве внешнего модуля и выполните команду:

```bash
git clone https://github.com/A1eksMa/excell_functions/
```
которая скопирует содержимое репозитория `excell_functions`.

Путь к директории с модулями может варьировать в зависимости от верссии Вашего python, настроек среды и установленной операционной системы.
Как правило, пути поиска модулей указаны в переменной `sys.path` и могут быть изменены вручную, что позволяет положить модуль в любое удобное для вас место.

По умолчанию при попытке импортировать модуль, python будет пытаться определить его местоположение в папке вызова текущего скрипта или в системных папках, в которых установлен python.
Если Вы используете виртуальное окружение python (что предпочтительно), модуль должен располагаться в папке site-packages Вашего виртуального окружения.

### Второй способ - автоматическая установка из центрального репозитория python
Второй способ установить библиотеку - загрузить ее из центрального репозитория python с помощью менеджера пакетов pip, используя команду:

```bash
pip install excell_functions
 ```

или, в некоторых случаях:

```bash
pip3 install excell_functions
```

Используйте эту команду с "`!`" в начале строки, если Вы запускаете ее из виртуального окружения python или Вашей любимой IDE (например, в jupyter notebook):

```python
!pip install excell_functions
```

или, в некоторых случаях:

```python
!pip3 install excell_functions
```

Данное действие достаточно совершить ОДНОКРАТНО (для скачивания и установки библиотеки и всех ее зависимостей).

Второй способ установки более прост, однако версия, размещенная в центральном репозитории может быть не самой актуальной и отличаться от текущего состояния проекта на github.


## Зависимости
Значительная часть фунций библиотеки `excell_functions` написана на базовом python и не требует специальной установки каких-либо дополнительных модулей.
Однако для корректной работы всех функций требуется наличие в Вашей среде разработки некоторых предустановленных модулей и библиотек.
Их перечень содержится в файле `requirements.txt` в корневом каталоге проекта. 

Ручная установка с помощью git предполагает, что все необходимые зависимости (такие как pandas, numpy  и прочие) уже установлены в Вашей системе.
Если нет - придется установить их вручную. Используйте стандартные методы установки и загрузки пакетов из центрального репозитория с помощью стандартного менеджера пакетов pip или pip3.

При установке библиотеки вторым способом (через pip) все требуемые зависимости будут загружены пакетным менеджером автоматически при первоначальной загрузке проекта.

## Структура проекта
Каждая из категорий функций Ексель выделена в отдельный модуль (отдельный каталог в корневой директории проекта), что позволяет подгружать отдельные категории функций используя конструкцию:

```python
from excell_functions import [categorie's name]
```

В корневой директории каждого модуля находятся:
- файл `__init__.py` с кодом на python:
    - название модуля в первой строке (под комментарием),
    - название функции модуля в терминах MS Excell (под комментарием),
    - название функции python,
    - многострочный литерал с описанием ожидаемой работы функции,
    - код функции.

    В случае, если в данном месте кода написано
```python
    pass
```
    можете расценивать это как фразу:
```python
    # "напишите Ваш код здесь!" ))).
```
- файл `[categorie's name].csv` с перечнем функций и кратким описанием работы функции с официального сайтм Майкрософт;
- файл `tests.xlsx`, который содержит результаты тестов каждой функции в отдельной вкладке. Некоторые комментарии в этом файле могут представлять интерес, если результат работы функций библиотеки будет отличаться от Ваших ожиданий;
- файлы `*.ipynb`, названия которых совпадают с названиями функций (в случаях, когда функция была протестирована в `jupyter notebook`)

## Как пользоваться
### Импорт библиотеки
После установки Вы можете обратиться к библиотеке, используя стандартный метод импорта:

```python
import excell_functions
```

или загрузить отдельно интересующую вас категорию функций Ексел как субмодуль:

```python
from excell_functions import [name_category]
```

Вы также можете назначить любой псевдоним загруженной Вами библиотеки или модулю по Вашему вкусу. 
Для моей библиотеки я рекомендую использовать `exfun` - с одной стороны это не слишком длинно, с другой - достаточно позитивно звучит:

```python
import excell_functions as exfun
```

Excellent! Fun!

### Использование функций библиотеки
После импорта библиотеки Вы можете начать использовать ее функционал, используя выбранное Вами обращение к библиотеке, категорию и название функции, разделенные через "`.`"

```python
excell_functions.category.FUNCTION(a, b, c)
```

Например, обращение к логической функции `ЕСЛИ()` будет выглядеть как:

```python
exfun.logical.IF(True, "It's true!", "It's false!")
```

Названия функций, как правило, будут совпадать, с названием функций MS Excell в английской версии MS Office.


## Примеры
Функция `IF(Condition, A, B)` возвращает `A`, в случае когда `condition == True`, в противном случае возвращает `B`.
