<?php

use App\Http\Controllers\dataBaseController;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\siteController;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// Route::get('/', function () {
//     return view('welcome');
// });

// work with siteController start

Route::get('/',[siteController::class,'homePage']);
Route::get('/login',[siteController::class,'loginPage']);
Route::get('/registration',[siteController::class,'registrationPage']);
Route::post('/login',[siteController::class,'login']);
Route::get('/sellerProfile',[siteController::class,'sellerProfile']);
Route::get('/seller',[dataBaseController::class,'seller']);
// work with siteController end

// work with databaseController start
Route::post('/registration',[dataBaseController::class,'registration']);
Route::get('/registration/view',[dataBaseController::class,'registrationDataView']);
// work with databaseController end