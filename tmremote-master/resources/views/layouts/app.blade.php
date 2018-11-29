<!doctype html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <meta name="csrf-token" content="{{ csrf_token() }}">

    <title>@yield('page-title') - {{ settings('app_name') }}</title>

    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="{{ url('assets/img/icons/apple-touch-icon-144x144.png') }}"/>
    <link rel="apple-touch-icon-precomposed" sizes="152x152" href="{{ url('assets/img/icons/apple-touch-icon-152x152.png') }}"/>
    <link rel="icon" type="image/png" href="{{ url('assets/img/icons/favicon-32x32.png') }}" sizes="32x32"/>
    <link rel="icon" type="image/png" href="{{ url('assets/img/icons/favicon-16x16.png') }}" sizes="16x16"/>
    <meta name="application-name" content="{{ settings('app_name') }}"/>
    <meta name="msapplication-TileColor" content="#FFFFFF"/>
    <meta name="msapplication-TileImage" content="{{ url('assets/img/icons/mstile-144x144.png') }}"/>

    <link media="all" type="text/css" rel="stylesheet" href="{{ mix('assets/css/vendor.css') }}">
    <link media="all" type="text/css" rel="stylesheet" href="{{ mix('assets/css/app.css') }}">

    @yield('styles')
</head>
<body>
@include('partials.navbar')

<div class="container-fluid">
    <div class="row">
        @include('partials.sidebar')

        <div class="content-page">
            <main role="main" class="px-4">
                @yield('content')

                <div class="footer">
                    <div class="row">
                        <div class="col-md-12 col-lg-4">
                            {{--<div class="text-muted">--}}
                                {{--tmremote.io is owned and operated by tmremote.io who is no way affiliated nor endorsed with/by any other company or entity regardless if implied or expressed.--}}
                                {{--<a href="{{ url('legal/disclaimer') }}">Read more here</a>.--}}
                            {{--</div>--}}
                        </div>
                        <div class="col-md-12 col-lg-8">
                            <div class="text-right text-muted">
                                Copyright &copy; <?php echo date('Y'); ?> <a href="{{ url('/') }}">tmremote.io</a>
                            </div>
                            <div class="text-right text-muted">
                                <a href="<?php echo url('/legal/tos') ?>" target="_blank">TOS</a> |
                                <a href="<?php echo url('/legal/privacy-policy') ?>" target="_blank">Privacy Policy</a> |
                                <a href="<?php echo url('/legal/eula') ?>" target="_blank">EULA</a> |
                                <a href="<?php echo url('/legal/disclaimer') ?>" target="_blank">Disclaimer</a>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    </div>
</div>

<script src="{{ mix('assets/js/vendor.js') }}"></script>
<script src="{{ url('assets/js/as/app.js') }}"></script>
@yield('scripts')
</body>
</html>
