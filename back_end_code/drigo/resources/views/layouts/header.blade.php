<section class="header">
    <div class="headertop">
        <div class="headertopleft">


            <a href="{{url('/')}}" class="headerleftlogo">
                <img src="{{url('font_end_code/image/logo.png')}}" alt="poor internet">
                <p class="headerTitleColor">D</p>
                <p class="headerTitle">r</p>
                <p class="headerTitleColor">i</p>
                <p class="headerTitle">g</p>
                <p class="headerTitleColor">o</p>
            </a>


            <div class="headerleftsearch">

                <form class="headerleftsearchform" action="{{url('/search')}}" method="GET">
                    <input class="headersearchfield" type="search" name="search" id="" placeholder="Search Your item.....">
                    <button class="headersearchbtn"> </button>
                </form>
            </div>
        </div>

        <div class="headertopright">
            <ul>
                <li><a href="#">Nearest Shop</a></li>
                <li><a href="#">List</a></li>
                <li>

                    @if(Session::get('seller_username'))
                    <a href="{{url('sellerProfile')}}">
                        <div>
                            <i class="gg-user"></i>
                            <p>
                                {{session()->get('seller_username')}}
                            </p>
                        </div> </i>
                    </a>
                    @else
                    <a href="{{url('login')}}">
                        <div>
                            <i class="gg-user"></i>
                            <p>

                                {{"profile"}}


                            </p>
                        </div> </i>
                    </a>
                    @endif



                </li>
                <li>
                    @if(Session::get('seller_username'))

                    <a href="{{url('logout')}}">
                        {{"logout"}}
                    </a>
                    @else
                    <a href="{{url('login')}}">
                        {{"login"}}
                    </a>
                    @endif
                </li>

            </ul>

        </div>
    </div>

    </div>
    </div>
    <div class="headerbottom">
        <ul>
            <li><a href="#">Cafe</a></li>
            <li><a href="#">Book Store</a></li>
            <li><a href="#">Hotel</a></li>
            <li><a href="#">Grocery</a></li>
            <li><a href="#">Electronic Device</a></li>
            <li><a href="#">Baby Food</a></li>
            <li><a href="#">Medicine</a></li>
            <li><a href="#">Laundry Store</a></li>
            <li><a href="#">Computer Shop</a></li>
            <li><a href="#">Resturent </a></li>
            <li><a href="#">Bank</a></li>
        </ul>
    </div>

</section>
<a class="dropdown" href="#">
    <div>
        <i class="gg-menu-left-alt" onclick="changeMenuIcon(this)"></i>


        </i>

    </div>
</a>

<section id="menuitem1" class="menuitem">
    <div class="menuitemobject">
        <ul>
            <li><a href="#">Nearest Shop</a></li>
            <li><a href="#">List</a></li>
            <li><a href="#">Profile</a></li>
            <li>

                @if(Session::get('seller_username'))
                <a href="{{url('sellerProfile')}}">
                    <div>
                        <i class="gg-user"></i>
                        <p>

                            {{session()->get('seller_username')}}



                        </p>
                    </div> </i>
                </a>
                @else
                <a href="{{url('login')}}">
                    <div>
                        <i class="gg-user"></i>
                        <p>

                            {{"profile"}}


                        </p>
                    </div> </i>
                </a>
                @endif






            </li>


        </ul>
    </div>

</section>
<div class="headergaph">

</div>