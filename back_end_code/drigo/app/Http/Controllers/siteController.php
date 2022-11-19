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
   public  function registrationPage()
   {
      return view('pages.registration');
   }
  
   public function login(Request $request)
   {
      $request->validate([

         'username' => 'required',
         'password' => 'required'
      ]);

      
      // echo "<pre>";
      // print_r($request->all());
   }
   public  function sellerProfile()
   {
      return view('pages.sellerProfile');
   }
    




}
