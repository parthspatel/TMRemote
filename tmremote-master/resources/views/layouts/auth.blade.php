<!doctype html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>@yield('page-title') - {{ settings('app_name') }}</title>

    {!! HTML::style('assets/css/app.css') !!}
    {!! HTML::style('assets/css/fontawesome-all.min.css') !!}

    @yield('header-scripts')
</head>
<body class="auth">

<div class="container">
    @yield('content')

    <div class="text-center text-muted">
        <a href="<?php echo url('/') ?>">Home</a> |
        <a href="<?php echo url('/legal/tos') ?>">TOS</a> |
        <a href="<?php echo url('/legal/privacy-policy') ?>">Privacy Policy</a> |
        <a href="<?php echo url('/legal/eula') ?>">EULA</a> |
        <a href="<?php echo url('/legal/disclaimer') ?>">Disclaimer</a>
    </div>
</div>

{!! HTML::script('assets/js/vendor.js') !!}
{!! HTML::script('assets/js/as/app.js') !!}
{!! HTML::script('assets/js/as/btn.js') !!}
@yield('scripts')
</body>
</html>
