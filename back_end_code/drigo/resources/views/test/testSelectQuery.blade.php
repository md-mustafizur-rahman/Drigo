<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>testSelectQuery</title>
</head>

<body>
    @foreach ($seller as $item)

    <div style="margin-bottom: 100px;">
        <h2>Seller ID :{{$item->seller_id}}</h2>
        <h2>name: {{$item->name}} </h2>
        <h2>username:{{$item->username}} </h2>
        <h2>category:{{$item->category}} </h2>
        <h2>shopname:{{$item->shopname}} </h2>
        <h2>email: {{$item->email}} </h2>
        <h2>latitude: {{$item->latitude}} </h2>
        <h2>latitude: {{$item->longitude}} </h2>
        <h2>password: {{$item->password}}</h2>
    </div>
    @endforeach
</body>

</html>