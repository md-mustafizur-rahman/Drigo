@extends('layouts.main');
@section('main-section')
<section class="mainContent">
    <div class="mainContentInner">
        <div class="mainContentLeft">
            <div class="mainContentLeftTop">
                <div class="mainContentLeftTopInnerItem">
                    <a href="{{url('/showSellerProfile/')}}/{{$products[0]->seller_id}}">
                        <img src="{{url('font_end_code/image/header.png')}}" alt="">
                        <div class="ownerName">

                    </a>

                    <a href="{{url('/showSellerProfile/')}}/{{$products[0]->seller_id}}" style="color:black;">
                        <h2>{{$products[0]->seller_name}}</h2>
                    </a>
                    <a href="{{url('/showSellerProfile/')}}/{{$products[0]->seller_id}}" style="color:black;">
                        <p>{{$products[0]->shopname}}</p>
                    </a>
                </div>


            </div>
            <div class="productTitle">

                <h2>{{$products[0]->product_name}}</h2>
                <p>Size: {{$products[0]->product_size}}</p>
            </div>

        </div>
        <div class="mainContentLeftBottom">
            <img src="{{asset('/storage/uploads/'.$products[0]->product_Image)}}" alt="">
        </div>
    </div>
    <div class="mainContentRight">
        <div class="mainContentRightInner">
            <div class="mainContentRightInnerTop">
                <div class="mainContentRightInnerTopLeft">
                    <div class="mainContentRightInnerTopLeftInner">
                        <a href="{{url('/showSellerProfile/')}}/{{$products[0]->seller_id}}" style="color:white;">
                            <h2>{{$products[0]->shopname}}</h2>
                        </a>

                        <p>Distance: 2km <br>{{$products[0]->product_price}} tk</p>
                    </div>


                </div>
                <div class="mainContentRightInnerTopRight">
                    <img src="{{url('font_end_code/image/logo.png')}}" alt="poor Connection">
                </div>
            </div>

            <div class="mainContentRightInnerTopMid">
                <div class="mainContentRightInnerTopMidInner">
                    <h2>{{$products[0]->product_name}}</h2>
                    <p>
                        Size: {{$products[0]->product_details}}
                    </p>
                </div>

            </div>
            <div class="mainContentRightInnerTopLast">
                @if(isset($_COOKIE['userLatitude']))
                <a href="https://www.google.com/maps/dir/{{$_COOKIE['userLatitude']}},{{$_COOKIE['userLongitude']}}/{{$products[0]->shop_latitude}}, {{$products[0]->shop_longitude}}/" target="black"><button>Get Location</button></a>
                @else
                <a href="https://www.google.com/maps/dir/{{$products[0]->shop_latitude}}, {{$products[0]->shop_longitude}}/" target="black"><button>Get Location</button></a>
                @endif
            </div>
        </div>
    </div>
    </div>

</section>

@endsection