**Стажировки:**
- \[12.20-02.21] Sberseasons: [Data Scientist](https://github.com/knyht/data-science-projects/blob/master/certificates/sberseasons.pdf)

**Дополнительные курсы:**
- \[01.20-09.20] Яндекс.Практикум: [Специалист по Data Science](https://github.com/knyht/data-science-projects/blob/master/certificates/diploma_yandex_practicum.pdf)

**Университет, Высшая Школа Экономики:**
- Ассистент по курсу:
  - \[2021, 4 курс, 1 семестр] Machine Learning with Python
  - \[2021, 4 курс, 1 семестр] [Основы глубинного обучения](http://wiki.cs.hse.ru/Современные_методы_машинного_обучения_(майнор_ИАД))
  - \[2020, 3 курс, 1 семестр] [Машинное обучение](http://wiki.cs.hse.ru/Машинное_обучение_(ФЭН)_-_2020) 
- \[2020-2021, 2-3 курсы] Майнор, Интеллектуальный анализ данных (ИАД):
  - [Введение в анализ данных](http://wiki.cs.hse.ru/Введение_в_анализ_данных_(майнор_ИАД))
  - [Глубинные методы машинного обучения](http://wiki.cs.hse.ru/Современные_методы_машинного_обучения_(майнор_ИАД))
  - [Прикладные задачи анализа данных](http://wiki.cs.hse.ru/Прикладные_задачи_анализа_данных)
- \[2021, 3 курс] Курсовой проект:
  -  [Косарев И.М.](https://www.hse.ru/staff/i.kosarev), [Построение рекомендательной системы для продвижения партнерских услуг физическим лицам коммерческого банка на основе данных их транзакций](https://github.com/knyht/data-science-projects/blob/master/projects/recsys_bank_transactions/recsys_bank_transactions.pdf)
- \[2020, 2 курс] Курсовая работа:
  - [Ефремов С.Г.](https://www.hse.ru/staff/sefremov), [Предиктивный анализ потока абитуриентов на образовательные программы НИУ ВШЭ](https://github.com/Naykht/DataScienceProjects/blob/master/projects/predictive_analysis_flow_of_applicants/polikarpov_kn_prediktivnyy-analiz-potoka-abiturientov-na-obrazovatelnye-programmy-niu-vshe_142611.pdf)

# Структура проектов
- [Регрессия](https://github.com/knyht/data-science-projects/blob/master/README.md#регрессия)
- [Классификация](https://github.com/knyht/data-science-projects/blob/master/README.md#классификация)
- [Тексты](https://github.com/knyht/data-science-projects/blob/master/README.md#тексты)
- [Временные ряды](https://github.com/knyht/data-science-projects/blob/master/README.md#временные-ряды)
- [Рекомендательные системы](https://github.com/knyht/data-science-projects/blob/master/README.md#рекомендательные-системы)
- [Нейронные сети](https://github.com/knyht/data-science-projects/blob/master/README.md#нейронные-сети)

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
|[Предсказание пользовательской оценки отеля по тексту отзыва][18]|ИАД|Необходимо научиться предсказывать оценку отеля по отзыву и получить значение MAE не превышающее 1.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `BOW` `TF-IDF` `nltk` `genism` `Word Vectors`|Завершен|
|[Токсичные комментарии][12]|Яндекс.Практикум|Необходимо построить модель, которая будет классифицировать комментарии на позитивные и негативные.|`pandas` `numpy` `matplotlib`  `sklearn` `BOW` `TF-IDF` `nltk` `re` `spacy`|Завершен|

## Временные ряды
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Предсказание заказов такси][13]|Яндекс.Практикум|Необходимо спрогнозировать количество заказов такси на следующий час.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `statsmodels`|Завершен|

## Рекомендательные системы
|Название проекта|Источник|Описание|Инструменты|Статус|
|:-------|:-------:|:-------|:-------:|:-------:|
|[Построение рекомендательной системы для продвижения партнерских услуг физическим лицам коммерческого банка на основе данных их транзакций][14]|Курсовой проект|Необходимо реализовать рекомендательную систему, которая позволит предсказывать наиболее релевантные категории товаров или услуг клиентам банка по истории их транзакций.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `catboost` `scipy` `psycopg2-binary`|Завершен|
|[Рекомендательная модель статей][19]|ИАД|Необходимо реализовать модель рекомендательной системы статей.|`pandas` `numpy` `matplotlib` `seaborn` `sklearn` `catboost` `scipy` `lightfm` `nltk` `TF-IDF` `sentence_transformers`|Завершен|

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
|[Детекция фруктов на изображении][17]|ИАД|Необходимо обучить детектор фруктов на изображении и добиться *PR-AUC* не менее 0.91 на тестовом.|`pandas` `numpy` `matplotlib` `sklearn` `torch` `torchvision` `albumentations`|Завершен|

[1]: https://github.com/knyht/data-science-projects/tree/master/projects/house_price_prediction
[2]: https://github.com/knyht/data-science-projects/tree/master/projects/prediction_price_of_cars
[3]: https://github.com/knyht/data-science-projects/tree/master/projects/well_drilling
[4]: https://github.com/knyht/data-science-projects/tree/master/projects/rate_of_recovery_of_gold
[5]: https://github.com/knyht/data-science-projects/tree/master/projects/data_encryption

[6]: https://github.com/knyht/data-science-projects/tree/master/projects/predictive_analysis_flow_of_applicants
[7]: https://github.com/knyht/data-science-projects/tree/master/projects/diabet_classification
[8]: https://github.com/knyht/data-science-projects/tree/master/projects/telecom
[9]: https://github.com/knyht/data-science-projects/tree/master/projects/mobile_plans_classification
[10]: https://github.com/knyht/data-science-projects/tree/master/projects/customer_outflow

[11]: https://github.com/knyht/data-science-projects/tree/master/projects/category_prediction
[12]: https://github.com/knyht/data-science-projects/tree/master/projects/toxic_comments

[13]: https://github.com/knyht/data-science-projects/tree/master/projects/prediction_of_taxi_orders

[14]: https://github.com/AleksandrRadist/RecommendationSystem
[19]: https://github.com/knyht/data-science-projects/tree/master/projects/recsys_articles

[15]: https://github.com/knyht/data-science-projects/tree/master/projects/predict_age_by_photo
[16]: https://github.com/knyht/data-science-projects/tree/master/projects/fashion_mnist_classification
[17]: https://github.com/knyht/data-science-projects/tree/master/projects/image_classification_detection
[18]: https://github.com/knyht/data-science-projects/tree/master/projects/hotel_ratings_review
