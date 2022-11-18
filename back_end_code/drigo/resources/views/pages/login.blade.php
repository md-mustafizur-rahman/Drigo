@extends('layouts.main')


@section('main-section')

<section class="loginMain">
    <div class="loginMainTop">
        <img src="{{url('font_end_code/image/logo.png')}}" alt="">
        <div class="mainItem">
            <div class="mainItemInner">
                <h2>Drigo</h2>
                <form class="mainItemForm" action="">
                    <div class="inputfield">


                        <input placeholder="username" type="text">
                        <input placeholder="password" type="password">
                    </div>
                    <input class="loginBtn" type="button" value="Login">
                </form>
            </div>
        </div>

    </div>
    <div class="loginMainBottom">
    <img src="{{url('font_end_code/image/logo.png')}}" alt="">
        <div class="loginBottomText">
            <div class="loginBottomTextInner">
                <p>If you have no account then you can be <a href="{{url('registration')}}">SignUP</a></p>
            </div>
        </div>
    </div>
</section>
@endsection