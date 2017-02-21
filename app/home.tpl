<!DOCTYPE html>
<html>

<head>
	<meta charset="utf-8">
	<title>Shop | admin panel</title>
</head>

<body>
	
	<table border='3'>
		<tr>
			<td>id</td>
			<td>monufacturer</td>
			<td>model</td>
			<td>amount</td>
			<td>price</td>
			<td>bprice</td>
			<td>description</td>
			<td>image</td>
		
		</tr>
		% for product in list_of_products:
			<tr>
				<td>{{product['_id']}}</td>
				<td>{{product['monufacturer']}}</td>
				<td>{{product['model']}}</td>
				<td>{{product['amount']}}</td>
				<td>{{product['price']}}</td>
				<td>{{product['bprice']}}</td>
				<td>{{product['description']}}</td>
				<td>{{product['image']}}</td>
		% end
			</tr>
	</table>
</body>

</html>
