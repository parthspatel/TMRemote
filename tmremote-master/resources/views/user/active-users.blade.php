@extends('layouts.app')

@section('page-title', 'Active Users')
@section('page-heading', 'Active Users')

@section('breadcrumbs')
    <li class="breadcrumb-item active">
        Active Users
    </li>
@stop

@section('content')
    @include('partials.messages')

    <div class="row">
        @foreach($users as $user)
            <a href="{{ route('user.show', $user->id) }}" class="col-md-2">
                <div class="card">
                    <div class="card-body d-flex align-items-center">
                        <div>
                            <img width="64" height="64"
                                 class="media-object mr-3 rounded-circle img-thumbnail img-responsive"
                                 src="{{ $user->present()->avatar }}">
                        </div>
                        <div class="d-flex justify-content-center flex-column">
                            <h5 class="mb-0">{{ $user->present()->username }}</h5>
                            {{--<small class="text-muted">{{ $user->present()->email }}</small>--}}
                        </div>
                    </div>
                </div>
            </a>
        @endforeach
    </div>
@stop

@section('styles')
@stop
