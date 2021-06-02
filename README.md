**Стажировки:**
- \[12.20-02.21] Sberseasons: [Data Scientist/Data Analyst](https://github.com/knyht/data-science-projects/blob/master/certificates/sberseasons.pdf)

**Дополнительные курсы:**
- \[04.21-08.21] Karpov.Courses: Аналитик данных
- \[01.20-09.20] Яндекс.Практикум: [Специалист по Data Science](https://github.com/knyht/data-science-projects/blob/master/certificates/diploma_yandex_practicum.pdf)

**Университет, Высшая Школа Экономики:**
- Ассистент по курсу:
  - \[2021, 4 курс, 1 семестр] [Современные методы машинного обучения](http://wiki.cs.hse.ru/Современные_методы_машинного_обучения_(майнор_ИАД))
  - \[2020, 3 курс, 1 семестр] [Машинное обучение (продвинутый уровень)](http://wiki.cs.hse.ru/Машинное_обучение_(ФЭН)_-_2020) 
- \[2020-2021, 2-3 курсы] Майнор, Интеллектуальный анализ данных (ИАД):
  - [Введение в анализ данных](http://wiki.cs.hse.ru/Введение_в_анализ_данных_(майнор_ИАД))
  - [Современные методы машинного обучения](http://wiki.cs.hse.ru/Современные_методы_машинного_обучения_(майнор_ИАД))
  - [Прикладные задачи анализа данных](http://wiki.cs.hse.ru/Прикладные_задачи_анализа_данных)
- \[2021, 3 курс] Курсовой проект:
  -  [Косарев И.М.](https://www.hse.ru/staff/i.kosarev), [Построение рекомендательной системы для продвижения партнерских услуг физическим лицам коммерческого банка на основе данных их транзакций](https://github.com/knyht/data-science-projects/blob/master/recsys_bank_transactions/recsys_bank_transactions.pdf)
- \[2020, 2 курс] Курсовая работа:
  - [Ефремов С.Г.](https://www.hse.ru/staff/sefremov), [Предиктивный анализ потока абитуриентов на образовательные программы НИУ ВШЭ](https://github.com/Naykht/DataScienceProjects/blob/master/predictive_analysis_flow_of_applicants/polikarpov_kn_prediktivnyy-analiz-potoka-abiturientov-na-obrazovatelnye-programmy-niu-vshe_142611.pdf)

## Регрессия
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------|:-------:|
|[Предсказание цен на недвижимость][1]|ИАД|- Необходимо пеализовать алгоритмы kNN и линейного регрессии своими руками - Добиться того, чтобы лучший алгоритм давал качество не больше 0.121 на тестовых данных по метрике *RMSE*.|pandas, sklearn, matplotlib, seaborn, numpy|`Завершен`|
|[Предсказание стоимости автомобилей][2]|Яндекс.Практикум|Необходимо построить модель машинного обучения, которая сможет быстро, качественно подсказать клиенту рыночную стоимость автомобиля.|pandas, sklearn, matplotlib, seaborn, numpy, catboost, lightgbm, бустинг|`Завершен`|
|[Бурение скважины][3]|Яндекс.Практикум|Необходимо решить, где бурить новую скважину, с помощью модели машинного обучения, которая позволит определить регион, который принесет наибольшую прибыль.|pandas, sklearn, matplotlib, seaborn, numpy, scipy, bootstrap, доверительные интервалы|`Завершен`|
|[Коэффициент восстановления золота][4]|Яндекс.Практикум|Необходимо построить прототип модели машинного обучения для предсказания коэффициента восстановления золота из золотосодержащей руды|pandas, sklearn, matplotlib, seaborn, numpy|`Завершен`|
|[Шифрование данных][5]|Яндекс.Практикум|Необходимо разработать метод преобразования данных для модели линейной регрессии, чтобы сложно было восстановить персональную информацию.|pandas, sklearn, numpy, линейная алгебра|`Завершен`|
- ## Нейронные сети
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------|:-------:|
|[Предсказание возраста покупателей по фотографии][6]|Яндекс.Практикум|Необходимо построить модель, определяющую по фотографии покупателя его возраст.|pandas, matplotlib, seaborn, tensorflow.keras, архитектура ResNet50|`Завершен`|

## Классификация
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------|:-------:|
|[Предсказание наличия диабета][7]|ИАД|Необходимо предсказать наличие или отсутствие диабета у человека.|pandas, sklearn, matplotlib, seaborn, numpy, бустинг, бэггинг, стэкинг|`Завершен`|
|[Предиктивный анализ потока абитуриентов][8]|Курсовая работа|Предскажем с какой вероятность абитуриент поступит в университет на определенную программу после подачи документов в приемную коммисию, а также определим, какие признаки являются наиболее важными при определении этой вероятности.|pandas, sklearn, matplotlib, seaborn, numpy|`Завершен`|
|[Телеком][9]|Яндекс.Практикум|Необходимо научиться прогнозировать отток клиентов.|pandas, sklearn, matplotlib, seaborn, numpy, catboost, кластеризация, работа с дисбалансом классов, PCA, TSNE|`Завершен`|
|[Рекомендация тарифов][10]|Яндекс.Практикум|Необходимо построить модель для задачи классификации, которая выберет подходящий тариф.|pandas, sklearn|`Завершен`|
|[Отток клиентов][11]|Яндекс.Практикум|Необходимо спрогнозировать, уйдёт клиент из банка в ближайшее время или нет.|pandas, sklearn, matplotlib, numpy, работа с дисбалансом классов|`Завершен`|
- ### Нейронные сети
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------|:-------:|
|[FashionMNIST][12]|ИАД|Необходимо построить модель, определяющую по фотографии покупателя его возраст.|pandas, matplotlib, seaborn, tensorflow.keras, архитектура ResNet50|`Завершен`|

## Тексты
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------|:-------:|
|[Предсказание категории товара][13]|ИАД|Имеется информация об объектах 50 классов. Необходимо по новым объектам предсказать категорию товара.|pandas, sklearn, matplotlib, numpy, pymystem3, pymorphy2, spacy, TF-IDF, Hasing Vectorizer, Word Vectors, BOW|`Завершен`|
|[Токсичные комментарии][14]|Яндекс.Практикум|Необходимо построить модель, которая будет классифицировать комментарии на позитивные и негативные.|pandas, sklearn, matplotlib, numpy, nltk, re, spacy, TF-IDF, BOW|`Завершен`|

## Временные ряды
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------|:-------:|
|[Предсказание заказов такси][15]|Яндекс.Практикум|Необходимо спрогнозировать количество заказов такси на следующий час.|pandas, sklearn, matplotlib, seaborn, numpy, statsmodels|`Завершен`|

## Рекомендательные системы
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------|:-------:|
|[Построение рекомендательной системы для продвижения партнерских услуг физическим лицам коммерческого банка на основе данных их транзакций][16]|Курсовой проект|||`Завершен`|

[1]: https://github.com/knyht/data-science-projects/tree/master/house_price_prediction
[2]: https://github.com/knyht/data-science-projects/tree/master/prediction_price_of_cars
[3]: https://github.com/knyht/data-science-projects/tree/master/well_drilling
[4]: https://github.com/knyht/data-science-projects/tree/master/rate_of_recovery_of_gold
[5]: https://github.com/knyht/data-science-projects/tree/master/data_encryption
[6]: https://github.com/knyht/data-science-projects/tree/master/predict_age_by_photo

[7]: https://github.com/knyht/data-science-projects/tree/master/diabet_classification
[8]: https://github.com/knyht/data-science-projects/tree/master/predictive_analysis_flow_of_applicants
[9]: https://github.com/knyht/data-science-projects/tree/master/telecom
[10]: https://github.com/knyht/data-science-projects/tree/master/mobile_plans_classification
[11]: https://github.com/knyht/data-science-projects/tree/master/customer_outflow
[12]: https://github.com/knyht/data-science-projects/tree/master/fashion_mnist_classification

[13]: https://github.com/Naykht/DataScienceProjects/tree/master/toxic_comments
[14]: https://github.com/Naykht/DataScienceProjects/tree/master/prediction_of_taxi_orders

[15]: https://github.com/Naykht/DataScienceProjects/tree/master/category_prediction

[16]: 


