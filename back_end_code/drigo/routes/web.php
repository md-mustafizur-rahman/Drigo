<?php

use App\Http\Controllers\dataBaseController;
use App\Http\Controllers\productDataBaseController;
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

Route::get('/', [siteController::class, 'homePage']);
Route::get('/login', [siteController::class, 'loginPage']);
Route::get('/logout', [siteController::class, 'logoutPage']);
Route::get('/registration', [siteController::class, 'registrationPage']);
Route::get('/sellerProfile', [siteController::class, 'sellerProfile']);
Route::get('/upload', [siteController::class, 'productUpload']);
Route::get('/sellerAllProduct', [siteController::class, 'sellerAllProduct']);
Route::get('/showSellerProfile/{id}', [siteController::class, 'showSellerProfile']);
Route::get('/showSellerAllProduct/{id}', [siteController::class, 'showSellerAllProduct']);
Route::get('/search', [siteController::class, 'searchProduct']);
Route::get('/categorysearch/{categoryName}', [siteController::class, 'searchProductWithCategory']);
Route::get('/productDetails/{id}', [siteController::class, 'productDetailsPage']);
// work with siteController end

// work with databaseController start
Route::get('/seller', [dataBaseController::class, 'seller']);
Route::post('/registration', [dataBaseController::class, 'registration']);
// This route only use for testing purpose
// Route::get('/registration/view', [dataBaseController::class, 'registrationDataView']);
Route::post('/login', [dataBaseController::class, 'login']);
// work with databaseController end


// work with productDatabaseController end
Route::post('/addproduct', [productDataBaseController::class, 'addProduct']);
Route::post('/updateProduct', [productDataBaseController::class, 'updateProduct']);
Route::get('/deleteProduct/{id}', [productDataBaseController::class, 'deleteProduct']);
Route::get('/editProduct/{id}', [productDataBaseController::class, 'editProduct']);
// work with productDatabaseController end