<nav class="col-md-2 sidebar">
    {{--<div class="user-box text-center pt-5 pb-3">--}}
    {{--<div class="user-img">--}}
    {{--<img src="{{ auth()->user()->present()->avatar }}"--}}
    {{--width="90"--}}
    {{--height="90"--}}
    {{--alt="user-img"--}}
    {{--class="rounded-circle img-thumbnail img-responsive">--}}
    {{--</div>--}}
    {{--<h5 class="my-3">--}}
    {{--<a href="{{ route('profile') }}">{{ auth()->user()->present()->nameOrEmail }}</a>--}}
    {{--</h5>--}}

    {{--<ul class="list-inline mb-2">--}}
    {{--<li class="list-inline-item">--}}
    {{--<a href="{{ route('profile') }}" title="@lang('app.my_profile')">--}}
    {{--<i class="fas fa-cog"></i>--}}
    {{--</a>--}}
    {{--</li>--}}

    {{--<li class="list-inline-item">--}}
    {{--<a href="{{ route('auth.logout') }}" class="text-custom" title="@lang('app.logout')">--}}
    {{--<i class="fas fa-sign-out-alt"></i>--}}
    {{--</a>--}}
    {{--</li>--}}
    {{--</ul>--}}
    {{--</div>--}}

    <div class="sidebar-sticky">
        <ul class="nav flex-column">
            <li class="nav-item">
                <a class="nav-link {{ Request::is('/') ? 'active' : ''  }}" href="{{ route('dashboard') }}">
                    <i class="fas fa-home"></i>
                    <span>@lang('app.dashboard')</span>
                </a>
            </li>

            @permission('app.download')
            <li class="nav-item">
                <a class="nav-link {{ Request::is('download*') ? 'active' : ''  }}" href="{{ route('app.download') }}">
                    <i class="fas fa-download"></i>
                    <span>Download</span>
                </a>
            </li>
            @endpermission

            @permission('users.manage')
            <li class="nav-item">
                <a href="#users-dropdown"
                   class="nav-link"
                   data-toggle="collapse"
                   aria-expanded="{{ Request::is('user*') || Request::is('active-users*') ? 'true' : 'false' }}">
                    <i class="fas fa-users"></i>
                    <span>@lang('app.users')</span>
                </a>
                <ul class="{{ Request::is('user*') || Request::is('active-users*') ? '' : 'collapse' }} list-unstyled sub-menu" id="users-dropdown">
                    <li class="nav-item">
                        <a class="nav-link {{ Request::is('user*') ? 'active' : ''  }}" href="{{ route('user.list') }}">
                            <span>All @lang('app.users')</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="{{ route('active-users') }}" class="nav-link {{ Request::is('active-users') ? 'active' : ''  }}">
                            Active Users
                        </a>
                    </li>
                </ul>
            </li>
            @endpermission

            @permission('users.activity')
            <li class="nav-item">
                <a class="nav-link {{ Request::is('activity*') ? 'active' : ''  }}" href="{{ route('activity.index') }}">
                    <i class="fas fa-server"></i>
                    <span>@lang('app.activity_log')</span>
                </a>
            </li>
            @endpermission

            @permission(['roles.manage', 'permissions.manage'])
            <li class="nav-item">
                <a href="#roles-dropdown"
                   class="nav-link"
                   data-toggle="collapse"
                   aria-expanded="{{ Request::is('role*') || Request::is('permission*') ? 'true' : 'false' }}">
                    <i class="fas fa-users-cog"></i>
                    <span>@lang('app.roles_and_permissions')</span>
                </a>
                <ul class="{{ Request::is('role*') || Request::is('permission*') ? '' : 'collapse' }} list-unstyled sub-menu" id="roles-dropdown">
                    @permission('roles.manage')
                    <li class="nav-item">
                        <a class="nav-link {{ Request::is('role*') ? 'active' : '' }}"
                           href="{{ route('role.index') }}">@lang('app.roles')</a>
                    </li>
                    @endpermission
                    @permission('permissions.manage')
                    <li class="nav-item">
                        <a class="nav-link {{ Request::is('permission*') ? 'active' : '' }}"
                           href="{{ route('permission.index') }}">@lang('app.permissions')</a>
                    </li>
                    @endpermission
                </ul>
            </li>
            @endpermission

            @permission(['settings.general', 'settings.auth', 'settings.notifications'], false)
            <li class="nav-item">
                <a href="#settings-dropdown"
                   class="nav-link"
                   data-toggle="collapse"
                   aria-expanded="{{ Request::is('settings*') ? 'true' : 'false' }}">
                    <i class="fas fa-cogs"></i>
                    <span>@lang('app.settings')</span>
                </a>
                <ul class="{{ Request::is('settings*') ? '' : 'collapse' }} list-unstyled sub-menu"
                    id="settings-dropdown">

                    @permission('settings.general')
                    <li class="nav-item">
                        <a class="nav-link {{ Request::is('settings') ? 'active' : ''  }}"
                           href="{{ route('settings.general') }}">
                            @lang('app.general')
                        </a>
                    </li>
                    @endpermission

                    @permission('settings.auth')
                    <li class="nav-item">
                        <a class="nav-link {{ Request::is('settings/auth*') ? 'active' : ''  }}"
                           href="{{ route('settings.auth') }}">@lang('app.auth_and_registration')</a>
                    </li>
                    @endpermission

                    @permission('settings.notifications')
                    <li class="nav-item">
                        <a class="nav-link {{ Request::is('settings/notifications*') ? 'active' : ''  }}"
                           href="{{ route('settings.notifications') }}">@lang('app.notifications')</a>
                    </li>
                    @endpermission
                </ul>
            </li>
            @endpermission
        </ul>
    </div>
</nav>

