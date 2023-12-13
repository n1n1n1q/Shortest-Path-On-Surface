# Shortest Path On Surface
![Alt Text](https://i.imgur.com/6eahnYD.gif)

## Загальна інформація
Пошук найкоротшого шляху - класична задачка у програмуванні. У цьому проєкті, ми розглядаєм більш адаптовану під реальне життя імплементацією цієї задачі, а саме пошук найкоротшого шляху на якійсь певній прямокутній ділянці. Попри те, що задача на пошук шляху є дуже поширеною та відносно простою, у нас виникло багато проблем протягом виконання цього завдання.
Програма тестилась на масивах різного розміру, за допомогою pypy3. 
Час виконання для 5000 х 5000 матриці - ~1 хвилина.
## Підготовка до реалізації
Перед тим, як приступити до реалізації проєкту - нам потрібно було дослідити саму задачу, вирішитись з алгоритмом.
Оскільки є багато різних алгоритмів, які вирішують цю проблему, нам було між чим вибирати. Провівши аналіз задачі, ми освідомили, що А* буде для нас найкращим рішенням. 
## Структури даних
У даному проєкті, все базувалось на пріоритетній черзі, оскільки вибраний алгоритм зазвичай і реалізується за допомогою неї.
Спочатку, ми використовували готовий варіант з стандартної бібліотеки Python, Queue. Зробвши чимало тестів, ми усвідомили, що на великих розмірах вхідних даних, програма працює дуже повільно. Після маленького дослідження, ми усвідомили, що проблема в вибраній структурі даних, так як пайтонівський варіант не є найбільш швидким; також обраховувались деякі варіанти.
Тому, ми написали власну імплементацію пріоритетної черги, на бази купи з стандартної бібліотеки Python, heapq.
## Алгоритм. Принципи дискретної математики
![Alt Text](https://habrastorage.org/web/293/cb8/f8c/293cb8f8c7df47f4b47977f5462d116b.png)  
Як і зазначалось раніше, ми використвуємо алгоритм А*.
#### Чому А*? 
- Варіація алгоритма Дійкстри; У рамках знаходження найкоротшої відстані від одної точки до іншої, працює швидше
- Концепт алгоритму дозволяє знахдити йому оптимальний шлях з меншою кількістю, ніж інші алгоритми.
- Завдяки евристичній оцінці дистанції, А* забезпечує більш точне знаходження оптимального шляху у графах з великою кількістю вершин
- А* завжди гарантує найоптимальніший шлях
- Використання на великій кількості вхідних даних є більш ефективним, ніж у інших розповсюджених алгоритмів, так як завдяки евристичній оцінці відкидує "дорожчі" ребра
- Гнучкість евристичної оцінки. Якщо правильно підібрати цю функцію, знаходження шляху стане значно ефективнішим
#### Принципи дискретної математики
1. Графи. Вхідне поле - зважений, неорієнтований граф, на якому і здійснюється пошук.
2. Алгоритм пошуку. А* - варіація алгоритма Дійкстри, яка спеціалізується саме на пошуку найкоротшої відстані. А* взяв від Дійкстри безумовний пошук для дослідження графа в ширину та оцінку вартості шляху. Основною відміністю ж є евристична оцінка шляху. Саме через це, А* є більш ефективним, ніж Дійкстра. Евристична оцінка дає змогу більш ефективно та точно знайти найкоротшу відстань, опускаючи гірші варіанти.
## Розподіл
Басистий Олег, Максим Жук - розробка програми
Софія Попенюк - звіт, тестування
Артур Рудіш - візуалізація
Максим Марич - презентація
## Фідбек
