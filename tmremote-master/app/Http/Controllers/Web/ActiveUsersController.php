<?php

namespace Vanguard\Http\Controllers\Web;

use Vanguard\Http\Controllers\Controller;
use Vanguard\User;

class ActiveUsersController extends Controller
{
    public function __construct()
    {
        // Allow access to authenticated users only.
        $this->middleware('auth');

        // Allow access to users with 'users.manage' permission.
        $this->middleware('permission:users.manage');
    }

    public function index()
    {
        // Fetch users from database
        $users = User::join('sessions', 'users.id', '=', 'sessions.user_id')
            ->select('users.*')
            ->distinct()
            ->get();

        // Uncomment the following line if you want to see the info you get from the database
        // dd($users);

        // Load appropriate view for displaying the users
        // Note: compact('users') is the same as ['users' => $users]
        return view('user.active-users', compact('users'));
    }
}
