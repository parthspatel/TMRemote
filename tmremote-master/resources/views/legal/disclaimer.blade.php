@extends('layouts.legal')

@section('page-title', 'End User License Agreement')

@section('content')
    <h1>Disclaimer</h1>
    <hr>
    <p>tmremote.io is owned and operated by tmremote.io who is no way affiliated nor endorsed with/by any other company or entity regardless if implied or expressed. All content on our web site
        (including, but not limited to, trademarks, screenshots and logos) are property of their respective owners. By showing this content tmremote.io does not claim to be affiliated or endorsed by
        these owners. Any screenshots or images appearing on this site are released under fair use as a derivative work and shall not be misconstrued as any relation to any other entity or
        company.</p>
@stop

@section('scripts')
    {!! HTML::script('assets/js/as/login.js') !!}
    {!! JsValidator::formRequest('Vanguard\Http\Requests\Auth\LoginRequest', '#login-form') !!}
@stop
