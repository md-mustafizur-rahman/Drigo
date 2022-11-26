<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Password;


class siteController extends Controller
{
   public function homePage()
   {
      return view('pages.home');
   }
   public function loginPage()
   {
      return view('pages.login');
   }
   public function logoutPage()
   {
      session()->flush();
      return view('pages.home');
   }
   public  function registrationPage()
   {
      return view('pages.registration');
   }

   public  function sellerProfile()
   {
      return view('pages.sellerProfile');
   }
   public function productUpload()
   {
      return view('pages.productUpload');
   }
}
