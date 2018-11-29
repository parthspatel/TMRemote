<?php

namespace Vanguard\Http\Controllers\Web;

use Illuminate\Http\Request;
use Vanguard\Http\Controllers\Controller;

class DownloadsController extends Controller
{
    public function __construct()
    {
        // Allow access to users with 'app.download' permission.
        $this->middleware('permission:app.download');
    }

    public function index()
    {
        return view('downloads.index');
    }
}
