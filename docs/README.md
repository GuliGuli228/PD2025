# Выполение проектной практики 
---
## Базовая часть 

### Задание:
Создать статический веб-сайт об основном проекте дисциплины "Проектная деятельность" (Графический интерфейс для NLP-анализа текстовых данных)

### Стек
**HTML**
**CSS**
**Visual Studio Code** со следующими расширениями:
1. HTML CSS Support
2. HTML Preview
3. Live Server
4. CSS Peek
5. colorize

### Релизация
Для освоения базовых навыков по программированию на HTML и CSS было принято решение воспользоваться учебным курсом на видеохостинге **YouTube** - [HTML & CSS Full Course - Beginner to Pro](https://www.youtube.com/watch?v=G3e-cpL7ofc&t=17794s). Курс состоит из 17 модулей, в каждом из которых подробно разбирается тот или иной элемент разработки. Так же курс предлагает закрепляющие упражнения после каждого модуля и финальный проект - разработка домашней страницы **YouTube**
Для оптимизации рабочего процесса была выбрана следующая стратегия:
1. Ознакомится с первой половиной курса
2. Создать шаблон сайта( закрепление навыков + выявление пробелов в знаниях)
3. Ознакомится со второй половиной курса
4. Интегрирование решений на основе новой информации
5. Завершение разработки

Вопрос дизайна был решен подбором референса на сайте [Referest](https://referest.ru/inspiration/web/pages). Так как сайт-визитка, чем дефакто является предложенный для реализации сайт, органичнее всего смотрится в формате одностраничного сайта, была реализована именно такая версия сайта(**site_ver1**).Однако техническое задание требует сайт как минимум с 5 страницами, поэтому ****site_ver1** был оптимизирован под формат многостраничного сайта (**site_ver2**). 

#### Основная структура веб сайта
Для удобной навигации по сайту было принято решение реализовать закрепленную верхнюю панель с кнопками 

**Реализация на сайте:**

![alt-Реализация на сайте](https://github.com/GuliGuli228/PD2025/blob/main/docs/images/image.png)

**Реализация в коде:**
```HTML
<div class="Header">
    <div class="Header-button"><a href="#sec1" class="Header-text"> Главная страница </a></div>
    <div class="Header-button"><a href="#sec2" class="Header-text"> О проекте</a></div>
    <div class="Header-button"><a href="#sec3" class="Header-text">Участники</a></div>
    <div class="Header-button"><a href="#sec4" class="Header-text"> Ресурсы </a></div>
    <div class="Header-button"><a href="#sec5" class="Header-text"> Журнал </a></div>
  </div>
```

Так сайт является одностраничныи, то кнопки выполняют функцию прокрутки до блока с информацией
**Реализация в коде:**
```HTML
  HTML
  <div id="sec1" style="position: absolute; top: 0px"></div>
  ...
  <div id="sec2" style="position: absolute; top: 650px"></div>
  ...
  <div id="sec3" style="position: absolute; top:1200px"></div>
  ...
  <div id="sec4" style="position: absolute; top:2300px"></div>
  ...
  <div id="sec5" style="position: absolute; top:3300px"></div>
```
```CSS
  CSS
  html{
        scroll-behavior: smooth;
      }
```
Как вы могли заметить, "якори" на странице закреплены на не относительной высоте (относительно других элементов), а на абсолютной (относительно страницы). В коммерческой практике обычно не используют такое решение, однако в рамках небольшого сайта такое решение более чем оправдано необходимостью сделать код простым и понятным.

В остальном же структура сайта типичная для HTML.
Версия моногостраничного сайта отличается от версии многостраничного тем, что вместо "якоря" используется ссылка на нужную веб страницу 

**Реализация в коде:**
```HTML
  site_ver1
  <div class="Header">
    <div class="Header-button"><a href="#sec1" class="Header-text"> Главная страница </a></div>
    <div class="Header-button"><a href="#sec2" class="Header-text"> О проекте</a></div>
    <div class="Header-button"><a href="#sec3" class="Header-text">Участники</a></div>
    <div class="Header-button"><a href="#sec4" class="Header-text"> Ресурсы </a></div>
    <div class="Header-button"><a href="#sec5" class="Header-text"> Журнал </a></div>
  </div>

  site_ver2
    <div class="Header">
    <div class="Header-button"><a href="Main.html" class="Header-text"> Главная страница </a></div>
    <div class="Header-button"><a href="About.html" class="Header-text"> О проекте</a></div>
    <div class="Header-button"><a href="Contestants.html" class="Header-text">Участники</a></div>
    <div class="Header-button"><a href="Res.html" class="Header-text"> Ресурсы </a></div>
    <div class="Header-button"><a href="Journal.html" class="Header-text"> Журнал </a></div>
  </div>

```
Заключение: в ходе выполнения обязательной части проектной практики были освоены HTML, CSS, создан веб сайт для основного проекта по учебной практики.

## Вариативная часть
---