from lmsbreaker import Breaker

#данные пользователя
username = "vasya"
password = "12345"
 #номер юнита, который хотим решить (номер задания со страницы результатов, самый верхний - первый)
unit_num = 1
#минимальный и максимальный процент выполнения каждого задания
percent_min = 90
percent_max = 100

breaker = Breaker()

try:
    breaker.login(username, password)
    breaker.attempt(unit_num, percent_min, percent_max)
    print("Юнит %s успешно выполнен." % str(unit_num))
finally:
    #иначе оставим открытую сессию
     breaker.logout()
