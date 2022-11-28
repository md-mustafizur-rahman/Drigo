@extends('layouts.main')
@section('main-section')
<section class="searchContent">

    <div class="searchContentInner">
        <h2 class="searchingTitle">Shop name: {{session()->get('seller_shopname')}}</h2>
        <p class="totalCount">Total Item: @if($products !=null)
            {{count($products)}}
            @else
            {{"0"}}
            @endif
        </p>
        <a href="{{url('/sellerProfile')}}"><button style="background-color:  black; width:80px; height:40px; border:1px solid black; font-size:1rem;color:white;  border-radius: 5px; cursor:pointer; margin-top:15px;">Back</button></a>
        @if(Session::get('seller_username'))
        <a href="upload"><button style="background-color:  #8BBA24; width:150px; height:40px; border:1px solid #8BBA24; font-size:1rem;color:white;  border-radius: 5px; cursor:pointer; margin-top:15px;">Add product</button></a>
        @else
        <a href="#"><button>Get Location</button></a>
        @endif

        <div class="productList">

            <!-- 
This is the product html start -->

            @if($products !=null)
            @foreach (array_slice($products, 0, 200) as $product)
            <div class="product">
                <div class="producttop">
                    <div class="producttopInner">
                        <div class="productinfo">
                            <div class="productinfoleft">
                                <p>{{$product->product_size}}</p>
                                <h5>{{$product->product_name}}</h5>
                            </div>
                            <div class="productinforight">
                                <img src="{{url('font_end_code/image/header.png')}}" alt="">
                            </div>
                        </div>
                    </div>
                    <div class="producttopInnerBottom">

                        <img src="{{asset('/storage/uploads/'.$product->product_Image)}}" alt="">
                    </div>
                </div>
                <div class="product_bottom_outer">
                    <div class="productbottom">
                        <p>{{$product->product_price}} tk</p>
                        <h2>{{$product["shopname"]}}</h2>
                    </div>

                    <div class="productbottomleft">
                        <a href="{{url('/deleteProduct/')}}/{{$product->product_id}}" class="productbottomleftTop">
                            <i class="gg-close 2x"></i>
                        </a>
                        <a href="{{url('/editProduct/')}}/{{$product->product_id}}" class="productbottomleftBottom">
                            <i class="gg-pen"></i>
                        </a>
                    </div>
                </div>
            </div>

            @endforeach
            @endif

            <!-- 
This is the product html end -->


        </div>

    </div>




    </div>
</section>

@endsection