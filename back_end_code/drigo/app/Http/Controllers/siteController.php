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
   public function registration(Request $request)
   {
      $request->validate([
         'name' => 'required',
         'username' => 'required',
         'shopname' => 'required',
         'latitude' => 'required',
         'longitude' => 'required',
         'email' => 'required | email ',
         'password' => 'required |confirmed',
         'password_confirmation' => 'required',


      ]);

      // echo "<pre>";
      // print_r($request->all());
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
