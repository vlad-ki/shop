<!DOCTYPE html>
<html>

<head>
	<meta charset="utf-8">
	<title>Shop | Admin panel</title>
</head>

<body>
	% include('templates/header.tpl')
	<table border='3'>
		<thead>
			<tr>
				<th>edit</th>
				<th>id</th>
				<th>monufacturer</th>
				<th>model</th>
				<th>amount</th>
				<th>price</th>
				<th>bprice</th>
				<th>description</th>
				<th>image</th>
			</tr>
		</thead>
		<tbody>
			
			% for product in list_of_products:
				<tr>
					<td><a href="/edit_product?_id={{product['_id']}}">e</a></td>
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
			</tbody>
	</table>
</body>

</html>
