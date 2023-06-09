C. Доставка со склада
=====================

+---------------------+----------------------------------+
| Ограничение времени | 4 секунды                        |
+---------------------+----------------------------------+
| Ограничение памяти  | 1 Gb                             |
+---------------------+----------------------------------+
| Ввод                | стандартный ввод или input.txt   |
+---------------------+----------------------------------+
| Вывод               | стандартный вывод или output.txt |
+---------------------+----------------------------------+

В городе работает два склада, из которых заказ может быть доставлен на дом. На каждом складе работает по одному курьеру. Курьер может доставлять только один заказ одновременно.

Сегодня поступило N заказов, каждый заказ может быть доставлен с любого из складов. Для каждого заказа и каждого из двух складов известно время, необходимое для доставки заказа и возвращения курьера обратно на склад. Заказы могут выполняться в любом порядке. Курьер может приступать к доставке следующего заказа сразу после возвращения на склад.

Для каждого из заказов определите, какой из курьеров должен его доставить чтобы последний из двух курьеров вернулся на склад после выполнения всех своих заказов как можно раньше.

Формат ввода
------------

В первой строке задаётся число N (:math:`1≤N≤1000`) — количество заказов.

В каждой из следующих N описвыются заказы, по одному в строке. В i-й строке даны два числа :math:`a_i` и :math:`b_i` (:math:`1≤ai,bi≤100`) — время доставки и возвращения первого и второго курьера соответственно для выполнения i-го заказа.

Формат вывода
-------------- 

Выведите N чисел 1 или 2, задающих номер курьера, который будет выполнять соответствующий заказ.

Если правильных ответов несколько — выведите любой из них.

Пример 1
--------

**Ввод**:

.. include:: in_1.txt
   :literal:

**Вывод**:

.. include:: out_1.txt
   :literal:

