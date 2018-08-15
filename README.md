Задача:  Организовать api для работы с token методами (​ http://localhost:8080/api/v1/ui/#/Token_operations​ ) с простой масштабируемостью. 
 
Шаги решения: 
1. Скачать ноду https://github.com/Remmeauth/remme-core/tree/dev#for-developers--contributors​ по мануалу for developers & contributors в ветке dev 
2. реализовать класс RemmeClient который будет принимать в себя две переменные: private_key_hex и network_config (параметры по умолчанию “” и default_config = {    node_address: "localhost",    socket_port: "9080",    api_port: "8080",    validator_port: "8008",    ssl_mode: false, }, соответственно) 
3. реализовать два класса RemmeRest и RemmeToken. в RemmeRest должны быть 4 главных метода, а именно get, post, put, delete, реализованы, а в RemmeToken реализованы два метода, а именно transfer и get_balance. 
4. метод get_balance принимает параметр public_key в виде hex строки из 66 символов и шлет get запрос на http://localhost:8080/api/v1/token/{public_key} 
5. метод token принимает параметр public_key_to и amount и шлет post запрос на http://localhost:8080/api/v1/token 
 
Результат: В RemmeClient должен быть метод token, в котором будет инициализирован RemmeToken. RemmeToken должен отправлять запросы через RemmeRest, который должен быть независимым от того кто его использует. 
 
Использование: from remme import RemmeClient 
 
remme = RemmeClient() beforeBalance = remme.token.get_balance(“02926476095ea28904c11f22d0da20e999801a267cd3455a0057 0aa1153086eb13”) print(f’balance: {beforeBalance}’) // >>> balance: 0 
 
remme.token.transfer(“02926476095ea28904c11f22d0da20e999801a267cd3455a00570aa1 153086eb13”, 1000) 
 
afterBalance = remme.token.get_balance(“02926476095ea28904c11f22d0da20e999801a267cd3455a0057 0aa1153086eb13”)  print(f’balance: {afterBalance}’) // >>> balance: 1000 
