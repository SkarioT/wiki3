### Features wiki3
В функциональные возможности заложено:

- Поиск по выбранной услуге и конкретному **УНП\ИНН**. В результате поиска по **УНП\ИНН** получаем перечень контактных email и телефонов для конкретно выбранного (введенного) **УНП\ИНН** в рамках услуги/сервиса.

- Поиск по выбранной услуге (без ввода  **УНП\ИНН**). В результате получаем список **ВСЕХ** контактных email/телефонов в рамках услуги. Выбираем услугу и просто нажимаем E**NTER**

- Поиск по выбранной услуге и перечню УНП находящихся в файле **unp.txt** . В результате получаем список контактных email/телефонов на основании **УНП\ИНН** находящихся в файле. Файл unp.txt должен находится в той же директори что и исполняемый файл **Wiki3**


В файле **info_urls.py** находятся примеры ссылок на страницы, где находятся таблицы с информацией о клиенте.
Примерная структура:


```html
<!DOCTYPE html>
<html>
    <head>
        <mate charest="utf-8" />
        <title>Услуга ХХ</title>
    </head>
    <body>
        <tbody aria-live="polite" aria-relevant="all">
			<tr role="row">
				<td class="numberingColumn confluenceTd" style="text-align: center;">1</td>
				<td confluenceTd" >Название</td>
				<td confluenceTd">УНП/ИНН</td>
				<td style="text-align: left;" colspan="1" class="confluenceTd">
					<p title="">номер-1</p>
					<p title="">номер-n</p>
				</td>


				....
			</tr>
			<tr role="row">
				<td class="numberingColumn confluenceTd" style="text-align: center;">1</td>
				<td confluenceTd" >Название</td>
				<td confluenceTd">УНП/ИНН</td>
				<td style="text-align: left;" colspan="1" class="confluenceTd">
					<p title="">номер-1</p>
					<p title="">номер-n</p>
				</td>
				....
			</tr>
			...
		</tbody>
    </body>
</html>
```