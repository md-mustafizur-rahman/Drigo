<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Seller;

class dataBaseController extends Controller
{
    public function seller()
    {
        $seller = Seller::all();
        echo "<pre>";
        print_r($seller->toArray());
    }
}
