<!DOCTYPE html>
<html>
<head>
	<title>Shop | Admin - edit product</title>
	<meta charset="utf-8">
</head>
<body>
	% include('templates/header.tpl')

	<form action="/edit_product" method="POST">
		<input type="text" name="_id" placeholder="ID" value="{{product['_id']}}" readonly><br>
		<input type="text" name="monufacturer" placeholder="Monufacturer" value="{{product['monufacturer']}}" required><br>
		<input type="text" name="model" placeholder="Model" value="{{product['model']}}" required><br>
		<input type="number" name="amount" placeholder="Amount" value="{{product['amount']}}"><br>
		<input type="number" name="price" placeholder="Price" value="{{product['price']}}"><br>
		<input type="number" name="bprice" placeholder="Bprice" value="{{product['bprice']}}"><br>
		<textarea name="description" placeholder="Description" value="{{product['description']}}"></textarea><br>
		нет значения поля description
		<input type="text" name="image" placeholder="Image" value="{{product['image']}}"><br>
		<input type="submit" value="Edit product" name="ADD"> 
	</form>


</body>
</html>