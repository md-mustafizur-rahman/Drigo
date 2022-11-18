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
                            <input type="email" placeholder="email" name="" id="">
                            <input type="password" placeholder="password" name="" id="">
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