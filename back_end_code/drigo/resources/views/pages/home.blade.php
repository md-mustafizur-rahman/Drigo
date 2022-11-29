@extends('layouts.main');


@section('main-section')

<section class="mainsearch">

    <div class="searchhome">
        <div class="searchhomeleft">
            <div class="searhomelefttitle">
                <h2>Search Your Item</h2>
            </div>
            <div class="searchhomeleftsearch">
                <form class="searchform" action="{{url('/search')}}" method="GET">
                    <input class="searchfield" placeholder="Search Now...." type="search" name="search" id="">
                    <button class="searchfieldbtn">Search</button>

                </form>
            </div>
        </div>
        <div class="searchhomeright">
            <img src="{{url('font_end_code/image/logo.png')}}" alt="poor internet">
        </div>
    </div>
</section>

<Section class="nearShopList">


    <div class="innerNearShopList">
        <div class="nearestTitle">
            <P>Most <span>Near</span>est <span>Shop</span> </P>
        </div>

        <!-- Product Viewing content 
this is most useble html css  -->
        <div class="productList">

            <!-- 
This is the product html start -->
            <!-- {{$products}} -->
            @php
            $totalHomeItemCount= 0;
            @endphp
            @if($products !=null)
            @foreach ($products as $product)

            @if( $totalHomeItemCount<=9) @if(session()->get('seller_seller_id')== $product->seller_id)
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
                @else
                <a href="{{('sellerProfile')}}" class="product">
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
                @endif
                @php $totalHomeItemCount++; @endphp
                @endforeach
                @endif

                <!-- 
This is the product html end -->

        </div>

    </div>



</Section>

<section class="homevideo">
    <div class="homevideoinner">
        <div class="homevideoinnerleft">

            <h2>Most Nearest Shop</h2>
            <p>This is the best place to find<br> your Item </p>
        </div>
        <div class="homevideoinnerright">

            <iframe width="100%" height="100%" src="https://www.youtube.com/embed/Cl3CcZAffTo">
            </iframe>
        </div>
    </div>
</section>

<section class="mostPopular">

    <div class="mostPopularInner">

        <div class="innerNearShopList">
            <div class="nearestTitle">
                <P>Most <span>Near</span>est <span>Shop</span> </P>
            </div>

            <!-- Product Viewing content 
    this is most useble html css  -->
            <div class="productList">

                <!-- 
This is the product html start -->

                @php
                $totalHomeItemCount= 0;
                @endphp
                @if($products !=null)
                @foreach ($products as $product)

                @if( $totalHomeItemCount<=3) @if(session()->get('seller_seller_id')== $product->seller_id)
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
                    @else
                    <a href="{{('sellerProfile')}}" class="product">
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
                    @endif
                    @php $totalHomeItemCount++; @endphp
                    @endforeach
                    @endif

                    <!-- 
                This is the product html end  -->


            </div>

        </div>


    </div>



</section>


@endsection