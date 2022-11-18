<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class siteController extends Controller
{
   function homePage()
   {
    return view('pages.home');
   }
   function loginPage()
   {
    return view('pages.login');
   }
   function registrationPage()
   {
    return view('pages.registration');
   }
   function sellerProfile()
   {
    return view('pages.sellerProfile');
   }
}
