@extends('layouts.main')


@section('main-section')

<section class="mainBackground">
    <div class="mainBackgroundTop">
        <div class="mainContain">
            <div class="mainContainInner">

                <form class="registerForm" action="">
                    <h2>Drigo</h2>
                    <div class="formInner">
                        <input type="text" placeholder="full name" name="" id="">
                        <input type="text" placeholder="user name" name="" id="">
                    </div>
                    <div class="formInner">
                        <select id="category" name="category">
                            <option selected value="Cafe">Cafe</option>
                            <option value="Book Store">Book Store</option>
                            <option value="Hotel">Hotel</option>
                            <option value="Grocery">Grocery</option>
                            <option value="Electronic Device">Electronic Device</option>
                            <option value="Baby Food">Baby Food</option>
                            <option value="Medicine">Medicine</option>
                            <option value="Laundry Store">Laundry Store</option>
                            <option value="Computer shop">Computer shop</option>
                            <option value="Resturent">Resturent</option>
                            <option value="Bank">Bank</option>
                           

                        </select>
                        <input type="text" placeholder="Shop Name" name="" id="">
                    </div>
                    <div class="formInner">
                        <input type="email" placeholder="email" name="" id="">
                        <input type="password" placeholder="password" name="" id="">
                    </div>
                    <div class="formInner">
                        <input type="text" placeholder="latitude" name="" id="">
                        <input type="text" placeholder="longitude" name="" id="">
                    </div>
                    <div class="formInner">

                        <input type="password" placeholder="confirm password" name="" id="">
                    </div>
                    <div class="formInner">

                        <input class="registerBtn" type="button" value="SignUp">
                    </div>

                </form>
                <div class="registerBottomText">
                    <div class="registerBottomTextInner">
                        <p>If you have no account then you can be <a href="{{url('login')}}">Login</a></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="mainBackgroundBottom">
        <div class="backgroundImg">
            <img src="{{url('font_end_code/image/logo.png')}}" alt="">
            <img src="{{url('font_end_code/image/logo.png')}}" alt="">

        </div>

    </div>
</section>
@endsection