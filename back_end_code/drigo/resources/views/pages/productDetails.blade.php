@extends('layouts.main');
@section('main-section')
<section class="mainContent">
    <div class="mainContentInner">
        <div class="mainContentLeft">
            <div class="mainContentLeftTop">
                <div class="mainContentLeftTopInnerItem">
                    <img src="{{url('font_end_code/image/header.png')}}" alt="">
                    <div class="ownerName">
                        <h2>{{$products[0]->seller_name}}</h2>
                        <p>{{$products[0]->shopname}}</p>
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
                            <h2>{{$products[0]->shopname}}</h2>
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
                    <a href="#"><button>Get Location</button></a>
                </div>
            </div>
        </div>
    </div>

</section>

@endsection