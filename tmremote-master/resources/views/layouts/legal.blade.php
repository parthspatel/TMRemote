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
<body class="legal">

<div class="container">
    <div class="col mx-auto my-10p">
        <div class="text-center">
            <a href="{{ url('/') }}">
                <img src="{{ url('assets/img/logo.png') }}" alt="{{ settings('app_name') }}" height="50">
            </a>
        </div>

        <div class="card mt-5">
            <div class="card-body">
                <div class="p-4">
                    <div class="text-center text-muted mb-5">
                        <a class="font-weight-bold" href="<?php echo url('/') ?>">Home</a> |
                        <a class="font-weight-bold" href="<?php echo url('/legal/tos') ?>">TOS</a> |
                        <a class="font-weight-bold" href="<?php echo url('/legal/privacy-policy') ?>">Privacy Policy</a> |
                        <a class="font-weight-bold" href="<?php echo url('/legal/eula') ?>">EULA</a> |
                        <a class="font-weight-bold" href="<?php echo url('/legal/disclaimer') ?>">Disclaimer</a>
                    </div>
                    @yield('content')
                    <div class="text-center text-muted mt-5">
                        <a class="font-weight-bold" href="<?php echo url('/') ?>">Home</a> |
                        <a class="font-weight-bold" href="<?php echo url('/legal/tos') ?>">TOS</a> |
                        <a class="font-weight-bold" href="<?php echo url('/legal/privacy-policy') ?>">Privacy Policy</a> |
                        <a class="font-weight-bold" href="<?php echo url('/legal/eula') ?>">EULA</a> |
                        <a class="font-weight-bold" href="<?php echo url('/legal/disclaimer') ?>">Disclaimer</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

{!! HTML::script('assets/js/vendor.js') !!}
{!! HTML::script('assets/js/as/app.js') !!}
{!! HTML::script('assets/js/as/btn.js') !!}
@yield('scripts')
</body>
</html>
