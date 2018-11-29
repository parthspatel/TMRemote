@extends('layouts.app')

@section('page-title', trans('app.general_settings'))
@section('page-heading', trans('app.general_settings'))

@section('breadcrumbs')
    <li class="breadcrumb-item text-muted">
        @lang('app.settings')
    </li>
    <li class="breadcrumb-item active">
        @lang('app.general')
    </li>
@stop

@section('content')

    @include('partials.messages')

    {!! Form::open(['route' => 'settings.general.update', 'id' => 'general-settings-form']) !!}

    <div class="row">
        <div class="col-md-6">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">
                        @lang('app.general')
                    </h5>

                    <div class="form-group">
                        <label for="name">@lang('app.name')</label>
                        <input type="text" class="form-control" id="app_name"
                               name="app_name" value="{{ settings('app_name') }}">
                    </div>

                    <div class="form-group my-4">
                        <div class="d-flex align-items-center">
                            <div class="switch">
                                <input type="hidden" value="0" name="enable_bots">
                                {!! Form::checkbox('enable_bots', 1, settings('enable_bots'), ['class' => 'switch', 'id' => 'switch-enable-bots']) !!}
                                <label for="switch-enable-bots"></label>
                            </div>
                            <div class="ml-3 d-flex flex-column">
                                <label class="mb-0">Enable Bot Logging</label>
                                <small class="pt-0 text-muted">
                                    Enables the API and front-end for Bot Logging
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <button type="submit" class="btn btn-primary">
        @lang('app.update_settings')
    </button>

    {{ Form::close() }}
@stop
