<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Test Email</title>
</head>
<body>
    <form action="{{route('mail.send')}}" method="POST">
        @csrf
        <input name="to" type="text"><br>
        <textarea name="text" width="100%"></textarea><br>
        <button type="submit">Iber</button>
    </form>
  
</body>
</html>