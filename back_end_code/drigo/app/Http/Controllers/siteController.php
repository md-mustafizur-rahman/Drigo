<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Password;
use App\Models\Product;

class siteController extends Controller
{
   public function homePage()
   {
      $products = Product::all()->sortDesc();
      if (!empty($products)) {
         view()->share('products', $products);
      } else {
         view()->share('products', null);
      }
      // print_r($products[0]["product_id"]);
      // echo "<pre>";
      // print_r($products->toArray());
      return view('pages.home', $products);
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
      $products = Product::where(
         'seller_id',
         '=',
         session()->get('seller_seller_id')
      )->orderBy('product_id', 'DESC')->get()->all();
      if (!empty($products)) {
         view()->share('products', $products);
      } else {
         view()->share('products', null);
      }
      return view('pages.sellerProfile');
   }
   public function productUpload()
   {
      return view('pages.productUpload');
   }
   public  function sellerAllProduct()
   {
      $products = Product::where(
         'seller_id',
         '=',
         session()->get('seller_seller_id')
      )->orderBy('product_id', 'DESC')->get()->all();
      if (!empty($products)) {
         view()->share('products', $products);
      } else {
         view()->share('products', null);
      }
      return view('pages.sellerAllProduct');
   }
}
