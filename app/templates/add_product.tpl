<!DOCTYPE html>
<html>
<head>
	<title>Shop | Admin - add product</title>
	<meta charset="utf-8">
</head>
<body>

	% include('templates/header.tpl')
	% if ProductSave == True:
		<strong>Измнениея сохранены</strong>
	% elif ProductSave == False:
		<strong>Изменения не сохранены. Измените проиводителя или добавте его в список.</strong>
	% end
	<form action="/add_product" method="POST">
		<input type="text" name="monufacturer" placeholder="Monufacturer" required><br>
		<input type="text" name="model" placeholder="Model" required><br>
		<input type="number" name="amount" placeholder="Amount"><br>
		<input type="number" name="price" placeholder="Price"><br>
		<input type="number" name="bprice" placeholder="Bprice"><br>
		<textarea name="description" placeholder="Description"></textarea><br>
		<input type="text" name="image" placeholder="Image"><br>
		<input type="checkbox" value="True" name="new_monufacturer">New monufacturer<br>
		<input type="submit" value="Add product" name="ADD"> 
	</form>

</body>
</html>