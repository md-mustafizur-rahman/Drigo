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
            @else
            <a href="#"><button>Get Location</button></a>
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
                                    <p>Product Name</p>
                                    <h5>{{$product["product_name"]}}</h5>
                                </div>
                                <div class="productinforight">
                                    <img src="{{url('font_end_code/image/header.png')}}" alt="">
                                </div>
                            </div>
                        </div>
                        <div class="producttopInnerBottom">
                            <img src="{{url('/font_end_code/image/cafe.jpg')}}" alt="">
                        </div>
                    </div>
                    <div class="product_bottom_outer">
                        <div class="productbottom">
                            <p>Distance: 2 km</p>
                            <h2>{{$product["shopname"]}}</h2>
                        </div>

                        <div class="productbottomleft">
                            <a href="#" class="productbottomleftTop">
                                <i class="gg-close 2x"></i>
                            </a>
                            <a href="#" class="productbottomleftBottom">
                                <i class="gg-pen"></i>
                            </a>
                        </div>
                    </div>
                </div>

                @endforeach
                @endif
            </div>

        </div>
        <a href="https://google.com" class="moreItem">
            <p>More>></p>
        </a>

    </div>

</section>
@endsection