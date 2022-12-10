<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Seller;
use Illuminate\Contracts\Session\Session;
use Illuminate\Support\Facades\Auth;

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

        $check1 = Seller::where([

            ['username', '=', $request->username],

        ])->first();
        $check2 = Seller::where([

            ['email', '=', $request->email],

        ])->first();

        if ($check1) {
            // echo   $request->password;
            // echo "check Again";
            return redirect('/registration')->with('usernameErrorKey', 'already exist');
            die;
        }
        if ($check2) {
            return redirect('/registration')->with('emailErrorKey', 'already exist');
            die;
        } else {

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
            return redirect('/login');
        }
    }
    // registration insert query code end


    // login insert query code end

    public function login(Request $request)
    {
        $request->validate([

            'username' => 'required',
            'password' => 'required'
        ]);
        // $seller = Seller::all();
        // if (Auth::attempt($request->only('username', 'password'))) {
        //     echo "sabbir";
        // } else {
        //     echo "na";
        // }
        $request->password = md5($request['password']);

        $check = Seller::where([

            ['username', '=', $request->username],
            ['password', '=', $request->password],
        ])->first();

        if ($check) {

            $callData = Seller::where(
                'username',
                '=',
                $request->username
            )->get(['seller_id', 'name', 'username','category', 'shopname', 'email', 'latitude', 'longitude'])->toArray();

            session([
                'seller_seller_id' => $callData[0]['seller_id'],
                'seller_name' => $callData[0]['name'],
                'seller_username' => $callData[0]['username'],
                'seller_shopname' => $callData[0]['shopname'],
                'seller_category' => $callData[0]['category'],
                'seller_sellerEmail' => $callData[0]['email'],
                'seller_sellerLatitude' => $callData[0]['latitude'],
                'seller_sellerLongitude' => $callData[0]['longitude'],
            ]);
// echo '<pre>';
//print_r($callData);
// print_r(session()->get('seller_category'));

            // session()->put([

            //     'seller_seller_id' => $callData[0]['seller_id'],
            //         'seller_name' => $callData[0]['name'],
            //         'seller_username' => $callData[0]['username'],
            //         'seller_shopname' => $callData[0]['shopname'],
            //         'seller_sellerEmail' => $callData[0]['email'],
            //         'seller_sellerLatitude' => $callData[0]['latitude'],
            //         'seller_sellerLongitude' => $callData[0]['longitude'],
            // ]);
            // echo '<pre>';
            // print_r(session()->get('seller_name'));
            // print_r($callData[0]['name']);

            return redirect('/');



        } else {
            echo   $request->password;
            echo "check Again";
            return redirect('/login')->with('invalidLoginkey', 'username/password invalid');
        }

        // echo "<pre>";
        // print_r($request->all());
    }
    // login insert query code end


    // registration select query code start this is only for testing purpose. 
    // public function registrationDataView()
    // {
    //     $seller = Seller::all();
    //     // echo "<pre>";
    //     // print_r($seller);
    //     // die;
    //     $data = compact('seller');
    //     return view('test.testSelectQuery')->with($data);
    // }


    // registration select query code end  this is only for testing purpose


}
