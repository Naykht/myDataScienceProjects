**Стажировки:**
- \[12.20-02.21] Sberseasons: [Data Scientist](https://github.com/knyht/data-science-projects/blob/master/certificates/sberseasons.pdf)

**Дополнительные курсы:**
- \[01.20-09.20] Яндекс.Практикум: [Специалист по Data Science](https://github.com/knyht/data-science-projects/blob/master/certificates/diploma_yandex_practicum.pdf)

**Университет, Высшая Школа Экономики:**
- Ассистент по курсу:
  - \[2021, 4 курс, 1 семестр] [Глубинные методы машинного обучения](http://wiki.cs.hse.ru/Современные_методы_машинного_обучения_(майнор_ИАД))
  - \[2020, 3 курс, 1 семестр] [Машинное обучение (продвинутый уровень)](http://wiki.cs.hse.ru/Машинное_обучение_(ФЭН)_-_2020) 
- \[2020-2021, 2-3 курсы] Майнор, Интеллектуальный анализ данных (ИАД):
  - [Введение в анализ данных](http://wiki.cs.hse.ru/Введение_в_анализ_данных_(майнор_ИАД))
  - [Глубинные методы машинного обучения](http://wiki.cs.hse.ru/Современные_методы_машинного_обучения_(майнор_ИАД))
  - [Прикладные задачи анализа данных](http://wiki.cs.hse.ru/Прикладные_задачи_анализа_данных)
- \[2021, 3 курс] Курсовой проект:
  -  [Косарев И.М.](https://www.hse.ru/staff/i.kosarev), [Построение рекомендательной системы для продвижения партнерских услуг физическим лицам коммерческого банка на основе данных их транзакций](https://github.com/knyht/data-science-projects/blob/master/recsys_bank_transactions/recsys_bank_transactions.pdf)
- \[2020, 2 курс] Курсовая работа:
  - [Ефремов С.Г.](https://www.hse.ru/staff/sefremov), [Предиктивный анализ потока абитуриентов на образовательные программы НИУ ВШЭ](https://github.com/Naykht/DataScienceProjects/blob/master/predictive_analysis_flow_of_applicants/polikarpov_kn_prediktivnyy-analiz-potoka-abiturientov-na-obrazovatelnye-programmy-niu-vshe_142611.pdf)

# Структура проектов
- [Регрессия](https://github.com/knyht/data-science-projects/blob/master/README.md#регрессия)
- [Классификация](https://github.com/knyht/data-science-projects/blob/master/README.md#классификация)
- [Тексты](https://github.com/knyht/data-science-projects/blob/master/README.md#тексты)
- [Временные ряды](https://github.com/knyht/data-science-projects/blob/master/README.md#временные_ряды)
- [Рекомендательные системы]
- [Нейронные сети]

## Регрессия
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Предсказание цен на недвижимость][1]|ИАД|Необходимо реализовать алгоритмы kNN и линейного регрессии с нуля и добиться качества не больше 0.121 на тестовых данных по метрике *RMSE*.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn`|Завершен|
|[Предсказание стоимости автомобилей][2]|Яндекс.Практикум|Необходимо построить модель машинного обучения, которая сможет быстро и качественно подсказать клиенту рыночную стоимость автомобиля.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `catboost` `lightgbm`|Завершен|
|[Бурение скважины][3]|Яндекс.Практикум|С помощью модели машинного обучения необходимо определить регион для бурения скважины, который принесет наибольшую прибыль.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `scipy` `бутстрап` `доверительные интервалы`|Завершен|
|[Коэффициент восстановления золота][4]|Яндекс.Практикум|Необходимо построить прототип модели машинного обучения для предсказания коэффициента восстановления золота из золотосодержащей руды.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn`|Завершен|
|[Шифрование данных][5]|Яндекс.Практикум|Необходимо разработать метод преобразования данных для модели линейной регрессии с целью шифрования персональной информации.|`pandas` `numpy` `sklearn`|Завершен|

## Классификация
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Предиктивный анализ потока абитуриентов][6]|Курсовая работа|Необходимо предсказать, с какой вероятность абитуриент поступит в университет на определенную программу после подачи документов в приемную коммисию, а также определить, какие признаки являются наиболее важными при определении этой вероятности.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn`|Завершен|
|[Предсказание наличия диабета][7]|ИАД|Необходимо предсказать наличие или отсутствие диабета у человека.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `бустинг` `бэггинг` `стэкинг`|Завершен|
|[Телеком][8]|Яндекс.Практикум|Необходимо научиться прогнозировать отток клиентов.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `кластеризация` `понижение размерности` `catboost`|Завершен|
|[Рекомендация тарифов][9]|Яндекс.Практикум|Необходимо построить модель для задачи классификации, которая выберет подходящий тариф клиенту.|`pandas` `sklearn`|Завершен|
|[Отток клиентов][10]|Яндекс.Практикум|Необходимо спрогнозировать, уйдет клиент из банка в ближайшее время или нет.|`pandas` `numpy` `matplotlib` `sklearn`|Завершен|

## Тексты
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Предсказание категории товара][11]|ИАД|Имеется информация об объектах 50 классов. Необходимо по новым объектам предсказать категорию товара.|`pandas` `numpy` `matplotlib`  `sklearn` `BOW` `TF-IDF` `Hasing Vectorizer` `pymystem3` `pymorphy2` `spacy` `genism` `Word Vectors`|Завершен|
|[Токсичные комментарии][12]|Яндекс.Практикум|Необходимо построить модель, которая будет классифицировать комментарии на позитивные и негативные.|`pandas` `numpy` `matplotlib`  `sklearn` `nltk` `re` `spacy` `BOW` `TF-IDF`|Завершен|

## Временные ряды
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Предсказание заказов такси][13]|Яндекс.Практикум|Необходимо спрогнозировать количество заказов такси на следующий час.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `statsmodels`|Завершен|

## Рекомендательные системы
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Построение рекомендательной системы для продвижения партнерских услуг физическим лицам коммерческого банка на основе данных их транзакций][14]|Курсовой проект|Необходимо реализовать рекомендательную систему, которая позволит предсказывать наиболее релевантные категории товаров или услуг клиентам банка по истории их транзакций.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `scipy` `psycopg2-binary`|Завершен|

## Нейронные сети
- ### Регрессия
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Предсказание возраста покупателей по фотографии][15]|Яндекс.Практикум|Необходимо построить модель, определяющую по фотографии покупателя его возраст.|`pandas` `matplotlib` `seaborn` `tensorflow.keras` `ResNet50`|Завершен|

- ### Классификация
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Классификация изображений][17]|ИАД|Необходимо построить нейронную сеть классификации 200 классов изображений и добиться *accuracy* не менее 0.44.|`numpy` `sklearn` `torch` `torchvision`|Завершен|
|[Fashion-MNIST][16]|ИАД|Необходимо реализовать оптимизатор Adam с нуля и построить архитектуры нейронных сетей, в том числе AlexNet и LeNet-5.|`numpy` `torch` `torchvision`|Завершен|

- ### Детекция
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Детекция фруктов на изображении][17]|ИАД|Необходимо обучить детектор фруктов на изображении и добиться *PR-AUC* не менее 0.91 на тестовом.|`pandas` `numpy` `matplotlib` `sklearn` `torch` `torchvision` `FastRCNNPredictor` `albumentations`|Завершен|

[1]: https://github.com/knyht/data-science-projects/tree/master/house_price_prediction
[2]: https://github.com/knyht/data-science-projects/tree/master/prediction_price_of_cars
[3]: https://github.com/knyht/data-science-projects/tree/master/well_drilling
[4]: https://github.com/knyht/data-science-projects/tree/master/rate_of_recovery_of_gold
[5]: https://github.com/knyht/data-science-projects/tree/master/data_encryption

[6]: https://github.com/knyht/data-science-projects/tree/master/predictive_analysis_flow_of_applicants
[7]: https://github.com/knyht/data-science-projects/tree/master/diabet_classification
[8]: https://github.com/knyht/data-science-projects/tree/master/telecom
[9]: https://github.com/knyht/data-science-projects/tree/master/mobile_plans_classification
[10]: https://github.com/knyht/data-science-projects/tree/master/customer_outflow

[11]: https://github.com/Naykht/DataScienceProjects/tree/master/category_prediction
[12]: https://github.com/Naykht/DataScienceProjects/tree/master/toxic_comments

[13]: https://github.com/Naykht/DataScienceProjects/tree/master/prediction_of_taxi_orders

[14]: https://github.com/AleksandrRadist/RecommendationSystem

[15]: https://github.com/knyht/data-science-projects/tree/master/predict_age_by_photo
[16]: https://github.com/knyht/data-science-projects/tree/master/fashion_mnist_classification
[17]: https://github.com/knyht/data-science-projects/tree/master/image_classification_detection
