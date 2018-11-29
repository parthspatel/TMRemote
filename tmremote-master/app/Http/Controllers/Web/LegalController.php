<?php

namespace Vanguard\Http\Controllers\Web;

use Vanguard\Http\Controllers\Controller;

class LegalController extends Controller
{
    public function eula()
    {
        return view('legal.eula');
    }

    public function tos()
    {
        return view('legal.tos');
    }

    public function privacyPolicy()
    {
        return view('legal.privacy-policy');
    }

    public function disclaimer()
    {
        return view('legal.disclaimer');
    }
}
