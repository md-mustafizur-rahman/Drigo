<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Seller;

class dataBaseController extends Controller
{

    // registration insert query code start
    public function seller()
    {
        $seller = Seller::all();
        echo "<pre>";
        print_r($seller->toArray());
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

        echo "<pre>";
        print_r($request->all());
        $seller = new Seller;
        $seller->name = $request['name'];
        $seller->username = $request['username'];
        $seller->category = $request['category'];
        $seller->shopname = $request['shopname'];
        $seller->email = $request['email'];
        $seller->latitude = $request['latitude'];
        $seller->longitude = $request['longitude'];
        $seller->password = md5($request['password']);
        $seller->save();
    }
    // registration insert query code end


    // registration select query code start

    public function registrationDataView()
    {
        $seller = Seller::all();
        // echo "<pre>";
        // print_r($seller);
        // die;
        $data=compact('seller');
        return view('test.testSelectQuery')->with($data);
    }


    // registration select query code end


}
