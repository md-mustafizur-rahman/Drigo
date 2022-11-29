@extends('layouts.main')
@section('main-section')
<section class="searchContent">

    <div class="searchContentInner">
        <h2 class="searchingTitle">Result As: {{$searchKey}}</h2>
        <p class="totalCount">Total Item: @if($products !=null)
            {{count($products)}}
            @else
            {{"0"}}
            @endif
        </p>


        <div class="productList">

            <!-- 
This is the product html start -->

            @php
            $totalHomeItemCount= 0;
            @endphp
            @if($products !=null)
            @foreach ($products as $product)
            @if( $totalHomeItemCount<=40) <a href="{{('sellerProfile')}}" class="product">
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
                <div class="productbottom">
                    <p>{{$product->product_price}} tk</p>
                    <p>{{$product->created_at->diffForHumans()}}</p>
                    <h4>{{$product["shopname"]}}</h4>
                    <p>Duration: </p>
                </div>
                </a>

                @endif
                @php $totalHomeItemCount++; @endphp
                @endforeach
                @endif




        </div>

    </div>




    </div>
</section>
@endsection