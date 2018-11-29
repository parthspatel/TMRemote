@extends('layouts.app')

@section('page-title', trans('app.dashboard'))
@section('page-heading', trans('app.dashboard'))

@section('breadcrumbs')
    <li class="breadcrumb-item active">
        @lang('app.dashboard')
    </li>
@stop

@section('content')

    <div class="row">

        <div class="col-xl-3 col-md-6">
            <div class="card widget">
                <div class="card-body">
                    <div class="row">
                        <div class="p-3 text-primary flex-1">
                            <i class="fa fa-users fa-3x"></i>
                        </div>

                        <div class="pr-3">
                            <h2 class="text-right">{{ number_format($stats['total']) }}</h2>
                            <div class="text-muted">@lang('app.total_users')</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-xl-3 col-md-6">
            <div class="card widget">
                <div class="card-body">
                    <div class="row">
                        <div class="p-3 text-success flex-1">
                            <i class="fa fa-user-plus fa-3x"></i>
                        </div>

                        <div class="pr-3">
                            <h2 class="text-right">{{ number_format($stats['new']) }}</h2>
                            <div class="text-muted">@lang('app.new_users_this_month')</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-xl-3 col-md-6">
            <div class="card widget">
                <div class="card-body">
                    <div class="row">
                        <div class="p-3 text-danger flex-1">
                            <i class="fa fa-user-slash fa-3x"></i>
                        </div>

                        <div class="pr-3">
                            <h2 class="text-right">{{ number_format($stats['banned']) }}</h2>
                            <div class="text-muted">@lang('app.banned_users')</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-xl-3 col-md-6">
            <div class="card widget">
                <div class="card-body">
                    <div class="row">
                        <div class="p-3 text-info flex-1">
                            <i class="fa fa-user fa-3x"></i>
                        </div>

                        <div class="pr-3">
                            <h2 class="text-right">{{ number_format($stats['unconfirmed']) }}</h2>
                            <div class="text-muted">@lang('app.unconfirmed_users')</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

    {{--<div class="row">--}}
    {{--<div class="col-lg-8 col-md-12">--}}
    {{--<div class="card">--}}
    {{--<div class="card-body">--}}
    {{--<h5 class="card-title">@lang('app.registration_history')</h5>--}}
    {{--<div class="pt-4 px-3">--}}
    {{--<canvas id="myChart" height="365"></canvas>--}}
    {{--</div>--}}
    {{--</div>--}}
    {{--</div>--}}
    {{--</div>--}}
    {{--<div class="col-md-12 col-lg-4">--}}
    {{--<div class="card">--}}
    {{--<div class="card-body">--}}
    {{--<h5 class="card-title">--}}
    {{--@lang('app.latest_registrations')--}}

    {{--@if (count($latestRegistrations))--}}
    {{--<small class="float-right">--}}
    {{--<a href="{{ route('user.list') }}">View All</a>--}}
    {{--</small>--}}
    {{--@endif--}}
    {{--</h5>--}}

    {{--@if (count($latestRegistrations))--}}
    {{--<ul class="list-group list-group-flush">--}}
    {{--@foreach ($latestRegistrations as $user)--}}
    {{--<li class="list-group-item list-group-item-action">--}}
    {{--<a href="{{ route('user.show', $user->id) }}" class="d-flex text-dark no-decoration">--}}
    {{--<img class="rounded-circle" width="40" height="40" src="{{ $user->present()->avatar }}">--}}
    {{--<div class="ml-2" style="line-height: 1.2;">--}}
    {{--<span class="d-block p-0">{{ $user->present()->nameOrEmail }}</span>--}}
    {{--<small class="text-muted">{{ $user->created_at->diffForHumans() }}</small>--}}
    {{--</div>--}}
    {{--</a>--}}
    {{--</li>--}}
    {{--@endforeach--}}
    {{--</ul>--}}
    {{--@else--}}
    {{--<p class="text-muted">@lang('app.no_records_found')</p>--}}
    {{--@endif--}}
    {{--</div>--}}
    {{--</div>--}}
    {{--</div>--}}
    {{--</div>--}}

    <div class="row">
        <div class="col-md-4">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">
                        Ban Detection Settings
                    </h5>

                    <div class="text-muted">Settings coming soon, stay tuned.</div>
                </div>
            </div>
        </div>
        <div class="col-md-8">
            <div class="card">
                <div class="card-body">
                    {{ Widget::GmStatus() }}
                </div>
            </div>
        </div>
    </div>

    @if(settings('enable_bots'))
        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        {{ Widget::BotLogs() }}
                    </div>
                </div>
            </div>
        </div>
    @endif

@stop

@section('scripts')
    {{--<script>--}}
    {{--var users = {!! json_encode(array_values($usersPerMonth)) !!};--}}
    {{--var months = {!! json_encode(array_keys($usersPerMonth)) !!};--}}
    {{--var trans = {--}}
    {{--chartLabel: "{{ trans('app.registration_history')  }}",--}}
    {{--new: "{{ trans('app.new_sm') }}",--}}
    {{--user: "{{ trans('app.user_sm') }}",--}}
    {{--users: "{{ trans('app.users_sm') }}"--}}
    {{--};--}}
    {{--</script>--}}
    {{--{!! HTML::script('assets/js/chart.min.js') !!}--}}
    {{--{!! HTML::script('assets/js/as/dashboard-admin.js') !!}--}}
    {!! HTML::script('assets/js/as/gm-status.js') !!}
@stop
