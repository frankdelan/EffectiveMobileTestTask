# Личный финансовый кошелек  
  
***  
## Описание  
  
CLI приложение для финансового учёта  
  
## Использование

> Форматом для хранения записей является **csv**.
  
Данное приложение предоставляет следующий функционал:  
### Просмотр баланса  
Пользователь получает информацию о балансе его счёта.

### Добавление новой транзакции  
Пользователь выбирает категорию транзакции - "Доход"/"Расход".
Далее он вводит сумму и описание транзакции. 
Если введенные данные корректны, создаётся новая запись в файле.

### Изменение существующей транзакции  
В первую очередь пользователю показывается пронумерованный список со всеми транзакциями, из которого он выбирает запись для изменения.
Далее он выбирает поле, которое хочет изменить и вводит новые данные.
Если введенные данные корректны, запись будет изменена.

### Поиск транзакции
Пользователь выбирает категорию, по которой хочет провести поиск.
После вводит данные, по которым будет проведен поиск.
Если совпадения найдены, они будут показаны пользователю.
