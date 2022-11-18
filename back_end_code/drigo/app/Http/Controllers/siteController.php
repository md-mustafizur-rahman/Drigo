<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class siteController extends Controller
{
   function homePage()
   {
    return view('pages.home');
   }
}
