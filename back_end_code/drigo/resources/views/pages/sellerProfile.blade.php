@extends('layouts.main')


@section('main-section')

<section class="mainViewOfSeller">
    <div class="mainViewOfSellerLeft">
        <div class="mainViewOfSellerLeftTop">

            <div class="mainViewOfSellerLeftTopInner">
                <img src="{{url('font_end_code/image/header.png')}}" alt="">
                <div class="owerInfoTitle">
                    <h2>@if(Session::get('seller_name'))
                        {{session()->get('seller_name')}}
                        @else
                        {{"unknown"}}
                        @endif
                    </h2>
                    <h2>@if(Session::get('seller_shopname'))
                        {{session()->get('seller_shopname')}}
                        @else
                        {{"unknown"}}
                        @endif
                    </h2>
                    <h3>@if(Session::get('seller_category'))
                        {{session()->get('seller_category')}}
                        @else
                        {{"unknown"}}
                        @endif
                    </h3>
                    <p>@if(Session::get('seller_username'))
                        {{session()->get('seller_username')}}
                        @else
                        {{"unknown"}}
                        @endif
                    </p>
                </div>

            </div>
        </div>
        <div class="mainViewOfSellerLeftBottom">

            @if(Session::get('seller_username'))
            <a href="upload"><button>Add product</button></a>
            @endif


        </div>


    </div>
    <div class="mainViewOfSellerRight">
        <div class="mainViewOfSellerRightTop">
            <img src="{{url('font_end_code/image/shopheader.jpg')}}" alt="">
        </div>
        <div class="itemTitle">
            <h2>
                @if($products !=null)
                {{$products[0]["shopname"]}}
                @else
                {{session()->get('seller_shopname')}}
                @endif
            </h2>
            <p>Item avalible:
                @if($products !=null)
                {{count($products)}}
                @else
                {{"0"}}
                @endif
            </p>

            @if(Session::get('seller_username'))
            <a href="upload"><button class="uploadBtnPhone">Add product</button></a>
            @endif

        </div>
        <div class="productPreview">


            <div class="productList">

                <!-- 
This is the product html start -->

                @if($products !=null)
                @foreach (array_slice($products, 0, 4) as $product)
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
                            <h2>{{$product->shopname}}</h2>
                            <p>{{$product->created_at->diffForHumans()}}</p>
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
                <!-- This is the product html end -->
            </div>

        </div>
        <a href="{{url('/sellerAllProduct')}}" class="moreItem">
            <p>More>></p>
        </a>

    </div>

</section>
@endsection